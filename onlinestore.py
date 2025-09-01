def check_username(name: str):
    if '<' in name:
        return "The character '<' is not allowed, " \
        "to prevent attempts at injecting code through" \
        " the username."
    else:
        if len(name) > 8:
            return "There must be no more than 8 characters."
        else:
                if not name.isalpha():
                    return "Only uppercase and lowercase letters are accepted."
                else:
                     return "Username made."
print(check_username("Ronen19"))