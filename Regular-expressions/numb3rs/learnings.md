# Learnings - CS50P Numb3rs

## Key Takeaways

1. **Regex Pattern Matching for Ranges**: Regular expressions match text patterns rather than evaluating numerical values. Validating 0–255 requires breaking down the range into explicit structural tiers:
   - **`0`**: Exact single zero `0`.
   - **`[1-9][0-9]?`**: Numbers from 1 to 99 (e.g., `1`, `9`, `10`, `99`).
   - **`1[0-9][0-9]`**: Numbers from 100 to 199 (e.g., `100`, `195`).
   - **`2[0-4][0-9]`**: Numbers from 200 to 249 (e.g., `200`, `249`).
   - **`25[0-5]`**: Numbers from 250 to 255 (e.g., `250`, `255`).
   - Combined pattern: `r"^(0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"`.

2. **Exact Boundary Anchors**: Always use anchors (`^` for start, `$` for end) or `re.fullmatch()`. Without them, `re.search()` performs partial matching. For example, matching `"300"` against `r"[0-9][0-9]?"` will successfully match the partial substring `"30"` and incorrectly pass an invalid number.

3. **Loop Control Flow & Return Statements**: Placing a `return` statement inside a loop terminates execution on the first iteration. To validate all items, invert the logic: use `if not condition: return False` to exit early only upon failure, and place `return True` outside the loop to ensure every item is fully checked.
