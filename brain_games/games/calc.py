
from random import randint, choice


def welcome():
    print('Welcome to the Brain Games!')
    global name
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')


def calc():
    welcome()
    i = 0
    while i < 3:
        list_1 = (randint(20, 30), randint(1, 20))
        list_2 = ('+', '-', '*')
        operation = choice(list_2)
        example = f'{list_1[0]} {operation} {list_1[1]}'
        print(f'Question: {example}')
        answer = input('Your answer: ')
        half = f"'{answer}' is wrong answer ;(. Correct answer was '{eval(example)}'."
        try:
            if eval(example) == int(answer):
                print('Correct!')
            elif eval(example) != int(answer):
                return print(half + "\nLet's try again, {}!".format(name))
            i += 1
        except ValueError:
            return print(half + "\nLet's try again, {}!".format(name))
    return print('Congratulations, {}!'.format(name))
