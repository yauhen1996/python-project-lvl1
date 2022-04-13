
from random import randint


num = randint(2, 50)


def prime(num):
    if num == 2 or num == 3:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_1():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        num = randint(2, 40)
        print('Question:', num)
        answer = input('Your answer: ')
        answer_yes = 'yes'
        answer_no = 'no'
        if prime(num) is False and answer == answer_no:
            print('Correct!')
        elif prime(num) is True and answer == answer_yes:
            print('Correct!')
        elif prime(num) is False and answer != answer_no:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{answer_no}'.?" + "\nLet's try again, {}!".format(name))
        elif prime(num) is True and answer != answer_yes:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{answer_yes}'.?" + "\nLet's try again, {}!".format(name))
        i += 1
    return print('Congratulations, {}!'.format(name))


def main():
    prime_1()


if __name__ == '__main__':
    main()
