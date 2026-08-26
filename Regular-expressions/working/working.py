import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = re.search(r'([1-9]|[1][0-2]):?([0-5][0-9])?\s+(AM|PM)\s+to\s+([1-9]|[1][0-2]):?([0-5][0-9])?\s+(AM|PM)', s)

    if time:
        try:
            hour_start = int(time.group(1))
            minute_start = int(time.group(2)) if time.group(2) else 0
            hour_end = int(time.group(4))
            minute_end = int(time.group(5)) if time.group(5) else 0
        except ValueError:
            sys.exit('Pls input integers for time')

        if not 1 <= hour_start <= 12 or not 0 <= minute_start < 60 or not 1 <= hour_end <= 12 or not 0 <= minute_end < 60:
            raise ValueError('Invalid time range!  Please retry.')

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
    else:
        raise ValueError('Pls input correct time format!')

    return f'{start} to {end}'

if __name__ == "__main__":
    main()
