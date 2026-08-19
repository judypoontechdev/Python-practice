# Learnings: CS50P - Bitcoin Price Index (`bitcoin.py`)

## Task Overview

The goal of this task was to create a command-line script (`bitcoin.py`) that accepts the number of Bitcoins as an argument, fetches the real-time Bitcoin price in USD using the CoinCap v3 API via the `requests` library, calculates the total cost, and formats the output as currency.

---

## Key Learnings

### 1. Command-Line Arguments & `sys.argv` Length

- **Mistake:** Initially checked `if len(sys.argv) != 1:` to verify user input.
- **Takeaway:** `sys.argv[0]` is always the script name itself (`bitcoin.py`). Therefore, expecting exactly **one** command-line argument requires checking `if len(sys.argv) != 2:`.

### 2. Handling Network Errors with `requests.RequestException`

- **Takeaway:** `requests.RequestException` is the base exception class for all HTTP request errors in the `requests` library (e.g., network loss, invalid URLs, missing protocols like `https://`). Catching this ensures network failures fail gracefully.

### 3. Understanding `json.dumps()` vs `response.json()`

- **Mistake:** Used `json.dumps()` thinking it formatted the dictionary for key-based access.
- **Takeaway:** `json.dumps()` converts a dictionary into a **formatted string** (for display/logging), rendering key lookup (`['data']`) invalid. To navigate nested data, use `response.json()` directly, which returns a native Python dictionary.

### 4. Data Type Conversion (String to Float)

- **Mistake:** Attempted to multiply `priceUsd` directly with the Bitcoin quantity.
- **Takeaway:** API values returned in JSON (like `"priceUsd"`) are often formatted as strings (e.g., `"69088.32"`). Extracted price strings must be explicitly cast using `float()` before performing arithmetic operations.

### 5. Number Formatting (`:,.4f`)

- **Takeaway:** To format floating-point numbers into standard currency presentation:
  - `,` adds commas as thousands separators (e.g., `1,000`).
  - `.4f` rounds and pads the number to exactly 4 decimal places.
  - Example: `f"${total_price:,.4f}"` outputs `$97,845.0243`.

### 6. Setting Up `.env` File and Terminal Commands

- **Purpose**: Store secrets and sensitive credentials (e.g., API keys, database passwords) locally without exposing them in git repositories.
- **Terminal Setup**:
  - Install dependency: `pip install python-dotenv`
  - Ensure `.env` is added to `.gitignore`
- **Inside `.env`**:
  - Use simple `KEY=VALUE` pairs (no quotes, no spaces around `=`).
  - Example:
    ```env
    COINCAP_API_KEY=your_actual_api_key_here
    ```

---

### 7. Core Concepts: Operating System, `os` Module, and `load_dotenv()` vs `os.getenv()`

- **Understanding the Operating System (OS)**:
  - **Concept**: An Operating System (e.g., macOS, Windows, Linux) is the core system software that manages computer hardware (CPU, RAM, SSD) and provides a runtime environment for programs to execute.
  - **Role**: It acts as an intermediary between hardware and your code, managing memory allocation, file systems, and background system processes.

- **Understanding the `os` Module**:
  - **Concept**: `os` is Python's built-in module that provides a bridge between your script and the underlying Operating System.
  - **Role**: It allows Python to interact with OS-level features, including managing processes, navigating file directories, and accessing environment variables stored in RAM.

- **`load_dotenv()` (Reads File & Loads to RAM)**:
  - **Action**: Opens the `.env` file on disk (SSD), reads the `KEY=VALUE` pairs, and populates them directly into system memory (RAM) as OS environment variables.
  - **Completion**: Once executed, its job is done—the `.env` file is no longer accessed during runtime.

- **`os.getenv('KEY_NAME')` (Fetches Data from RAM)**:
  - **Action**: Queries the active OS process memory (RAM) via the `os` module to retrieve the value associated with the specified environment variable name.
  - **Key Behavior**: It has no direct interaction with or awareness of the physical `.env` file; it strictly reads what is already present in the OS environment.

---

### 8. Implementation Inside the Script (`load_dotenv()` & `os.getenv()`)

- **Step 1: Load Environment Variables**
  - Call `load_dotenv()` early in the script execution (usually right after imports).
- **Step 2: Retrieve Key via `os.getenv()`**
  - Use `os.getenv('KEY_NAME')` to retrieve the environment variable.
  - Unlike dictionary access (`os.environ['KEY_NAME']`), `os.getenv()` safely returns `None` instead of throwing a `KeyError` if the key does not exist.
- **Example Code Integration**:

  ```python
  import os
  import requests
  from dotenv import load_dotenv

  # Load variables from .env into system environment
  load_dotenv()

  # Retrieve API key
  api_key = os.getenv("COINCAP_API_KEY")

  # Use in API request
  response = requests.get(f"[https://rest.coincap.io/v3/assets/bitcoin?apiKey=](https://rest.coincap.io/v3/assets/bitcoin?apiKey=){api_key}")
  ```
