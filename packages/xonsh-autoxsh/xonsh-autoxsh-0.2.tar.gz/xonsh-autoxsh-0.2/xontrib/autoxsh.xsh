#!/usr/bin/env xonsh
from xonsh.dirstack import cd as _cd

import os
_AUTHORIZED_FILE = os.path.expanduser('~/.autoxonsh_authorized')
_IGNORE_FILE = os.path.expanduser('~/.autoxonsh_ignore')
del os


def _auto_cd(args, stdin=None):
    import os
    rtn = _cd(args, stdin=stdin)
    target = os.path.join(os.getcwd(), '.autoxsh')
    target = os.path.expanduser(target)
    is_envfile = os.path.isfile(target)
    if not is_envfile:
        return rtn
    # Deal with authorization
    open(_AUTHORIZED_FILE, 'a').close()
    open(_IGNORE_FILE, 'a').close()
    with open(_IGNORE_FILE, 'r') as ignore_file:
        for line in ignore_file.readlines():
            if target in line:
                return rtn
    authorized = False
    with open(_AUTHORIZED_FILE, 'r') as trust_file:
        for line in trust_file.readlines():
            if target in line:
                authorized = True
                break
    if not authorized:
        msg = 'Unauthorized ".autoxsh" file found in this directory. Authorize and invoke? (y/n/ignore): '
        to_authorize = input(msg).lower()
        if "y" in to_authorize:
            authorized = True
            with open(_AUTHORIZED_FILE, 'a') as trust_file:
                trust_file.write('{}\n'.format(target))
        if "ignore" in to_authorize:
            with open(_IGNORE_FILE, 'a') as ignore_file:
                ignore_file.write('{}\n'.format(target))
    if authorized:
        source @(target)
    return rtn

aliases['cd'] = _auto_cd
