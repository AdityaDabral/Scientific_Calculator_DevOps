import math


def evaluate_expression(expression):
    allowed_names = {
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log10,
        "ln": math.log,
        "pi": math.pi,
        "e": math.e
    }

    return eval(expression, {"__builtins__": None}, allowed_names)


class CalculatorMemory:
    def __init__(self):
        self.memory = 0

    def store(self, value):
        self.memory = value

    def recall(self):
        return self.memory

    def clear(self):
        self.memory = 0
