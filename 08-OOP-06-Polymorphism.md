---
## **1. Polymorphism?**

**Polymorphism** is derived from two Greek words: 
   - **Poly**: Many  
   - **Morph**: Forms  

In programming, polymorphism refers to the ability of different objects to respond to the same method name or operator in their own unique way.

---

### **Why Use Polymorphism?**
- Encourages **code flexibility**.
- Supports **dynamic behavior** without altering existing code.
- Facilitates **reusability** and **scalability** in object-oriented programs.

---

## **2. Types of Polymorphism in Python**

Python supports **two main types of polymorphism**:

1. **Compile-Time Polymorphism (Static Polymorphism):**
   - Achieved through **method overloading** or **operator overloading**.
   - Python natively does not support method overloading but allows operator overloading.

2. **Run-Time Polymorphism (Dynamic Polymorphism):**
   - Achieved through **method overriding** in inheritance.

---

## **3. Compile-Time Polymorphism**

### **3.1 Operator Overloading**

Python allows operators like `+`, `-`, `*`, etc., to work differently based on the objects involved. This is achieved through **magic methods** (dunder methods).

#### **Example:**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2
print(result)  # Output: Point(4, 6)
```

#### **Common Magic Methods for Operator Overloading:**
- `__add__`: For `+`
- `__sub__`: For `-`
- `__mul__`: For `*`
- `__truediv__`: For `/`
- `__eq__`: For `==`
- `__lt__`: For `<`
- `__gt__`: For `>`

---

### **3.2 Method Overloading**

Python **does not support method overloading directly**. However, you can achieve it by using default arguments or variable-length arguments (`*args` or `**kwargs`).

#### **Example:**
```python
class MathOperations:
    def multiply(self, a, b, c=None):
        if c is not None:
            return a * b * c
        return a * b

obj = MathOperations()
print(obj.multiply(2, 3))      # Output: 6
print(obj.multiply(2, 3, 4))   # Output: 24
```

---

## **4. Run-Time Polymorphism**

### **4.1 Method Overriding**
- Inheritance allows a child class to provide a specific implementation for a method defined in its parent class.
- The child class overrides the parent method, enabling **dynamic behavior**.

#### **Example:**
```python
class Animal:
    def sound(self):
        print("Animals make sounds.")

class Dog(Animal):
    def sound(self):
        print("Dogs bark.")

class Cat(Animal):
    def sound(self):
        print("Cats meow.")

# Dynamic behavior
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()
# Output:
# Dogs bark.
# Cats meow.
```

---

## **5. Polymorphism in Built-In Functions**

Python's built-in functions like `len()` and `print()` are inherently polymorphic, as they behave differently depending on the object type.

#### **Example:**
```python
print(len("Hello"))  # Output: 5 (Length of string)
print(len([1, 2, 3]))  # Output: 3 (Length of list)
```

---

## **6. Polymorphism in Function Arguments**
Functions in Python can accept objects of different types, as long as the object implements the required behavior (methods or properties). This is known as **Duck Typing**.

#### **What is Duck Typing?**
- Python follows a principle: **"If it looks like a duck and quacks like a duck, it must be a duck."**
- The focus is on behavior, not on explicit inheritance.

#### **Example:**
```python
class Duck:
    def sound(self):
        print("Quack!")

class Dog:
    def sound(self):
        print("Bark!")

def make_sound(animal):
    animal.sound()

duck = Duck()
dog = Dog()

make_sound(duck)  # Output: Quack!
make_sound(dog)   # Output: Bark!
```

---

## **7. Polymorphism with Abstract Classes**
Polymorphism often works with **abstract classes** and **interfaces**. An abstract class defines methods that must be implemented in derived classes.

#### **Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(10, 5), Circle(7)]
for shape in shapes:
    print(shape.area())
# Output:
# 50
# 153.86
```

---

## **8. Limitations of Polymorphism in Python**

1. **Method Overloading Limitation:**
   - Python does not natively support multiple methods with the same name in a single class. You must use optional arguments or differentiate methods.

2. **Ambiguities in Operator Overloading:**
   - Overusing operator overloading can make code harder to read and debug.

3. **Performance Overhead:**
   - Polymorphism introduces an overhead during runtime, as Python needs to resolve the appropriate methods dynamically.

4. **Potential Errors in Duck Typing:**
   - While flexible, Duck Typing can lead to runtime errors if objects do not conform to the expected behavior.

---

## **9. Advantages of Polymorphism**

1. **Flexibility**: Write generic and reusable code.
2. **Scalability**: Add new functionality with minimal changes to existing code.
3. **Ease of Maintenance**: Simplifies code modifications.

---

## **10. Capabilities of Polymorphism in Python**

- **Cross-Class Compatibility**: Polymorphism allows seamless integration of multiple object types.
- **Dynamic Behavior**: Enables runtime determination of method execution.
- **Support for Abstract Classes**: Allows defining clear contracts for derived classes.

---
