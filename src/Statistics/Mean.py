from src.Calculator.Addition import addition
from src.Calculator.Division import division

def mean(data):
    num_values = len(data)
    for num in data:
        total = 0
        total = total + addition (total,num)
    result = division(total, num_values)
    return result
