

def check_prefix(user, tools):
    chosen = user.strip().lower()
    for key, tool in tools.items():
        if chosen.startswith(key):
            return chosen, tool
    else:
        return None, None