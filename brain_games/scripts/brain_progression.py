#! /usr/bin/env python3

from random import randint

import prompt


def pro():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    m = 0
    while m < 3:
        a = (randint(2, 15), randint(16, 35), randint(1, 3))
        b = list(range(a[0], a[1], a[2]))
        x = randint(0, len(b) - 1)
        for n, i in enumerate(b):
            if i == b[x]:
                b[n] = '..'
                if len(b) > 5 and len(b) < 10:
                    print('Question:', *b)
                    answer = int(input('Your answer: '))
                    if i == answer:
                        print('Correct!')
                        m += 1
                    elif i != answer:
                        return print(f"'{answer}' is wrong answer ;(. Correct answer was '{i}'." + "\nLet's try again, {}!".format(name))
    return print('Congratulations, {}!'.format(name))


def main():
    pro()


if __name__ == '__main__':
    main()
