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



