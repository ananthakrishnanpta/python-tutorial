Let's create a simple **Calculator** class with basic operations:

* Addition
* Subtraction
* Multiplication
* Division

Then we’ll write **unit tests** to test each method using Python’s built-in `unittest` framework.

---

## Project Structure

```bash
calculator_project/
├── calculator.py
└── test_calculator.py
```

---

### `calculator.py` – Main Program

```python
# calculator.py

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
```

---

### `test_calculator.py` – Our Unit Test File

```python
# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
```

---

## How to Run the Tests

1. **Open terminal and navigate to your project directory:**

```bash
cd calculator_project
```

2. **Run the test script using Python:**

```bash
python test_calculator.py
```

You should see output like:

```plaintext
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

Each `.` represents a passed test.

---

## Explanation

* `setUp()` runs before every test method to initialize the `Calculator` object.
* `assertEqual()` checks if the expected and actual values match.
* `assertRaises()` verifies if the exception is properly raised (for divide by zero).

---
---

# `unittest` Assertions Reference with Examples

This section lists the most commonly used assertion methods in Python’s `unittest` framework with simple explanations and examples.

| Assertion                  | Explanation                                  | Example                                            |
| -------------------------- | -------------------------------------------- | -------------------------------------------------- |
| `assertEqual(a, b)`        | Passes if `a == b`                           | `self.assertEqual(2 + 2, 4)`                       |
| `assertNotEqual(a, b)`     | Passes if `a != b`                           | `self.assertNotEqual(5, 3)`                        |
| `assertTrue(x)`            | Passes if `x` is `True`                      | `self.assertTrue(3 < 5)`                           |
| `assertFalse(x)`           | Passes if `x` is `False`                     | `self.assertFalse(10 < 5)`                         |
| `assertIs(a, b)`           | Passes if `a is b` (same object)             | `self.assertIs(obj1, obj1)`                        |
| `assertIsNot(a, b)`        | Passes if `a is not b`                       | `self.assertIsNot(obj1, obj2)`                     |
| `assertIsNone(x)`          | Passes if `x is None`                        | `self.assertIsNone(None)`                          |
| `assertIsNotNone(x)`       | Passes if `x is not None`                    | `self.assertIsNotNone(5)`                          |
| `assertIn(a, b)`           | Passes if `a in b`                           | `self.assertIn(3, [1, 2, 3])`                      |
| `assertNotIn(a, b)`        | Passes if `a not in b`                       | `self.assertNotIn('z', 'abc')`                     |
| `assertGreater(a, b)`      | Passes if `a > b`                            | `self.assertGreater(10, 5)`                        |
| `assertLess(a, b)`         | Passes if `a < b`                            | `self.assertLess(3, 10)`                           |
| `assertGreaterEqual(a, b)` | Passes if `a >= b`                           | `self.assertGreaterEqual(5, 5)`                    |
| `assertLessEqual(a, b)`    | Passes if `a <= b`                           | `self.assertLessEqual(2, 4)`                       |
| `assertAlmostEqual(a, b)`  | Passes if `a ≈ b` (for floats)               | `self.assertAlmostEqual(0.1 + 0.2, 0.3, places=1)` |
| `assertRaises(Exception)`  | Passes if code raises the expected exception | `with self.assertRaises(ZeroDivisionError): 1 / 0` |

---

## Notes

* Use `assertEqual` for comparing values.
* Use `assertRaises` when testing code that should throw exceptions.
* Use `assertIn`/`assertNotIn` for checking membership (like in lists or strings).
* Use `assertAlmostEqual` for comparing floating-point values.

---

## Example

```python
import unittest

class TestExamples(unittest.TestCase):

    def test_assertions(self):
        self.assertEqual(2 * 2, 4)
        self.assertNotEqual(2 + 2, 5)
        self.assertTrue(10 > 1)
        self.assertFalse(0 > 1)
        self.assertIs(None, None)
        self.assertIsNot([], None)
        self.assertIsNone(None)
        self.assertIsNotNone("data")
        self.assertIn("a", "cat")
        self.assertNotIn("z", "cat")
        self.assertGreater(9, 3)
        self.assertLess(3, 9)
        self.assertGreaterEqual(5, 5)
        self.assertLessEqual(5, 5)
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=1)

    def test_exception(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

if __name__ == '__main__':
    unittest.main()
```

---


