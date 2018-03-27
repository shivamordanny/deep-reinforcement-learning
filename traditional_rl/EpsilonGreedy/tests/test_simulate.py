from unittest import TestCase

import EpsilonGreedy as eg


class TestSimulate(TestCase):
    def test_simulate(self):
        # test the exception raising behaviour
        with self.assertRaises(ValueError):
            eg.simulate(1, 2, 3, epsilon=100, n=999)
            eg.simulate(1, 2, 3, n=-100)

        # test the method
        val = eg.simulate(2, 2, 2, epsilon=0.2, n=3)

        # I have checked that the values are consistent. here, I just check the shape
        # of the obtained cumulative_averages
        self.assertEqual(len(val), 3)