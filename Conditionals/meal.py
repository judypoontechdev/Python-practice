def main():
    #Prompt user to input time
    time = input('What is the time now? ')
    outcome = convert(time)
    judge(outcome)

def convert(time):
    #Split time string by ':' into hours and minutes
    cal = time.split(':')

    #Convert minutes into a fractional hour and hours into integer, then sum them up
    minutes = int(cal[1]) / 60
    hour = int(cal[0])
    outcome = minutes + hour

    return outcome

def judge(time):
    #Check which meal time the converted float falls into and print the result
    if 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print('lunch time')
    elif 18 <= time <= 19:
        print('dinner time')
    else:
        print('')

if __name__ == "__main__":
    main()
