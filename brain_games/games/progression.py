import random

RULE = "What number is missing in the progression?"

PROGRESSION_MIN_LENGTH = 5
PROGRESSION_MAX_LENGTH = 10
STEP_MIN = 1
STEP_MAX = 10
START_MIN = 1
START_MAX = 50


def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]


def get_question_and_correct_answer():
    length = random.randint(PROGRESSION_MIN_LENGTH, PROGRESSION_MAX_LENGTH)
    step = random.randint(STEP_MIN, STEP_MAX)
    start = random.randint(START_MIN, START_MAX)

    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(str(x) for x in progression)
    return question, correct_answer
