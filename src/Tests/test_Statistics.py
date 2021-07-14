import unittest
from numpy.random import seed
from numpy.random import randint
from src.Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(4)
        self.testData = randint(1, 10, 10)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertAlmostEqual(self.statistics.mean(self.testData), mean)
        self.assertAlmostEqual(self.statistics.result, mean)

    def test_variance_calculator(self):
        variance = self.statistics.variance(self.testData)
        self.assertAlmostEqual(self.statistics.variance(self.testData), variance)
        self.assertAlmostEqual(self.statistics.result, variance)




if __name__ == '__main__':
    unittest.main()