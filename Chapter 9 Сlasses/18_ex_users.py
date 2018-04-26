# -*- coding: utf-8 -*-

from collections import OrderedDict
users = OrderedDict()

users['efermi'] = 'fermi'
users['alekset'] = 'kochetov'

for key, value in users.items():
    print("\nKey: " + key)
    print("Value: " + value)