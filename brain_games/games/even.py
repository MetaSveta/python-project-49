import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_correct_answer():
    number = random.randint(1, 1000)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer
