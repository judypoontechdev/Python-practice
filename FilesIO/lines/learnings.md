# Key Takeaways — CS50 Python: lines.py

## open() Modes & File Handling Exceptions

Opening a non-existent file in read mode (`open(file, "r")`) triggers a `FileNotFoundError`. Exception handling (`try...except`) is required to prevent the script from crashing. In contrast, write (`"w"`) or append (`"a"`) modes automatically create the file if missing. Using the `with` context manager does not bypass `FileNotFoundError` when a file is missing; its primary function is ensuring the file closes automatically upon block exit.

## File Object Iteration

A file handle in Python is directly iterable. Running `for line in file:` loops through the file line by line without needing to load the entire dataset into memory at once via `readlines()`.

## Implicit Truthiness & Defensive Guards

In the conditional `if stripped and not stripped.startswith('#'):`

- `stripped` acts as an implicit boolean guard. Non-empty strings evaluate to `True`, while empty strings `""` (blank lines) automatically evaluate to `False`.
- This eliminates redundant explicit length checks like `len(stripped) > 0`.

## Toggle Logic & Multi-line String Handling

Docstrings are considered valid code lines in this exercise, but multi-line block toggling (`state = not state`) remains a useful pattern for stateful parsing.

## Handling Multi-Line Quotes on the Same Line

To account for standard block entries and single-line docstrings (where opening and closing quotes exist on the same line, e.g., `''' docstring '''`), count the total triple-quote occurrences per line. An odd count flips the state; an even count leaves the state unchanged while skipping the line.

```python
import sys

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.py'):
        sys.exit('Invalid command line arguments')

    count = 0
    state = False

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                stripped = line.strip()

                # Count triple-quote occurrences on the line
                triple_single = stripped.count("'''")
                triple_double = stripped.count('"""')
                total_quotes = triple_single + triple_double

                if total_quotes > 0:
                    # If quotes appear, check state transition
                    if total_quotes % 2 != 0:
                        state = not state
                    continue  # Skip counting the line containing docstring syntax

                # Skip processing if currently inside a multi-line docstring block
                if state:
                    continue

                # Count valid code lines (excluding blank lines and # comments)
                if stripped and not stripped.startswith('#'):
                    count += 1

    except FileNotFoundError:
        sys.exit('File does not exist')

    print(count)

if __name__ == '__main__':
    main()
```
