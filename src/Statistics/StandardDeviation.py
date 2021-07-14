from src.Calculator.Square import square
from src.Calculator.Division import division
from src.Calculator.SquareRoot import squareRoot
from src.Statistics.Mean import mean

def standardDeviation(data):
    mean_data = mean(data)
    num_values = len(data)
    for num in data:
        total = 0
        total = total + square(num - mean_data)
    result = squareRoot(division(total, num_values))
    return result