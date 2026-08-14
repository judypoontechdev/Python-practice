# Figlet Exercise - Learnings

## Overview

The goal of this exercise is to utilize the external Python library `pyfiglet` to render text strings in large ASCII art fonts via command-line arguments. During this exercise, I strengthened my handling of command-line arguments (`sys.argv`), error handling with `sys.exit()`, and instantiating third-party classes to process and render text dynamically.

---

## Learning Reflection: Python Classes vs. JavaScript Prototypal Inheritance

Having recently completed a JavaScript course before diving into Python, I cross-compared both languages to better understand how they handle object creation and inheritance. In JavaScript, objects inherit directly from other objects through the prototype chain (prototypal inheritance), whereas Python uses a classical object-oriented approach built around explicit `class` definitions and instantiation. To bridge this concept, I implemented a simple `Dog` example in both languages:

**Python (Class-Based):**

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())
```

**JavaScript (Prototypal):**

```javascript
function Dog(name) {
  this.name = name;
}

Dog.prototype.bark = function () {
  return `${this.name} says woof!`;
};

const my_dog = new Dog("Buddy");
console.log(my_dog.bark());
```

---

## Summary of differences:

Python relies on a formal class blueprint where methods and properties are bundled neatly inside the block and instantiated via **init**, making object-oriented structures straightforward and structured. In contrast, JavaScript achieves similar behavior under the hood by linking object instances directly to shared prototype objects ( prototype ), offering a more dynamic and flexible approach to inheritance.
