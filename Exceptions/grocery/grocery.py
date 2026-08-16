# **Task description**
# Prompts the user for grocery items until Control-D (`EOFError`) is entered, 
# then outputs a sorted, uppercase list of the items prefixed by their respective counts.

def main():

    counting = {}
    bucket = []

    while True:
        try:
            items = input('')
            bucket.append(items)

        # Break when control-d
        except EOFError:
            print()
            break

        else:
            # Update the counting dictionary dynamically with each input
            unique = list(set(bucket))

            for u in unique:
                number = bucket.count(u)
                counting[u] = number

    # Alphabetically sort the dictionary keys, convert to uppercase
    # and format as 'number: food'
    result = {k.upper(): counting[k] for k in sorted(counting.keys())}

    # Print the final sorted grocery list
    for key, value in result.items():
        print(f'{value} {key}')

main()
