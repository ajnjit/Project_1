from src.Calculator.Division import division


try:
    def zeroDivision(data):
        for num in data:
            total = 0
            total = total + division(num, 0)
        result = division(num, 0)
        return result

except ZeroDivisionError:
    print("There is a value error:", ValueError)

