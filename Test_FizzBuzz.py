import unittest
import FizzBuzz

class testCaseAdd(unittest.TestCase):
    def first_test(self):
        #self.assertEqual(FizzBuzz.FizzBuzz(0), "")
        self.assertEqual(FizzBuzz.FizzBuzz(1), "1")

if __name__ == '__main__':
    unittest.main()
