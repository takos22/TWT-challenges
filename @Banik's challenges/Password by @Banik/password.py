def security(password: str):
    if len(password) < 7:
        return "Weak"
    number = 0
    special = 0
    for c in password:
        if c.isdigit():
            number += 1
        if c in ["!", "@", "#", "$", "%", "&", "*"]:
            special += 1
        if number >= 2 and special >= 2:
            return "Strong"
    return "Weak"
