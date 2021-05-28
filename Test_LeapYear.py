import unittest
import LeapYear

class testCaseAdd(unittest.TestCase):
    def test4(self):
        self.assertEqual(LeapYear.LeapYear(4), True)

    def test100(self):
        self.assertEqual(LeapYear.LeapYear(100), False)

if __name__ == '__main__':
    unittest.main()
