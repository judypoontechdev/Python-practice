# Exercise 2.1: camelCase (camel.py)

## 📌 Task Description

Implement a program that prompts the user for the name of a variable in camel case (`camelCase`) and outputs the corresponding name in snake case (`snake_case`).

- **Input Example:** `preferredFirstName`
- **Output Example:** `preferred_first_name`
- **Rule:** Insert an underscore (`_`) before any uppercase letter and convert that letter to lowercase.

---

## 💡 Core Logic & Algorithm Mechanism

To convert camelCase to snake_case, we iterate through each character in the input string:

1. **Iterate by Index:** Loop through each character index from `0` to `len(camel) - 1`.
2. **Check Uppercase:** If the character at `camel[c]` is uppercase (`.isupper()`), prepend an underscore `_` and convert the character to lowercase using `.lower()`.
3. **Handle Lowercase:** Otherwise, keep the lowercase character as-is.
4. **Collect & Join:** Store processed characters in a list (`my_list`) and merge them into a single string using `''.join(my_list)`.

---

## 💻 Implementation (Python)

```python
def main():
    # Prompt the user for camelCase input
    camel = input('camelCase: ')
    snake(camel)

def snake(camel):
    # Define an empty list to store the converted characters
    my_list = []

    # Loop through each character index in the camelCase string
    for c in range(len(camel)):
        # If the character is uppercase, prepend an underscore and convert to lowercase
        if camel[c].isupper():
            my_list.append('_' + camel[c].lower())
        # Otherwise, keep the lowercase character as it is
        else:
            my_list.append(camel[c])

    # Join all elements in the list into a single string and print the result
    final = ''.join(my_list)
    print(final)

if __name__ == '__main__':
    main()
```

---

## 💻 Implementation Comparison (JavaScript)

For comparison, here is the equivalent implementation in JavaScript using traditional index-based iteration:

```javascript
function main() {
  const camel = prompt("camelCase: ");
  snake(camel);
}

function snake(camel) {
  let myList = [];

  // JavaScript index loop
  for (let i = 0; i < camel.length; i++) {
    // Robust uppercase check: Must equal uppercase AND NOT equal lowercase (to exclude numbers/symbols)
    if (
      camel[i] === camel[i].toUpperCase() &&
      camel[i] !== camel[i].toLowerCase()
    ) {
      myList.push("_" + camel[i].toLowerCase());
    } else {
      myList.push(camel[i]);
    }
  }

  const final = myList.join("");
  console.log(final);
}

main();
```

---

## 🛠️ Python Learnings & Gotchas

### 1. Index-Based Looping: Python `range(len())` vs JavaScript

- **Where:** `for c in range(len(camel)):`
- **Concept Difference:**
  - In JavaScript, looping by index is written using an explicit loop condition:
    ```javascript
    for (let i = 0; i < array.length; i++) { ... }
    ```
  - Python does not use `for (init; condition; step)` syntax. To iterate by index in Python, we generate a sequence of index numbers using `range(len(sequence))` and access elements via bracket indexing `sequence[c]`.
- **How `range()` Works:**
  - Python's `range()` stops right before the boundary number (exclusive upper bound). For example, `range(3)` produces `0, 1, 2`.
  - Because it starts at `0` and stops at `len - 1`, passing `range(len(camel))` naturally matches 0-based array indexing without needing to write `range(len(camel) - 1)`.
- **Key Takeaway:**
  - In Python, while iterating directly over elements (`for char in camel:`) is idiomatic when indices are not needed, using `range(len(camel))` grants direct access to the index `c`, serving the same role as `i` in JavaScript.

### 2. Uppercase Inspection: Python `.isupper()` vs JavaScript Inspection

- **Python Built-in:** Python provides `.isupper()` out of the box, which natively handles checking for uppercase letters while ignoring non-alphabetic characters.
- **JavaScript Workaround:** JavaScript has no native `isUpper()` string method. To achieve parity without Regex, JS requires checking if `char === char.toUpperCase()` **and** `char !== char.toLowerCase()` to prevent non-letter characters (e.g. numbers, punctuation) from falsely evaluating as uppercase.
