#! /usr/bin/env python3


from random import randint

import prompt


num = randint(2, 50)


def prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_1(num):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        num = randint(2, 40)
        print('Question:', num)
        answer = input('Your answer: ')
        if (prime(num) is False and answer == 'no') or (prime(num) is True and answer == 'yes'):
            print('Correct!')
        elif prime(num) is False and answer == 'yes':
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.?" + "\nLet's try again, {}!".format(name))
        elif prime(num) is True and answer == 'no':
            return print(f"'no' is wrong answer ;(. Correct answer was 'yes'.?" + "\nLet's try again, {}!".format(name))
        i += 1
    return print('Congratulations, {}!'.format(name))


def main():
    prime_1(num)


if __name__ == '__main__':
    main()
