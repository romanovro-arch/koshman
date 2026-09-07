from main import summ, umnoj, delenie, minus, stepen, chooser
import unittest

class TestCalculatorFunctions(unittest.TestCase):
    def test_summ(self):
        self.assertEqual(summ(2, 3), 5)
        self.assertEqual(summ(-5, 5), 0)
        self.assertEqual(summ(0, 0), 0)
        self.assertEqual(summ(100, 200), 300)

    def test_umnoj(self):
        self.assertEqual(umnoj(2, 3), 6)
        self.assertEqual(umnoj(-2, 3), -6)
        self.assertEqual(umnoj(0, 5), 0)
        self.assertEqual(umnoj(7, 1), 7)

    def test_delenie(self):
        self.assertEqual(delenie(10, 2), 5.0)
        self.assertEqual(delenie(7, 2), 3.5)
        self.assertEqual(delenie(0, 5), 0.0)
        with self.assertRaises(ValueError):
            delenie(5, 0)

    def test_minus(self):
        self.assertEqual(minus(10, 3), 7)
        self.assertEqual(minus(3, 10), -7)
        self.assertEqual(minus(0, 0), 0)
        self.assertEqual(minus(-5, -3), -2)

    def test_stepen(self):
        self.assertEqual(stepen(2, 3), 8)
        self.assertEqual(stepen(5, 0), 1)
        self.assertEqual(stepen(3, 2), 9)
        self.assertEqual(stepen(2, 10), 1024)

    def test_chooser(self):
        self.assertFalse(chooser('0', 0, 0))
        self.assertTrue(chooser('1', 2, 3))
        self.assertTrue(chooser('2', 2, 3))
        self.assertTrue(chooser('3', 6, 2))
        self.assertTrue(chooser('4', 5, 3))
        self.assertTrue(chooser('5', 2, 3))
        self.assertTrue(chooser('9', 0, 0))

class TestCalculatorIntegration(unittest.TestCase):
    def test_chooser_summ(self):
        import io
        import sys
        original_stdout = sys.stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            chooser('1', 2, 3)
            self.assertEqual(captured_output.getvalue().strip(), "2 + 3 = 5")
        finally:
            sys.stdout = original_stdout

    def test_chooser_umnoj(self):
        import io
        import sys
        original_stdout = sys.stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            chooser('2', 2, 3)
            self.assertEqual(captured_output.getvalue().strip(), "2 * 3 = 6")
        finally:
            sys.stdout = original_stdout

    def test_chooser_delenie(self):
        import io
        import sys
        original_stdout = sys.stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            chooser('3', 6, 2)
            self.assertEqual(captured_output.getvalue().strip(), "6 / 2 = 3.0")
        finally:
            sys.stdout = original_stdout

    def test_chooser_minus(self):
        import io
        import sys
        original_stdout = sys.stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            chooser('4', 5, 3)
            self.assertEqual(captured_output.getvalue().strip(), "5 - 3 = 2")
        finally:
            sys.stdout = original_stdout

    def test_chooser_stepen(self):
        import io
        import sys
        original_stdout = sys.stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            chooser('5', 2, 3)
            self.assertEqual(captured_output.getvalue().strip(), "2 ^ 3 = 8")
        finally:
            sys.stdout = original_stdout

if __name__ == "__main__":
    unittest.main()