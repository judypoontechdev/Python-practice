# Learnings: Processing CSV Data & Data Structures in Python

### Reading Technical Documentation

- **Targeted Syntax Usage**: Learned how to read library docs (like `tabulate`) to identify supported input types (e.g., `list of lists` vs. `list of dicts`) and map them to appropriate modules.

### `csv.reader` vs. `csv.DictReader`

- **`csv.reader`**: Yields each CSV row as a **list** of values (`List[str]`). Works seamlessly with `tabulate(..., headers="firstrow")`.
- **`csv.DictReader`**: Maps each row to a **dictionary** (`Dict[str, str]`) using header names as keys. Pair with `tabulate(..., headers="keys")`.

### Streamlining Data Conversion with `list()`

- **Avoiding Redundant Loops**: Instead of initializing an empty list `[]` and manually appending each row via a `for` loop:
  ```python
  # Redundant pattern
  data = []
  for row in reader:
      data.append(row)
  ```
- **Direct Conversion**: Pass the CSV reader iterator directly into the `list()` constructor to instantly build either a 2D list (`list of lists`) or a list of dictionaries (`list of dicts`):
  ```python
  # Efficient pattern
  data = list(reader)
  ```
