# **Task description**
#Prompts the user for the answer to the Great Question of Life,
#  the Universe, and Everything, outputting `Yes` if the input is `42`, 
# `forty-two`, or `forty two` (case-insensitively), and `No` otherwise.


def main():
    #Prompt user for the answer to the great question of life
    answer = input('What is the Great Question of Life? ').lower().strip()
    decide(answer)

def decide(a):
    #Print Yes if the user's answer is 42, otherwise No
    if a == '42' or a == 'forty-two' or a == 'forty two':
        print('Yes')
    else:
        print('No')

main()
