#! /usr/bin/env/ python3

from random import randint

from math import gcd

import prompt


def welcome():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')


def nod():
    welcome()
    i = 0
    while i < 3:
        num = (randint(50, 90), randint(30, 80))
        print(f'Question: {num[0]} {num[1]}')
        answer = input('Your answer: ')
        gcd_1 = gcd(num[0], num[1])
        try:
            if gcd_1 == int(answer):
                print('Correct!')
            else:
                return print(f"'{answer}' is wrong answer ;(. Correct answer was '{gcd_1}'.\nLet's try again, {name}!")
            i += 1
        except ValueError:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{gcd_1}'.\nLet's try again, {name}!")
    return print(f'Congratulations, {name}!')
