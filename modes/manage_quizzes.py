

import os
from checker.checker import checker
from checker.checker import check_prefix
from checker.checker import check_name
from checker.checker import check_quizzes


def manage_quizzes():
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

    input(
        "\nQuizpin:  Type r-[number] to rename the quiz."
        "\n          Type d-[number] to delete the quiz."
        "\n          Type l- to leave."
        "\n          Example: r-2"
        "\n"
    )

    number = 0
    quiz_list = {}
    print("List of Quizzes:")
    for quiz in quizzes:
        number += 1
        quiz_list.update({str(number): quiz})
        print(f"{number}) {quiz}")
    print()

    tools = {
        "r-": "rename",
        "d-": "delete",
        "l-": "leave",
    }
    while True:
        user = input("User:     ")
        chosen, tool = check_prefix(user, tools)
        if chosen:
            if tool == tools["l-"]:
                break
            else:
                selected_quiz = checker(chosen[2:], quiz_list)
                if selected_quiz:
                    break
                else:
                    print("Quizpin:  Invalid. Please select a valid quiz.")
        else:
            print("Quizpin:  Invalid. Please use the right format.")

    if tool == tools["r-"]:
        rename_file(quiz_path, selected_quiz)
    elif tool == tools["d-"]:
        delete_quiz(quiz_path, selected_quiz)
    else:
        input()


def rename_file(quiz_path, selected_quiz):
    quizzes = os.listdir(quiz_path)
    quizzes.remove(selected_quiz)
    
    print(
        f"Quizpin:  Enter the new name for '{selected_quiz}'."
        "\n          Note: Spaces are replaced by '_'."
    )
    while True:
        user_file = input("User:     ")
        result, file_name = check_name(user_file, quizzes)
        match result:
            case True:
                break
            case False:
                print(f"Quizpin:  '{file_name}.csv' already exists.")
                continue
            case _:
                print("Quizpin:  Invalid. Please enter a valid file name.")
                continue

    old_quiz = os.path.join(quiz_path, selected_quiz)
    new_quiz = os.path.join(quiz_path, file_name + ".csv")
    os.rename(old_quiz, new_quiz)
    input(
        "\n==============="
        "\n File renamed."
        "\n==============="
        "\n"
    )


def delete_quiz(quiz_path, selected_quiz):
    quiz = os.path.join(quiz_path, selected_quiz)
    os.remove(quiz)
    input(
        "\n==============="
        "\n File deleted."
        "\n==============="
        "\n"
    )