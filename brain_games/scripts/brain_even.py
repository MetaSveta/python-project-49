import random

import prompt

from brain_games.cli import welcome_user


def play():
    number = random.randint(1, 1_000_000)
    print(f"Question: {number}")
    users_answer = prompt.string("Your answer: ").strip().lower()

    if number % 2 == 0:
        answer = "yes"
    else:
        answer = "no"

    if users_answer == answer:
        print("Correct!")
        return True
    else:
        print(
            f"'{users_answer}' is wrong answer ;(. "
            f"Correct answer was '{answer}'."
        )
        return False


def main():
    name = welcome_user()
    
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds = 3
    for _ in range(rounds):
        if not play():
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
