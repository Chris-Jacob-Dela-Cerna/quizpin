

import random
from checker.checker import check_score


def identification(quiz_items):
    quiz = convert_identification(quiz_items)
    random.shuffle(quiz)

    input(
        "\nQ. Read each statement carefully."
        "\n   Identify the term or concept being described "
        "\n   and write your answer in the space provided."
        "\n"
    )

    score = 0
    idx = 0
    for item in quiz:
        idx += 1
        print(f"{idx}) {item['question']}")
        user_answer = input("User:     ").strip().lower()
        if user_answer == item["answer"].strip().lower():
            score += 1

    message, outline = check_score(score, idx)
    input(
        f"\n{outline}"
        f"\n {message}"
        f"\n You got {score}/{idx}."
        f"\n{outline}"
        "\n"
    )
    return quiz


def convert_identification(quiz_items):
    quiz = []
    for item in quiz_items:
        question = item["definition"]
        answer = item["term"]
        problem = {"question": question, "answer": answer}
        quiz.append(problem)
    return quiz