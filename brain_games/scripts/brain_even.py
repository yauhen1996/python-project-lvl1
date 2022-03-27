#! /usr/bin/env python3

from random import randint


import prompt


def random_num():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    correct = "'yes' is wrong answer ;(. Correct answer was 'no'."
    while i <= 2:
        a = randint(1, 100)
        print('Question:', a)
        b = input('Your answer: ')
        if a % 2 == 0 and b == 'yes' or a % 2 != 0 and b == 'no':
            print('Correct!')
            i += 1
        if a % 2 == 0 and b != 'yes' or a % 2 != 0 and b != 'no':
            return print(correct + "\nLet's try again, {}!".format(name))
    return print('Congratulations, {}!'.format(name))


def main():
    random_num()


if __name__ == '__main__':
    main()
