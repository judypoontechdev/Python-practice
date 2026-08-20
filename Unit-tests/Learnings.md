# Unit Testing Learnings & Key Takeaways

## 1. Module Execution & Test Isolation (`test_twttr`)

- **The `if __name__ == "__main__":` Safety Net**:
  - **Mistake**: Forgetting `if __name__ == "__main__": main()` causes `main()` to execute automatically when imported by `pytest`. Because `pytest` cannot handle manual `input()`, the test suite crashes.
  - **Mechanism**: Every Python file has a built-in `__name__` variable.
    - Executing directly -> `__name__ == "__main__"`.
    - Importing as a module -> `__name__ == "filename"` (e.g., `"fuel"`).
  - **Takeaway**: Always wrap `main()` execution behind this conditional guard so tests can import helper functions without triggering full program execution.

- **Granular Test Functions**:
  - Break tests into multiple small, focused test functions (e.g., `test_vowels()`, `test_numbers()`, `test_punctuation()`) rather than one giant function.
  - If an `assert` fails, `pytest` stops that specific test function. Splitting tests ensures failure in one case does not block execution of independent test cases.

- **Refactoring for Testability**:
  - Core logic functions must **return values**, not `print()` them.
  - `print()` creates side effects (output to stdout) which unit tests cannot directly compare with simple `assert` statements.

---

## 2. Input Normalization & Helper Responsibilities (`test_bank`)

- **Shift String Transformations to Core Functions**:
  - **Mistake**: Placing `.lower().strip()` inside `main()` on user `input()` leaves string cleaning untested.
  - **Problem**: `pytest` tests helper functions directly, bypassing `main()`. If `main()` handles cleaning, dirty test inputs passed directly to helper functions (e.g., `" Hello "`) will fail.
  - **Solution**: Move input sanitization (like `.lower().strip()`) inside the helper function itself. This guarantees consistent behavior across both manual user execution and automated unit testing.

```python
# In main() - Hard to unit test string cleaning
greeting = input("Greeting: ").strip().lower()
value(greeting)

# Inside helper function - Clean, self-contained, testable
def value(greeting):
    greeting = greeting.strip().lower()
    ...
```

---

## 3. Business Logic vs. System Errors (`test_fuel`)

- **Explicit Business Logic Errors**:
  - Custom rules (e.g., X > Y, negative numbers, missing `/`) must be explicitly validated and thrown using `raise ValueError` or `raise ZeroDivisionError`.
  - Grouping guard clauses at the top of the function ensures custom constraints convert into standard Python exceptions for `main()` and `pytest` to handle.

- **Implicit Runtime Errors**:
  - Non-business logic errors (e.g., passing non-numeric text like `"cat/dog"` to `int()`) naturally trigger standard Python exceptions (`ValueError`).
  - You do not need explicit `if` checks for syntax/type failures—let Python raise them natively.

```python
def convert(fraction):
    fractions = fraction.split('/')
    if len(fractions) != 2:
        raise ValueError  # Explicit Business Rule

    z = [int(f) for f in fractions]  # Implicit Type Check (fails naturally on non-ints)

    if z[1] == 0:
        raise ZeroDivisionError  # Explicit Business Rule
    if z[0] < 0 or z[1] < 0 or z[0] > z[1]:
        raise ValueError  # Explicit Business Rule

    return round((z[0] / z[1]) * 100)
```

---

## 4. `pytest` Syntax & The `with` Statement

Unit tests generally fall into two categories:

### Type 1: Return Value Assertions

Used when validating deterministic function outputs.

```python
assert convert("3/4") == 75
assert gauge(1) == "E"
```

### Type 2: Exception Handling

Used when verifying that bad input raises the expected error.

```python
import pytest

with pytest.raises(ValueError):
    convert("cat/dog")

with pytest.raises(ZeroDivisionError):
    convert("1/0")
```

### Context Managers (`with` Keyword)

- **What `with` Does**: The `with` keyword establishes a temporary runtime context (Context Manager) that sets up resources, monitors code execution inside its indented block, and handles cleanup or exceptions upon exiting.
- **How `pytest.raises` Uses It**:
  1. `with pytest.raises(ValueError):` instructs `pytest` to monitor the block.
  2. If the code inside throws `ValueError`, the Context Manager catches and suppresses it, marking the test as **PASSED**.
  3. If no exception (or a different exception) is thrown, it flags the test as **FAILED**.

```

```
