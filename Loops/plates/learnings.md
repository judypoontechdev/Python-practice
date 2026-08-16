# Exercise 2.4: Vanity Plates (plates.py)

## 📌 Task Description

Implement a program that prompts the user for a vanity plate and outputs `Valid` if it meets all requirements, or `Invalid` if it does not.

- **Length Constraint:** Must contain between 2 and 6 characters (inclusive).
- **Starting Requirement:** Must start with at least two letters.
- **Number Rules:**
  - Numbers must come at the end (no letters after the first number).
  - The first number used cannot be `'0'`.
- **Character Restrictions:** No periods, spaces, or punctuation marks allowed.

---

## 💡 Core Logic & Validation Flow

To validate a vanity plate, `is_valid(s)` checks each rule sequentially and returns `False` as soon as a rule is violated:

1. **Allowed Characters Check:** Iterate through all characters to ensure each is either alphabetic (`.isalpha()`) or numeric (`.isnumeric()`).
2. **Start Characters Check:** Ensure the first two characters (`s[0]` and `s[1]`) are letters.
3. **Length Bounds Check:** Verify `2 <= len(s) <= 6`.
4. **Number Placement & First Digit Rules:**
   - Iterate through indices using `range(len(s))` to locate the index `p` of the **first number**.
   - Check if this first digit is `'0'`. If so, return `False`.
   - Use string slicing (`s[p + 1:]`) to inspect all characters occurring _after_ the first digit. If any of those remaining characters are letters (`.isalpha()`), return `False`.

---

## 💻 Implementation (Python)

```python
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    # No periods, spaces, or punctuation marks allowed
    for p in plate:
        if not p.isalpha() and not p.isnumeric():
            return False

    # Must have two English alphabets as starting
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    # Length MIN 2 MAX 6
    if not 2 <= len(plate) <= 6:
        return False

    # Numbers can't be in between alphabets
    for p in range(len(plate)):
        if plate[p].isnumeric():
            # The first number cannot be '0'
            if plate[p] == '0':
                return False

            # Check remaining slice after the first number for any letters
            for q in plate[p + 1:]:
                if q.isalpha():
                    return False
            break

    return True

if __name__ == '__main__':
    main()
```

---

## 🛠️ Python Learnings & Gotchas

### 1. Identifying the First Match Pattern (`for` + `break`)

- **Finding First Occurrence:** To identify something that appears **first** in a loop, use a `for` loop combined with `break`:
  ```python
  for p in range(len(plate)):
      if plate[p].isnumeric():
          # Index p is now captured as the FIRST number's index
          break
  ```
  This pattern stops the loop as soon as the first match is found, freezing `p` at that exact position so the index can be passed down for further evaluations.

### 2. Slicing the Remaining Substring (`plate[p + 1:]`)

- **Extracting After First Match:** Once index `p` of the first number is identified, `plate[p + 1:]` extracts all characters that come after it.
- **Validation Check:** Sweeping through this remaining slice (`for q in plate[p + 1:]`) allows us to ensure that no alphabetic characters appear after the numeric sequence begins.

### 3. Logic Negation Gotcha: `if not ... and not ...`

- **Common Mistake:** Writing `if not A and B` (or `if not A or B`) often leads to logic bugs due to operator precedence.
- **Correct Syntax:** To check that a character is _neither_ a letter _nor_ a number, both conditions must be explicitly negated: `if not p.isalpha() and not p.isnumeric():`.

### 4. New String Inspection Methods

- **`.isalpha()`**: Returns `True` if all characters in the string are alphabetic letters.
- **`.isnumeric()`**: Returns `True` if all characters in the string are numeric digits.
