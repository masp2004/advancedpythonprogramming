def classify_number(num):
    if num < 0:
        if num % 2 == 0:
            return "Negative even"
        else:
            return "Negative odd"
    elif num > 0:
        if num % 2 == 0:
            return "Positive even"
        else:
            return "Positive odd"
    else:
        return "Zero"