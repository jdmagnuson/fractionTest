import unittest

from fraction import Fraction

class TestFractionAddition(unittest.TestCase):
    def test_adds_two_fractions(self):
        result = Fraction(3, 10) + Fraction(4, 10)

        self.assertEqual("7/10", str(result))

    def test_adds_fraction_by_integer(self):
        result = Fraction(3, 4) + 8

        self.assertEqual("35/4", str(result))

    def test_adds_negative_fractions(self):
        result = Fraction(-3, 10) + Fraction(4, 10)

        self.assertEqual("1/10", str(result))

    def test_does_not_modify_operands(self):
        left = Fraction(2, 3)
        right = Fraction(9, 10)

        left + right

        self.assertEqual("2/3", str(left))
        self.assertEqual("9/10", str(right))

    def test_normalizes_result(self):
        result = Fraction(1, 4) + Fraction(1, 4)

        self.assertEqual("1/2", str(result))

    def test_rejects_unsupported_operand_types(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) + "not a fraction"


if __name__ == "__main__":
    unittest.main()