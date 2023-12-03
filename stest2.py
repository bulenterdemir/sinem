import unittest
from sodev import isprime, sieve, factorization, euler_phi, gcd # Import the iscoprime function from your program

class TestMathFunctions(unittest.TestCase):

    def test_isprime(self):
        # Test case 1: Prime number
        self.assertTrue(isprime(17))

        # Test case 2: Composite number
        self.assertFalse(isprime(15))

        # Test case 3: Edge case, less than 2
        self.assertIsNone(isprime(1))

        # Test case 4: Edge case, less than 0
        self.assertIsNone(isprime(-5))

    def test_sieve(self):
        # Test case 1: n = 10
        self.assertEqual(sieve(10), [2, 3, 5, 7])

        # Test case 2: n = 2
        self.assertEqual(sieve(2), [2])

        # Test case 3: Edge case, n less than 2
        self.assertIsNone(sieve(1))

        # Test case 4: Edge case, n less than 0
        self.assertIsNone(sieve(-5))

    def test_factorization(self):
        # Test case 1: Factorization of 24
        self.assertEqual(factorization(24), [[2, 3], [3, 1]])

        # Test case 2: Prime number
        self.assertEqual(factorization(17), [[17, 1]])

        # Test case 3: Edge case, less than 2
        self.assertIsNone(factorization(1))

        # Test case 4: Edge case, less than 0
        self.assertIsNone(factorization(-5))

    def test_euler_phi(self):
        # Test case 1: Euler's Totient function of 10
        self.assertEqual(euler_phi(10), 4)

        # Test case 2: Euler's Totient function of prime number (17)
        self.assertEqual(euler_phi(17), 16)

        # Test case 3: Edge case, less than 1
        self.assertIsNone(euler_phi(0))

        # Test case 4: Edge case, less than 0
        self.assertIsNone(euler_phi(-5))

    def test_gcd(self):
        # Test case 1: GCD of 12 and 18
        self.assertEqual(gcd(12, 18), 6)

        # Test case 2: GCD of prime numbers (7 and 13)
        self.assertEqual(gcd(7, 13), 1)

        # Test case 3: GCD of a number with itself
        self.assertEqual(gcd(15, 15), 15)

        # Test case 4: GCD of 0 and a number
        self.assertEqual(gcd(0, 8), 8)

if __name__ == '__main__':
    unittest.main()
