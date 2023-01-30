# -*- coding: utf-8 -*-
# This is Steven's Toolbox version [alpha]
# Visit website www.github.com/Steven-Jim
from modules import password_maker, word_backward

tools = ['word_backward', 'password_maker']
print('Welcome to Steven\'s Toolbox! We now have ' + str(len(tools)) + ' tools. They are: ' + str(tools))
tool = input('please choose tool')
if tool == 'word_backward':
    word_backward.main(input('word?'))
elif tool == 'password_maker':
    password_maker.main()
