

import random
from checker.checker import check_score


def multiple_choice(quiz_items):
    quiz = convert_multiple_choice(quiz_items)
    random.shuffle(quiz)

    input(
        "\nQ. Read each item carefully."
        "\n   Choose the letter of the correct/best answer."
        "\n   Write only the letter that corresponds to your choice."
        "\n"
    )

    score = 0
    idx = 0
    for item in quiz:
        idx += 1
        print(f"{idx}) {item['question']}")
        for letter, choice in item["choices"].items():
            print(f"{letter}. {choice}")
        user_answer = input("User:     ").strip().lower()
        try:
            if item["choices"][user_answer] == item["answer"]:
                score += 1
        except KeyError:
            pass
    
    message, outline = check_score(score, idx)
    input(
        f"\n{outline}"
        f"\n {message}"
        f"\n You got {score}/{idx}."
        f"\n{outline}"
        "\n"
    )
    return quiz


def convert_multiple_choice(quiz_items):
    quiz = []
    all_terms = [item["term"] for item in quiz_items if item["term"]]
    for item in quiz_items:
        question = item["definition"]
        answer = item["term"]
        problem = {"question": question, "answer": answer, "choices": {}}

        terms = [term for term in all_terms if term != answer]

        choices = [answer]
        choices.extend(random.sample(terms, 3))
        random.shuffle(choices)

        letters = "abcd"
        problem["choices"].update(zip(letters, choices))
        quiz.append(problem)
    return quiz