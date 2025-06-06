import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 2
MAX_NUMBER = 100


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_question_and_correct_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer
