from random import randint


import prompt


def welcome():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')


def random_num():
    welcome()
    i = 0
    while i < 3:
        num = randint(1, 100)
        print('Question:', num)
        answer = input('Your answer: ')
        yes = 'yes'
        no = 'no'
        cor = f"'{answer}' is wrong answer ;(."
        cor_1 = f"Correct answer was '{yes}'."
        cor_2 = f"Correct answer was '{no}'."
        if num % 2 == 0 and answer == yes or num % 2 != 0 and answer == no:
            print('Correct!')
        elif num % 2 == 0 and answer != yes:
            return print(cor + cor_1 + f"\nLet's try again, {name}!")
        else:
            return print(cor + cor_2 + f"\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')
