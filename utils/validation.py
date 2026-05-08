

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


def check_name(user_file, quizzes):
    file_name = user_file.strip().replace(" ", "_")
    for quiz in quizzes:
        if file_name == quiz[:-4]:
            return False, file_name
        elif file_name == "":
            return None, None
    return True, file_name