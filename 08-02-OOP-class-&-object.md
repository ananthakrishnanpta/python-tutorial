### **Classes and Objects in Python**

#### **1. Basic Concepts**
 **Class**: A blueprint or template for creating objects. It encapsulates data (attributes) and behavior (methods).
 **Object**: A specific instance of a class. Objects are tangible implementations of the class.

### **2. Class Declaration**
```python
class ClassName:
    # Attributes and methods go here
    pass

# Create an object of the class
object_name = ClassName()
```

---

### **3. Instance Variables vs Class Variables**

#### **Instance Variables**
- Attributes specific to an object.
- Defined using `self` inside methods.
- Stored in the object’s namespace.

#### **Class Variables**
- Shared by all objects of the class.
- Defined directly inside the class, but outside any methods.
- Stored in the class’s namespace.

#### **Example**
```python
class Example:
    class_variable = "Shared Value"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

# Instance-level usage
obj1 = Example("Object1 Value")
obj2 = Example("Object2 Value")

print(obj1.instance_variable)  # Output: Object1 Value
print(obj2.instance_variable)  # Output: Object2 Value

# Class-level usage
print(Example.class_variable)  # Output: Shared Value
```

---

### **4. Methods in a Class**

#### **Instance Methods**
- Operate on instance variables.
- Defined with `self` as the first parameter.
- Can access both instance and class variables.

#### **Class Methods**
- Operate on class variables.
- Defined with `@classmethod` and `cls` as the first parameter.

#### **Static Methods**
- Do not operate on instance or class variables.
- Declared with `@staticmethod`.

#### **Example**
```python
class MyClass:
    class_variable = "Shared Value"

    def __init__(self, value):
        self.instance_variable = value

    def instance_method(self):
        return f"Instance Variable: {self.instance_variable}"

    @classmethod
    def class_method(cls):
        return f"Class Variable: {cls.class_variable}"

    @staticmethod
    def static_method():
        return "This is a static method"

# Usage
obj = MyClass("Instance Value")
print(obj.instance_method())    # Output: Instance Variable: Instance Value
print(MyClass.class_method())   # Output: Class Variable: Shared Value
print(MyClass.static_method())  # Output: This is a static method
```

---

### **5. Special (`dunder`) Methods**

#### **5.1. Initialization and Construction**
- `__init__(self, ...)`: Initializes an object after creation.
- `__new__(cls, ...)`: Allocates memory for an object; used for custom object creation.

#### **5.2. String Representation**
- `__str__(self)`: User-friendly representation. Used in `str()` or `print()`.
- `__repr__(self)`: Developer-friendly representation. Used in `repr()` or debugging.

#### **5.3. Arithmetic Operations**
- `__add__(self, other)`: Implements addition (`+`).
- `__sub__(self, other)`: Implements subtraction (`-`).

#### **5.4. Comparison**
- `__eq__(self, other)`: Defines equality (`==`).
- `__lt__(self, other)`: Defines less than (`<`).

#### **5.5. Container Behavior**
- `__len__(self)`: Defines length (`len()`).
- `__getitem__(self, key)`: Indexing behavior.
- `__setitem__(self, key, value)`: Assignment behavior.

#### **5.6. Callable Objects**
- `__call__(self, *args, **kwargs)`: Makes an object callable.

#### **5.7. Iterable Objects**
- `__iter__(self)`: Defines an iterable object.
- `__next__(self)`: Returns the next value in iteration.

#### **Example**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Output: Vector(4, 6)
```

---

### **6. The `self` and `cls` Variables**

#### **`self`**
- Refers to the instance of the class.
- Used to access instance variables and methods.

#### **`cls`**
- Refers to the class itself.
- Used in class methods to access or modify class variables.

#### **Common Mistake**
`self` and `cls` are **not keywords** in Python. They are conventions. You can use any name, but using `self` and `cls` is highly recommended for readability.

#### **Example**
```python
class Example:
    def instance_method(self):
        print("Called with self:", self)

    @classmethod
    def class_method(cls):
        print("Called with cls:", cls)
```

---

### **7. What Happens When a Constructor Runs**

1. **Object Creation (`__new__`)**:
   - Allocates memory.
   - Returns a new instance.

2. **Object Initialization (`__init__`)**:
   - Sets up the initial state of the object.

#### **Flow**
```python
class Demo:
    def __new__(cls, *args, **kwargs):
        print("Creating object")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print("Initializing object")
        self.name = name

obj = Demo("Example")
# Output:
# Creating object
# Initializing object
```

---

### **8. Type Hints and Declarations**

#### **Type Hints**
- Allow specifying types for variables, function arguments, and return values.
- Improves readability and enables static type checking with tools like `mypy`.

#### **Example**
```python
class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def greet(self) -> str:
        return f"Hi, my name is {self.name} and I am {self.age} years old."
```

---

### **9. Implicit Methods**

Implicit methods are those automatically invoked by Python. Examples include:
- `__init__` (for initialization),
- `__del__` (for cleanup),
- `__repr__` (for representation),
- `__call__` (for callable objects).

#### **Example of Callable Object**
```python
class CallableClass:
    def __call__(self, *args, **kwargs):
        print("Object called like a function!")

obj = CallableClass()
obj()  # Output: Object called like a function!
```

---

### **10. Advanced Topics**

#### **Instance vs Class Namespaces**
- Instance variables are stored in the instance dictionary (`__dict__`).
- Class variables are stored in the class dictionary.

#### **Access Control**
Python doesn’t have strict access modifiers, but conventions exist:
- `_variable`: Protected (internal use, not enforced).
- `__variable`: Private (name-mangled to avoid accidental access).

---

### **11. Putting It All Together**

#### **Complete Example**
```python
class Employee:
    company_name = "TechCorp"  # Class variable

    def __init__(self, name: str, salary: float):
        self.name = name  # Instance variable
        self.salary = salary

    def display_info(self) -> str:
        return f"{self.name} earns {self.salary} at {self.company_name}"

    @classmethod
    def update_company_name(cls, new_name: str):
        cls.company_name = new_name

    @staticmethod
    def is_high_salary(salary: float) -> bool:
        return salary > 100000

# Usage
emp1 = Employee("Alice", 90000)
emp2 = Employee("Bob", 120000)

print(emp1.display_info())  # Alice earns 90000 at TechCorp
Employee.update_company_name("NextGenTech")
print(emp2.display_info())  # Bob earns 120000 at NextGenTech
print(Employee.is_high_salary(120000))  # True
```

---
