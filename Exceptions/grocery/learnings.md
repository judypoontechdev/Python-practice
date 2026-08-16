# Exercise 3.3: Grocery List (grocery.py)

## 📌 Task Description

Implement a program that prompts the user for items, one per line, until the user inputs Control-D (`Control-d` / EOF).

- **Output Formatting:** Output the user's grocery list in **all uppercase**, sorted **alphabetically** by item, prefixing each line with the number of times the user inputted that item (e.g., `1 APPLE`, `2 BANANA`).
- **Rules:** Do not pluralize items; treat input case-insensitively.

---

## 💡 Core Logic & Algorithm Mechanism

1. **Accumulating Frequency directly:** Instead of storing all inputs into an intermediate list and counting repeatedly, accumulate item counts directly into a dictionary using `.get(item, 0) + 1`.
2. **Normalized Key Storage:** Standardize inputs using `.strip().lower()` during entry so duplicates like `"apple"` and `"Apple"` update the same key seamlessly.
3. **Alphabetical Sorting:** Use `sorted(counting.keys())` to extract and sort dictionary keys alphabetically.
4. **Dictionary Comprehension Formatting:** Construct a sorted dictionary with uppercase keys using `{k.upper(): counting[k] for k in sorted(counting.keys())}`.
5. **KeyValue Iteration:** Iterate through `.items()` to print formatted pairs as `f'{value} {key}'`.

---

## 💻 Implementation (Python)

### Method 1: Initial Approach (List + Set + Count)

```python
def main():
    counting = {}
    bucket = []

    while True:
        try:
            items = input('')
            bucket.append(items)

        # Break when control-d
        except EOFError:
            print()
            break

        else:
            # Update the counting dictionary dynamically with each input
            unique = list(set(bucket))

            for u in unique:
                number = bucket.count(u)
                counting[u] = number

    # Alphabetically sort the dictionary keys, convert to uppercase, and format
    result = {k.upper(): counting[k] for k in sorted(counting.keys())}

    # Print the final sorted grocery list
    for key, value in result.items():
        print(f'{value} {key}')

if __name__ == '__main__':
    main()
```

### Method 2: Optimized & Simplified Approach (`.get()` Method)

```python
def main():
    counting = {}

    while True:
        try:
            # Normalize input directly
            item = input().strip().lower()

            # Increment count using .get() with default value 0
            counting[item] = counting.get(item, 0) + 1

        except EOFError:
            print()
            break

    # Sort keys alphabetically and capitalize
    sorted_result = {k.upper(): counting[k] for k in sorted(counting.keys())}

    # Print output formatted as "COUNT ITEM"
    for key, value in sorted_result.items():
        print(f'{value} {key}')

if __name__ == '__main__':
    main()
```

---

## 🛠️ Python Learnings & Gotchas

### 1. Removing Duplicates via `list(set())`

- **Where:** `unique = list(set(bucket))`
- **Technique:** Converting a list into a `set` automatically strips all duplicate elements. Wrapping it back with `list()` restores an iterable sequence of unique values.

### 2. Counting List Elements with `.count()`

- **Where:** `number = bucket.count(u)`
- **Technique:** Scans the list to return the total occurrences of element `u`.

### 3. Direct Dictionary Assignment & Updates

- **Where:** `counting[u] = number`
- **Technique:** Directly maps key `u` to value `number` inside the dictionary.

### 4. Alphabetical Sorting with `sorted()`

- **Where:** `sorted(counting.keys())`
- **Technique:** Returns a new sorted list containing all keys from the dictionary arranged in alphabetical order.

### 5. Tuple Unpacking via `.items()`

- **Where:** `for key, value in result.items():`
- **Technique:** Calling `.items()` converts dictionary key-value entries into a list of tuples `(key, value)`, allowing direct access to both variables within loop iterations.

### 6. Handling multi-line inputs via 'while True' & 'EOFError'

- **Where:** `while True:` block paired with `except EOFError:`
- **Technique:** Combining an infinite `while True` loop with `input()` allows continuous multi-line input collection (dynamically appending values to a list or updating a structure per iteration). The loop only breaks when the user sends an EOF signal (`Control-D`), triggering the `except EOFError` block to safely exit.

---

## ⚡ Code Simplification: Why Method 2 is Superior

1. **Eliminating Extra Memory Allocation:** Method 1 uses an extra `bucket` list to store every raw entry and re-runs `bucket.count(u)` inside a `set()` loop on every input iteration (an $O(N^2)$ operation that slows down significantly with large inputs). Method 2 updates counts in real time with $O(1)$ lookup performance.
2. **Leveraging `dict.get(key, default)`:** Using `counting[item] = counting.get(item, 0) + 1` checks if `item` exists in the dictionary. If present, it returns its current count; if absent, it safely falls back to `0` before adding `1`, entirely replacing the need for extra list storage or explicit key checks.
