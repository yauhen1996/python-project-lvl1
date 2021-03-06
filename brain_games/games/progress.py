from random import randint

import prompt


def welcome():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What number is missing in the progression?')


def progression():
    welcome()
    m = 0
    while m < 3:
        num = (randint(2, 15), randint(16, 35), randint(1, 3))
        num_list = list(range(num[0], num[1], num[2]))
        length_random = randint(0, len(num_list) - 1)
        for n, i in enumerate(num_list):
            if i == num_list[length_random] and len(num_list) == 8:
                num_list[n] = '..'
                print('Question:', *num_list)
                answer = input('Your answer: ')
                if str(i) == answer:
                    print('Correct!')
                else:
                    cor = f"'{answer}' is wrong answer ;(."
                    cor_1 = f"Correct answer was '{str(i)}'."
                    return print(cor + cor_1 + f"\nLet's try again, {name}!")
                m += 1
    return print(f'Congratulations, {name}!')
