# Learnings: Object-Oriented Programming (OOP) in Python

## 1. The Basic Class Structure & Dunder Methods

A Python class encapsulates data and behavior. The structure relies heavily on instance variables (data specific to the object) and instance methods (functions defining behavior, always taking `self` as the first argument).

Python uses special "dunder" (double underscore) methods that are automatically called behind the scenes:

- **`__new__(cls)`**: The true constructor that allocates memory for an empty object.
- **`__init__(self, ...)`**: The initializer. It is called immediately after `__new__` to populate the new object with instance variables.
- **`__str__(self)`**: Automatically triggered when the object is evaluated as a string (e.g., using `print()` or `str()`).

**Code Example (`Jar` Class):**

```python
class Jar:
    def __init__(self, capacity=12, size=0):
        # Triggers the setters for validation upon initialization
        self.capacity = capacity
        self.size = size

    def __str__(self):
        # Automatically called when printing the object
        return f"{'🍪' * self.size}"

    def deposit(self, n):
        # Instance method defining behavior
        if not self.size + n <= self.capacity:
            raise ValueError('Cookies added have exceeded the current capacity!')
        self.size += n
```

## 2. Data Encapsulation: `@property` and Setters

When you want to access a plain attribute but need to enforce validation rules without setting up independent, traditional functions (like `jar.get_capacity()`), you use property decorators.

A property object wraps these methods, allowing you to use clean dot notation (`jar.capacity`). Behind the scenes, it routes the assignment or retrieval through your custom logic.

**Data Flow Visualization:**

- **Writing Data (`jar.capacity = 12`)**: Assignment -> Triggers `@capacity.setter` -> Runs validation -> Stores in `self._capacity`.
- **Reading Data (`print(jar.capacity)`)**: Access requested -> Triggers `@property` -> Returns `self._capacity`.

**Code Example (`Jar` Getters & Setters):**

```python
    @property
    def capacity(self):
        # Getter: Returns the underlying variable
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        # Setter: Validates data before storing it in the underlying variable
        try:
            int(capacity)
        except ValueError:
            raise ValueError('Pls input integers!')
        else:
            if not capacity >= 0:
                raise ValueError
        self._capacity = capacity
```

## 3. Class Methods (`@classmethod`)

Class methods handle functionality associated with the class itself, regardless of any specific object's instance variables.

- They do **not** have access to `self`.
- They take `cls` as their first argument, granting access to class variables.
- You can call them without first instantiating an object.
- They are often used as "alternative constructors" to instantiate and directly return a new object.

**Code Example (David Malan's `Student` Class):**

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    @classmethod
    def get(cls):
        # Called directly on the class: Student.get()
        name = input("Name: ")
        house = input("House: ")
        # Returns a new instantiated Student object
        return cls(name, house)

# How to call it:
student = Student.get()
```

## 4. Inheritance

When multiple classes share commonalities (attributes or methods), we extract those shared traits into a separate superclass. The original classes then inherit from this superclass, promoting code reuse and establishing a logical hierarchy.

**Code Example (Wizards and Students):**

```python
class Wizard:
    def __init__(self, name):
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        # Calls the __init__ of the Wizard superclass to handle the name
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# How to call it:
student = Student("Harry", "Gryffindor")
print(student.name)   # Inherited from Wizard -> outputs "Harry"
```

## 5. Operator Overloading

Operator overloading allows you to redefine how standard mathematical symbols (like `+`, `-`, `*`) work with your custom class objects by defining dunder methods like `__add__`.

Remember that **`self` and `other` are just variable names** representing the objects; you can technically name them anything (like `left_obj` and `right_obj`). A class is simply a blueprint, and **both** the left-side object and the right-side object are fully functional instances of that class. Because they are both objects from the same blueprint, **both** can access any attributes or methods inside the class.

**Code Example (Combining Game Scores):**

```python
class Score:
    def __init__(self, points):
        self.points = points

    def print_info(self):
        return f"Score value: {self.points}"

    # You can name the parameters anything (e.g., left_obj and right_obj),
    # and both can access instance attributes or methods!
    def __add__(left_obj, right_obj):
        # Both left_obj and right_obj can access instance methods and attributes:
        print(right_obj.print_info())

        total_points = left_obj.points + right_obj.points
        return Score(total_points)

# ---------------------------------------------------------
# HOW TO CALL IT:
# ---------------------------------------------------------
round1 = Score(10)
round2 = Score(15)

# Writing 'round1 + round2' triggers: round1.__add__(round2)
final_score = round1 + round2

print(final_score.points)  # Outputs: 25
```
