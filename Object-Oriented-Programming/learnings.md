# Python Documentation Study Guide & Learnings

## Key Takeaway: How to Study Documentation Effectively

Reading official documentation is a core skill for any developer. We can look at the **class definitions**, **constructors**, **class methods**, and **magic methods** directly from the source.

Below are two case studies breaking down how to read and interpret documentation using Python's built-in `datetime` library and the third-party `inflect` library.

---

## Case Study 1: Built-in `datetime` Module (`date` Class)

From the Python documentation for `date objects`:

```text
class datetime.date(year, month, day)
```

### 1. Hierarchy & Instantiation

- **`datetime`** is the module.
- **`date`** is the class inside the module.
- **`datetime.date(year, month, day)`** is the constructor used to **instantiate** a new date object (e.g., `date(2026, 8, 27)`).

### 2. Using Class Methods

Documentation often lists alternative constructors or utility tools as `classmethod`:

```text
classmethod date.today()
classmethod date.fromtimestamp(timestamp)
classmethod date.fromordinal(ordinal)
classmethod date.fromisoformat(date_string)
```

- **How to call them:** Because they are class methods, we call them directly on the class itself without needing an instance first (e.g., `date.today()` or `date.fromtimestamp(time.time())`).

### 3. Object-to-Object Operations & Magic Methods (`__sub__`, `__str__`)

When we calculate a time difference:

```python
difference = date2 - date1  # date object minus date object returns a timedelta object
```

- **Why can two objects be subtracted directly?** Just like `__add__` defines addition (`+`), Python classes use **magic methods** (specifically **`__sub__`**) under the hood to handle subtraction (`-`) between instances. Subtracting two `date` objects returns a `timedelta` object.
- **Why can we directly `print()` the object?** When we `print(difference)`, it cleanly outputs text (e.g., `10 days, 0:00:00`). This is because the class implements a **`__str__`** (or `__repr__`) method, which tells Python how to convert the object into a human-readable string automatically.

---

## Case Study 2: Third-Party `inflect` Library

From the `inflect.py` documentation:

```text
>>> import inflect
>>> p = inflect.engine()
```

### 1. Instantiating an Engine Object

- **`engine`** is a class inside the `inflect` module.
- **`inflect.engine()`** acts as the constructor function that **instantiates** the engine object, which we assign to the variable `p`.

### 2. Calling Instance Methods

Once the object `p` is created, we use it to call **instance methods** for English pluralization and number formatting:

```python
# Methods available from documentation:
p.plural_verb('was', count)
p.number_to_words(minutes, andword="")
p.plural_noun('person', count)
```

- We call these methods directly on our instantiated object `p` (e.g., `p.number_to_words(...)`) to access the library's functionality.
