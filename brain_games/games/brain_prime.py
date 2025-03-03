import random
from brain_games.engine import run_game

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_question():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    return str(number), correct_answer

def main():
    RULE = "Answer 'yes' if given number is prime. Otherwise answer 'no'."
    run_game(RULE, generate_question)

if __name__ == "__main__":
    main()
