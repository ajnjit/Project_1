from src.Calculator.Division import division
from src.Calculator.Square import square
from src.Statistics.Mean import mean

def variance(data):
    mean_data = mean(data)
    num_values = len(data)
    for num in data:
        total = 0
        total = total + square(num - mean_data)
    result = division(total, num_values)
    return result