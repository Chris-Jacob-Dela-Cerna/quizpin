# Document: This python is my 2nd application of CS50P Week 6.

import sys
from quizpin.utils.validation import checker
from modes.create_quiz import create_quiz
from modes.start_quiz import start_quiz
from modes.manage_quizzes import manage_quizzes


def main():
    input(
        "\n====================="
        "\n Welcome to Quizpin!"
        "\n====================="
        "\n"
    )

    while True:
        modes = {
            "a": "Create Quiz Items",
            "b": "Start a Quiz",
            "c": "Manage Quizzes",
            "d": "Quit",
        }
        print("Quizpin:  Choose a mode:")
        for letter, mode in modes.items():
            print(f"          {letter}) {mode}")

        while True:
            chosen = input("User:     ")
            result = checker(chosen, modes)
            if result:
                break
            else:
                print(f"Quizpin:  Invalid. Please enter a valid mode.")

        if result == modes["a"]:
            create_quiz()
        elif result == modes["b"]:
            start_quiz()
        elif result == modes["c"]:
            manage_quizzes()
        elif result == modes["d"]:
            print(
                "Quizpin:  Thank you for using Quizpin."
                "\n"
                "\n============"
                "\n Goodbye :)"
                "\n============"
                "\n"
            )
            sys.exit()


if __name__ == "__main__":
    main()