# -*- coding: utf-8 -*-
# This is Steven's Toolbox version [alpha]
# Visit website www.github.com/Steven-Jim
from modules import Battle_Ship_No_GUI, password_maker, word_backward


def check():
    if tool == 'word_backward':
        word_backward.main(input('word?'))
    elif tool == 'password_maker':
        password_maker.main()
    elif tool == 'Battle_Ship_No_GUI':
        Battle_Ship_No_GUI.main()
    else:
        print('hi the worst speller in town!')
        check()


tools = ['word_backward', 'password_maker', 'Battle_Ship_No_GUI']
print('Welcome to Steven\'s Toolbox! We now have ' + str(len(tools)) + ' tools. They are: ' + str(tools))
tool = input('please choose tool')
check()
