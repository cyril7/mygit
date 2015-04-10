# coding=utf-8

'''A simple interface to execute shell commands.

These ideas are taken from fabric/operations.py.

Examples 1: execute local command

    # import command
    # out = command.local('uname -r')
    # print out.stdout
    2.6.32
    # print out.stderr
    ''
    # print out.succeeded
    True

Example 2: execute command in remote host through ssh

    # import command
    # out = command.remote('10.x.x.x', 'uname -r')
    # print out.stdout
    2.6.32

Sum Up:
    out.failed
    out.succeeded
    out.return_code
    out.stdout
    out.stderr
'''
__author__ = 'tuantuan.lv <dangoakachan@foxmail.com>'

import subprocess

# see https://gist.github.com/3883162
from storage import Storage

def remote(ip, cmd, capture = True, timeout = None):
    ssh = "ssh -o StrictHostKeyChecking=no -o LogLevel=quiet -o BatchMode=yes"

    if timeout is not None:
        ssh += ' -o ConnectTimeout=%d' % timeout

    cmd = '%s %s "%s"' % (ssh, ip, cmd)

    return local(cmd, capture)

def local(cmd, capture = True, shell = None):
    out_stream = subprocess.PIPE if capture else None
    err_stream = subprocess.PIPE if capture else None

    p = subprocess.Popen(cmd, shell = True, stdout = out_stream,
            stderr = err_stream, executable = shell)

    (stdout, stderr) = p.communicate()

    out = Storage()

    out.stdout = stdout.strip() if stdout else ""
    out.stderr = stderr.strip() if stdout else ""

    out.cmd = cmd

    out.failed = False
    out.return_code = p.returncode

    if p.returncode != 0:
        out.failed = True

    out.succeeded = not out.failed

    return out

'''
# Taken from web/utils.py
class Storage(dict):
    """
    A Storage object is like a dictionary except `obj.foo` can be used
    in addition to `obj['foo']`.
 
        >>> o = storage(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> o.a
        Traceback (most recent call last):
            ...
        AttributeError: 'a'
    """
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, k:
            raise AttributeError, k
 
    def __setattr__(self, key, value):
        self[key] = value
 
    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            raise AttributeError, k
 
    def __repr__(self):
        return '&lt;storage ' + dict.__repr__(self) + '&gt;'
'''
