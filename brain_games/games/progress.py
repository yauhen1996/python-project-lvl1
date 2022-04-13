from random import randint

import prompt


def progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What number is missing in the progression?')
    m = 0
    while m < 3:
        num = (randint(2, 15), randint(16, 35), randint(1, 3))
        num_list = list(range(num[0], num[1], num[2]))
        length_random = randint(0, len(num_list) - 1)
        for n, i in enumerate(num_list):
            try:
                if i == num_list[length_random] and len(num_list) == 8:
                    num_list[n] = '..'
                    print('Question:', *num_list)
                    answer = input('Your answer: ')
                    if i == int(answer):
                        print('Correct!')
                    else:
                        return print(f"'{int(answer)}' is wrong answer ;(. Correct answer was '{i}'." + "\nLet's try again, {}!".format(name))
                    m += 1
            except ValueError:
                return print(f"'{answer}' is wrong answer ;(. Correct answer was '{i}'." + "\nLet's try again, {}!".format(name))
    return print('Congratulations, {}!'.format(name))
