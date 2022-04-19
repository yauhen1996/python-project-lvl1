
from random import randint, choice


def welcome():
    print('Welcome to the Brain Games!')
    global name
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')


def calc():
    i = 0
    while i < 3:
        list_1 = (randint(20, 30), randint(1, 20))
        list_2 = ('+', '-', '*')
        operation = choice(list_2)
        example = f'{list_1[0]} {operation} {list_1[1]}'
        print(f'Question: {example}')
        answer = input('Your answer: ')
        cor = f"'{answer}' is wrong answer ;(."
        cor_1 = f" Correct answer was '{str(eval(example))}'."
        if str(eval(example)) == answer:
            print('Correct!')
        else:
            return print(cor + cor_1 + f"\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')
