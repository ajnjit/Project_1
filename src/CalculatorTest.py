import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator,Calculator)

    def test_add(self):
        test_data = CsvReader('/src/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Results']))
            self.assertEqual(self.calculator.result, int(row['Results']))


    def test_subtract(self):
        test_data = CsvReader('/src/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Results']))
            self.assertEqual(self.calculator.result, int(row['Results']))

    def test_multiply(self):
        test_data = CsvReader('/src/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Results']))
            self.assertEqual(self.calculator.result, int(row['Results']))




if __name__ == '__main__':
    unittest.main()


