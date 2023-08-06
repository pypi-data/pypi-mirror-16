#   Copyright Red Hat, Inc. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

from decorator import decorator

import cachetclient.client as client
import cachetclient.exceptions as exceptions


@decorator
def api_token_required(f, *args, **kwargs):
    try:
        if args[0].api_token is None:
            raise AttributeError('Parameter api_token is required.')
    except AttributeError:
        raise AttributeError('Parameter api_token is required.')

    return f(*args, **kwargs)


def check_required_args(required_args, args):
    for arg in required_args:
        if arg not in args:
            raise KeyError('Required argument: %s' % arg)


class Cachet(client.CachetClient):
    """
    Wrapper library around the available API calls for the admin.ci.centos.org
    node infrastructure.
    """
    def __init__(self, **kwargs):
        super(Cachet, self).__init__(**kwargs)

    # Default to unimplemented methods
    def delete(self, **kwargs):
        raise exceptions.UnimplementedException

    def get(self, **kwargs):
        raise exceptions.UnimplementedException

    def post(self, **kwargs):
        raise exceptions.UnimplementedException

    def put(self, **kwargs):
        raise exceptions.UnimplementedException


class Ping(Cachet):
    def __init__(self, **kwargs):
        super(Ping, self).__init__(**kwargs)

    def get(self, **kwargs):
        return self._get('ping')


class Version(Cachet):
    def __init__(self, **kwargs):
        super(Version, self).__init__(**kwargs)

    def get(self, **kwargs):
        return self._get('version')


class Components(Cachet):
    def __init__(self, **kwargs):
        super(Components, self).__init__(**kwargs)

    @api_token_required
    def delete(self, id):
        return self._delete('components/%s' % id)

    def get(self, id=None, **kwargs):
        if id is not None:
            return self._get('components/%s' % id)
        else:
            return self._get('components')

    @api_token_required
    def post(self, **kwargs):
        # default values
        kwargs.setdefault('enabled', kwargs.get('enabled', True))

        required_args = ['name', 'status', 'enabled']
        check_required_args(required_args, kwargs)

        return self._post('components', data=kwargs)

    @api_token_required
    def put(self, **kwargs):
        required_args = ['id']
        check_required_args(required_args, kwargs)

        return self._put('components/%s' % kwargs['id'], data=kwargs)


class Groups(Cachet):
    def __init__(self, **kwargs):
        super(Groups, self).__init__(**kwargs)

    @api_token_required
    def delete(self, id):
        return self._delete('components/groups/%s' % id)

    def get(self, id=None, **kwargs):
        if id is not None:
            return self._get('components/groups/%s' % id, data=kwargs)
        else:
            return self._get('components/groups', data=kwargs)

    @api_token_required
    def post(self, **kwargs):
        required_args = ['name']
        check_required_args(required_args, kwargs)

        return self._post('components/groups', data=kwargs)

    @api_token_required
    def put(self, **kwargs):
        required_args = ['id']
        check_required_args(required_args, kwargs)

        return self._put('components/groups/%s' % kwargs['id'], data=kwargs)


class Incidents(Cachet):
    def __init__(self, **kwargs):
        super(Incidents, self).__init__(**kwargs)

    @api_token_required
    def delete(self, id):
        return self._delete('incidents/%s' % id)

    def get(self, id=None, **kwargs):
        if id is not None:
            return self._get('incidents/%s' % id, data=kwargs)
        else:
            return self._get('incidents', data=kwargs)

    @api_token_required
    def post(self, **kwargs):
        # default values
        kwargs.setdefault('visible', kwargs.get('visible', True))
        kwargs.setdefault('notify', kwargs.get('notify', False))

        required_args = ['name', 'message', 'status', 'visible', 'notify']
        check_required_args(required_args, kwargs)

        return self._post('incidents', data=kwargs)

    @api_token_required
    def put(self, **kwargs):
        required_args = ['id']
        check_required_args(required_args, kwargs)

        return self._put('incidents/%s' % kwargs['id'], data=kwargs)
