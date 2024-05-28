import random

NUM_PAIRS = 3

def get_valid_index(display, truth):
    valid = False
    user_index = "not an integer"
    while not valid:
        user_index = input("Enter an index: ")
        while not user_index.isdigit():
            user_index = input("Enter a valid index: ")
        user_index = int(user_index)
        if user_index >= 0 and user_index < len(display):
            if display[user_index] == "*":
                #update the display with the guessed item
                display[user_index] = truth[user_index]
                #print("Thanks.")
                valid = True
            else:
                print(str(user_index) + " is not a valid index.")
        else:
            print(str(user_index) + " is not a valid index.")
    return user_index

def main():
    #initialize the list
    truth = []
    
    #fill the list with numbered pairs
    for i in range(NUM_PAIRS):
        truth.append(i)
        truth.append(i)

    random.shuffle(truth)
    print(truth)

    #initialize the display list
    display = []
    
    #fill the display list with asterisk symbols
    for i in range(NUM_PAIRS):
        display.append("*")
        display.append("*")

    #loop the game until all matches solved
    while "*" in display:
        print(display)
        guess1 = get_valid_index(display, truth)
        guess2 = get_valid_index(display, truth)
        print("Value at index " + str(guess1) + " is " + str(truth[guess1]))
        print("Value at index " + str(guess2) + " is " + str(truth[guess2]))
        if truth[guess1] == truth[guess2]:
            print("Match!")
        else:
            display[guess1] = "*"
            display[guess2] = "*"
            input("No match. Try again. Press Enter to continue...")
        
        #clear_terminal()
    
    print()
    print(display)
    print()
    print("Congratulations, You won!")

def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()