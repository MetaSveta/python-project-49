import random

RULE = "What number is missing in the progression?"


def generate_round():
    length = random.randint(5, 10)
    step = random.randint(1, 10)
    start = random.randint(1, 50)

    progression = list(range(start, start + step * length, step))
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(str(x) for x in progression)
    return question, correct_answer
