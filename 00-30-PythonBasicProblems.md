# Beginner Python Practice — 30 Problems with Simple Solutions

> Before you start:
>
> * Run each code block in a Python notebook (or save into a `.py` file and run).
> * The solutions are using only basic constructs: variables, `for`/`while` loops, `if`/`else`, lists and dictionaries, and simple functions.
> * Read the explanation after each solution — it points out the logic, variable roles, and common pitfalls.

---

## 1. Print odd numbers from 1 to N

**Problem:** Print all odd numbers from `1` to `number_limit` inclusive.

```python
def print_odds_up_to(number_limit):
    current_number = 1
    while current_number <= number_limit:
        if current_number % 2 != 0:
            print(current_number)
        current_number = current_number + 1

# Example
print_odds_up_to(15)
```

**Explanation:**
Start `current_number` at `1`, loop until it exceeds `number_limit`. Use `% 2 != 0` to check oddness. Increment `current_number` each loop.

---

## 2. Print first N Fibonacci numbers

**Problem:** Print Fibonacci numbers starting from `0, 1, 1, 2...` up to `count` numbers.

```python
def print_fibonacci(count):
    if count <= 0:
        return
    previous_number = 0
    current_number = 1
    print(previous_number)
    if count == 1:
        return
    print(current_number)
    printed_count = 2
    while printed_count < count:
        next_number = previous_number + current_number
        print(next_number)
        previous_number = current_number
        current_number = next_number
        printed_count = printed_count + 1

# Example
print_fibonacci(7)
```

**Explanation:**
Keep `previous_number` and `current_number`. Generate `next_number` as their sum, print it, then shift the two variables forward.

---

## 3. Check if a number is a palindrome

**Problem:** Check if `number` reads same forwards and backwards (e.g., `121`).

```python
def is_number_palindrome(number):
    original_number = number
    reversed_number = 0
    working_number = number
    while working_number > 0:
        last_digit = working_number % 10
        reversed_number = reversed_number * 10 + last_digit
        working_number = working_number // 10
    return reversed_number == original_number

# Example
print(is_number_palindrome(121))  # True
print(is_number_palindrome(123))  # False
```

**Explanation:**
Extract digits using `% 10`, build `reversed_number`, then compare to original. Uses integer math only.

---

## 4. Check if a number is Armstrong (narcissistic)

**Problem:** Check if the given number is armstrong number.

```python
def is_armstrong_number_any_digits(number):
    # Work with the absolute value for digit extraction; Armstrong property is for non-negative integers.
    original_number = abs(number)

    # Special-case: 0 is an Armstrong number (0^1 == 0).
    if original_number == 0:
        return True

    # 1) Count digits (do not modify original_number yet)
    digit_count = 0
    temp_for_count = original_number
    while temp_for_count > 0:
        digit_count = digit_count + 1
        temp_for_count = temp_for_count // 10

    # 2) Compute sum of each digit raised to the power of digit_count
    sum_of_powers = 0
    working_number = original_number
    while working_number > 0:
        digit = working_number % 10
        sum_of_powers = sum_of_powers + (digit ** digit_count)
        working_number = working_number // 10

    # 3) Compare the computed sum with the original number
    return sum_of_powers == original_number

# Examples
print(is_armstrong_number_any_digits(153))    # True  (3 digits: 1^3 + 5^3 + 3^3 = 153)
print(is_armstrong_number_any_digits(370))    # True  (3 digits)
print(is_armstrong_number_any_digits(9474))   # True  (4 digits: 9^4 + 4^4 + 7^4 + 4^4 = 9474)
print(is_armstrong_number_any_digits(1634))   # True  (4 digits)
print(is_armstrong_number_any_digits(123))    # False
print(is_armstrong_number_any_digits(0))      # True

```

**Explanation:**
Extract each digit, raise it to the power of total number of digits in the original number, add them up, then compare with original. This is the standard Armstrong check.

---

## 5. Factorial of N (iterative)

**Problem:** Compute `N!` using a simple loop.

```python
def factorial(number):
    if number < 0:
        return None  # factorial not defined for negative numbers
    result = 1
    current_multiplier = 2
    while current_multiplier <= number:
        result = result * current_multiplier
        current_multiplier = current_multiplier + 1
    return result

# Example
print(factorial(5))  # 120
```

**Explanation:**
Multiply numbers from `2` to `number`. Handle negative input by returning `None`.

---

## 6. Check prime number (simple)

**Problem:** Return True/False whether `number` is prime using trial division.

```python
def is_prime(number):
    if number <= 1:
        return False
    test_divider = 2
    while test_divider <= number // 2:
        if number % test_divider == 0:
            return False
        test_divider = test_divider + 1
    return True

# Example
print(is_prime(2))   # True
print(is_prime(15))  # False
```

**Explanation:**
Check divisibility from `2` to `number // 2`. This is simple and easy for beginners (not optimized for large numbers).

---

## 7. Sum of digits of a number

**Problem:** Return sum of digits of `number`.

```python
def sum_of_digits(number):
    total = 0
    working_number = abs(number)  # handle negative numbers
    while working_number > 0:
        last_digit = working_number % 10
        total = total + last_digit
        working_number = working_number // 10
    return total

# Example
print(sum_of_digits(1234))  # 10
print(sum_of_digits(-56))   # 11
```

**Explanation:**
Use `%` and `//` to get digits. Use `abs` for negative numbers.

---

## 8. Reverse a string

**Problem:** Reverse a string `text`.

```python
def reverse_string(text):
    reversed_text = ""
    index = 0
    while index < len(text):
        current_character = text[index]
        reversed_text = current_character + reversed_text
        index = index + 1
    return reversed_text

# Example
print(reverse_string("hello"))  # "olleh"
```

**Explanation:**
Prepend each character to `reversed_text` to build the reversed string. This uses only basic string operations.

---

## 9. Check if a string is palindrome

**Problem:** Determine whether `text` is a palindrome (case-insensitive).

```python
def is_string_palindrome(text):
    normalized_text = text.lower().replace(" ", "")
    reversed_text = ""
    index = 0
    while index < len(normalized_text):
        reversed_text = normalized_text[index] + reversed_text
        index = index + 1
    return reversed_text == normalized_text

# Example
print(is_string_palindrome("Madam"))           # True
print(is_string_palindrome("Step on no pets")) # True
```

**Explanation:**
Normalize to lower case and remove spaces, then reverse and compare.

---

## 10. Swap two numbers without using a third variable

**Problem:** Swap `x` and `y` using arithmetic.

```python
def swap_without_temp(x, y):
    x = x + y
    y = x - y
    x = x - y
    return x, y

# Example
print(swap_without_temp(5, 10))  # (10, 5)
```

**Explanation:**
Use additions/subtractions to swap. Works for integers; watch overflow for very large numbers (not usually an issue in Python).

---

## 11. Count digits in a number

**Problem:** Count how many digits are in `number`.

```python
def count_digits(number):
    if number == 0:
        return 1
    working_number = abs(number)
    digit_count = 0
    while working_number > 0:
        digit_count = digit_count + 1
        working_number = working_number // 10
    return digit_count

# Example
print(count_digits(12345))  # 5
print(count_digits(0))      # 1
```

**Explanation:**
Divide `working_number` by 10 repeatedly and count iterations.

---

## 12. Print numbers in reverse from N to 1

**Problem:** Print numbers from `number_limit` down to `1`.

```python
def print_reverse_down_to_one(number_limit):
    current_number = number_limit
    while current_number >= 1:
        print(current_number)
        current_number = current_number - 1

# Example
print_reverse_down_to_one(5)
```

**Explanation:**
Simple downward loop with decrement.

---

## 13. Find largest among three numbers

**Problem:** Return the largest of three numbers.

```python
def largest_of_three(number_one, number_two, number_three):
    largest = number_one
    if number_two > largest:
        largest = number_two
    if number_three > largest:
        largest = number_three
    return largest

# Example
print(largest_of_three(10, 25, 7))  # 25
```

**Explanation:**
Start with one number and compare with others, updating `largest` as needed.

---

## 14. Sum of first N natural numbers

**Problem:** Compute sum `1 + 2 + ... + N` using a loop.

```python
def sum_first_n(n):
    total = 0
    current_number = 1
    while current_number <= n:
        total = total + current_number
        current_number = current_number + 1
    return total

# Example
print(sum_first_n(10))  # 55
```

**Explanation:**
Accumulate values from `1` to `n`. (You could use formula `n*(n+1)//2`, but loop is clearer for beginners.)

---

## 15. Generate multiplication table for N

**Problem:** Print multiplication table for `number` up to 10.

```python
def multiplication_table(number):
    multiplier = 1
    while multiplier <= 10:
        product = number * multiplier
        print(f"{number} x {multiplier} = {product}")
        multiplier = multiplier + 1

# Example
multiplication_table(7)
```

**Explanation:**
Loop multiplier `1..10` and compute `product`.

---

## 16. List Problem 1 — Find maximum in a list

**Problem:** Given `numbers_list`, find the maximum value.

```python
def find_max_in_list(numbers_list):
    if len(numbers_list) == 0:
        return None
    maximum_value = numbers_list[0]
    index = 1
    while index < len(numbers_list):
        if numbers_list[index] > maximum_value:
            maximum_value = numbers_list[index]
        index = index + 1
    return maximum_value

# Example
print(find_max_in_list([3, 8, 2, 15, 6]))  # 15
```

**Explanation:**
Initialize `maximum_value` to first item and update while traversing.

---

## 17. List Problem 2 — Find minimum in a list

**Problem:** Find minimum value in `numbers_list`.

```python
def find_min_in_list(numbers_list):
    if len(numbers_list) == 0:
        return None
    minimum_value = numbers_list[0]
    index = 1
    while index < len(numbers_list):
        if numbers_list[index] < minimum_value:
            minimum_value = numbers_list[index]
        index = index + 1
    return minimum_value

# Example
print(find_min_in_list([3, 8, 2, 15, 6]))  # 2
```

**Explanation:**
Similar to max but checks for smaller values.

---

## 18. List Problem 3 — Sum of all elements in a list

**Problem:** Return the sum of elements in `numbers_list`.

```python
def sum_of_list(numbers_list):
    total_sum = 0
    index = 0
    while index < len(numbers_list):
        total_sum = total_sum + numbers_list[index]
        index = index + 1
    return total_sum

# Example
print(sum_of_list([1, 2, 3, 4]))  # 10
```

**Explanation:**
Accumulate each element in `total_sum`.

---

## 19. List Problem 4 — Count occurrences of a value in a list

**Problem:** Count how many times `target_value` appears in `items_list`.

```python
def count_occurrences(items_list, target_value):
    occurrence_count = 0
    index = 0
    while index < len(items_list):
        if items_list[index] == target_value:
            occurrence_count = occurrence_count + 1
        index = index + 1
    return occurrence_count

# Example
print(count_occurrences([1, 2, 2, 3, 2], 2))  # 3
```

**Explanation:**
Increment `occurrence_count` every time a match is found.

---

## 20. List Problem 5 — Remove duplicates from a list (simple)

**Problem:** Return a new list containing unique elements in the order of first appearance.

```python
def remove_duplicates_preserve_order(original_list):
    unique_list = []
    index = 0
    while index < len(original_list):
        current_item = original_list[index]
        already_present = False
        check_index = 0
        while check_index < len(unique_list):
            if unique_list[check_index] == current_item:
                already_present = True
                break
            check_index = check_index + 1
        if not already_present:
            unique_list.append(current_item)
        index = index + 1
    return unique_list

# Example
print(remove_duplicates_preserve_order([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
```

**Explanation:**
For each item, check if already in `unique_list`. If not, append it. This uses nested loops but is easy to understand.

---

## 21. List Problem 6 — Reverse a list (without using built-in reverse)

**Problem:** Return a new list with elements in reverse order.

```python
def reverse_list(original_list):
    reversed_list = []
    index = 0
    while index < len(original_list):
        current_item = original_list[index]
        reversed_list = [current_item] + reversed_list  # prepend
        index = index + 1
    return reversed_list

# Example
print(reverse_list([1, 2, 3, 4]))  # [4, 3, 2, 1]
```

**Explanation:**
Prepend each item to `reversed_list`. Simple and transparent.

---

## 22. Dictionary Problem 1 — Count frequency of words in a sentence

**Problem:** Given a `sentence`, return a dictionary mapping each word to its frequency.

```python
def word_frequencies(sentence):
    normalized_sentence = sentence.lower()
    words = normalized_sentence.split()
    frequency_map = {}
    index = 0
    while index < len(words):
        current_word = words[index]
        if current_word in frequency_map:
            frequency_map[current_word] = frequency_map[current_word] + 1
        else:
            frequency_map[current_word] = 1
        index = index + 1
    return frequency_map

# Example
print(word_frequencies("Hello world hello"))
# {'hello': 2, 'world': 1}
```

**Explanation:**
Split sentence into words, then update the count in `frequency_map`. Use `lower()` to treat words case-insensitively.

---

## 23. Dictionary Problem 2 — Merge two dictionaries (simple)

**Problem:** Merge `dict_one` and `dict_two`. If a key exists in both, use the value from `dict_two`.

```python
def merge_dictionaries(dict_one, dict_two):
    merged = {}
    for key in dict_one:
        merged[key] = dict_one[key]
    for key in dict_two:
        merged[key] = dict_two[key]
    return merged

# Example
print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
# {'a': 1, 'b': 3, 'c': 4}
```

**Explanation:**
Copy all items from `dict_one`, then overwrite/add items from `dict_two`.

---

## 24. Dictionary Problem 3 — Get keys with maximum value

**Problem:** From `score_map` find which key(s) have the highest score.

```python
def keys_with_max_value(score_map):
    if len(score_map) == 0:
        return []
    max_value = None
    result_keys = []
    for current_key in score_map:
        current_value = score_map[current_key]
        if max_value is None or current_value > max_value:
            max_value = current_value
            result_keys = [current_key]
        elif current_value == max_value:
            result_keys.append(current_key)
    return result_keys

# Example
print(keys_with_max_value({'alice': 80, 'bob': 95, 'carol': 95}))  # ['bob', 'carol']
```

**Explanation:**
Track `max_value`. When encountering a bigger value, reset `result_keys`; when equal, append.

---

## 25. Dictionary Problem 4 — Invert a dictionary (values become keys)

**Problem:** Given `mapping` with unique values, return an inverted dictionary.

```python
def invert_dictionary(mapping):
    inverted = {}
    for key in mapping:
        value = mapping[key]
        inverted[value] = key
    return inverted

# Example
print(invert_dictionary({'a': 1, 'b': 2}))  # {1: 'a', 2: 'b'}
```

**Explanation:**
Swap `key` and `value` into a new dict. Assumes original values are unique and hashable.

---

## 26. Check perfect number

**Problem:** A perfect number equals sum of its proper divisors (e.g., `6` = 1+2+3). Check if `number` is perfect.

```python
def is_perfect_number(number):
    if number <= 1:
        return False
    sum_of_divisors = 1  # 1 is always a proper divisor
    divisor = 2
    while divisor <= number // 2:
        if number % divisor == 0:
            sum_of_divisors = sum_of_divisors + divisor
        divisor = divisor + 1
    return sum_of_divisors == number

# Example
print(is_perfect_number(6))   # True
print(is_perfect_number(28))  # True
```

**Explanation:**
Check divisors up to `number // 2` and sum them.

---

## 27. GCD of two numbers (Euclidean algorithm using subtraction — simple)

**Problem:** Compute greatest common divisor using repeated subtraction (easy to understand).

```python
def gcd_by_subtraction(number_one, number_two):
    a = abs(number_one)
    b = abs(number_two)
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Example
print(gcd_by_subtraction(48, 18))  # 6
```

**Explanation:**
Repeatedly subtract the smaller from the bigger until equal. It's slower but very explicit.

---

## 28. Count vowels and consonants in a string

**Problem:** Count how many vowels and consonants are in `text` (letters only).

```python
def count_vowels_and_consonants(text):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    index = 0
    normalized_text = text.lower()
    while index < len(normalized_text):
        character = normalized_text[index]
        if 'a' <= character <= 'z':
            if character in vowels:
                vowel_count = vowel_count + 1
            else:
                consonant_count = consonant_count + 1
        index = index + 1
    return vowel_count, consonant_count

# Example
print(count_vowels_and_consonants("Hello World"))  # (3, 7)  (counts only letters)
```

**Explanation:**
Check alphabetic letters in lowercase, then classify as vowel or consonant.

---

## 29. Dictionary + List Problem — Group numbers by even/odd

**Problem:** Given `numbers_list`, return `{'even': [...], 'odd': [...]}`.

```python
def group_even_and_odd(numbers_list):
    grouped = {'even': [], 'odd': []}
    index = 0
    while index < len(numbers_list):
        current_number = numbers_list[index]
        if current_number % 2 == 0:
            grouped['even'].append(current_number)
        else:
            grouped['odd'].append(current_number)
        index = index + 1
    return grouped

# Example
print(group_even_and_odd([1, 2, 3, 4, 5, 6]))
# {'even': [2, 4, 6], 'odd': [1, 3, 5]}
```

**Explanation:**
Traverse list once and append to corresponding list in `grouped` dictionary.

---

## 30. List + Dictionary Problem — Count item frequencies and return top item

**Problem:** Given `items_list`, return `(most_common_item, frequency)`.

```python
def most_common_item_and_frequency(items_list):
    frequency_map = {}
    index = 0
    while index < len(items_list):
        current_item = items_list[index]
        if current_item in frequency_map:
            frequency_map[current_item] = frequency_map[current_item] + 1
        else:
            frequency_map[current_item] = 1
        index = index + 1

    if len(frequency_map) == 0:
        return None, 0

    top_item = None
    top_frequency = 0
    for key in frequency_map:
        if frequency_map[key] > top_frequency:
            top_item = key
            top_frequency = frequency_map[key]
    return top_item, top_frequency

# Example
print(most_common_item_and_frequency(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))
# ('apple', 3)
```

**Explanation:**
Create a frequency dictionary, then scan it to find the key with the largest value.

---
