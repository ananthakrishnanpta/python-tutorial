# Operators in Python

Operators are symbols that perform operations on variables and values. This tutorial provides a comprehensive explanation of all Python operators with relatable examples.

## Types of Operators

### 1. Arithmetic Operators
These are used for mathematical calculations.

| Operator | Description            | Example         |
|----------|------------------------|-----------------|
| `+`      | Addition               | `5 + 3 = 8`     |
| `-`      | Subtraction            | `5 - 3 = 2`     |
| `*`      | Multiplication         | `5 * 3 = 15`    |
| `/`      | Division               | `5 / 2 = 2.5`   |
| `%`      | Modulus (Remainder)    | `5 % 2 = 1`     |
| `**`     | Exponentiation         | `5 ** 2 = 25`   |
| `//`     | Floor Division         | `5 // 2 = 2`    |

#### Example: Calculating Total Expenses
```python
price_per_item = 50
quantity = 4
budget = 300

# Perform arithmetic calculations
subtotal = price_per_item * quantity
remaining_budget = budget - subtotal

print("Subtotal:", subtotal)
print("Remaining Budget:", remaining_budget)
```

### 2. Comparison Operators
These compare two values and return a boolean (`True` or `False`).

| Operator | Description                  | Example          |
|----------|------------------------------|------------------|
| `==`     | Equal to                    | `5 == 5` (True)  |
| `!=`     | Not equal to                | `5 != 3` (True)  |
| `>`      | Greater than                | `5 > 3` (True)   |
| `<`      | Less than                   | `3 < 5` (True)   |
| `>=`     | Greater than or equal to    | `5 >= 3` (True)  |
| `<=`     | Less than or equal to       | `3 <= 5` (True)  |

#### Example: Checking Eligibility
```python
age = 20
required_age = 18

# Compare values
is_eligible = age >= required_age
print("Is eligible to vote:", is_eligible)
```

### 3. Logical Operators
Logical operators are used to combine conditional statements.

| Operator | Description            | Example                           |
|----------|------------------------|-----------------------------------|
| `and`    | Returns `True` if both conditions are `True` | `True and False = False` |
| `or`     | Returns `True` if at least one condition is `True` | `True or False = True` |
| `not`    | Reverses the logical state | `not True = False` |

#### Detailed Explanation and Examples
- **`and` Operator:**
  The `and` operator ensures that both conditions must be true for the overall result to be `True`.
  ```python
  age = 25
  income = 30000

  # Check eligibility for a premium credit card
  is_eligible = age > 18 and income > 25000
  print("Eligible for premium credit card:", is_eligible)  # True
  ```
- **`or` Operator:**
  The `or` operator returns `True` if at least one condition is true.
  ```python
  is_student = True
  is_employed = False

  # Check for discount eligibility
  gets_discount = is_student or is_employed
  print("Eligible for discount:", gets_discount)  # True
  ```
- **`not` Operator:**
  The `not` operator negates the logical state of a condition.
  ```python
  has_balance = False

  # Check if account is empty
  is_empty = not has_balance
  print("Account is empty:", is_empty)  # True
  ```

#### Example: Loan Eligibility
```python
age = 30
income = 40000
has_good_credit = True

# Combine conditions
is_eligible = (age > 18 and income > 25000) or has_good_credit
print("Eligible for loan:", is_eligible)
```

### 4. Bitwise Operators
Bitwise operators operate on integers at the binary level.

| Operator | Description            | Example         |
|----------|------------------------|-----------------|
| `&`      | Bitwise AND            | `5 & 3 = 1`     |
| `|`      | Bitwise OR             | `5 | 3 = 7`     |
| `^`      | Bitwise XOR            | `5 ^ 3 = 6`     |
| `~`      | Bitwise NOT            | `~5 = -6`       |
| `<<`     | Left Shift             | `5 << 1 = 10`   |
| `>>`     | Right Shift            | `5 >> 1 = 2`    |

#### Binary Representation and Theory
Binary representation helps in understanding bitwise operations. For example:
- **`5` in decimal:** `0101` in binary (4 bits)
- **`3` in decimal:** `0011` in binary (4 bits)

**Bitwise AND (`&`)** performs a logical AND on each pair of bits. For example:
```
  0101  (5 in binary)
& 0011  (3 in binary)
------
  0001  (1 in decimal)
```

#### Detailed Explanation and Examples
- **Bitwise AND (`&`)**
  ```python
  a = 5  # Binary: 0101
  b = 3  # Binary: 0011

  result = a & b
  print("Bitwise AND:", result)  # 1 (Binary: 0001)
  ```

- **Bitwise OR (`|`)**
  Performs a logical OR on each pair of bits.
  ```python
  a = 5
  b = 3

  result = a | b
  print("Bitwise OR:", result)  # 7 (Binary: 0111)
  ```

- **Bitwise XOR (`^`)**
  Performs a logical XOR on each pair of bits. Different bits yield `1`.
  ```python
  a = 5
  b = 3

  result = a ^ b
  print("Bitwise XOR:", result)  # 6 (Binary: 0110)
  ```

- **Bitwise NOT (`~`)**
  Flips all bits, effectively performing `-(n+1)` in two's complement representation.
  ```python
  a = 5

  result = ~a
  print("Bitwise NOT:", result)  # -6 (Binary: -0110)
  ```

- **Bitwise Shifts (`<<` and `>>`)**
  - **Left Shift (`<<`)** multiplies by 2 for each shift.
  - **Right Shift (`>>`)** divides by 2 for each shift (floor value).
  ```python
  a = 5  # Binary: 0101

  left_shift = a << 1
  print("Left Shift:", left_shift)  # 10 (Binary: 1010)

  right_shift = a >> 1
  print("Right Shift:", right_shift)  # 2 (Binary: 0010)
  ```

#### Mathematical Example: Permissions
Imagine we use binary numbers to store file permissions (read, write, execute).
- **`read = 0b0001`**
- **`write = 0b0010`**
- **`execute = 0b0100`**

To combine permissions:
```python
read = 0b0001
write = 0b0010
execute = 0b0100

# Combine permissions
full_access = read | write | execute
print("Full Access (binary):", bin(full_access))

# Check if write permission exists
has_write = full_access & write != 0
print("Has Write Permission:", has_write)
```

### 5. Assignment Operators
Used to assign values and perform shorthand calculations.

| Operator | Description                | Example     |
|----------|----------------------------|-------------|
| `=`      | Assign value               | `x = 5`     |
| `+=`     | Add and assign             | `x += 5`    |
| `-=`     | Subtract and assign        | `x -= 5`    |
| `*=`     | Multiply and assign        | `x *= 5`    |
| `/=`     | Divide and assign          | `x /= 5`    |
| `%=`     | Modulus and assign         | `x %= 5`    |
| `**=`    | Exponentiation and assign  | `x **= 5`   |
| `//=`    | Floor division and assign  | `x //= 5`   |

#### Example: Tracking Scores
```python
score = 0
score += 10  # Earned points
score -= 3   # Lost points

print("Current Score:", score)
```

### 6. Identity Operators
Check if two variables refer to the same object in memory.

| Operator | Description            | Example              |
|----------|------------------------|----------------------|
| `is`     | Same object            | `a is b`            |
| `is not` | Different objects      | `a is not b`        |

#### Example: Object Identity
```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)  # True
print("x is z:", x is z)  # False
```

### 7. Membership Operators
Check if a value exists in a sequence.

| Operator  | Description            | Example               |
|-----------|------------------------|-----------------------|
| `in`      | Exists in sequence     | `'a' in 'apple'`      |
| `not in`  | Does not exist         | `'b' not in 'apple'`  |

#### Example: Checking Membership
```python
fruits = ['apple', 'banana', 'cherry']

# Check if a fruit exists in the list
print('apple' in fruits)  # True
print('grape' not in fruits)  # True
```
