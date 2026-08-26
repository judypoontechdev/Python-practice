# CS50P Working 9 to 5 - Learnings & Key Takeaways

## 1. Algorithm Overview

The core objective of this exercise is to convert 12-hour US time formats (e.g., `9:00 AM to 5:00 PM`) into 24-hour time formats (`09:00 to 17:00`). As shown in the input possibilities, the program must gracefully handle combinations with or without minutes:

- `9:00 AM to 5:00 PM`
- `9 AM to 5 PM`
- `9:00 AM to 5 PM`
- `9 AM to 5:00 PM`

### Core Conversion Logic:

- **Hours:**
  - If **PM**, add `12` to the hour (except for `12 PM`, which remains `12`).
  - If **AM**, keep it as it is (except for `12 AM`, which converts to `00`).
- **Minutes:**
  - Keep the captured minute as it is.
  - If the input omits the minutes (e.g., `9 AM`), default it to `0`.

---

## 2. Key Takeaways

### Key Takeaway 1: Handling Optional Regex Groups (`None` Check)

When a regex pattern contains an optional capturing group (such as the optional minute portion `([0-5][0-9])?`), if the user input omits it (e.g., `9 AM`), `time.group()` will return `None`.

We can handle this cleanly using a inline conditional expression to default it to `0`:

```python
minute_start = int(time.group(2)) if time.group(2) else 0
```

### Key Takeaway 2: Defensive Programming for Unmatched Inputs

If `re.search()` fails to find a match because the user input doesn't fit the expected format, it returns `None`. Failing to check for this can lead to runtime errors like `UnboundLocalError`. We must explicitly validate the search result early:

```python
if not time:
    raise ValueError('Please input correct time format!')
```

### Key Takeaway 3: Code Refactoring (Simplifying Complex Conditionals)

Originally, I used multiple redundant `if` statements to handle every permutation of AM/PM and 12-hour edges separately, which made the code overly verbose and messy (Version X).

I refactored this into a much cleaner, more maintainable structure using helper logic and uniform formatting (Version Y).

**Original Code (X):**

```python
if time.group(3) == 'AM' and not hour_start == 12:
    start = f'{hour_start:02}:{minute_start:02}'
if time.group(6) == 'AM' and not hour_end == 12:
    end = f'{hour_end:02}:{minute_end:02}'
if time.group(3) == 'AM' and hour_start == 12:
    start = f'00:{minute_start:02}'
if time.group(6) == 'AM' and hour_end == 12:
    end = f'00:{minute_end:02}'
if time.group(3) == 'PM' and not hour_start == 12:
    start = f'{12 + hour_start}:{minute_start:02}'
if time.group(6) == 'PM' and not hour_end == 12:
    end = f'{12 + hour_end}:{minute_end:02}'
if time.group(3) == 'PM' and hour_start == 12:
    start = f'{hour_start}:{minute_start:02}'
if time.group(6) == 'PM' and hour_end == 12:
    end = f'{hour_end}:{minute_end:02}'
```

**Refactored Code (Y):**

```python
def get_24hr(hour, period):
    if period == 'AM':
        return 0 if hour == 12 else hour
    else:  # PM
        return 12 if hour == 12 else hour + 12

start_hour = get_24hr(hour_start, time.group(3))
end_hour = get_24hr(hour_end, time.group(6))

start = f'{start_hour:02}:{minute_start:02}'
end = f'{end_hour:02}:{minute_end:02}'
```

### Key Takeaway 4: Regular Expression Breakdown

Let's break down the regex pattern used to validate and capture the time range:
`r'([1-9]|[1][0-2]):?([0-5][0-9])?\s+(AM|PM)\s+to\s+([1-9]|[1][0-2]):?([0-5][0-9])?\s+(AM|PM)'`

- `([1-9]|[1][0-2])` **[Group 1 & 4]**: Matches the hour, allowing single digits from `1-9` or double digits `10`, `11`, and `12`.
- `:?` **[Optional Colon]**: Matches an optional colon separating the hour and minutes (e.g., matching both `9` and `9:00`).
- `([0-5][0-9])?` **[Group 2 & 5]**: An optional group matching valid minutes from `00` to `59`.
- `\s+` **[Whitespace]**: Matches one or more spaces separating the time and the period.
- `(AM|PM)` **[Group 3 & 6]**: Matches either literal `"AM"` or `"PM"`.
- `\s+to\s+` **[Literal Separator]**: Ensures both time blocks are strictly connected by the word `"to"` surrounded by spaces.
