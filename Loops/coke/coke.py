# **Task description**
# Simulates a vending machine selling Coke for 50 cents, prompting the user for 
# accepted coins (25, 10, or 5 cents) one at a time, displaying the remaining 
# amount due, and outputting any change owed once at least 50 cents is inserted.

def main():

    # Initialize the total amount inserted to 0
    b = 0

    # Continuously prompt the user for coins until enough is paid
    while True:
        try:
            # Display the current remaining amount due
            print(f'Amount due: {50 - b}')
            # Prompt the user to input the value of the coin
            a = int(input('Insert coin: '))
        except ValueError:
            # Handle invalid non-integer inputs
            print('Pls input integers')
        else:
            # Check if the inserted coin is a valid denomination (5, 10, or 25 cents)
            if a in [5, 10, 25]:
                b += a

            # Exit the loop once the total inserted amount reaches or exceeds 50 cents
            if b >= 50:
                break

    print(f'Change owed: {b - 50}')

main()
