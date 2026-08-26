import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = re.search(r'([1-9]|[1][0-2]):?([0-5][0-9])?\s+(AM|PM)\s+to\s+([1-9]|[1][0-2]):?([0-5][0-9])?\s+(AM|PM)', s)

    if not time:
        raise ValueError('Pls input correct time format!')

    try:
        hour_start = int(time.group(1))
        minute_start = int(time.group(2)) if time.group(2) else 0
        hour_end = int(time.group(4))
        minute_end = int(time.group(5)) if time.group(5) else 0
    except ValueError:
        sys.exit('Pls input integers for time')

    if not 1 <= hour_start <= 12 or not 0 <= minute_start < 60 or not 1 <= hour_end <= 12 or not 0 <= minute_end < 60:
        raise ValueError('Invalid time range!  Please retry.')

    def get_hour(hour, period):
        if period == 'AM':
            return 0 if hour == 12 else hour
        else:
            return 12 if hour == 12 else hour + 12

    start_hour = get_hour(hour_start, time.group(3))
    end_hour = get_hour(hour_end, time.group(6))

    return f'{start_hour:02}:{minute_start:02} to {end_hour:02}:{minute_end:02}'

if __name__ == "__main__":
    main()
