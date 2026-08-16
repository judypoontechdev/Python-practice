# 📝 Exercise Learnings: Adieu, Adieu (`adieu.py`)

## 1. Task Description

Implement a program that continuously prompts the user for names (one per line) until input is terminated with `Control-D` (`EOFError`). The program then outputs a formatted farewell message adhering to standard English grammar and Oxford comma rules:

- **1 Name:** `Adieu, adieu, to [Name 1]`
- **2 Names:** `Adieu, adieu, to [Name 1] and [Name 2]`
- **3+ Names:** `Adieu, adieu, to [Name 1], [Name 2], ..., and [Name N]` (separated by $n-1$ commas and one `and`).

---

## 2. Logic & Algorithm Flow

1. **Initialize Data Structure:** Create an empty list `names` to store valid user inputs.
2. **Infinite Input Loop (`while True`):**
   - Continuously prompt the user with `Name: `.
   - **Input Sanitization:** Check `if name.strip():` to ensure non-empty strings and strip away accidental whitespaces before appending to `names`.
3. **Handle Exit Signal (`except EOFError`):**
   - Catch `Control-D` (`EOFError`), print a clean newline (`print()`) to prevent CLI line overlapping, and `break` out of the loop.
4. **Format & Output:**
   - Evaluate `len(names)` to apply conditional formatting rules ($1$, $2$, or $3+$ items) using string interpolation (`f-string`) and `.join()`.

---

## 3. Code Implementation

def main():
names = []

    while True:
        try:
            name = input("Name: ")
            if name.strip():
                names.append(name.strip())
        except EOFError:
            print()
            break

    output(names)

def output(names):
if len(names) == 1:
print(f"Adieu, adieu, to {names[0]}")
elif len(names) == 2:
print(f"Adieu, adieu, to {names[0]} and {names[1]}")
elif len(names) > 2:
formatted_names = ", ".join(names[:-1])
print(f"Adieu, adieu, to {formatted_names}, and {names[-1]}")

if **name** == "**main**":
main()

---

## 4. Learnings & Gotchas

### 1. Rejecting Empty Inputs & Whitespace via `.strip()`

- **Where:** `if name.strip():`
- **Technique:** Calling `.strip()` removes leading and trailing whitespaces. In Python, empty strings `""` evaluate to `False` in boolean contexts. Evaluating `if name.strip():` prevents blank lines or pure whitespace entries (e.g., accidental `Enter` presses) from being appended to the list.

### 2. Clean CLI Formatting on `Control-D` (`EOFError`)

- **Where:** `except EOFError:` block
- **Technique:** When a user triggers `Control-D` in the terminal to raise an `EOFError`, no trailing newline character is automatically emitted. Adding a simple `print()` statement inside the `except EOFError:` block before breaking ensures the final output begins neatly on a new line rather than directly adjacent to the input prompt.
