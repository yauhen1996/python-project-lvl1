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
        num_1 = randint(50, 90)
        num_2 = randint(30, 80)
        print(f'Question: {num_1} {num_2}')
        answer = input('Your answer: ')
        gcd_1 = gcd(num_1, num_2)
        if str(gcd_1) == answer:
            print('Correct!')
        else:
            cor = f"'{answer}' is wrong answer ;(."
            cor_1 = f"Correct answer was '{gcd_1}'."
            return print(cor + cor_1 + f"\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')
