def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "ERROR: Can't divide by zero"
