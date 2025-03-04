import operator
import random

from brain_games.cli import ask_question, welcome_user


def get_calculation():
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    operation = random.choice(list(operations.keys()))
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {operation} {num2}"
    correct_answer = operations[operation](num1, num2)
    return question, str(correct_answer)


def main():
    name = welcome_user()
    rounds = 3
    print("What is the result of the expression?")

    for _ in range(rounds):
        question, correct_answer = get_calculation()
        user_answer = ask_question(question)
        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")

    print(f"Congratulations, {name}!")

