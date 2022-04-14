
from random import randint


def welcome():
    print('Welcome to the Brain Games!')
    global name
    name = input('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


num = randint(2, 40)


def prime(num):
    if num == 2 or num == 3:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_1():
    welcome()
    i = 0
    while i < 3:
        num = randint(2, 40)
        print('Question:', num)
        answer = input('Your answer: ')
        if prime(num) is False and answer == 'no' or prime(num) is True and answer == 'yes':
            print('Correct!')
        elif prime(num) is False and answer != 'no':
            return print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.?\nLet's try again, {name}!")
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.?\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')
