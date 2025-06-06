import operator
import random

RULE = "What is the result of the expression?"

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def get_question_and_correct_answer():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(list(OPERATIONS.keys()))
    question = f"{num1} {op} {num2}"
    result = OPERATIONS[op](num1, num2)
    correct_answer = str(result)
    return question, correct_answer
