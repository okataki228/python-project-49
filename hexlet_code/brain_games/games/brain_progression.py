import random


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(2, 5)
    length = random.randint(5, 10)

    progression = [
        start + step * i for i in range(length)
    ]
    hidden_index = random.randint(0, length - 1)

    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    rounds = 3
    for _ in range(rounds):
        question, correct_answer = generate_progression()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

