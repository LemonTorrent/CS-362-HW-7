import unittest
import LeapYear

class testCaseAdd(unittest.TestCase):
    def test4(self):
        self.assertEqual(LeapYear.LeapYear(4), True)

    def test100(self):
        self.assertEqual(LeapYear.LeapYear(100), False)

    def test400(self):
        self.assertEqual(LeapYear.LeapYear(400), True)

    def test0(self):
        self.assertEqual(LeapYear.LeapYear(0), True)

    def test2000(self):
        self.assertEqual(LeapYear.LeapYear(2000), True)

    def test2100(self):
        self.assertEqual(LeapYear.LeapYear(2100), False)

if __name__ == '__main__':
    unittest.main()
