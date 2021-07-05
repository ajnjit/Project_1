from CsvReader import CsvReader

def addition(a, b):
    return int(a) + int(b)

def subtraction(a, b):
    return int(a) - int(b)

def multipication(a, b):
    return int(a) * int(b)

def division(a, b):
    return float(a) / float(b)

def square(a):
    a = int(a) ** 2
    return int(a) ** 2

def squareRoot(a):
    a = float(a) ** 0.5
    return float(a) ** 0.5


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result= multipication(a, b)
        return self.result

    def divide(self, a, b):
        self.result= division(a, b)
        return self. result

    def square(self, a):
        self.result= square(a)
        return self.result

    def squareRoot(self, a):
        self.result= squareRoot(a)
        return self.result
