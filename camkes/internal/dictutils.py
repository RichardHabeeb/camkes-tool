#
# Copyright 2014, NICTA
#
# This software may be distributed and modified according to the terms of
# the BSD 2-Clause license. Note that NO WARRANTY is provided.
# See "LICENSE_BSD2.txt" for details.
#
# @TAG(NICTA_BSD)
#

'''Various helpers for doing advanced things with dictionaries.'''

import re

def get_fields(s):
    '''Return a set of field names referenced as formatting keys in the given
    string. I thought there would be an easier way to get this, but I can't
    find one. E.g. get_fields('%(hello)s %(world)s') returns
    set('hello', 'world').'''
    return set(re.findall(r'%\(([^)]+)\)', s))

class Guard(object):
    '''Representation of a condition required for some action. See usage in
    Template.py.'''
    def __init__(self, guard_fn):
        self.guard_fn = guard_fn

    def __call__(self, arg):
        return self.guard_fn(arg)
