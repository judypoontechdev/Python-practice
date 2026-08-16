# Exercise 2.2: Coke Machine (coke.py)

## 📌 Task Description

Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.

- **Cost:** A bottle of Coke costs 50 cents.
- **Accepted Denominations:** 25 cents, 10 cents, and 5 cents.
- **Output:** Once the user inputs at least 50 cents, calculate and output how many cents in change the user is owed (`Change Owed: X`).
- **Rule:** Ignore any integer input that is not an accepted denomination.

---

## 💡 Core Logic & Algorithm Mechanism

To handle continuous coin insertion and track accumulated payment:

1. **State Initialization:** Define an accumulator variable (`b = 0`) **outside** the loop to persist inserted values across iterations.
2. **Continuous Loop:** Use a `while True` loop to continuously prompt the user for coins until the threshold is met.
3. **Input Validation:** Convert the input to an integer (`int()`) and verify if it matches one of the valid coin values (`5`, `10`, or `25`).
4. **Accumulation & Termination:** Add valid coins to `b`. Once `b >= 50`, terminate the loop (`break`) and output the calculated change (`b - 50`).

---

## 💻 Implementation (Python)

```python
def main():
    # Initialize total accumulated coins outside the loop
    b = 0

    while True:
        try:
            a = int(input('What is the value of your coins? '))
        except ValueError:
            print('Pls input integers')
        else:
            # Check if the inserted coin is an accepted denomination
            if a in [5, 10, 25]:
                b += a

            # Exit loop once payment reaches or exceeds 50 cents
            if b >= 50:
                break

    print(f'Change owed: {b - 50}')

if __name__ == '__main__':
    main()
```

---

## 🛠️ Python Learnings & Gotchas

### 1. Variable Scope & Loop Initialization

- **Where:** Initializing `b = 0` at line 3 before `while True:`
- **What went wrong:** Placing state variables (like `b = 0`) _inside_ the `while` loop resets their value back to `0` on every iteration.
- **Why it matters:** Variables intended to accumulate values over time must be initialized outside the loop scope so state persists across iterations.

### 2. Logical Operators vs Sequence Membership (`or` vs `in`)

- **Where:** `if a in [5, 10, 25]:`
- **Syntax Gotcha:** Writing `if a == 5 or 10 or 25:` is a common bug. Python evaluates `10` and `25` as truthy non-zero integers, making the entire expression evaluate to `True` regardless of `a`.
- **Correct Approaches:**
  - **Explicit Equality Checks:** `if a == 5 or a == 10 or a == 25:` ensures each condition is evaluated against `a`.
  - **Idiomatic Python Membership:** `if a in [5, 10, 25]:` provides a far more concise and readable way to check if a value exists within a collection of valid options.
