#! /usr/bin/env python3

from random import randint, choice


import prompt


def calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        list_1 = (randint(20, 30), randint(1, 20))
        list_2 = ('+', '-', '*')
        operation = choice(list_2)
        su = f'{list_1[0]} {operation} {list_1[1]}'
        print(f'Question: {su}')
        a = int(input('Your answer: '))
        if eval(su) == a:
            print('Correct!')
            i += 1
        else:
            cor = f"'{a}' is wrong answer ;(. Correct answer was '{eval(su)}'."
            return print(cor + "\nLet's try again, {}".format(name))
    return print('Congratulations, {}!'.format(name))


def main():
    calc()


if __name__ == '__main__':
    main()
