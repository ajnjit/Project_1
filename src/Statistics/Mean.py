from src.Calculator.Addition import addition
from src.Calculator.Division import division

def mean(num):
    num_values = len(num)
    total = sum(num)
    return float(division(total, num_values))
