import unittest
import FizzBuzz

class testCaseAdd(unittest.TestCase):
    def test1(self):
        self.assertEqual(FizzBuzz.FizzBuzz(1), "1 ")

    def test0(self):
        self.assertEqual(FizzBuzz.FizzBuzz(0), "")

    def test3(self):
        self.assertEqual(FizzBuzz.FizzBuzz(3), "1 2 Fizz ")

    def test5(self):
        self.assertEqual(FizzBuzz.FizzBuzz(5), "1 2 Fizz 4 Buzz ")

    def test15(self):
        self.assertEqual(FizzBuzz.FizzBuzz(15), "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz ")

if __name__ == '__main__':
    unittest.main()
