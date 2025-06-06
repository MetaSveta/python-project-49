import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def run_game(game):
    name = welcome_user()
    print(game.RULE)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip()

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
