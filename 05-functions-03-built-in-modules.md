# **Built-in Python Modules: A Beginner’s Guide**

Python's standard library offers an extensive range of built-in modules that make programming tasks easier and more efficient. These modules are available without requiring any additional installation.

---

## **What Are Built-in Modules?**
Built-in modules are Python libraries that provide pre-defined functions and variables for performing common programming tasks, such as file handling, math operations, string manipulation, and more. You can use them by importing the module using the `import` keyword.

---

## **1. File Handling Modules**

### **`os` Module**
The `os` module lets you interact with the operating system.

#### Key Functions:
- `os.getcwd()` – Get the current working directory.
- `os.listdir()` – List the contents of a directory.
- `os.mkdir()` – Create a new directory.
- `os.remove()` – Delete a file.

#### Example:
```python
import os

# Get current working directory
print("Current Directory:", os.getcwd())

# Create a new directory
os.mkdir("test_folder")

# List files in the current directory
print("Directory Contents:", os.listdir())
```

---

### **`shutil` Module**
The `shutil` module provides high-level file operations like copying and moving files.

#### Key Functions:
- `shutil.copy()` – Copy a file.
- `shutil.move()` – Move a file.
- `shutil.rmtree()` – Delete a directory and its contents.

#### Example:
```python
import shutil

# Copy a file
shutil.copy("source.txt", "copy_of_source.txt")

# Move a file
shutil.move("copy_of_source.txt", "moved_source.txt")

# Delete a directory
shutil.rmtree("test_folder")
```

---

## **2. Math Libraries**

### **`math` Module**
The `math` module provides mathematical functions and constants.

#### Key Functions:
- `math.sqrt(x)` – Square root of `x`.
- `math.pow(x, y)` – `x` raised to the power of `y`.
- `math.ceil(x)` – Smallest integer greater than or equal to `x`.
- `math.floor(x)` – Largest integer less than or equal to `x`.
- `math.pi` – Value of Pi.

#### Example:
```python
import math

# Square root
print("Square Root of 16:", math.sqrt(16))

# Power
print("2 to the power of 3:", math.pow(2, 3))

# Rounding up and down
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.7:", math.floor(4.7))

# Value of Pi
print("Value of Pi:", math.pi)
```

---

### **`random` Module**
The `random` module generates random numbers and performs random operations.

#### Key Functions:
- `random.randint(a, b)` – Random integer between `a` and `b`.
- `random.random()` – Random float between 0 and 1.
- `random.choice(seq)` – Random element from a sequence.
- `random.shuffle(seq)` – Shuffle a sequence in place.

#### Example:
```python
import random

# Random integer
print("Random Integer between 1 and 10:", random.randint(1, 10))

# Random float
print("Random Float between 0 and 1:", random.random())

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled Numbers:", numbers)
```

---

## **3. String Manipulation Modules**

### **`string` Module**
The `string` module provides useful constants and functions for string manipulation.

#### Key Constants:
- `string.ascii_letters` – All lowercase and uppercase English letters.
- `string.digits` – All numeric digits (0–9).
- `string.punctuation` – All punctuation characters.

#### Example:
```python
import string

# Constants
print("Letters:", string.ascii_letters)
print("Digits:", string.digits)
print("Punctuation:", string.punctuation)

# Generate a secure password
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
print("Generated Password:", password)
```

---

### **`re` Module**
The `re` module allows you to use regular expressions for pattern matching in strings.

#### Key Functions:
- `re.match(pattern, string)` – Check if a string starts with a pattern.
- `re.search(pattern, string)` – Search for a pattern anywhere in the string.
- `re.sub(pattern, replacement, string)` – Replace a pattern with a replacement.

#### Example:
```python
import re

# Check if a string starts with 'Hello'
if re.match(r"Hello", "Hello, World!"):
    print("Match found!")

# Replace 'World' with 'Python'
modified_string = re.sub(r"World", "Python", "Hello, World!")
print("Modified String:", modified_string)
```

---

## **4. Date and Time Modules**

### **`datetime` Module**
The `datetime` module allows you to work with dates and times.

#### Key Functions:
- `datetime.now()` – Current date and time.
- `datetime.strftime()` – Format date/time into a string.
- `datetime.strptime()` – Parse a string into a date/time object.

#### Example:
```python
from datetime import datetime

# Get current date and time
now = datetime.now()
print("Now:", now)

# Format date into a string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted)

# Parse a string into a datetime object
parsed = datetime.strptime("2024-12-12 10:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed Date:", parsed)
```

---

## **5. Input/Output Modules**

### **`sys` Module**
The `sys` module provides access to system-specific parameters and functions.

#### Key Functions:
- `sys.argv` – List of command-line arguments.
- `sys.exit()` – Exit the program.

#### Example:
```python
import sys

# Print command-line arguments
print("Command-line Arguments:", sys.argv)

# Exit the program
sys.exit("Exiting...")
```

---

### **`pickle` Module**
The `pickle` module serializes and deserializes Python objects for saving to or loading from files.

#### Key Functions:
- `pickle.dump(obj, file)` – Save object to a file.
- `pickle.load(file)` – Load object from a file.

#### Example:
```python
import pickle

# Save data to a file
data = [1, 2, 3]
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

# Load data from a file
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
print("Loaded Data:", loaded_data)
```

---

## **Conclusion: Why Use Built-in Modules?**

### **Advantages of Built-in Modules**
- **Time-Saving**: Eliminates the need to write code from scratch.
- **Pre-Tested**: Reliable and tested by the Python community.
- **Comprehensive**: Covers most programming needs, from math to file handling.

### **How to Use Built-in Modules**
1. Import the module using the `import` keyword.
2. Access the module’s functions and constants using the dot `.` notation.

---
