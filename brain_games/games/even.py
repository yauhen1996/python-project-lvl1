from random import randint


import prompt


def random_num():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i <= 2:
        num = randint(1, 100)
        print('Question:', num)
        answer = input('Your answer: ')
        answer_yes = 'yes'
        answer_no = 'no'
        if num % 2 == 0 and answer == answer_yes or num % 2 != 0 and answer == answer_no:
            print('Correct!')
        elif num % 2 == 0 and answer != answer_yes:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{answer_yes}'." + "\nLet's try again, {}!".format(name))
        elif num % 2 != 0 and answer != answer_no:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{answer_no}'." + "\nLet's try again, {}!".format(name))
        i += 1
    return print('Congratulations, {}!'.format(name))
