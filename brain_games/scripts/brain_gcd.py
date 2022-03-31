#! /usr/bin/env python3


from random import randint
from math import gcd

import prompt


def nod():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        a = (randint(50 ,90), randint(30, 80))
        print(f'Question: {a[0]} {a[1]}')
        answer = int(input('Your answer: '))
        if int(gcd(a[0], a[1])) == answer:
            print('Correct!')
            i += 1
        else:
            x = f"'{answer}' is wrong answer ;(. Correct answer was '{int(gcd(a[0], a[1]))}'."
            return print(x + "\nLet's try again, {}!".format(name))
    return print('Congratulations, {}!'.format(name))


def main():
    nod()


if __name__ == '__main__':
    main()

