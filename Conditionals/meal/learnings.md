# Exercise 1.5: Meal Time (meal.py)

## 📌 Task Description

Implement a program that prompts the user for a time in 24-hour format (`#:##` or `##:##`) and outputs whether it's `breakfast time`, `lunch time`, or `dinner time`.

- **Breakfast:** 7:00 to 8:00 (inclusive)
- **Lunch:** 12:00 to 13:00 (inclusive)
- **Dinner:** 18:00 to 19:00 (inclusive)

---

## 💡 Core Logic & Time Conversion Mechanism

To make range comparisons straightforward (e.g., checking if a time falls between `7:00` and `8:00`), the `convert(time)` function translates a string time (like `"8:30"`) into a comparable `float` value (`8.5`).

- **Hour & Minute Splitting:** We split the input string by the colon (`:`) into hours and minutes.
- **Minute Normalization:** If there are minutes (e.g., `30` in `8:30`), we divide them by 60 to convert them into a decimal fraction ($30 / 60 = 0.5$) and add it to the hour.
- **Exact Hour Handling:** If the minutes are `00` or `0` (e.g., `8:00`), we skip minute division and return just the integer hour (`8`).

---

## 💻 Implementation

```python
def main():
    time = input('What is the time now? ')
    outcome = convert(time)
    judge(outcome)

def convert(time):
    # [Mistake 1 Location] Must assign split result to a variable
    cal = time.split(':')

    # [Mistake 2 Location] Fixed logical operator error when checking zero-minute cases
    if cal[1] != '00' and cal[1] != '0':
        minutes = int(cal[1]) / 60
        hour = int(cal[0])
        outcome = minutes + hour
    else:
        hour = int(cal[0])
        outcome = hour
    return outcome

def judge(time):
    if 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print('lunch time')
    elif 18 <= time <= 19:
        print('dinner time')
    else:
        print('')

if __name__ == '__main__':
    main()
```

---

## 🛠️ Python Learnings & Gotchas

### 1. String Immutability & Variable Assignment

- **Where:** `cal = time.split(':')`
- **What went wrong:** Initially tried to access or manipulate string parts without saving the returned list from `.split(':')` because strings in Python are immutable.
- **Why it matters:** Without capturing the split output in a variable (`cal`), we cannot index into `cal[0]` (hours) and `cal[1]` (minutes) to perform our fractional conversion.

### 2. Logical Operator Bug in Minute Checking (`and` vs `or`)

- **Where:** `if cal[1] != '00' and cal[1] != '0':`
- **What went wrong:**
  - Previously used `or` instead of `and` when checking for non-zero minutes.
  - For instance, with an exact hour input like `'00'`, `cal[1] != '00'` evaluates to `False`, but `cal[1] != '0'` evaluates to `True`. Because `or` only requires one condition to be true, the code incorrectly entered the minute-conversion branch.
- **The Fix:** Switched to an `and` operator to ensure both zero-checks hold true before treating it as a non-zero minute offset, ensuring exact hours correctly skip the division step.
