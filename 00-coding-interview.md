# Python Interview Preparation

This repository provides a comprehensive collection of Python coding problems categorized into Basic, Medium, and Tough levels, along with their well-documented solutions. Each question is explained thoroughly to aid in understanding and mastering Python concepts.

## Basic Questions

### 1. Check Odd or Even Number
#### Problem Statement
Write a Python program to check whether a given number is odd or even.

#### Solution
```python
# Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
num = 10
result = check_odd_even(num)
print(f"The number {num} is {result}.")
```

### 2. Check if a Number is Prime
#### Problem Statement
Write a Python program to check whether a given number is a prime number.

#### Solution
```python
# Function to check for prime number
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
num = 29
result = is_prime(num)
if result:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
```

### 3. Calculate Factorial
#### Problem Statement
Write a Python program to calculate the factorial of a number using both recursion and iteration.

#### Recursive Solution
```python
# Recursive function to calculate factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Example usage
num = 5
print(f"Factorial of {num} is {factorial_recursive(num)}.")
```

#### Iterative Solution
```python
# Iterative function to calculate factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = 5
print(f"Factorial of {num} is {factorial_iterative(num)}.")
```

### 4. Generate Fibonacci Sequence
#### Problem Statement
Write a Python program to generate the Fibonacci sequence up to a given number of terms using both recursion and iteration.

#### Recursive Solution
```python
# Recursive function to find Fibonacci numbers
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
terms = 10
for i in range(terms):
    print(fibonacci_recursive(i), end=" ")
```

#### Iterative Solution
```python
# Iterative function to generate Fibonacci sequence
def fibonacci_iterative(terms):
    a, b = 0, 1
    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
terms = 10
fibonacci_iterative(terms)
```
### 5. Finding all possible permutations of a given string


```python
def find_permutations(string, current_permutation=""):
    if len(string) == 0:
        print(current_permutation)  # Base case: print the permutation when no characters are left
        return

    for i in range(len(string)):
        # Choose an index
        chosen_char = string[i]

        # Remaining characters after removing the `i` index character
        remaining_chars = string[:i] + string[i+1:]

        find_permutations(remaining_chars, current_permutation + chosen_char)

find_permutations('abc')
```

## Medium-Level Questions

### 1. Implement Bubble Sort
#### Problem Statement
Write a Python program to implement the Bubble Sort algorithm.

#### Solution
```python
# Function to perform bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)
```

### 2. Find GCD of Two Numbers
#### Problem Statement
Write a Python program to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

#### Solution
```python
# Function to find GCD using Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1, num2 = 56, 98
print(f"GCD of {num1} and {num2} is {gcd(num1, num2)}.")
```

### 3. Implement Merge Sort
#### Problem Statement
Write a Python program to implement the Merge Sort algorithm.

#### Solution
```python
# Function to perform merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array is:", arr)
```

### 4. Find the First Non-Repeating Character in a String
#### Problem Statement
Write a Python program to find the first non-repeating character in a string.

#### Solution
```python
# Function to find first non-repeating character
def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in s:
        if char_count[char] == 1:
            return char
    return None

# Example usage
s = "swiss"
result = first_non_repeating_char(s)
if result:
    print(f"The first non-repeating character is '{result}'.")
else:
    print("No non-repeating character found.")
```

### 5. Find All Permutations of a String
#### Problem Statement
Write a Python program to find all permutations of a given string.

#### Solution
```python
from itertools import permutations

# Function to find all permutations of a string
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Example usage
s = "abc"
perms = string_permutations(s)
print(f"Permutations of '{s}': {perms}")
```

## Tough Questions

### 1. Find Longest Palindromic Substring
#### Problem Statement
Write a Python program to find the longest palindromic substring in a given string.

#### Solution
```python
# Function to find longest palindromic substring
def longest_palindrome(s):
    def expand_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_center(i, i)
        even_palindrome = expand_center(i, i + 1)
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    return longest

# Example usage
s = "babad"
print(f"Longest palindromic substring of '{s}' is '{longest_palindrome(s)}'.")
```

### 2. Solve the N-Queens Problem
#### Problem Statement
Write a Python program to solve the N-Queens problem and print all possible solutions.

#### Solution
```python
# Function to solve N-Queens problem
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, col):
        if col >= n:
            solutions.append([row[:] for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    solutions = []
    board = [[0] * n for _ in range(n)]
    solve(board, 0)
    return solutions

# Example usage
n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
for solution in solutions:
    for row in solution:
        print(row)
    print()
```
