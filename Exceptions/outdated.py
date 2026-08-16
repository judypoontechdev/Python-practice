# **Task description**
# Prompts the user for a date in `M/D/YYYY` or `Month Day, Year` format
#  and outputs it in ISO 8601 `YYYY-MM-DD` format with leading zeroes, 
# reprompting the user if the input date is invalid.

def main():

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Prompt user for old type of dates
    while True:
        try:
            date = input('Date: ').strip()

            # Check if the format is (MM/DD/YYYY) or (Month Day, Year).  If not, prmopt input again.

            # For MM/DD/YYYY
            if '/' in date:
                d1 = date.split('/')

                # Check 1: if the input is number
                month = int(d1[0])
                day = int(d1[1])
                year = int(d1[2])

                # Check 2: if the input is within range:
                if not 1 <= month <= 12 or not 1 <= day <= 31:
                    continue

                # Convert the date to YYYY-MM-DD format
                if month < 10 and day >= 10:
                    month_date = '0' + d1[0]
                    day_date = d1[1]

                elif day < 10 and month >= 10:
                    month_date = d1[0]
                    day_date = '0' + d1[1]

                elif month < 10 and day < 10:
                    day_date = '0' + d1[1]
                    month_date = '0' + d1[0]

                else:
                    month_date = d1[0]
                    day_date = d1[1]

                print(f'{year}-{month_date}-{day_date}')


            # For Month Day, Year
            elif ',' in date:
                d2 = date.replace(',', '').split()

                # Check 1: if month is valid
                if d2[0] not in months:
                    continue

                # Check 2: if day and year are number
                day = int(d2[1])
                year = int(d2[2])

                # Convert month to number
                for m in range(len(months)):
                    if months[m] == d2[0]:
                        month = m + 1

                # Check 3: if the input is within range:
                if not 1 <= month <= 12 or not 1 <= day <= 31:
                    continue

                # Convert the date to YYYY-MM-DD format
                # Convert the date to YYYY-MM-DD format
                if month < 10 and day >= 10:
                    day_date = d2[1]
                    month_date = '0' + str(month)

                elif day < 10 and month >= 10:
                    day_date = '0' + d2[1]
                    month_date = month

                elif month < 10 and day < 10:
                    day_date = '0' + d2[1]
                    month_date = '0' + str(month)
                else:
                    month_date = month
                    day_date = d2[1]

                print(f'{year}-{month_date}-{day_date}')

            else:
                continue

        except ValueError:
            print('Pls input valid integers as date')

        else:
            break

main()
