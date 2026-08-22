# Python `csv` Module: Core Concepts

## 1. Reading CSV Files

### `csv.reader(file)`

- **Nature:** A factory function that returns a reader object (an iterator).
- **Return Type per Iteration:** A `list` of strings representing a single row (e.g., `['Potter, Harry', 'Gryffindor']`).
- **Header Handling:** Treats the first line of the file identically to standard data rows. If the CSV contains a header, `next(reader)` must be explicitly called before processing to extract or bypass the header row.
- **Subsequent Usage:** Paired with a manual `for` loop to iterate through the remaining rows line by line.

### `csv.DictReader(file, fieldnames=...)`

- **Nature:** A class constructor that instantiates and returns a `DictReader` object.
- **Return Type per Iteration:** A `dict` mapping column names to row data (e.g., `{'name': 'Potter, Harry', 'house': 'Gryffindor'}`).
- **Header Handling:** If `fieldnames` is omitted, the first row of the CSV is automatically consumed and assigned as the dictionary keys. If `fieldnames` is explicitly provided, those values serve as the keys.
- **Subsequent Usage:** Paired with a manual `for` loop to iterate through the dataset row by row.

---

## 2. Writing CSV Files

### `csv.writer(file)`

- **Nature:** A factory function that returns a writer object.
- **Subsequent Usage:**
  - Paired with the `.writerow([list])` method to write a single sequence to the file.
  - It does not loop automatically. To write multiple rows, a `for` loop must be explicitly constructed to execute `.writerow()` iteratively (or use `.writerows()` for an entire collection).

### `csv.DictWriter(file, fieldnames=[...])`

- **Nature:** A class constructor that instantiates and returns a `DictWriter` object.
- **Arguments & Attributes:** The `file` parameter functions as a positional argument. The `fieldnames` parameter is required; it passes a list that the object stores internally as an attribute (`self.fieldnames`), rather than inheriting it.
- **Subsequent Usage:**
  - **`.writeheader()`:** Executed once before writing data. It takes no arguments because it reads the internally stored `fieldnames` attribute to generate the header row.
  - **`.writerow(dict)`:** Executed to write one dictionary as a CSV row. It does not loop automatically. A manual `for` loop must be utilized to write multiple dictionaries sequentially.

---

## 3. String Manipulation Pitfalls

- **`string.strip().split(',')`:** The `.strip()` method only cleans leading and trailing whitespace from the _entire_ string prior to splitting. It does not clean whitespace that exists immediately after a comma.
- **`string.split(', ')`:** Utilizing a comma followed by a space as the delimiter successfully splits the elements and discards the separating space in a single operation.
