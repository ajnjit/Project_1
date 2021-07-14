
from src.CsvReader.CsvReader import CsvReader
from src.Calculator.Subtraction import subtraction
from src.Calculator.Addition import addition
from src.Calculator.Multiplication import multiplication
from src.Calculator.Division import division
from src.Calculator.Square import square
from src.Calculator.SquareRoot import squareRoot
from src.Statistics.Mean import mean


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
        self.result= multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result= division(a, b)
        return self. result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareRoot(self, a):
        self.result = squareRoot(a)
        return self.result

    def mean(self, a):
        self.result = mean(a)
        return self.result