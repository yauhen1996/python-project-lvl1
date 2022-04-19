
from random import randint


def welcome():
    print('Welcome to the Brain Games!')
    global name
    name = input('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


num = randint(2, 40)


def prim(num):
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
        ans = input('Your answer: ')
        yes = 'yes'
        no = 'no'
        cor = f"'{ans}' is wrong answer ;(."
        cor_1 = f"Correct answer was "
        if prim(num) is False and ans == no or prim(num) is True and ans == no:
            print('Correct!')
        elif prim(num) is False and ans != no:
            return print(cor + cor_1 + f"'{no}'\nLet's try again, {name}!")
        else:
            return print(cor + cor_1 + f"'{yes}'\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')
