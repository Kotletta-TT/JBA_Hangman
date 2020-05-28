def what_to_do(instructions):
    number = instructions.find("Simon says")
    if instructions.endswith("Simon says"):
        return f"I {instructions.replace(' Simon says', '')}"
    elif instructions.startswith("Simon says"):
        return f"I {instructions.replace('Simon says ', '')}"
    else:
        return "I won't do it!"