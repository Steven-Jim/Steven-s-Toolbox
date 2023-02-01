# -*- coding: utf-8 -*-
import random


def main():
    pass


def ai():
    thing = None
    number = random.randint(0, 4)
    if number == 0:
        thing = '■'
    elif number == 1:
        thing = 'pass'
    elif number == 2:
        thing = 'pass'
    elif number == 3:
        thing = 'pass'
    return thing


def start():
    sea = (ai(), ai(), ai(), ai(), ai(),
           ai(), ai(), ai(), ai(), ai(),
           ai(), ai(), ai(), ai(), ai(),
           ai(), ai(), ai(), ai(), ai(),
           ai(), ai(), ai(), ai(), ai())


def hit_action(line_number, number_in_line):
    pass
