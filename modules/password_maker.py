# -*- coding: utf-8 -*-
import pyperclip
import random


def main():
    adj_list = ['happy', 'sleepy', 'angry', 'sad', 'stupid']
    noun_list = ['dinosaur', 'dragon', 'cat', 'cats', 'dog', 'dogs', 'dragonfly', 'fly', 'lion']
    things = [',', '.', ':', '"', ':', ';', '+', '-', '_', '?']
    number = random.randint(0, 99)
    password = (adj_list[random.randint(0, 4)] + noun_list[random.randint(0, 8)] + str(number) + things[
        random.randint(0, 9)])
    pyperclip.copy(password)
    print(password+'\nCopied, yay!')
