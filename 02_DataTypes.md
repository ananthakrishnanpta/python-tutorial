
# Data Types in Python

Python provides various data types to work with different kinds of data.

## Built-in Data Types
1. **Numeric Types**: `int`, `float`, `complex`
2. **Sequence Types**: `str`, `list`, `tuple`, `range`
3. **Mapping Type**: `dict`
4. **Set Types**: `set`, `frozenset`
5. **Boolean Type**: `bool`
6. **Binary Types**: `bytes`, `bytearray`, `memoryview`

### 1. **Numeric Data Types**
- **`int`**: Whole numbers without a fractional component.
- **`float`**: Numbers with decimals, used when precision is required.
- **`complex`**: Numbers with a real and imaginary component (rarely used in traditional app backends).

#### Theoretical Explanation:
- Python supports arbitrarily large integers, which is useful for high-precision calculations.
- Floats follow IEEE 754 standards, providing reliability in scientific computations.

#### Real-World Applications:
1. **E-commerce platforms**:
   - **`int`**: Inventory counts (e.g., number of items left in stock).
   - **`float`**: Prices (e.g., $199.99), discounts, taxes.
2. **Banking systems**:
   - **`float`**: Interest rate calculations.
   - **`int`**: Tracking the number of transactions.

#### Example:
```python
# E-commerce discount calculation
price = 199.99  # float
discount_percent = 10  # int
discounted_price = price * (1 - discount_percent / 100)
print(f"Discounted Price: {discounted_price}")
```

---

### 2. **Sequence Data Types**
Python sequences represent ordered collections of items.

#### a. **String (`str`)**
- Immutable, stores text.
- **Theoretical use**: Essential for any data requiring textual representation (e.g., names, descriptions, messages).

#### Real-World Applications:
1. **Social Media Platforms**:
   - Storing user posts, comments, and bios.
2. **E-commerce**:
   - Product names, descriptions, and reviews.

#### Example:
```python
# Social media comment
comment = "This product is amazing!"
if "amazing" in comment:
    print("Positive review detected.")
```

---

#### b. **List**
- Mutable, ordered, heterogeneous.
- **Theoretical use**: Ideal for collections that frequently change.

#### Real-World Applications:
1. **To-do apps**:
   - Store a user’s list of tasks.
2. **Web scrapers**:
   - Collect and temporarily hold data for parsing.

#### Example:
```python
# Backend for a to-do app
tasks = ["Buy groceries", "Read a book"]
tasks.append("Pay bills")
print("Updated Tasks:", tasks)
```

---

#### c. **Tuple**
- Immutable, ordered, heterogeneous.
- **Theoretical use**: Ideal for fixed collections where data integrity is critical.

#### Real-World Applications:
1. **Geolocation systems**:
   - Storing fixed coordinate pairs (latitude, longitude).
2. **Configuration files**:
   - Define constants that shouldn't be modified (e.g., database connection details).

#### Example:
```python
# Backend geolocation example
location = (37.7749, -122.4194)  # San Francisco (latitude, longitude)
print(f"User's location: {location}")
```

---

### 3. **Mapping Data Type**
#### **Dictionary (`dict`)**
- Stores key-value pairs.
- **Theoretical use**: Excellent for representing relationships between unique keys and corresponding values.

#### Real-World Applications:
1. **Web applications**:
   - Storing and retrieving session data (e.g., user IDs, preferences).
2. **REST APIs**:
   - Return structured JSON responses.

#### Example:
```python
# API response simulation
user_profile = {"name": "Alice", "email": "alice@example.com"}
print(user_profile)
```

---

### 4. **Set Data Types**
#### a. **Set**
- Unordered collection of unique elements.
- **Theoretical use**: Useful for eliminating duplicates and performing set operations.

#### Real-World Applications:
1. **Recommendation systems**:
   - Identify unique categories of user preferences.
2. **Data cleaning**:
   - Eliminate duplicate entries in datasets.

#### Example:
```python
# Data cleaning example
raw_data = ["Python", "Java", "Python", "C++"]
unique_data = set(raw_data)
print("Unique Programming Languages:", unique_data)
```

---

#### b. **Frozen Set**
- Immutable version of a set.
- **Theoretical use**: Used when data integrity is critical, and no modifications are allowed.

#### Real-World Applications:
1. **Database systems**:
   - Represent fixed attributes or keys.
2. **Machine Learning Models**:
   - Store fixed feature sets.

#### Example:
```python
# Fixed feature set for a model
features = frozenset(["age", "income", "gender"])
print(features)
```

---

### 5. **Boolean (`bool`)**
- Represents `True` or `False`.
- **Theoretical use**: Essential for decision-making in control flows.

#### Real-World Applications:
1. **Authentication systems**:
   - Check if a user is authenticated (`is_authenticated`).
2. **Feature toggles**:
   - Enable/disable specific functionalities.

#### Example:
```python
# Authentication backend
is_authenticated = True
if is_authenticated:
    print("Welcome back!")
else:
    print("Please log in.")
```

---

### 6. **Binary Data Types**
- Handle binary data such as images or encoded text.

#### Real-World Applications:
1. **Media streaming services**:
   - Store and transmit audio/video files in binary format.
2. **File upload systems**:
   - Handle image or document uploads.

#### Example:
```python
# Simulating binary data storage
image_data = b"binarydatahere"
print(f"Image data length: {len(image_data)} bytes")
```

---

### 7. **NoneType**
- Represents absence or "no value."
- **Theoretical use**: Useful for initializing variables that will be assigned later.

#### Real-World Applications:
1. **Database operations**:
   - Represent NULL values in records.
2. **API placeholders**:
   - Default for missing data fields.

#### Example:
```python
# Default field value
user_last_login = None
if user_last_login is None:
    print("User has not logged in yet.")
```

---

### Real-World Backend Scenarios and Summary Table
| **Data Type**  | **Backend Use Case**                                      | **Real-World Example**                        |
|-----------------|----------------------------------------------------------|-----------------------------------------------|
| `int`          | Counters, IDs                                             | Inventory counts in e-commerce                |
| `float`        | Precision calculations                                    | Price calculations in financial systems       |
| `str`          | User inputs, descriptions, messages                       | User comments on social media                 |
| `list`         | Dynamic collections                                       | Shopping cart in an e-commerce site           |
| `tuple`        | Fixed configuration values                                | Database connection settings                  |
| `dict`         | Key-value store                                           | Session data in a web app                     |
| `set`          | Unique collections                                        | Unique tags in a recommendation system        |
| `frozenset`    | Immutable unique collections                              | Fixed features in machine learning models     |
| `bool`         | Logic gates, feature toggles                              | Authentication status                         |
| `bytes`        | Binary data for media or file handling                    | Image storage in cloud systems                |
| `NoneType`     | Missing values                                            | NULL equivalent in databases                  |

```
