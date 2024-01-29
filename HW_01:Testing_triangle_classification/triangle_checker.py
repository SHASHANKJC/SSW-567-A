import unittest


def classify_triangle(a, b, c):
    # Check for invalid input
    if not all(isinstance(side, (int, float)) for side in (a, b, c)) or any(side <= 0 for side in (a, b, c)):
        return "Invalid input"

    # Check for equilateral triangle
    if a == b == c:
        return "Equilateral"

    # Check for isosceles triangle
    if a == b or b == c or a == c:
        return "Isosceles"

    # Check for right triangle
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        return "Right"

    elif a != b and a != c and c != b:
        return "Scalene"


class TestTriangleClassification(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles")
        self.assertEqual(classify_triangle(4, 3, 3), "Isosceles")
        self.assertEqual(classify_triangle(3, 4, 3), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(5, 4, 8), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(16, 63, 65), "Right")
        self.assertEqual(classify_triangle(5, 12, 13), "Right")
        self.assertEqual(classify_triangle(8, 15, 17), "Right")

    def test_invalid_input(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid input")
        self.assertEqual(classify_triangle(3, "a", 5), "Invalid input")
        self.assertEqual(classify_triangle(-3, 4, 5), "Invalid input")


if __name__ == '__main__':
    unittest.main()
