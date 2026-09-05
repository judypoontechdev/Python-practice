# Project Learnings & Technical Takeaways

## 1. State Persistence and RAM Volatility (Managing the Running Total)

When designing a personal finance tracker, tracking the cumulative running total is essential. Initially, setting `total = 0` in the script serves to initialize the tracking mechanism. However, a major bottleneck arises: every time the script is rerun from the terminal, the running total resets and only reflects the newly inputted transaction rather than accumulating past historical records.

- **The Reason**: Every script execution allocates an isolated, temporary block of **RAM**. Because RAM is volatile memory, all runtime variables are completely wiped the moment the program finishes executing.
- **The Solution**: To prevent data loss between runs, the program must implement a retrieval function (such as `get_previous_total()`) to fetch the persistent historical balance directly from disk storage (`finance.csv`) before processing new inputs.

---

## 2. File Handling Logic: Comparing Reader and Writer Validation

When interacting with persistent storage, safeguarding against missing files or empty 0-byte placeholders is crucial. However, the validation strategy differs significantly between reading and writing due to how Python's file streams behave.

### Part A: Reader Validation (`get_previous_total`) & The Empty-List Catch

When reading historical data, the validation must be handled in **two separate, sequential steps** because the reading process cannot create a missing file on its own:

```python
def get_previous_total():
    # Step 1: Check if the file path exists first to prevent FileNotFoundError
    if not os.path.exists('finance.csv'):
        return 0.0

    # Step 2: Open and parse the file contents
    with open('finance.csv') as file:
        reader = list(csv.DictReader(file))

        # Step 3: Check if the file contains actual rows
        if not reader:
            return 0.0

        return float(reader[-1]["Total"])
```

- **Why it requires separate checks**:
  1. If the file does not exist, attempting to open it directly throws a fatal `FileNotFoundError`. Therefore, path existence must be checked first.
  2. Even if the file exists, `csv.DictReader` works by taking headers as keys and contents as values to form dictionaries. If the file is completely empty (0 bytes) or contains _only_ a header with no content rows below it, there are no values to pair with the keys, meaning no dictionaries can be formed and `list(DictReader)` will return an empty list `[]`.
  3. Evaluating `if not reader:` catches this empty list, preventing a fatal `IndexError` that would occur if you tried to index `reader[-1]` on an empty structure, allowing the script to safely return `0.0`.

### Part B: Writer Validation (`output`)

When writing or appending data to the tracker, the validation logic can be streamlined into a **combined, single-line check**:

```python
def output():
    # Combined check: evaluates both existence and content size upfront
    file_exists = os.path.exists('finance.csv') and os.path.getsize('finance.csv') > 0

    with open('finance.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=["Income", "Expense", "Source", "Total"])

        # If the file didn't exist or was empty, write the header row first
        if not file_exists:
            writer.writeheader()

        writer.writerow(user_input())
```

- **Why it differs from the Reader**:
  - Unlike reading—where a missing file causes an immediate crash—opening a file in append mode (`'a'`) allows Python's file stream to dynamically create the file on the fly if it is missing.
  - By checking `os.path.exists('finance.csv') and os.path.getsize('finance.csv') > 0` upfront, `writer.writeheader()` will only run if the file is truly empty or non-existent, successfully preventing issues like duplicate or repeated headers.
