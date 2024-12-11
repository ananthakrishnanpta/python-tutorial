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
Used to combine multiple conditions.

| Operator | Description            | Example                           |
|----------|------------------------|-----------------------------------|
| `and`    | Both conditions true   | `True and False = False`          |
| `or`     | At least one true      | `True or False = True`            |
| `not`    | Negates a condition    | `not True = False`                |

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
Operate at the bit level.

| Operator | Description            | Example         |
|----------|------------------------|-----------------|
| `&`      | AND                    | `5 & 3 = 1`     |
| `|`      | OR                     | `5 | 3 = 7`     |
| `^`      | XOR                    | `5 ^ 3 = 6`     |
| `~`      | NOT (one's complement) | `~5 = -6`       |
| `<<`     | Left Shift             | `5 << 1 = 10`   |
| `>>`     | Right Shift            | `5 >> 1 = 2`    |

#### Example: Permissions
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

#### Example: Item Search
```python
fruits = ["apple", "banana", "cherry"]

print("apple in fruits:", "apple" in fruits)
print("grape not in fruits:", "grape" not in fruits)
```

### 8. Other Operators
#### 8.1 Ternary Operator
Used for inline conditional expressions.
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)
```

#### 8.2 Chained Comparison
Combine multiple comparisons.
```python
x = 5
print(1 < x < 10)  # True
```

## Combining Operators in Real-Life Scenarios
#### Example: Shopping Checkout
```python
price_per_item = 100
quantity = 3
wallet_balance = 500

total_cost = price_per_item * quantity
can_afford = wallet_balance >= total_cost

if can_afford:
    wallet_balance -= total_cost
    print("Purchase successful! Remaining balance:", wallet_balance)
else:
    print("Insufficient balance!")
```
