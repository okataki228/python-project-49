import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ").strip()
    print(f"Hello, {name}!")
    return name


def ask_question(question):
    """Функция для запроса ответа у пользователя"""
    return prompt.string(f"Question: {question}\nYour answer: ").strip()
