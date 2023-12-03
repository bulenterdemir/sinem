import unittest
from bodev import iscoprime  # Import the iscoprime function from your program

class TestIsCoprimeFunction(unittest.TestCase):

    # Basic coprime checks
    def test_basic_coprime_1(self):
        self.assertTrue(iscoprime(3, 4))

    def test_basic_coprime_2(self):
        self.assertTrue(iscoprime(6, 35))

    # Non-coprime checks
    def test_non_coprime_1(self):
        self.assertFalse(iscoprime(6, 8))

    def test_non_coprime_2(self):
        self.assertFalse(iscoprime(15, 25))

    # Negative numbers
    def test_negative_numbers_1(self):
        self.assertTrue(iscoprime(-7, 9))

    def test_negative_numbers_2(self):
        self.assertFalse(iscoprime(-12, -18))

    # Zero and negative combinations
    def test_zero_negative_combinations_1(self):
        self.assertIsNone(iscoprime(0, -5))

    def test_zero_negative_combinations_2(self):
        self.assertIsNone(iscoprime(-5, 0))

    # Identical numbers
    def test_identical_numbers_1(self):
        self.assertFalse(iscoprime(5, 5))

    def test_identical_numbers_2(self):
        self.assertTrue(iscoprime(1, 1))

    # One and non-one
    def test_one_and_non_one_1(self):
        self.assertTrue(iscoprime(1, 9))

    def test_one_and_non_one_2(self):
        self.assertTrue(iscoprime(7, 1))

    # Large numbers
    def test_large_numbers_1(self):
        self.assertFalse(iscoprime(123456, 789012))

    def test_large_numbers_2(self):
        self.assertTrue(iscoprime(123456, 123457))

    # Edge cases
    def test_edge_cases_1(self):
        self.assertIsNone(iscoprime(0, 0))

    def test_edge_cases_2(self):
        self.assertIsNone(iscoprime(0, 1))

    def test_edge_cases_3(self):
        self.assertIsNone(iscoprime(1, 0))

    # Additional tests for thorough coverage
    def test_additional_1(self):
        self.assertTrue(iscoprime(17, 28))

    def test_additional_2(self):
        self.assertFalse(iscoprime(100, 200))

    def test_additional_3(self):
        self.assertTrue(iscoprime(35, 48))

    def test_additional_4(self):
        self.assertFalse(iscoprime(22, 44))

    def test_additional_5(self):
        self.assertFalse(iscoprime(13, 26))

    def test_additional_6(self):
        self.assertFalse(iscoprime(2, 4))

    def test_additional_7(self):
        self.assertTrue(iscoprime(3, 5))

    def test_additional_8(self):
        self.assertFalse(iscoprime(10, 15))

    def test_additional_9(self):
        self.assertTrue(iscoprime(11, 13))

    def test_additional_10(self):
        self.assertFalse(iscoprime(16, 24))

    def test_additional_11(self):
        self.assertTrue(iscoprime(29, 31))

    def test_additional_12(self):
        self.assertFalse(iscoprime(9, 27))

    def test_additional_13(self):
        self.assertTrue(iscoprime(7, 20))

    def test_additional_14(self):
        self.assertFalse(iscoprime(14, 28))

    def test_additional_15(self):
        self.assertTrue(iscoprime(23, 45))

    def test_additional_16(self):
        self.assertFalse(iscoprime(12, 18))

    def test_additional_17(self):
        self.assertTrue(iscoprime(19, 27))

    def test_additional_18(self):
        self.assertFalse(iscoprime(30, 45))

    def test_additional_19(self):
        self.assertTrue(iscoprime(21, 22))

    def test_additional_20(self):
        self.assertFalse(iscoprime(50, 100))

    def test_additional_21(self):
        self.assertTrue(iscoprime(51, 52))

    # Additional edge cases
    def test_additional_edge_cases_1(self):
        self.assertTrue(iscoprime(2, 3))

    def test_additional_edge_cases_2(self):
        self.assertFalse(iscoprime(4, 6))

    def test_additional_edge_cases_3(self):
        self.assertTrue(iscoprime(5, 7))

    def test_additional_edge_cases_4(self):
        self.assertFalse(iscoprime(8, 12))

    def test_additional_edge_cases_5(self):
        self.assertTrue(iscoprime(9, 10))

    def test_small_coprime_numbers(self):
        self.assertTrue(iscoprime(3, 4), "3 and 4 should be coprime")

    def test_small_non_coprime_numbers(self):
        self.assertFalse(iscoprime(4, 6), "4 and 6 should not be coprime")

    def test_prime_numbers(self):
        self.assertTrue(iscoprime(17, 19), "17 and 19 should be coprime")

    def test_one_is_one(self):
        self.assertTrue(iscoprime(1, 7), "1 and any number should be coprime")

    def test_negative_numbers(self):
        self.assertTrue(iscoprime(-3, 4), "Negative and positive numbers can be coprime")
        self.assertFalse(iscoprime(-6, 9), "Negative and positive numbers can be non-coprime")

    def test_with_zero(self):
        self.assertFalse(iscoprime(0, 5), "Zero and any number should not be coprime")

    def test_large_numbers(self):
        self.assertFalse(iscoprime(123456789, 987654321), "Large coprime numbers")
        self.assertFalse(iscoprime(1234567890, 987654321), "Large non-coprime numbers")

    def test_very_large_numbers(self):
        self.assertTrue(iscoprime(10*18 + 7, 10*18 + 9), "Very large coprime numbers")
        self.assertFalse(iscoprime(10*18, 10*18 + 10), "Very large non-coprime numbers")



    def test_same_prime_numbers(self):  
        self.assertFalse(iscoprime(13, 13), "Same prime numbers should not be coprime")

    def test_same_non_prime_numbers(self):
        self.assertFalse(iscoprime(15, 15), "Same non-prime numbers should not be coprime")

    def test_one_and_negative_number(self):
        self.assertTrue(iscoprime(1, -13), "1 and any negative number should be coprime")

    def test_two_negative_numbers(self):
        self.assertFalse(iscoprime(-15, -25), "Two negative non-coprime numbers")
        self.assertTrue(iscoprime(-17, -19), "Two negative coprime numbers")

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            iscoprime(3.5, 5)
            iscoprime('3', 5)

    def test_large_non_prime_numbers(self):
        self.assertFalse(iscoprime(123456789012345, 987654321987654), "Large non-prime non-coprime numbers")
        self.assertTrue(iscoprime(123456789012349, 987654321987659), "Large non-prime coprime numbers")


if __name__ == '__main__':
    unittest.main()