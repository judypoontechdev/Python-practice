# Exercise 3.1: Fuel Gauge (fuel.py)

## 📌 Task Description

Implement a program that prompts the user for a fraction, formatted as `X/Y`, wherein `X` is a non-negative integer and `Y` is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.

- **Empty Tank:** If 1% or less remains, output `E` instead.
- **Full Tank:** If 99% or more remains, output `F` instead.
- **Validation Rules:** Re-prompt the user if `X` or `Y` is not an integer, if `X > Y`, or if `Y == 0`.
- **Exception Handling:** Explicitly catch exceptions like `ValueError` and `ZeroDivisionError`.

---

## 💡 Core Logic & Validation Flow

To handle user re-prompting and error catching gracefully:

1. **Continuous Retry Loop:** Wrap input prompt and conversion within a `while True` loop so the program repeatedly asks for input until valid data is provided.
2. **Action Inside `try` Block:** Place the action to be repeated (prompting input, splitting by `/`, list comprehension integer casting, and testing division) directly inside the `try` block.
3. **Exception Handling:** Catch `ValueError` (for non-integer inputs) and `ZeroDivisionError` (when denominator `Y == 0`).
4. **Business Logic in `else`:** Use the `else` block to validate domain rules ($X \ge 0$, $Y > 0$, and $X \le Y$). If requirements are met, `break` out of the loop; otherwise, print an error message to prompt again.
5. **Output Evaluation:** Calculate $Percentage = \text{round}\left(\frac{X}{Y} \times 100\right)$ and evaluate output conditions (`<= 1` $\rightarrow$ `E`, `>= 99` $\rightarrow$ `F`, else `output%`).

---

## 💻 Implementation (Python)

```python
def main():
    while True:
        try:
            # Prompt user for fraction input and split it by the slash
            amount = input('Fraction: ')
            amounts = amount.split('/')

            # Convert string inputs into a list of integers using list comprehension
            z = [int(a) for a in amounts]

            # Test division to catch ZeroDivisionError if denominator is 0
            z[0] / z[1]

        except ValueError:
            # Catch invalid integer conversions (e.g. letters or decimals)
            print('Your input is not an integer')

        except ZeroDivisionError:
            # Catch division by zero errors
            print('y cannot be 0')

        else:
            # Validate business rules: X >= 0, Y > 0, and X <= Y
            if z[0] >= 0 and z[1] > 0 and z[0] <= z[1]:
                break
            else:
                print('Invalid numbers according to requirement. Try again!')

    # Calculate percentage and round to the nearest integer
    output = (z[0] / z[1]) * 100

    judge(round(output))

def judge(output):
    # Evaluate percentage and print corresponding fuel level message
    if output <= 1:
        print('E')
    elif output >= 99:
        print('F')
    else:
        print(f'{output}%')

if __name__ == '__main__':
    main()
```

---

## 🛠️ Python Learnings & Gotchas

### 1. Re-prompting with `while True` + `try`

- **Where:** `while True:` wrapping the entire `try...except...else` block.
- **Key Takeaway:** Using `try...except` alone only catches an error once without looping. Combining `while True` with `try` ensures the program re-prompts the user continuously until valid input allows the execution flow to reach `break`.
- **Action Location:** Place the action to be repeated (e.g., `input()`) _inside_ the `try` block so that any runtime exception immediately restarts the attempt cycle.

### 2. List Comprehension for Inline Array Conversion

- **Where:** `z = [int(a) for a in amounts]`
- **Technique:** Simulates array mapping (like `Array.prototype.map` in JavaScript) directly in Python. It cleanly converts a list of split strings into integers in a single, concise line.

### 3. Separation of Concerns: `except` vs `else`

- **Catching Errors (`except`):** Reserved strictly for catching Python syntax or runtime exception crashes (`ValueError`, `ZeroDivisionError`).
- **Business Logic Validation (`else`):** Used to check domain rule constraints ($X \le Y$) _after_ verifying that no code execution errors occurred. `break` is only executed when the input fits all business requirements.
