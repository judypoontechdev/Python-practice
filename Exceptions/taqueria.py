
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

main()
