import validators

def main():
    email = input('email: ')
    if validators.email(email):
        print('Valid')
    else:
        print('Invalid')

if __name__ == '__main__':
    main()
