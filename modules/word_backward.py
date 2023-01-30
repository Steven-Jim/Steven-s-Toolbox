# -*- coding: utf-8 -*-
import pyperclip


def main(putin):
    output = putin[::-1]
    pyperclip.copy(output)
    print(output+'\nCopied, yay!')
