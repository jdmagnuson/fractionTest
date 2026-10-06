import unittest

from fraction import Fraction


class TestFractionMultiplication(unittest.TestCase):
    def test_multiplies_two_fractions(self):
        result = Fraction(2, 3) * Fraction(9, 10)

        self.assertEqual("3/5", str(result))

    def test_multiplies_fraction_by_integer(self):
        result = Fraction(3, 4) * 8

        self.assertEqual("6", str(result))

    def test_multiplies_by_zero(self):
        result = Fraction(7, 12) * 0

        self.assertEqual("0", str(result))

    def test_multiplies_negative_fractions(self):
        result = Fraction(-2, 3) * Fraction(9, -4)

        self.assertEqual("3/2", str(result))

    def test_does_not_modify_operands(self):
        left = Fraction(2, 3)
        right = Fraction(9, 10)

        left * right

        self.assertEqual("2/3", str(left))
        self.assertEqual("9/10", str(right))

    def test_rejects_unsupported_operand_types(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) * "not a fraction"

    def test_normalizes_result(self):
        result = Fraction(1, 4) * Fraction(2, 3)

        self.assertEqual("1/6", str(result))


if __name__ == "__main__":
    unittest.main()
