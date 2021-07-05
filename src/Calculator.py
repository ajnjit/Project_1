from CsvReader import CsvReader



def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = a - b
    return c

def multipication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c



def square(a):
    a = int(a) ** 2
    return int(a) ** 2


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



    def square(self, a):
        self.result= square(a)
        return self.result