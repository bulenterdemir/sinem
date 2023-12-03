import unittest
from bodev import isprime, sieve, factorization, euler_phi, gcd # Import the iscoprime function from your program

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

    def test_negative_numbers(self):
        self.assertIsNone(isprime(-1), "Negative numbers should return None")
        self.assertIsNone(isprime(-10), "Negative numbers should return None")

    def test_zero_and_one(self):
        self.assertIsNone(isprime(0), "0 should return None")
        self.assertIsNone(isprime(1), "1 should return None")

    def test_prime_numbers(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for num in prime_numbers:
            self.assertTrue(isprime(num), f"{num} should be identified as a prime number")

    def test_non_prime_numbers(self):
        non_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
        for num in non_prime_numbers:
            self.assertFalse(isprime(num), f"{num} should be identified as a non-prime number")

    def test_large_prime_number(self):
        self.assertTrue(isprime(7919), "7919 should be identified as a prime number")

    def test_large_non_prime_number(self):
        self.assertFalse(isprime(7920), "7920 should be identified as a non-prime number")




    def test_sieve(self):
        # Test case 1: n = 10
        self.assertEqual(sieve(10), [2, 3, 5, 7])

        # Test case 2: n = 2
        self.assertEqual(sieve(2), [2])

        # Test case 3: Edge case, n less than 2
        self.assertIsNone(sieve(1))

        # Test case 4: Edge case, n less than 0
        self.assertIsNone(sieve(-5))


    def test_negative_number(self):
        self.assertIsNone(sieve(-1), "Negative numbers should return None")

    def test_zero_and_one(self):
        self.assertIsNone(sieve(0), "0 should return None")
        self.assertIsNone(sieve(1), "1 should return None")

    def test_prime_generation(self):
        self.assertEqual(sieve(10), [2, 3, 5, 7], "Sieve up to 10 should return primes [2, 3, 5, 7]")
        self.assertEqual(sieve(20), [2, 3, 5, 7, 11, 13, 17, 19], "Sieve up to 20 should return primes [2, 3, 5, 7, 11, 13, 17, 19]")

    def test_large_number(self):
        primes_up_to_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(sieve(100), primes_up_to_100, "Sieve up to 100 should return correct prime numbers")


    def test_factorization(self):
        # Test case 1: Factorization of 24
        self.assertEqual(factorization(24), [[2, 3], [3, 1]])

        # Test case 2: Prime number
        self.assertEqual(factorization(17), [[17, 1]])

        # Test case 3: Edge case, less than 2
        self.assertIsNone(factorization(1))

        # Test case 4: Edge case, less than 0
        self.assertIsNone(factorization(-5))

    def test_negative_and_low_numbers(self):
        self.assertIsNone(factorization(-1), "Negative numbers should return None")
        self.assertIsNone(factorization(0), "0 should return None")
        self.assertIsNone(factorization(1), "1 should return None")

    def test_prime_numbers(self):
        self.assertEqual(factorization(2), [[2, 1]], "Factorization of 2 should be [[2, 1]]")
        self.assertEqual(factorization(3), [[3, 1]], "Factorization of 3 should be [[3, 1]]")
        self.assertEqual(factorization(5), [[5, 1]], "Factorization of 5 should be [[5, 1]]")

    def test_composite_numbers(self):
        self.assertEqual(factorization(4), [[2, 2]], "Factorization of 4 should be [[2, 2]]")
        self.assertEqual(factorization(6), [[2, 1], [3, 1]], "Factorization of 6 should be [[2, 1], [3, 1]]")
        self.assertEqual(factorization(8), [[2, 3]], "Factorization of 8 should be [[2, 3]]")
        self.assertEqual(factorization(100), [[2, 2], [5, 2]], "Factorization of 100 should be [[2, 2], [5, 2]]")

    def test_large_number(self):
        self.assertEqual(factorization(97), [[97, 1]], "Factorization of 97 (a prime number) should be [[97, 1]]")
        self.assertEqual(factorization(99), [[3, 2], [11, 1]], "Factorization of 99 should be [[3, 2], [11, 1]]")




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


    def test_isprime(self):
        # Test case 1: Prime number
        self.assertTrue(isprime(17))

        # Test case 2: Composite number
        self.assertFalse(isprime(15))

        # Test case 3: Edge case, less than 2
        self.assertIsNone(isprime(1))

        # Test case 4: Edge case, less than 0
        self.assertIsNone(isprime(-5))

        # Test case 5: Large prime number
        self.assertTrue(isprime(9973))

        # Test case 6: Large composite number
        self.assertFalse(isprime(10000))

    def test_sieve(self):
        # Test case 1: n = 10
        self.assertEqual(sieve(10), [2, 3, 5, 7])

        # Test case 2: n = 2
        self.assertEqual(sieve(2), [2])

        # Test case 3: Edge case, n less than 2
        self.assertIsNone(sieve(1))

        # Test case 4: Edge case, n less than 0
        self.assertIsNone(sieve(-5))

        # Test case 5: Large value of n
        self.assertEqual(sieve(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_factorization(self):
        # Test case 1: Factorization of 24
        self.assertEqual(factorization(24), [[2, 3], [3, 1]])

        # Test case 2: Prime number
        self.assertEqual(factorization(17), [[17, 1]])

        # Test case 3: Edge case, less than 2
        self.assertIsNone(factorization(1))

        # Test case 4: Edge case, less than 0
        self.assertIsNone(factorization(-5))

        # Test case 5: Factorization of a large composite number
        self.assertEqual(factorization(123456), [[2, 6], [3, 1], [643, 1]])

    def test_euler_phi(self):
        # Test case 1: Euler's Totient function of 10
        self.assertEqual(euler_phi(10), 4)

        # Test case 2: Euler's Totient function of prime number (17)
        self.assertEqual(euler_phi(17), 16)

        # Test case 3: Edge case, less than 1
        self.assertIsNone(euler_phi(0))

        # Test case 4: Edge case, less than 0
        self.assertIsNone(euler_phi(-5))

        # Test case 5: Euler's Totient function of a large number
        self.assertEqual(euler_phi(123456), 41088)

    def test_negative_and_zero(self):
        self.assertIsNone(euler_phi(-1), "Negative numbers should return None")
        self.assertIsNone(euler_phi(0), "0 should return None")

    def test_one(self):
        self.assertEqual(euler_phi(1), 1, "Euler's Totient of 1 should be 1")

    def test_prime_numbers(self):
        self.assertEqual(euler_phi(2), 1, "Euler's Totient of 2 should be 1")
        self.assertEqual(euler_phi(3), 2, "Euler's Totient of 3 should be 2")
        self.assertEqual(euler_phi(5), 4, "Euler's Totient of 5 should be 4")

    def test_composite_numbers(self):
        self.assertEqual(euler_phi(4), 2, "Euler's Totient of 4 should be 2")
        self.assertEqual(euler_phi(6), 2, "Euler's Totient of 6 should be 2")
        self.assertEqual(euler_phi(8), 4, "Euler's Totient of 8 should be 4")
        self.assertEqual(euler_phi(10), 4, "Euler's Totient of 10 should be 4")

    def test_large_number(self):
        self.assertEqual(euler_phi(100), 40, "Euler's Totient of 100 should be 40")
   



    def test_gcd(self):
        # Test case 1: GCD of 12 and 18
        self.assertEqual(gcd(12, 18), 6)

        # Test case 2: GCD of prime numbers (7 and 13)
        self.assertEqual(gcd(7, 13), 1)

        # Test case 3: GCD of a number with itself
        self.assertEqual(gcd(15, 15), 15)

        # Test case 4: GCD of 0 and a number
        self.assertEqual(gcd(0, 8), 8)

        # Test case 5: GCD of two large numbers
        self.assertEqual(gcd(1234567890, 9876543210), 90)


if __name__ == '__main__':
    unittest.main()