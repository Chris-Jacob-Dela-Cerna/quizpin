

def check_score(score, total):
    percentage = score / total * 100
    if percentage == 100:
        message = "A perfect score, bravo!"
    elif percentage >= 75:
        message = "What a great run!"
    elif percentage >= 50:
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