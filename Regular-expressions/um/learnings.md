# CS50P Regular Expressions - Learnings & Cheat Sheet

This file summarizes key regex shorthand character classes, flags, and the crucial concept of word boundaries (`\b`).

---

## 1. Regex Shorthand Character Classes & Boundaries

* **`\d`**: Decimal digits (`0-9`).
* **`\D`**: Not a decimal digit (anything except `0-9`).
* **`\s`**: Whitespace characters (spaces, tabs, newlines).
* **`\S`**: Not a whitespace character.
* **`\w`**: Word characters (letters `a-z`, `A-Z`, numbers `0-9`, and underscore `_`).
* **`\W`**: Not a word character (symbols, punctuation, spaces).
* **`\b`**: Word boundary (a zero-width invisible wall between a word character and a non-word character, or string start/end, used to match standalone words safely without consuming surrounding symbols).

---

## 2. Regex Flags (`re.IGNORECASE`, `re.MULTILINE`, `re.DOTALL`)

### 1. `re.IGNORECASE` (or `re.I`)
* **What it does**: Makes matching case-insensitive (treats uppercase and lowercase letters the same).
* **Code Example**:
  ```python
  import re
  result = re.findall(r"cat", "CAT and cat", re.IGNORECASE)
  # Returns: ['CAT', 'cat']
  ```

### 2. `re.MULTILINE`
* **Text to check**:
  ```text
  cat sat on the mat.
  dog barked at the cat.
  cat ran away.
  ```
* **Without Multiline (Default)**: If you use `r"^cat"`, it only looks at the absolute start of the entire string (line 1), matching only **1** result. The `cat` at the start of lines 2 and 3 are ignored because they are not at the very beginning of the whole text.
* **With `re.MULTILINE`**: The caret (`^`) expands to match the start of **every individual line**. Thus, the `cat` at the beginning of lines 1, 2, and 3 are all successfully matched, finding a total of **3** results.
* **Code Example & Explanation**:
  ```python
  import re
  text = "cat sat on the mat.\ndog barked at the cat.\ncat ran away."
  results = re.findall(r"^cat", text, re.MULTILINE)
  ```
  1. We import the `re` module to use regular expression functions in Python.
  2. We define a multi-line string containing the word `cat` at the beginning of different lines.
  3. `re.findall` uses the `re.MULTILINE` flag to match `^cat` at the start of every single line, returning all occurrences.

### 3. `re.DOTALL`
* **Text to check**:
  ```text
  Start: Hello World
  This is line 2.
  End: Goodbye
  ```
* **Without Dotall (Default)**: If you use `r"Start.*End"`, the dot (`.`) stops and breaks when it hits the newline character (`\n`) at the end of the first line, so it finds **nothing at all**.
* **With `re.DOTALL`**: The dot (`.`) gets the privilege to cross newline characters (`\n`). Therefore, `.*` can smoothly cross the middle line breaks until it reaches `End`, successfully matching the entire multi-line string.
* **Code Example & Explanation**:
  ```python
  import re
  text = "Start: Hello World\nThis is line 2.\nEnd: Goodbye"
  results = re.findall(r"Start.*End", text, re.DOTALL)
  ```
  1. We import the `re` module to handle regex operations in our script.
  2. We create a text block where `Start` and `End` are separated by line breaks (`\n`).
  3. `re.findall` uses `re.DOTALL` so the dot matches newlines, successfully capturing the entire block from `Start` to `End`.

---

## 3. The Power of `\b` (Word Boundary)

### What is `\b`?
* It is a **"zero-width assertion"** (an invisible wall or position).
* It marks the boundary between a word character (`\w`) and a non-word character (`\W`), or the start/end of a string.

### Why use `\b` instead of `\W`?
* If you use `\W` to check boundaries (e.g., `r"\Wum\W"`), it **"consumes"** (swallows) the surrounding punctuation or spaces. This breaks overlapping matches or sentences starting with the word (where there is no `\W` on the left).
* `\b` checks the boundary automatically without consuming any characters, handling spaces, punctuation, and start/end of strings effortlessly.

### Code Example:
```python
import re

text = "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"

# This will correctly find all standalone "um" (case-insensitive) 
# while ignoring substrings like "Mum", "album", "alums", and "umm".
standalone_ums = re.findall(r"\bum\b", text, re.IGNORECASE)

print(f"Found standalone 'um' count: {len(standalone_ums)}")
print(f"Matches: {standalone_ums}")
```
