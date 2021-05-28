import unittest
import FizzBuzz

class testCaseAdd(unittest.TestCase):
    def test1(self):
        self.assertEqual(FizzBuzz.FizzBuzz(1), "1 ")

    def test0(self):
        self.assertEqual(FizzBuzz.FizzBuzz(0), "")

if __name__ == '__main__':
    unittest.main()
