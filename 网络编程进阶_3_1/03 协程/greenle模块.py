#!/usr/bin/env  python3
# coding utf-8

from greenlet import greenlet


def eat(name):
    print('%s eat1 '%name)
    g2.switch('egon')
    print('%s eat 2 ' %name)
    g2.switch()

def play(name):
    print('%s play 1 '%name)
    g1.switch()
    print('%s play 2 ' %name)


g1 = greenlet(eat)
g2 = greenlet(play)

g1.switch('egon')

