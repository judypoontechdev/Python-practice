# Exercise: Validate user-entered email addresses using the external 
# 'validators' library. Prints 'Valid' or 'Invalid' based on syntax rules.

import validators

def main():
    email = input('email: ')
    if validators.email(email):
        print('Valid')
    else:
        print('Invalid')

if __name__ == '__main__':
    main()
