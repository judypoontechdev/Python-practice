# Exercise 3.2: Felipe’s Taqueria (taqueria.py)

## 📌 Task Description

Implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs Control-D (`Control-d` / EOF), which is a common way of ending input to a program.

- **Output Formatting:** After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign (`$`) and formatted to two decimal places (e.g., `$8.50`).
- **Case Insensitivity:** Treat the user's input case-insensitively (menu items are titlecased).
- **Invalid Input:** Ignore any input that isn't a menu item.

---

## 💡 Core Logic & Algorithm Mechanism

1. **Titlecase Normalization:** Clean user input using `.title().strip()` to automatically match key formatting in the `taqueria` dictionary regardless of input case or extra spaces.
2. **Key Extraction & Validation:** Extract dictionary keys via `list(taqueria.keys())` and verify if the input exists in the menu.
3. **Accumulating Total:** Increment the running total `current += taqueria[item]` when a valid item is matched.
4. **Flow Control with `continue`:** If an invalid item is entered, trigger `continue` inside the `else` block to immediately skip execution of the printing line and jump back to the top of the `while True` loop.
5. **Termination via `EOFError`:** Catch `EOFError` when the user presses `Control-d`, cleanly breaking out of the loop and terminating the program.

---

## 💻 Implementation (Python)

```python
def main():
    taqueria = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Extract all menu item names into a list for validation
    total = list(taqueria.keys())

    # Initialize the running total cost to 0
    current = 0

    # Continuously prompt the user for orders until EOF (Ctrl+D) is received
    while True:
        try:
            item = input('Item: ').title().strip()

            # Check if the entered item exists in the menu
            if item in total:
                # Add the item's price to the running total
                current += taqueria[item]
            else:
                # Skip invalid items that are not on the menu
                continue

            print(f'${current:.2f}')

        # Catch Ctrl+D (EOF) to gracefully exit the loop with a newline
        except EOFError:
            print()
            break

if __name__ == '__main__':
    main()
```

---

## 🛠️ Python Learnings & Gotchas

### 1. Re-looping via `continue`

- **Where:** Inside the `else` block (`continue`).
- **Key Takeaway:** While we normally rely on `try-except` or `try-else` handling to manage flow, using `continue` directly in the middle of a loop immediately halts further statement execution in the current iteration and jumps straight back to the top of the `while` loop. This prevents printing the current price when invalid items are entered.

### 2. Signal Handling with `EOFError`

- **Where:** `except EOFError:`
- **Key Takeaway:** A specialized exception triggered when an end-of-file condition is signaled via keyboard shortcuts (`Ctrl+D` on Unix/Mac or `Ctrl+Z` on Windows). Catching `EOFError` allows the program to terminate cleanly without crashing when the user finishes inputting data.

### 3. Currency Precision Formatting (`:.2f` vs `round()`)

- **Where:** `print(f'${current:.2f}')`
- **Key Takeaway:** Using standard `round(12.2, 2)` outputs `12.2` without trailing zeros. To strictly maintain standard financial output (e.g., converting `12.2` to `12.20` or rounding `12.256` to `12.26`), format floating-point values using the `:.2f` string specifier.
