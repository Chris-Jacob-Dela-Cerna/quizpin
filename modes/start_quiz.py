

import csv
import os
from checker.checker import checker
from checker.checker import if_yes
from checker.checker import check_quizzes
from quiz_types.multiple_choice import multiple_choice
from quiz_types.identification import identification


def start_quiz():
    abs_filedir = os.path.abspath(__file__)
    filedir = os.path.dirname(abs_filedir)
    root = os.path.dirname(filedir)
    quiz_path = os.path.join(root, "quizzes")
    os.makedirs(quiz_path, exist_ok=True)
    quizzes = os.listdir(quiz_path)

    if not check_quizzes(quizzes):
        input(
            "Quizpin:  You have not created a quiz yet."
            "\n          Select a) to create a quiz!"
            "\n"
        )
        return None
    
    print(
        "\nQuizpin:  Select a quiz to start. Type the"
        "\n          corresponding number for that quiz."
    )
    number = 0
    quiz_list = {}
    for quiz in quizzes:
        number += 1
        quiz_list.update({str(number): quiz})
        print(f"          {number}) {quiz}")

    while True:
        chosen = input("User:     ")
        result = checker(chosen, quiz_list)
        if result:
            break
        else:
            print("Quizpin:  Invalid. Please select a valid quiz.")
    items = decompile_file(quiz_path, result)

    input(
        "\n================"
        "\n Starting quiz!"
        "\n================"
        "\n"
    )

    quiz_types = {
        "a": "Multiple Choice",
        "b": "Identification",
    }
    print("Quizpin:  Choose a quiz type:")
    for letter, quiz_type in quiz_types.items():
        print(f"          {letter}) {quiz_type}")

    while True:
        chosen = input("User:     ")
        result = checker(chosen, quiz_types)
        if result:
            break
        else:
            print(f"Quizpin:  Invalid. Please enter a valid quiz type.")

    if result == quiz_types["a"]:
        quiz = multiple_choice(items)
    elif result == quiz_types["b"]:
        quiz = identification(items)
    
    print(
        "Quizpin:  Would you like to see the correct answers?"
        "\n          Enter y or n."
    )
    user = input("User:     ")
    if if_yes(user):
        show_results(quiz)


def decompile_file(quiz_path, result):
    items = []
    quiz = os.path.join(quiz_path, result)
    with open(quiz) as quiz_items:
        reader = csv.DictReader(quiz_items)
        for row in reader:
            items.append({"term": row['term'], "definition": row['definition']})
    return items


def show_results(quiz):
    print("\nA. Here are the following questions and answers.")
    number = 0
    for item in quiz:
        number += 1
        print(
            f"{number}) {item['question']}"
            f"\nAnswer: {item['answer']}"
        )
    input()