

import csv
import os
from utils import validation as val


def create_quiz():
    input(
        "\n================"
        "\n Creating quiz!"
        "\n================"
        "\n"
    )

    print(
        "Quizpin:  Give me the number of items for your quiz."
        "\n          Note: Minimum of 4 items."
    )
    while True:
        user_items = input("User:     ")
        result = check_number(user_items)
        if result:
            break
        else:
            print(f"Quizpin:  Invalid. Please enter a valid number.")
                
    print(
        "\nQuizpin:  For each item. Give me its term and definition"
        "\n          in this format: [Term - Definition]"
        "\n          Note: You cannot repeat a term."
    )
    items = []
    for number in range(result):
        while True:
            user_item = input(f"{number + 1}) ")
            if add_item(user_item, items):
                break
            else:
                print("Quizpin:  Invalid. Please use the right format.")
    
    abs_filedir = os.path.abspath(__file__)
    filedir = os.path.dirname(abs_filedir)
    root = os.path.dirname(filedir)
    quiz_path = os.path.join(root, "quizzes")
    os.makedirs(quiz_path, exist_ok=True)
    quizzes = os.listdir(quiz_path)
    
    print(
        "\nQuizpin:  Name the file you'll be storing your items in."
        "\n          Note: Spaces are replaced by '_'."
    )
    while True:
        user_file = input("User:     ")
        result, file_name = val.check_name(user_file, quizzes)
        match result:
            case True:
                pass
            case False:
                print(
                    f"Quizpin:  '{file_name}.csv' already exists."
                    "\n          Would you like to overwrite? Enter y or n."
                )
                user = input("User:     ")
                if not val.if_yes(user):
                    print("Quizpin:  Name the file you'll be storing your items in.")
                    continue
            case None:
                print("Quizpin:  Invalid. Please enter a valid file name.")
                continue
        csv_path = os.path.join(quiz_path, file_name + ".csv")
        break

    store_items(items, csv_path)
    input(
        "\n========================="
        "\n Quiz saved succesfully."
        "\n========================="
        "\n"
    )


def check_number(user_items):
    try:
        items = int(user_items)
        if items < 4:
            raise ValueError
    except ValueError:
        return None
    else:
        return items


def add_item(user_item, items):
    try:
        term, definition = user_item.split(" - ")
        term = term.strip()
        definition = definition.strip()
        if term == "" or definition == "":
            raise ValueError
        for item in items:
            if term.lower() == item["term"].lower():
                raise ValueError
    except ValueError:
        return False
    else:
        items.append({"term": term, "definition": definition})
        return True


def store_items(items, csv_path):
    with open(csv_path, "w", newline="") as quiz_items:
        writer = csv.DictWriter(quiz_items, fieldnames=["term", "definition"])
        writer.writeheader()
        writer.writerows(items)