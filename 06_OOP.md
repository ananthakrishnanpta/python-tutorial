
# Object-Oriented Programming (OOP) in Python

OOP is a paradigm based on the concept of "objects," which contain data and behavior.

## Classes and Objects
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

p = Person("Alice", 30)
print(p.greet())
```
**Output:**
```
Hi, I'm Alice and I'm 30 years old.
```

## Inheritance
```python
class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job
    def work(self):
        return f"I'm working as a {self.job}."
e = Employee("Bob", 25, "Engineer")
print(e.greet())
print(e.work())
```
**Output:**
```
Hi, I'm Bob and I'm 25 years old.
I'm working as a Engineer.
```
