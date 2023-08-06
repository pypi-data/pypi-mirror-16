# -*- coding: utf-8 -*-
'''Determine whether a client matches a specification (beta)

Usage:
    exo [options] spec <auth> <spec-yaml> [--ids=<id1,id2,idN>] [--portal|--domain] [-f]
    exo [options] spec <auth> --generate=<filename> [--scripts=<dir>] [--asrid]
    exo [options] spec <spec-yaml> --check
    exo [options] spec --example

The --generate form creates spec YAML and scripts from an RPC auth (e.g. CIK).
<spec-yaml> may be a filesystem path, - to read the spec from stdin,
  or a URL to get.

Command options:
    --update-scripts  Update any scripts that do not match what's
                      on the filesystem
    --check           Validate the jsonschema elements to be valid schemas
    --create          Create any resources that do not exist
    --asrid           When generating a spec, do not convert RIDs into aliases.
    --ids substitutes values for <% id %> when matching alias
    --example         Show an annotated example spec YAML file
    --portal          Will apply the spec command to all devices in a portal
                      that match the vendor/model in the given spec file
    --domain          Will apply the spec command to all devices, in all of the
                      portals under the given domain, that match the vendor/model
                      in the given spec file
    -f                Used with the `--portal` or `--domain flag to override the
                      prompt when updating multiple devices.
    --no-diff         Do not show diff output on scripts.
'''

from __future__ import unicode_literals
import re
import os
import json
from pprint import pprint
import sys
import pyonep
import ast

import ruamel.yaml as yaml
import jsonschema
import requests
import six
from six import iteritems

TYPES = ['dataport', 'client', 'script', 'datarule', 'dispatch']

def plural(typ):
    if typ == 'dispatch':
        return 'dispatches'
    else:
        return typ + 's'

class Spec401Exception(BaseException):
    # Used when a 401 is caught during a spec
    pass


class Plugin():
    def command(self):
        return 'spec'
    def run(self, cmd, args, options):
        if args['--example']:
            s = '''
# Example client specification file
# Specification files are in YAML format (a superset of JSON
# with more readable syntax and support for comments) and
# look like this. They may contain comments that begin
# with a # sign.

# Device client model information
device:
    model: "myModel"
    vendor: "myVendor"

# list of dataports that must exist
dataports:
      # this the absolute minimum needed to specify a
      # dataport.
    - alias: mystring
      # names are created, but not compared
    - name: Temperature
      # aliases, type, and format are created
      # and compared
      alias: temp
      format: float
      unit: °F
    - name: LED Control
      alias: led6
      format: integer
    - alias: config
      # format should be string, and parseable JSON
      format: string/json
      # initial value (if no other value is read back)
      initial: '{"text": "555-555-1234", "email": "jeff@555.com"}'
    - alias: person
      format: string/json
      # JSON schema specified inline (http://json-schema.org/)
      # format must be string/json to do validate
      # you may also specify a string to reference schema in an
      # external file. E.g. jsonschema: personschema.json
      jsonschema: {"title": "Person Schema",
                   "type": "object",
                   "properties": {"name": {"type": "string"}},
                   "required": ["name"]}
      initial: '{"name":"John Doe"}'
    - alias: place
      # An description of the dataport.
      description: 'This is a place I have been'
      # Dataports are not public by default,
      # but if you want to share one with the world
      public: true

    # any dataports not listed but found in the client
    # are ignored. The spec command does not delete things.

# list of script datarules that must exist
scripts:
    # by default, scripts are datarules with
    # names and aliases set to the file name
    - file: test/files/helloworld.lua
    # you can also set them explicitly
    - file: test/files/helloworld.lua
      alias: greeting
    # you can also place lua code inline
    - alias: singleLineScript
      code: debug('hello from inside lua!')
    # multiline lua scripts should start with | and
    # be indented inside the "code:" key.
    - alias: multilineScript
      code: |
        for x=1,10 do
            debug('hello from for loop ' .. x)
        end
    # simple templating for script aliases and
    # content is also supported.
    - file: test/files/convert.lua
      # if <% id %> is embedded in aliases
      # or script content, the --ids parameter must
      # be passed in. The spec command then expects
      # a script or dataport resource per id passed, substituting
      # each ID for <% id %>. In this example, if the command was:
      #
      # $ exo spec mysensor sensorspec.yaml --ids=A,B
      #
      # ...then the spec command looks for *two* script datarules
      # in mysensor, with aliases convertA.lua and convertB.lua.
      # Additionally, any instances of <% id %> in the content of
      # convert.lua are substituted with A and B before being
      # written to each script datarule.
      #
      alias: convert<% id %>.lua

# list of dispatches that must exist
dispatches:
    - alias: myDispatch
      # email | http_get | http_post | http_put | sms | xmpp
      method: email
      recipient: support@exosite.com
      message: hello from Exoline spec example!
      subject: hello!
      # may be an RID or alias
      subscribe: mystring

# list of simple datarules that must exist.
# scripts may go here too, but it's better to
# to put them under scripts (above)
datarules:
    - alias: highTemp
      format: float
      subscribe: temp
      rule: {
        "simple": {
          "comparison": "gt",
          "constant": 80,
          "repeat": true
        }
      }
'''
            if not six.PY3:
                s = s.encode('utf-8')
            print(s)
            return

        ExoException = options['exception']
        def load_file(path, base_url=None):
            '''load a file based on a path that may be a filesystem path
            or a URL. Consider it a URL if it starts with two or more
            alphabetic characters followed by a colon'''
            def load_from_url(url):
                # URL. use requests
                r = requests.get(url)
                if r.status_code >= 300:
                    raise ExoException('Failed to read file at URL ' + url)
                return r.text, '/'.join(r.url.split('/')[:-1])

            if re.match('[a-z]{2}[a-z]*:', path):
                return load_from_url(path)
            elif base_url is not None:
                # non-url paths when spec is loaded from URLs
                # are considered relative to that URL
                return load_from_url(base_url + '/' + path)
            else:
                with open(path, 'rb') as f:
                    return f.read(), None


        def load_spec(args):
            # returns loaded spec and path for script files
            try:
                content, base_url = load_file(args['<spec-yaml>'])
                spec = yaml.safe_load(content)
                return spec, base_url
            except yaml.scanner.ScannerError as ex:
                raise ExoException('Error parsing YAML in {0}\n{1}'.format(args['<spec-yaml>'],ex))

        def check_spec(spec, args):
            msgs = []
            for typ in TYPES:
                if typ in spec and plural(typ) not in spec:
                    msgs.append('found "{0}"... did you mean "{1}"?'.format(typ, typ + 's'))
            for dp in spec.get('dataports', []):
                if 'alias' not in dp:
                    msgs.append('dataport is missing alias: {0}'.format(dp))
                    continue
                alias = dp['alias']
                if 'jsonschema' in dp:
                    schema = dp['jsonschema']
                    if isinstance(schema, six.string_types):
                        schema = json.loads(open(schema).read())
                    try:
                        jsonschema.Draft4Validator.check_schema(schema)
                    except Exception as ex:
                        msgs.append('{0} failed jsonschema validation.\n{1}'.format(alias, str(ex)))
            if len(msgs) > 0:
                raise ExoException('Found some problems in spec:\n' + '\n'.join(msgs))

        if args['--check']:
            # Validate all the jsonschema
            spec, base_url = load_spec(args)
            check_spec(spec, args)
            return

        reid = re.compile('<% *id *%>')
        def infoval(input_auth, alias):
            '''Get info and latest value for a resource'''
            return rpc._exomult(
                input_auth,
                [['info', {'alias': alias}, {'description': True, 'basic': True}],
                ['read', {'alias': alias}, {'limit': 1}]])

        def check_or_create_description(auth, info, args):
            if 'device' in spec and 'limits' in spec['device']:
                speclimits = spec['device']['limits']
                infolimits = info['description']['limits']
                limits_mismatched = False
                for limit in speclimits:
                    if limit not in infolimits:
                        raise ExoException('spec file includes invalid limit {0}'.format(limit))
                    if speclimits[limit] != infolimits[limit]:
                        limits_mismatched = True
                if limits_mismatched:
                    if create:
                        if 'client_id' not in auth:
                            raise ExoException('limits update for client requires --portal or --domain')

                        rpc.update(auth['cik'], auth['client_id'], {'limits': speclimits})
                        sys.stdout.write('updated limits for client' +
                                         ' RID {0}'.format(auth['client_id']))
                    else:
                        sys.stdout.write(
                            'limits for client {0} do not match spec:\nspec: {1}\nclient: {2}'.format(
                                auth,
                                json.dumps(speclimits, sort_keys=True),
                                json.dumps(infolimits, sort_keys=True)))


        def check_or_create_common(auth, res, info, alias, aliases):
            if info['basic']['type'] != typ:
                raise ExoException('{0} is a {1} but should be a {2}.'.format(alias, info['basic']['type'], typ))

            new_desc = info['description'].copy()
            need_update = False

            if 'public' in res:
                res_pub = res['public']
                desc = info['description']
                if desc['public'] != res_pub:
                    if create:
                        new_desc['public'] = res_pub
                        need_update = True
                    else:
                        sys.stdout.write('spec expects public for {0} to be {1}, but it is not.\n'.format(alias, res_pub))
                        print(json.dumps(res))

            if 'subscribe' in res:
                # Alias *must* be local to this client
                resSub = res['subscribe']
                # Lookup alias/name if need be
                if resSub in aliases:
                    resSub = aliases[resSub]
                desc = info['description']
                if desc['subscribe'] != resSub:
                    if create:
                        new_desc['subscribe'] = resSub
                        need_update = True
                    else:
                        sys.stdout.write('spec expects subscribe for {0} to be {1}, but they are not.\n'.format(alias, resSub))

            if 'preprocess' in res:
                def fromAliases(pair):
                    if pair[1] in aliases:
                        return [pair[0], aliases[pair[1]]]
                    else:
                        return pair
                resPrep = [fromAliases(x) for x in res['preprocess']]
                preprocess = info['description']['preprocess']
                if create:
                    new_desc['preprocess'] = resPrep
                    need_update = True
                else:
                    if preprocess is None or len(preprocess) == 0:
                        sys.stdout.write('spec expects preprocess for {0} to be {1}, but they are missing.\n'.format(alias, resPrep))
                    elif preprocess != resPrep:
                        sys.stdout.write('spec expects preprocess for {0} to be {1}, but they are {2}.\n'.format(alias, resPrep, preprocess))

            if 'retention' in res:
                resRet = {}
                if 'count' in res['retention']:
                    resRet['count'] = res['retention']['count']
                if 'duration' in res['retention']:
                    resRet['duration'] = res['retention']['duration']
                retention = info['description']['retention']
                if create:
                    new_desc['retention'] = resRet
                    need_update = True
                elif retention != resRet:
                    sys.stdout.write('spec expects retention for {0} to be {1}, but they are {2}.\n'.format(alias, resRet, retention))

            if need_update:
                rpc.update(auth, {'alias': alias}, new_desc)

        def get_format(res, default='string'):
            format = res['format'] if 'format' in res else default
            pieces = format.split('/')
            if len(pieces) > 1:
                format = pieces[0]
                format_content = pieces[1]
            else:
                format_content = None
            return format, format_content

        def add_desc(key, res, desc, required=False):
            '''add key from spec resource to a 1P resource description'''
            if key in res:
                desc[key] = res[key]
            else:
                if required:
                    raise ExoException('{0} in spec is missing required property {1}.'.format(alias, key))

        def create_resource(auth, typ, desc, alias, msg=''):
            name = res['name'] if 'name' in res else alias
            print('Creating {0} with name: {1}, alias: {2}{3}'.format(
                typ, name, alias, msg))
            rid = rpc.create(auth, typ, desc, name=name)
            rpc.map(auth, rid, alias)
            info, val = infoval(auth, alias)
            aliases[alias] = rid
            return info, val

        def check_or_create_datarule(auth, res, info, val, alias, aliases):
            format, format_content = get_format(res, 'float')
            if not exists and create:
                desc = {'format': format}
                desc['retention'] = {'count': 'infinity', 'duration': 'infinity'}
                add_desc('rule', res, desc, required=True)
                info, val = create_resource(
                    auth,
                    'datarule',
                    desc,
                    alias,
                    msg=', format: {0}, rule: {1}'.format(desc['format'], desc['rule']))

            # check format
            if format != info['description']['format']:
                raise ExoException(
                    '{0} is a {1} but should be a {2}.'.format(
                    alias, info['description']['format'], format))

            # check rule
            infoRule = json.dumps(info['description']['rule'], sort_keys=True)
            specRule = json.dumps(res['rule'], sort_keys=True)
            if infoRule != specRule:
                if create:
                    info['description']['rule'] = res['rule']
                    rpc.update(auth, {'alias': alias}, info['description'])
                    sys.stdout.write('updated rule for {0}\n'.format(alias))
                else:
                    sys.stdout.write(
                        'spec expects rule for {0} to be:\n{1}\n...but it is:\n{2}\n'.format(
                        alias, specRule, infoRule))

            check_or_create_common(auth, res, info, alias, aliases)

        def check_or_create_dataport(auth, res, info, val, alias, aliases):
            format, format_content = get_format(res, 'string')
            if not exists and create:
                desc = {'format': format}
                desc['retention'] = {'count': 'infinity', 'duration': 'infinity'}
                info, val = create_resource(
                    auth,
                    'dataport',
                    desc,
                    alias,
                    msg=', format: {0}'.format(format))

            # check format
            if format != info['description']['format']:
                raise ExoException(
                    '{0} is a {1} but should be a {2}.'.format(
                    alias, info['description']['format'], format))

            # check initial value
            if 'initial' in res and len(val) == 0:
                if create:
                    initialValue = template(res['initial'])
                    print('Writing initial value {0}'.format(initialValue))
                    rpc.write(auth, {'alias': alias}, initialValue)
                    # update values being validated
                    info, val = infoval(auth, alias)
                else:
                    print('Required initial value not found in {0}. Pass --create to write initial value.'.format(alias))

            # check format content (e.g. json)
            if format_content == 'json':
                if format != 'string':
                    raise ExoException(
                        'Invalid spec for {0}. json content type only applies to string, not {1}.'.format(alias, format));
                if len(val) == 0:
                    print('Spec requires {0} be in JSON format, but it is empty.'.format(alias))
                else:
                    obj = None
                    try:
                        obj = json.loads(val[0][1])
                    except:
                        print('Spec requires {0} be in JSON format, but it does not parse as JSON. Value: {1}'.format(
                            alias,
                            val[0][1]))

                    if obj is not None and 'jsonschema' in res:
                        schema = res['jsonschema']
                        if isinstance(schema, six.string_types):
                            schema = json.loads(open(schema).read())
                        try:
                            jsonschema.validate(obj, schema)
                        except Exception as ex:
                            print("{0} failed jsonschema validation.".format(alias))
                            print(ex)

            elif format_content is not None:
                raise ExoException(
                    'Invalid spec for {0}. Unrecognized format content {1}'.format(alias, format_content))

            # check unit
            if 'unit' in res or 'description' in res:
                meta_string = info['description']['meta']
                try:
                    meta = json.loads(meta_string)
                except:
                    meta = None

                def bad_desc_msg(s):
                    desc='""'
                    if 'description' in res:
                        desc = res['description']
                    sys.stdout.write('spec expects description for {0} to be {1}{2}\n'.format(alias, desc, s))
                def bad_unit_msg(s):
                    unit=''
                    if 'unit' in res:
                        unit = res['unit']
                    sys.stdout.write('spec expects unit for {0} to be {1}{2}\n'.format(alias, unit, s))

                if create:
                    if meta is None:
                        meta = {'datasource':{'description':'','unit':''}}
                    if 'datasource' not in meta:
                        meta['datasource'] = {'description':'','unit':''}
                    if 'unit' in res:
                        meta['datasource']['unit'] = res['unit']
                    if 'description:' in res:
                        meta['datasource']['description'] = res['description']

                    info['description']['meta'] = json.dumps(meta)
                    rpc.update(auth, {'alias': alias}, info['description'])

                else:
                    if meta is None:
                        sys.stdout.write('spec expects metadata but found has no metadata at all. Pass --create to write metadata.\n')
                    elif 'datasource' not in meta:
                        sys.stdout.write('spec expects datasource in metadata but found its not there. Pass --create to write metadata.\n')
                    elif 'unit' not in meta['datasource'] and 'unit' in res:
                        bad_unit_msg(', but no unit is specified in metadata. Pass --create to set unit.\n')
                    elif 'description' not in meta['datasource'] and 'description' in res:
                        bad_desc_msg(', but no description is specified in metadata. Pass --create to set description.\n')
                    elif 'unit' in res and meta['datasource']['unit'] != res['unit']:
                        bad_unit_msg(', but metadata specifies unit of {0}. Pass --create to update unit.\n'.format(meta['datasource']['unit']))
                    elif 'description' in res and meta['datasource']['description'] != res['description']:
                        bad_desc_msg(', but metadata specifies description of {0}. Pass --create to update description.\n'.format(meta['datasource']['description']))

            check_or_create_common(auth, res, info, alias, aliases)

        def check_or_create_dispatch(auth, res, info, alias, aliases):
            if not exists and create:
                desc = {}
                add_desc('method', res, desc, required=True)
                add_desc('recipient', res, desc, required=True)
                add_desc('subject', res, desc)
                add_desc('message', res, desc)
                desc['retention'] = {'count': 'infinity', 'duration': 'infinity'}
                info, val = create_resource(
                    auth,
                    'dispatch',
                    desc,
                    alias,
                    msg=', method: {0}, recipient: {1}'.format(desc['method'], desc['recipient']))

            # check dispatch-specific things
            def check_desc(key, res, desc):
                '''check a specific key and return whether an update is required'''
                if key in res and desc[key] != res[key]:
                    if create:
                        desc[key] = res[key]
                        return True
                    else:
                        sys.stdout.write(
                            'spec expects {0} for {1} to be {2} but it is {3}\n'.format(
                            key, alias, res[key], desc[key]))
                return False

            desc = info['description']
            need_update = False
            need_update = check_desc('method', res, desc) or need_update
            need_update = check_desc('recipient', res, desc) or need_update
            need_update = check_desc('subject', res, desc) or need_update
            need_update = check_desc('message', res, desc) or need_update
            if need_update:
                rpc.update(auth, {'alias': alias}, desc)
                sys.stdout.write('updated {0} to {1}\n'.format(alias, json.dumps(desc, sort_keys=True)))

            check_or_create_common(auth, res, info, alias, aliases)


        input_auth = options['auth']
        exoutils = options['utils']
        rpc = options['rpc']
        asrid = args['--asrid']

        if cmd == 'spec':

            if args['--generate'] is not None:
                spec_file = args['--generate']
                if args['--scripts'] is not None:
                    script_dir = args['--scripts']
                else:
                    script_dir = 'scripts'
                print('Generating spec for {0}.'.format(input_auth))
                print('spec file: {0}, scripts directory: {1}'.format(spec_file, script_dir))

                # generate spec file, download scripts
                spec = {}
                info, listing = rpc._exomult(input_auth,
                    [['info', {'alias': ''}, {'basic': True,
                                              'description': True,
                                              'aliases': True}],
                     ['listing', ['dataport', 'datarule', 'dispatch'], {}, {'alias': ''}]])
                rids = listing['dataport'] + listing['datarule'] + listing['dispatch']

                if len(rids) > 0:
                    child_info = rpc._exomult(input_auth, [['info', rid, {'basic': True, 'description': True}] for rid in rids])
                    for idx, rid in enumerate(rids):
                        myinfo = child_info[idx]
                        name = myinfo['description']['name']
                        def skip_msg(msg):
                            print('Skipping {0} (name: {1}). {2}'.format(rid, name, msg))
                        if rid not in info['aliases']:
                            skip_msg('It needs an alias.')
                            continue

                        # adds properties common to dataports and dispatches:
                        # preprocess, subscribe, retention, meta, public
                        def add_common_things(res):
                            res['name'] = myinfo['description']['name']
                            res['alias'] = info['aliases'][rid][0]
                            preprocess = myinfo['description']['preprocess']
                            if preprocess is not None and len(preprocess) > 0:
                                def toAlias(pair):
                                    if not asrid and pair[1] in info['aliases']:
                                        return [pair[0], info['aliases'][pair[1]][0]]
                                    else:
                                        return pair
                                res['preprocess'] = [toAlias(x) for x in preprocess]


                            subscribe = myinfo['description']['subscribe']
                            if subscribe is not None and subscribe is not "":
                                if not asrid and subscribe in info['aliases']:
                                    res['subscribe'] = info['aliases'][subscribe][0]
                                else:
                                    res['subscribe'] = subscribe

                            retention = myinfo['description']['retention']
                            if retention is not None:
                                count = retention['count']
                                duration = retention['duration']
                                if count is not None and duration is not None:
                                    if count == 'infinity':
                                        del retention['count']
                                    if duration == 'infinity':
                                        del retention['duration']
                                    if len(retention) > 0:
                                        res['retention'] = retention

                            meta_string = myinfo['description']['meta']
                            try:
                                meta = json.loads(meta_string)
                                unit = meta['datasource']['unit']
                                if len(unit) > 0:
                                    res['unit'] = unit
                                desc = meta['datasource']['description']
                                if len(desc) > 0:
                                    res['description'] = desc
                            except:
                                # assume unit is not present in metadata
                                pass

                            public = myinfo['description']['public']
                            if public is not None and public:
                                res['public'] = public


                        typ = myinfo['basic']['type']
                        if typ == 'dataport':
                            res = {
                                'format': myinfo['description']['format']
                            }
                            add_common_things(res)
                            spec.setdefault('dataports', []).append(res)

                        elif typ == 'datarule':
                            desc = myinfo['description']
                            is_script = desc['format'] == 'string' and 'rule' in desc and 'script' in desc['rule']
                            if is_script:
                                if not os.path.exists(script_dir):
                                    os.makedirs(script_dir)
                                filename = os.path.join(script_dir, info['aliases'][rid][0])
                                spec.setdefault('scripts', []).append({'file': filename})
                                with open(filename, 'w') as f:
                                    print('Writing {0}...'.format(filename))
                                    f.write(desc['rule']['script'].encode('utf8'))
                            else:
                                res = {
                                    'rule': desc['rule']
                                }
                                add_common_things(res)
                                spec.setdefault('datarules', []).append(res)

                        elif typ == 'dispatch':
                            desc = myinfo['description']
                            res = {
                                'method': desc['method'],
                                'message': desc['message'],
                                'recipient': desc['recipient'],
                                'subject': desc['subject']
                            }
                            add_common_things(res)
                            spec.setdefault('dispatches', []).append(res)

                with open(spec_file, 'w') as f:
                    print('Writing {0}...'.format(spec_file))
                    yaml.safe_dump(spec, f, encoding='utf-8', indent=4, default_flow_style=False, allow_unicode=True)
                return

            updatescripts = args['--update-scripts']
            create = args['--create']

            def query_yes_no(question, default="yes"):
                """Ask a yes/no question via raw_input() and return their answer.

                "question" is a string that is presented to the user.
                "default" is the presumed answer if the user just hits <Enter>.
                    It must be "yes" (the default), "no" or None (meaning
                    an answer is required of the user).

                The "answer" return value is one of "yes" or "no".
                """
                valid = {"yes":True,   "y":True,  "ye":True,
                         "no":False,     "n":False}
                if default == None:
                    prompt = " [y/n] "
                elif default == "yes":
                    prompt = " [Y/n] "
                elif default == "no":
                    prompt = " [y/N] "
                else:
                    raise ValueError("invalid default answer: '%s'" % default)

                while True:
                    sys.stdout.write(question + prompt)
                    choice = raw_input().lower()
                    if default is not None and choice == '':
                        return valid[default]
                    elif choice in valid:
                        return valid[choice]
                    else:
                        sys.stdout.write("Please respond with 'yes' or 'no' "\
                                         "(or 'y' or 'n').\n")

            def generate_aliases_and_data(res, args):
                ids = args['--ids']
                if 'alias' in res:
                    alias = res['alias']
                else:
                    if 'file' in res:
                        alias = os.path.basename(res['file'])
                    else:
                        raise ExoException('Resources in spec must have an alias. (For scripts, "file" will substitute.)')

                if reid.search(alias) is None:
                    yield alias, None
                else:
                    alias_template = alias
                    if ids is None:
                        raise ExoException('This spec requires --ids')
                    ids = ids.split(',')
                    for id, alias in [(id, reid.sub(id, alias_template)) for id in ids]:
                        yield alias, {'id': id}

            spec, base_url = load_spec(args)
            check_spec(spec, args)

            device_auths = []
            portal_ciks = []

            iterate_portals = False

            def auth_string(auth):
                if isinstance(auth, dict):
                    return json.dumps(auth)
                else:
                    return auth

            if args['--portal'] == True:
                cik = exoutils.get_cik(input_auth, allow_only_cik=True)
                portal_ciks.append((cik,''))
                iterate_portals = True

            if args['--domain'] == True:
                cik = exoutils.get_cik(input_auth, allow_only_cik=True)
                #set iterate_portals flag to true so we can interate over each portal
                iterate_portals = True
                # Get list of users under a domain
                user_keys = []
                clients = rpc._listing_with_info(cik,['client'])

                email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')

                for k,v in clients['client'].items():
                    name = v['description']['name']
                    # if name is an email address
                    if email_regex.match(name):
                        user_keys.append(v['key'])


                # Get list of each portal
                for key in user_keys:
                    userlisting = rpc._listing_with_info(key,['client'])
                    for k,v in userlisting['client'].items():
                        portal_ciks.append((v['key'],v['description']['name']))
                    #print(x)


            if iterate_portals == True:
                for portal_cik, portal_name in portal_ciks:
                    # If user passed in the portal flag, but the spec doesn't have
                    # a vendor/model, exit
                    if (not 'device' in spec) or (not 'model' in spec['device']) or (not 'vendor' in spec['device']):
                        print("With --portal (or --domain) option, spec file requires a\r\n"
                              "device model and vendor field:\r\n"
                              "e.g.\r\n"
                              "device:\r\n"
                              "    model: modelName\r\n"
                              "    vendor: vendorName\r\n")
                        raise ExoException('--portal flag requires a device model/vendor in spec file')
                    else:

                        # get device vendor and model
                        modelName = spec['device']['model']
                        vendorName = spec['device']['vendor']

                        # If the portal has no name, use the cik as the name
                        if portal_name == '':
                            portal_name = portal_cik
                        print('Looking in ' + portal_name + ' for ' + modelName + '/' + vendorName)
                        # Get all clients in the portal
                        clients = rpc._listing_with_info(portal_cik, ['client'])
                        #print(modelName)
                        # for each client
                        for rid, v in iteritems(list(iteritems(clients))[0][1]):
                            # Get meta field
                            validJson = False
                            meta = None
                            try:
                                meta = json.loads(v['description']['meta'])
                                validJson = True
                            except ValueError as e:
                                # no json in this meat field
                                validJson = False
                            if validJson == True:
                                # get device type (only vendor types have a model and vendor
                                typ = meta['device']['type']

                                # if the device type is 'vendor'
                                if typ == 'vendor':
                                    # and it matches our vendor/model in the spec file
                                    if meta['device']['vendor'] == vendorName:
                                        if meta['device']['model'] == modelName:
                                            # Append an auth for this device to our list
                                            auth = {
                                                'cik': portal_cik, # v['key'],
                                                'client_id': rid
                                            }
                                            device_auths.append(auth)
                                            print('  found: {0} {1}'.format(v['description']['name'], auth_string(auth)))
            else:
                # only for single client
                device_auths.append(input_auth)

            # Make sure user knows they are about to update multiple devices
            # unless the `-f` flag is passed
            if ((args['--portal'] or args['--domain']) and args['--create']) and not args['-f']:
                res = query_yes_no("You are about to update " + str(len(device_auths)) + " devices, are you sure?")
                if res == False:
                    print('exiting')
                    return

            # for each device in our list of device_auths
            for auth in device_auths:
                try:
                    aliases = {}
                    print("Running spec on: {0}".format(auth_string(auth)))
                    #   apply spec [--create]

                    # Get map of aliases and description
                    info = rpc.info(auth, {'alias': ''}, {'aliases': True, 'description': True})
                    try:
                        for rid, alist in info['aliases'].items():
                            for alias in alist:
                                aliases[alias] = rid
                    except:
                        pass

                    # Check limits
                    check_or_create_description(auth, info, args)

                    for typ in TYPES:
                        for res in spec.get(plural(typ), []):
                            for alias, resource_data in generate_aliases_and_data(res, args):
                                # TODO: handle nonexistence
                                exists = True
                                try:
                                    info, val = infoval(auth, alias)
                                except rpc.RPCException as e:
                                    info = None
                                    val = None
                                    exists = False
                                    print('{0} not found.'.format(alias))
                                    if not create:
                                        print('Pass --create to create it')
                                        continue
                                except pyonep.exceptions.OnePlatformException as ex:
                                    exc = ast.literal_eval(ex.message)

                                    if exc['code'] == 401:
                                        raise Spec401Exception()
                                    else:
                                        raise ex

                                def template(script):
                                    if resource_data is None:
                                        return script
                                    else:
                                        return reid.sub(resource_data['id'], script)

                                if typ == 'client':
                                    if not exists:
                                        if create:
                                            print('Client creation is not yet supported')
                                        continue
                                elif typ == 'dataport':
                                    check_or_create_dataport(auth, res, info, val, alias, aliases)
                                elif typ == 'dispatch':
                                    check_or_create_dispatch(auth, res, info, alias, aliases)
                                elif typ == 'datarule':
                                    check_or_create_datarule(auth, res, info, val, alias, aliases)
                                elif typ == 'script':
                                    if 'file' not in res and 'code' not in res:
                                        raise ExoException('{0} is a script, so it needs a "file" or "code" key'.format(alias))
                                    if 'file' in res and 'code' in res:
                                        raise ExoException('{0} specifies both "file" and "code" keys, but they\'re mutually exclusive.')

                                    name = res['name'] if 'name' in res else alias

                                    if 'file' in res:
                                        content, _ = load_file(res['file'], base_url=base_url)
                                        if not six.PY3 or type(content) is bytes:
                                            content = content.decode('utf8')
                                    else:
                                        content = res['code']
                                    if not exists and create:
                                        rpc.upload_script_content([auth], content, name=alias, create=True, filterfn=template)
                                        continue

                                    script_spec = template(content)
                                    script_svr = info['description']['rule']['script']
                                    script_friendly = 'file {0}'.format(res['file']) if 'file' in res else '"code" value in spec'
                                    if script_svr != script_spec:
                                        print('Script for {0} does not match {1}.'.format(alias, script_friendly))
                                        if updatescripts:
                                            print('Uploading script to {0}...'.format(alias))
                                            rpc.upload_script_content([auth], script_spec, name=name, create=False, filterfn=template)
                                        elif not args['--no-diff']:
                                            # show diff
                                            import difflib
                                            differences = '\n'.join(
                                                difflib.unified_diff(
                                                    script_spec.splitlines(),
                                                    script_svr.splitlines(),
                                                    fromfile=script_friendly,
                                                    tofile='info["description"]["rule"]["script"]'))

                                            print(differences)
                                else:
                                    raise ExoException('Found unsupported type {0} in spec.'.format(typ))
                except Spec401Exception as ex:
                    print("******WARNING******* 401 received in spec, is the device expired?")
                    pass

