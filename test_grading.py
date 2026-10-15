import unittest
from grading import calculate_grade


class TestGrading(unittest.TestCase):

    def test_39(self):
        self.assertEqual(calculate_grade(39), "F")

    def test_40(self):
        self.assertEqual(calculate_grade(40), "C")

    def test_59(self):
        self.assertEqual(calculate_grade(59), "C")

    def test_60(self):
        self.assertEqual(calculate_grade(60), "B")

    def test_79(self):
        self.assertEqual(calculate_grade(79), "B")

    def test_80(self):
        self.assertEqual(calculate_grade(80), "A")

    def test_100(self):
        self.assertEqual(calculate_grade(100), "A")

    def test_negative_marks(self):
        with self.assertRaises(ValueError):
            calculate_grade(-1)

    def test_marks_above_100(self):
        with self.assertRaises(ValueError):
            calculate_grade(101)


if __name__ == "__main__":
    unittest.main()
