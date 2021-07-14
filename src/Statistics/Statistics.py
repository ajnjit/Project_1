from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import mean
from src.Statistics.Variance import variance

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
