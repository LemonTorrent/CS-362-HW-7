import unittest
import LeapYear

class testCaseAdd(unittest.TestCase):
    def test4(self):
        self.assertEqual(LeapYear.LeapYear(4), True)

if __name__ == '__main__':
    unittest.main()
