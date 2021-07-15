from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import mean
from src.Statistics.Variance import variance
from src.Statistics.StandardDeviation import standardDeviation
from src.Statistics.zeroDivision import zeroDivision

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def variance (self, data):
        self.result = variance(data)
        return self.result

    def standardDeviation(self, data):
        self.result = standardDeviation(data)
        return self.result

    def zeroDivision(self, data):
        self.result = zeroDivision(data)
        return self.result