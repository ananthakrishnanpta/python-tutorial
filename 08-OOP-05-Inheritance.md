---
## **1. Inheritance?**

Inheritance is a core concept in Object-Oriented Programming (OOP) where one class (child or derived class) inherits attributes and methods from another class (parent or base class). It allows you to create new classes that reuse, extend, or modify the functionality of existing ones.

#### **Key Terms:**
- **Parent/Base Class**: The class being inherited from.
- **Child/Derived Class**: The class inheriting from the parent class.

---

### **Why Use Inheritance?**
- **Code Reusability**: Avoid rewriting the same logic for similar functionalities.
- **Hierarchy Representation**: Reflect real-world relationships (e.g., a Dog is an Animal).
- **Polymorphism**: Achieve dynamic behavior where child classes can override parent methods for their specific needs.

---

## **2. Basic Syntax**
```python
class ParentClass:
    def method(self):
        print("This is a method in the Parent class.")

class ChildClass(ParentClass):
    pass

# Usage
obj = ChildClass()
obj.method()  # Output: This is a method in the Parent class.
```

---

## **3. Types of Inheritance**

### **3.1 Single Inheritance**
The simplest form of inheritance where a child class inherits from one parent class.
```python
class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    pass

c = Child()
c.greet()  # Output: Hello from Parent!
```

---

### **3.2 Multiple Inheritance**
A child class inherits from two or more parent classes. Python resolves conflicts using the **Method Resolution Order (MRO)**.

#### **Syntax Example**
```python
class Parent1:
    def greet(self):
        print("Hello from Parent1!")

class Parent2:
    def greet(self):
        print("Hello from Parent2!")

class Child(Parent1, Parent2):
    pass

c = Child()
c.greet()  # Output: Hello from Parent1! (Based on MRO)
```

#### **What is MRO?**
- MRO stands for **Method Resolution Order**, the sequence Python follows to look up methods and attributes.
- Python uses the **C3 Linearization Algorithm** to determine the MRO for classes in a multiple inheritance hierarchy.
- You can view the MRO using `ClassName.__mro__` or `help(ClassName)`.

#### **Example:**
```python
print(Child.__mro__)
# Output: (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>)
```

---

### **3.3 Multilevel Inheritance**
Inheritance forms a chain where a class inherits from a child class, which in turn inherits from another parent class.

#### **Example:**
```python
class Grandparent:
    def show(self):
        print("I am Grandparent.")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.show()  # Output: I am Grandparent.
```

---

### **3.4 Hierarchical Inheritance**
Multiple child classes inherit from a single parent class.

#### **Example:**
```python
class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()

c1.greet()  # Output: Hello from Parent!
c2.greet()  # Output: Hello from Parent!
```

---

### **3.5 Hybrid Inheritance**
A combination of multiple types of inheritance. Python resolves ambiguities using the MRO.

#### **Example:**
```python
class A:
    def greet(self):
        print("Hello from A!")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.greet()  # Output: Hello from A! (Resolved by MRO)
```

---

## **4. Method Resolution Order (MRO)**
- **Definition**: MRO determines the order in which Python searches for a method or attribute in a class hierarchy.
- **Purpose**: Prevents ambiguity in multiple inheritance.

#### **MRO Resolution with `super()`**
`super()` follows the MRO to call the next method in the hierarchy.
```python
class Parent:
    def show(self):
        print("Parent's show method")

class Child1(Parent):
    def show(self):
        super().show()
        print("Child1's show method")

class Child2(Child1):
    def show(self):
        super().show()
        print("Child2's show method")

c = Child2()
c.show()
# Output:
# Parent's show method
# Child1's show method
# Child2's show method
```

---

## **5. Overriding Methods**
When a child class defines a method with the same name as one in the parent class, it overrides the parent method.

#### **Example:**
```python
class Parent:
    def show(self):
        print("Parent's show method")

class Child(Parent):
    def show(self):
        print("Child's show method")

c = Child()
c.show()  # Output: Child's show method
```

---

## **6. The `super()` Keyword**
`super()` is used to call methods from the parent class, following the MRO.

#### **Example:**
```python
class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child!")

c = Child()
c.greet()
# Output:
# Hello from Parent!
# Hello from Child!
```

---

## **7. Abstract Classes**
An abstract class defines methods that must be implemented by derived classes. Abstract classes cannot be instantiated.

#### **Example:**
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()  # Output: Bark
```

---

## **8. Constructors in Inheritance**
Constructors (`__init__`) in a child class override the parent class constructor. You can call the parent’s constructor using `super()`.

#### **Example:**
```python
class Parent:
    def __init__(self, name):
        print(f"Parent initialized with name: {name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        print(f"Child initialized with age: {age}")

c = Child("Alice", 12)
# Output:
# Parent initialized with name: Alice
# Child initialized with age: 12
```

---

## **9. Advantages of Inheritance**
1. **Code Reusability**: Avoid redundancy.
2. **Maintainability**: Easier to maintain and extend.
3. **Polymorphism**: Provides dynamic method overriding.

---

## **10. Drawbacks of Inheritance**
1. **Tight Coupling**: Child classes depend on parent classes, making changes risky.
2. **Complexity**: Multiple inheritance can introduce ambiguities.
3. **Overengineering**: Misuse of inheritance can lead to unnecessary complexity.

---
