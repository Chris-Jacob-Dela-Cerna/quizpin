

def checker(user, options):
    chosen = user.strip().lower()
    for item, option in options.items():
        if chosen == item:
            return option
    return None


def if_yes(user_select):
    chosen = user_select.strip().lower()
    if chosen == "y":
        return True
    return False


def check_quizzes(quizzes):
    return bool(quizzes)


def check_score(score, total):
    percentage = score / total * 100
    if percentage == 100:
        message = "A perfect score, bravo!"
    elif percentage >= 75:
        message = "What a great run!"
    elif percentage == 50:
        message = "Well done! Solid work."
    elif percentage >= 25:
        message = "You're getting there!"
    else:
        message = "A great learning opportunity!"
    length = len(message) + 2
    outline = ""
    for _ in range(length):
        outline += "="
    return message, outline


def check_prefix(user, tools):
    chosen = user.strip().lower()
    for key, tool in tools.items():
        if chosen.startswith(key):
            return chosen, tool
    else:
        return None, None


def check_name(user_file, quizzes):
    file_name = user_file.strip().replace(" ", "_")
    for quiz in quizzes:
        if file_name == quiz[:-4]:
            return False, file_name
        elif file_name == "":
            return None, None
    return True, file_name