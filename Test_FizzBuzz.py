import unittest
import FizzBuzz

class testCaseAdd(unittest.TestCase):
    def test1(self):
        self.assertEqual(FizzBuzz.FizzBuzz(1), "1 ")

    def test0(self):
        self.assertEqual(FizzBuzz.FizzBuzz(0), "")

    def test3(self):
        self.assertEqual(FizzBuzz.FizzBuzz(3), "1 2 Fizz ")

if __name__ == '__main__':
    unittest.main()
