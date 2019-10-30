#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


"""

names = ['kevin','black girl','peiqi']

def change_name():
    del names[2]
    names[1] = '黑姑娘'
    print(names)


change_name()

print(names)