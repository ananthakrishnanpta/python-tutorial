# Control Flow in Python

Control flow statements are used to determine the execution path of a program based on conditions or repeated execution of code blocks. Python provides several control flow statements to handle decision-making and looping.

---

## Conditional Statements
Conditional statements allow the program to make decisions based on certain conditions.

### 1. `if` Statement
The simplest form of decision-making, the `if` statement, executes a block of code if a condition is true.

#### Syntax
```python
if condition:
    # Code to execute if condition is true
```

#### Example: Check for Positive Number
```python
x = 10
if x > 0:
    print("Positive")
```
**Output:**
```
Positive
```

---

### 2. `if-else` Statement
Includes an alternate block of code if the condition is false.

#### Syntax
```python
if condition:
    # Code to execute if condition is true
else:
    # Code to execute if condition is false
```

#### Example: Check for Positive or Negative Number
```python
x = -5
if x > 0:
    print("Positive")
else:
    print("Negative")
```
**Output:**
```
Negative
```

---

### 3. `if-elif-else` Statement
For multiple conditions, use `elif` (short for "else if").

#### Syntax
```python
if condition1:
    # Code for condition1
elif condition2:
    # Code for condition2
else:
    # Code if none of the conditions are true
```

#### Example: Categorize Number
```python
x = 0
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```
**Output:**
```
Zero
```

---

### 4. Nested `if`
You can nest `if` statements inside each other for more complex conditions.

#### Example: Eligibility for Loan
```python
age = 25
income = 50000
if age > 18:
    if income > 30000:
        print("Eligible for loan")
    else:
        print("Not eligible due to low income")
else:
    print("Not eligible due to age")
```
**Output:**
```
Eligible for loan
```

---

### 5. Ternary Operator (Conditional Expression)
Python allows a shorthand for `if-else` using a ternary operator.

#### Syntax
```python
value_if_true if condition else value_if_false
```

#### Example: Finding Maximum
```python
a, b = 10, 20
max_value = a if a > b else b
print("Maximum:", max_value)
```
**Output:**
```
Maximum: 20
```

---

## Match-Case Statement
Introduced in Python 3.10, the `match` statement provides a pattern-matching mechanism.

### 1. Basic `match` Example
#### Syntax
```python
match variable:
    case pattern1:
        # Code block for pattern1
    case pattern2:
        # Code block for pattern2
    case _:
        # Default code block
```

#### Example: Simple Matching
```python
def weekday(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case _:
            return "Invalid day"

print(weekday(2))
```
**Output:**
```
Tuesday
```

---

### 2. Nested `match` Example
You can nest `match` statements to handle complex scenarios.

#### Example: Categorize Vehicle
```python
def vehicle_type(vehicle, wheels):
    match vehicle:
        case "car":
            match wheels:
                case 4:
                    return "Standard Car"
                case _:
                    return "Unknown Car Type"
        case "bike":
            match wheels:
                case 2:
                    return "Motorbike"
                case 3:
                    return "Trike"
                case _:
                    return "Unknown Bike Type"
        case _:
            return "Unknown Vehicle"

print(vehicle_type("car", 4))
```
**Output:**
```
Standard Car
```

---

## Loops
Loops are used for repetitive execution of code blocks.

### 1. `for` Loop
The `for` loop iterates over a sequence (list, tuple, string, etc.) or range of numbers.

#### Syntax
```python
for variable in sequence:
    # Code to execute for each element
```

#### Example: Iterating Over a List
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
**Output:**
```
apple
banana
cherry
```

#### Example: Using `range()`
```python
for i in range(5):
    print("Number:", i)
```
**Output:**
```
Number: 0
Number: 1
Number: 2
Number: 3
Number: 4
```

#### Nested `for` Loop Example
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()
```
**Output:**
```
(1, 1) (1, 2) (1, 3) 
(2, 1) (2, 2) (2, 3) 
(3, 1) (3, 2) (3, 3) 
```

#### Use Case: Factorial of a Number
```python
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")
```
**Output:**
```
Factorial of 5 is 120
```

---

### 2. `while` Loop
The `while` loop continues execution as long as the condition is true.

#### Syntax
```python
while condition:
    # Code to execute while condition is true
```

#### Example: Count Down
```python
count = 5
while count > 0:
    print(count)
    count -= 1
```
**Output:**
```
5
4
3
2
1
```

#### Nested `while` Loop Example
```python
row, col = 1, 1
while row <= 3:
    while col <= 3:
        print(f"({row}, {col})", end=" ")
        col += 1
    print()
    row += 1
    col = 1
```
**Output:**
```
(1, 1) (1, 2) (1, 3) 
(2, 1) (2, 2) (2, 3) 
(3, 1) (3, 2) (3, 3) 
```

#### Dangers of Infinite Loops
An infinite loop occurs when the terminating condition of a `while` loop never becomes false. This can freeze your program.

#### Example: Infinite Loop
```python
while True:
    print("This will run forever!")
```
To avoid infinite loops:
- Ensure the condition will eventually evaluate to `False`.
- Use break statements if necessary.

#### Example: Controlled Infinite Loop
```python
while True:
    response = input("Type 'exit' to quit: ")
    if response == "exit":
        break
```

---

### 3. `break`, `continue`, and `else` in Loops
- **`break`**: Exits the loop prematurely.
- **`continue`**: Skips the current iteration.
- **`else`**: Executes if the loop completes without a `break`.

#### Example: Prime Number Check
```python
number = 29
for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
```
**Output:**
```
Prime
```

---

### Use Case: Multiplication Table with `break`
```python
for i in range(1, 6):
    for j in range(1, 6):
        if i * j > 10:
            break
        print(i * j, end=" ")
    print()
```
**Output:**
```
1 2 3 4 5 
2 4 6 8 10 
3 6 9 
4 8 
5 
```

---

## Summary
- Use `for` loops for iterating over sequences.
- Use `while` loops for repeating actions with conditions.
- Avoid infinite loops by ensuring a clear termination condition.
- Combine `break` and `else` for better loop control.
- Utilize nested loops and `match` for complex scenarios.
