# Python Data Types and Methods

---

## **1. Numeric Types**

### **1.1 Integer (`int`)**
Integers are whole numbers, positive or negative.

**Declaration**:
```python
x = 42
```

#### **Methods**:
1. `bit_length()` – Returns the number of bits required to represent the number.
    ```python
    x = 42
    print(x.bit_length())  # Output: 6
    ```

2. `to_bytes(length, byteorder)` – Converts an integer to a byte array.
    ```python
    x = 255
    print(x.to_bytes(2, 'big'))  # Output: b'\x00\xff'
    ```

3. `from_bytes(bytes, byteorder)` – Converts a byte array back to an integer.
    ```python
    b = b'\x00\xff'
    print(int.from_bytes(b, 'big'))  # Output: 255
    ```

4. `__add__(other)` – Adds another number.
    ```python
    print((5).__add__(3))  # Output: 8
    ```

5. `__sub__(other)` – Subtracts another number.
    ```python
    print((10).__sub__(4))  # Output: 6
    ```

6. `__mul__(other)` – Multiplies with another number.
    ```python
    print((7).__mul__(6))  # Output: 42
    ```

7. `__pow__(other)` – Raises to the power of another number.
    ```python
    print((2).__pow__(3))  # Output: 8
    ```

8. `__mod__(other)` – Finds the remainder.
    ```python
    print((10).__mod__(3))  # Output: 1
    ```

9. `__floordiv__(other)` – Performs floor division.
    ```python
    print((10).__floordiv__(3))  # Output: 3
    ```

10. `__truediv__(other)` – Performs true division.
    ```python
    print((10).__truediv__(4))  # Output: 2.5
    ```

11. `is_integer()` – Checks if the number is an integer.
    ```python
    x = 10
    print(x.is_integer())  # Output: True
    ```

12. `real` – Returns the real part of the number.
    ```python
    x = 5 + 3j
    print(x.real)  # Output: 5.0
    ```

13. `imag` – Returns the imaginary part of the number.
    ```python
    x = 5 + 3j
    print(x.imag)  # Output: 3.0
    ```

14. `conjugate()` – Returns the conjugate of the complex number.
    ```python
    x = 5 + 3j
    print(x.conjugate())  # Output: (5-3j)
    ```

15. `hex()` – Converts the integer to a hexadecimal string.
    ```python
    x = 255
    print(hex(x))  # Output: '0xff'
    ```

---

### **1.2 Float (`float`)**
Floats represent decimal numbers.

**Declaration**:
```python
y = 3.14159
```

#### **Methods**:
1. `is_integer()` – Checks if the float is an integer.
    ```python
    x = 4.0
    print(x.is_integer())  # Output: True
    ```

2. `as_integer_ratio()` – Returns a tuple of integers representing the float as a fraction.
    ```python
    x = 0.75
    print(x.as_integer_ratio())  # Output: (3, 4)
    ```

3. `hex()` – Converts the float to a hexadecimal string.
    ```python
    x = 10.5
    print(x.hex())  # Output: '0x1.5000000000000p+3'
    ```

4. `fromhex(s)` – Converts a hexadecimal string to a float.
    ```python
    x = float.fromhex('0x1.5000000000000p+3')
    print(x)  # Output: 10.5
    ```

5. `__add__(other)` – Adds another number.
    ```python
    print((3.5).__add__(2.5))  # Output: 6.0
    ```

6. `__sub__(other)` – Subtracts another number.
    ```python
    print((5.5).__sub__(1.1))  # Output: 4.4
    ```

7. `__mul__(other)` – Multiplies with another number.
    ```python
    print((2.5).__mul__(4.0))  # Output: 10.0
    ```

8. `__truediv__(other)` – Divides by another number.
    ```python
    print((10.5).__truediv__(2.5))  # Output: 4.2
    ```

9. `__floordiv__(other)` – Performs floor division.
    ```python
    print((9.0).__floordiv__(2.0))  # Output: 4.0
    ```

10. `__mod__(other)` – Finds the remainder.
    ```python
    print((10.5).__mod__(3.0))  # Output: 1.5
    ```

11. `isfinite()` – Checks if the float is finite.
    ```python
    x = 1.0
    print(x.isfinite())  # Output: True
    ```

12. `isinf()` – Checks if the float is infinite.
    ```python
    x = float('inf')
    print(x.isinf())  # Output: True
    ```

13. `isnan()` – Checks if the float is NaN.
    ```python
    x = float('nan')
    print(x.isnan())  # Output: True
    ```

14. `round()` – Rounds the float to the nearest integer.
    ```python
    x = 3.14159
    print(round(x, 2))  # Output: 3.14
    ```

15. `__neg__()` – Negates the float.
    ```python
    x = 5.5
    print((x).__neg__())  # Output: -5.5
    ```

---

## **2. Sequence Types**

### **2.1 String (`str`)**
Strings represent text data.

**Declaration**:
```python
text = "hello"
```

#### **Methods**:
1. `upper()` – Converts the string to uppercase.
    ```python
    print(text.upper())  # Output: "HELLO"
    ```

2. `lower()` – Converts the string to lowercase.
    ```python
    print(text.lower())  # Output: "hello"
    ```

3. `strip()` – Removes leading and trailing spaces.
    ```python
    text = "   hello   "
    print(text.strip())  # Output: "hello"
    ```

4. `replace(old, new)` – Replaces substrings.
    ```python
    text = "apples"
    print(text.replace("a", "o"))  # Output: "opples"
    ```

5. `split(separator)` – Splits the string into a list.
    ```python
    text = "hello world"
    print(text.split())  # Output: ["hello", "world"]
    ```

6. `join(iterable)` – Joins elements of an iterable with the string.
    ```python
    text = "-"
    print(text.join(["hello", "world"]))  # Output: "hello-world"
    ```

7. `find(substring)` – Finds the first index of a substring.
    ```python
    print(text.find("e"))  # Output: 1
    ```

8. `startswith(prefix)` – Checks if the string starts with a prefix.
    ```python
    print(text.startswith("he"))  # Output: True
    ```

9. `endswith(suffix)` – Checks if the string ends with a suffix.
    ```python
    print(text.endswith("lo"))  # Output: True
    ```

10. `isalpha()` – Checks if all characters are alphabetic.
    ```python
    print(text.isalpha())  # Output: True
    ```

11. `isdigit()` – Checks if all characters are digits.
    ```python
    text = "123"
    print(text.isdigit())  # Output: True
    ```

12. `isnumeric()` – Checks if all characters are numeric.
    ```python
    text = "123.45"
    print(text.isnumeric())  # Output: False
    ```

13. `isspace()` – Checks if all characters are whitespace.
    ```python
    text = "   "
    print(text.isspace())  # Output: True
    ```

14. `capitalize()` – Capitalizes the first character of the string.
    ```python
    text = "hello"
    print(text.capitalize()) 

 # Output: "Hello"
    ```

15. `swapcase()` – Swaps the case of all characters.
    ```python
    text = "Hello"
    print(text.swapcase())  # Output: "hELLO"
    ```

---

### **2.2 List (`list`)**
Lists represent ordered collections of items.

**Declaration**:
```python
lst = [1, 2, 3]
```

#### **Methods**:
1. `append(item)` – Adds an item to the end.
    ```python
    lst.append(4)
    print(lst)  # Output: [1, 2, 3, 4]
    ```

2. `extend(iterable)` – Extends the list with elements from another iterable.
    ```python
    lst.extend([3, 4])
    print(lst)  # Output: [1, 2, 3, 4, 3, 4]
    ```

3. `insert(index, item)` – Inserts an item at a specific index.
    ```python
    lst.insert(1, 10)
    print(lst)  # Output: [1, 10, 2, 3, 4, 3, 4]
    ```

4. `pop(index)` – Removes and returns an item at the index.
    ```python
    lst.pop(2)
    print(lst)  # Output: [1, 10, 3, 4, 3, 4]
    ```

5. `remove(item)` – Removes the first occurrence of an item.
    ```python
    lst.remove(3)
    print(lst)  # Output: [1, 10, 4, 3, 4]
    ```

6. `clear()` – Removes all items.
    ```python
    lst.clear()
    print(lst)  # Output: []
    ```

7. `index(item)` – Returns the index of the first occurrence of an item.
    ```python
    lst = [1, 2, 3]
    print(lst.index(2))  # Output: 1
    ```

8. `count(item)` – Counts occurrences of an item.
    ```python
    lst = [1, 2, 2, 3]
    print(lst.count(2))  # Output: 2
    ```

9. `reverse()` – Reverses the list in place.
    ```python
    lst = [1, 2, 3]
    lst.reverse()
    print(lst)  # Output: [3, 2, 1]
    ```

10. `sort()` – Sorts the list in ascending order.
    ```python
    lst = [3, 1, 2]
    lst.sort()
    print(lst)  # Output: [1, 2, 3]
    ```

11. `copy()` – Creates a shallow copy of the list.
    ```python
    lst_copy = lst.copy()
    print(lst_copy)  # Output: [1, 2, 3]
    ```

12. `__contains__(item)` – Checks if an item exists in the list.
    ```python
    print(2 in lst)  # Output: True
    ```

13. `__getitem__(index)` – Accesses an element by index.
    ```python
    print(lst[0])  # Output: 1
    ```

14. `__setitem__(index, item)` – Sets an item at a specific index.
    ```python
    lst[0] = 9
    print(lst)  # Output: [9, 2, 3]
    ```

15. `__delitem__(index)` – Deletes an item at a specific index.
    ```python
    del lst[1]
    print(lst)  # Output: [9, 3]
    ```

---

## **3. Set Types**

### **3.1 Set (`set`)**
Sets are unordered collections of unique items.

**Declaration**:
```python
s = {1, 2, 3}
```

#### **Methods**:
1. `add(item)` – Adds an item to the set.
    ```python
    s.add(4)
    print(s)  # Output: {1, 2, 3, 4}
    ```

2. `remove(item)` – Removes an item from the set.
    ```python
    s.remove(2)
    print(s)  # Output: {1, 3, 4}
    ```

3. `discard(item)` – Removes an item if it exists, but doesn't raise an error if not.
    ```python
    s.discard(2)
    print(s)  # Output: {1, 3, 4}
    ```

4. `pop()` – Removes and returns an arbitrary element.
    ```python
    print(s.pop())  # Output: Arbitrary element (e.g., 1)
    ```

5. `clear()` – Removes all elements from the set.
    ```python
    s.clear()
    print(s)  # Output: set()
    ```

6. `copy()` – Creates a shallow copy of the set.
    ```python
    s_copy = s.copy()
    print(s_copy)  # Output: set()
    ```

7. `union(other_set)` – Returns the union of two sets.
    ```python
    s1 = {1, 2}
    s2 = {3, 4}
    print(s1.union(s2))  # Output: {1, 2, 3, 4}
    ```

8. `intersection(other_set)` – Returns the intersection of two sets.
    ```python
    s1 = {1, 2}
    s2 = {2, 3}
    print(s1.intersection(s2))  # Output: {2}
    ```

9. `difference(other_set)` – Returns the difference between two sets.
    ```python
    s1 = {1, 2}
    s2 = {2, 3}
    print(s1.difference(s2))  # Output: {1}
    ```

10. `symmetric_difference(other_set)` – Returns the symmetric difference of two sets.
    ```python
    s1 = {1, 2}
    s2 = {2, 3}
    print(s1.symmetric_difference(s2))  # Output: {1, 3}
    ```

11. `issubset(other_set)` – Checks if the set is a subset of another set.
    ```python
    s1 = {1, 2}
    s2 = {1, 2, 3}
    print(s1.issubset(s2))  # Output: True
    ```

12. `issuperset(other_set)` – Checks if the set is a superset of another set.
    ```python
    s1 = {1, 2, 3}
    s2 = {1, 2}
    print(s1.issuperset(s2))  # Output: True
    ```

13. `__contains__(item)` – Checks if an item is in the set.
    ```python
    print(2 in s)  # Output: True
    ```

14. `__iter__()` – Returns an iterator for the set.
    ```python
    for elem in s:
        print(elem)  # Output: 1, 2, 3 (unordered)
    ```

15. `__len__()` – Returns the number of elements in the set.
    ```python
    print(len(s))  # Output: 3
    ```

---

## **4. Mapping Types**

### **4.1 Dictionary (`dict`)**
Dictionaries are key-value pairs.

**Declaration**:
```python
d = {'a': 1, 'b': 2}
```

#### **Methods**:
1. `get(key)` – Returns the value associated with the key.
    ```python
    print(d.get('a'))  # Output: 1
    ```

2. `keys()` – Returns all keys in the dictionary.
    ```python
    print(d.keys())  # Output: dict_keys(['a', 'b'])
    ```

3. `values()` – Returns all values in the dictionary.
    ```python
    print(d.values())  # Output: dict_values([1, 2])
    ```

4. `items()` – Returns a view object of key-value tuple pairs.
    ```python
    print(d.items())  # Output: dict_items([('a', 1), ('b', 2)])
    ```

5. `update(other_dict)` – Updates the dictionary with elements from another dictionary.
    ```python
    d.update({'c': 3})
    print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}
    ```

6. `pop(key)` – Removes and returns the value for the key.
    ```python
    print(d.pop('a'))  # Output: 1
    print(d)  # Output: {'b': 2}
    ```

7. `popitem()` – Removes and returns the last key-value pair.
    ```python
    print(d.popitem())  # Output: ('b', 2)
    ```

8. `clear()` – Removes all elements from the dictionary.
    ```python
    d.clear()
    print(d)  # Output: {}
    ```

9. `copy()` – Returns a shallow copy of the dictionary.
    ```python
   

 d_copy = d.copy()
    print(d_copy)  # Output: {'a': 1, 'b': 2}
    ```

10. `setdefault(key, default)` – Returns the value for a key if it exists, else sets it to the default.
    ```python
    print(d.setdefault('c', 3))  # Output: 3
    ```

11. `__contains__(key)` – Checks if a key is in the dictionary.
    ```python
    print('a' in d)  # Output: True
    ```

12. `__getitem__(key)` – Retrieves the value for a key.
    ```python
    print(d['a'])  # Output: 1
    ```

13. `__setitem__(key, value)` – Sets the value for a key.
    ```python
    d['a'] = 4
    print(d)  # Output: {'a': 4, 'b': 2}
    ```

14. `__delitem__(key)` – Deletes an item by key.
    ```python
    del d['a']
    print(d)  # Output: {'b': 2}
    ```

15. `fromkeys(iterable, value)` – Creates a new dictionary with keys from an iterable and values set to the given value.
    ```python
    keys = ['a', 'b', 'c']
    print(dict.fromkeys(keys, 0))  # Output: {'a': 0, 'b': 0, 'c': 0}
    ```

---
