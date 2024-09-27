# test_app.py
import unittest
from app import add, Sustract

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        
    def test_Sustract(self):
        self.assertEqual(Sustract(5, 2), 3)


if __name__ == "__main__":
    unittest.main()
