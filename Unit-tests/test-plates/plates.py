def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # No periods, spaces, or punctuation marks are allowed
    for p in s:
        if not p.isalpha() and not p.isnumeric():
            return False

    # Must have two English alphabets as starting
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Length MIN 2 MAX 6
    if not 2 <= len(s) <= 6:
        return False

    # Numbers can't be in between alphabets
    for p in range(len(s)):
        if s[p].isnumeric():
            break

    if s[p] == '0':
        return False

    for q in s[p + 1:]:
        if q.isalpha():
            return False

    return True

if __name__ == '__main__':
    main()
