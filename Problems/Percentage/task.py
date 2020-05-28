def get_percentage(digit, round_digits=None):
    if round_digits == None:
        return f"{round(digit * 100)}%"
    else:
        return f"{round(digit * 100, round_digits)}%"