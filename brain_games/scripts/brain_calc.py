import random
import operator
from brain_games.cli import welcome_user, ask_question

def get_calculation():

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
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
    for _ in range(rounds):
        question, correct_answer = get_calculation()
        user_answer = ask_question(question)
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
