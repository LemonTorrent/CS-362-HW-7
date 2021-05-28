import unittest
import FizzBuzz

class testCaseAdd(unittest.TestCase):
    def test_test(self):
        self.assertEqual(FizzBuzz.FizzBuzz(1), "1 ")

        #self.assertEqual(FizzBuzz.FizzBuzz(0), "")

if __name__ == '__main__':
    unittest.main()
