# Integration Testing with `unittest` in Python

Here we build a simple **user registration system** and write integration tests that cover validation, database interaction, and business logic.

---

## Integration Testing?

Integration testing checks how **multiple modules work together** as a system. Unlike unit tests, which test isolated components, integration tests ensure proper **interaction between components**.

---

## Project Structure

```
user_system/
├── auth.py              # Business logic (register_user)
├── db.py                # Simulated in-memory database
├── validator.py         # Email and password validation
└── tests/
    └── test_integration.py  # Integration tests
```

---

### 1. `db.py` – Simulated Database

```python
# db.py
users = {}

def save_user(email, password):
    if email in users:
        return False
    users[email] = password
    return True

def user_exists(email):
    return email in users

def clear_users():
    users.clear()  # For test cleanup
```

---

### 2. `validator.py` – Input Validation

```python
# validator.py
import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def is_strong_password(password):
    return len(password) >= 6
```

---

### 3. `auth.py` – Business Logic

```python
# auth.py
from db import save_user, user_exists
from validator import is_valid_email, is_strong_password

def register_user(email, password):
    if not is_valid_email(email):
        return "Invalid email"
    if not is_strong_password(password):
        return "Weak password"
    if user_exists(email):
        return "User already exists"
    if save_user(email, password):
        return "Registration successful"
    return "Registration failed"
```

---

### 4. `tests/test_integration.py` – Integration Tests

```python
# tests/test_integration.py
import unittest
from auth import register_user
from db import user_exists, clear_users

class TestUserRegistrationIntegration(unittest.TestCase):

    def setUp(self):
        clear_users()  # Reset state before each test

    def test_successful_registration(self):
        result = register_user("user@example.com", "secure123")
        self.assertEqual(result, "Registration successful")
        self.assertTrue(user_exists("user@example.com"))

    def test_invalid_email(self):
        result = register_user("invalid-email", "secure123")
        self.assertEqual(result, "Invalid email")

    def test_weak_password(self):
        result = register_user("user2@example.com", "123")
        self.assertEqual(result, "Weak password")

    def test_duplicate_user(self):
        register_user("user@example.com", "secure123")
        result = register_user("user@example.com", "anotherpass")
        self.assertEqual(result, "User already exists")

if __name__ == "__main__":
    unittest.main()
```

---

##  Run the Integration Tests

From the root directory, run:

```bash
python -m unittest discover -s tests
```

This will find and run all test files inside the `tests/` directory.

---

* Tests check how **`auth.py`**, **`validator.py`**, and **`db.py`** work **together**.
* Each function is **not tested in isolation**—instead, we ensure the **flow and coordination** across modules work as expected.


---
