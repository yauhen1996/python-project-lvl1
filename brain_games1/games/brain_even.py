
from random import randint


import prompt


def random_num():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    correct_2 = "'yes' is wrong answer ;(. Correct answer was 'no'."
    correct = "'no' is wrong answer ;(. Correct answer was 'yes'."
    while i <= 2:
        a = randint(1, 100)
        print('Question:', a)
        b = input('Your answer: ')
        if a % 2 == 0 and b == 'yes' or a % 2 != 0 and b == 'no':
            print('Correct!')
            i += 1
        if a % 2 == 0 and b != 'yes':                                                                                               return print(correct + "\nLet's try again, {}!".format(name))                                                       if a % 2 != 0 and b != 'no':
            return print(correct_2 + "\nLet's try again, {}!".format(name))
    return print('Congratulations, {}!'.format(name))
