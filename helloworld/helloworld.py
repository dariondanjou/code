import sys

def main():
    print()
    print("Hello World! a Darion D'Anjou program created in python")
    print()
    
    print("Languages to choose from:")
    print("D or N - Dutch/Nederlands")
    print("E - English")
    print("F or F - French/Français") 
    print("Q or ENTER - Quit")
    print()

    #set nonsense placeholder for user_language variable so it enters while loop
    user_language = "nonsense"

    #loop the program until user enters no input at all
    while user_language != "" and user_language != "Q":
        #accept user language choice
        user_language = input("Choose a language: ").upper()
        #validate user choice is a valid option, loop prompt until user complies with valid choice
        while user_language not in ["D", "N", "E", "F", "Q", ""]:
            user_language = input("Be sure to choose either D, E, F, or N: ").upper()
        if user_language == "D" or user_language == "N" :
            print ("Hallo Wereld!")
        elif user_language == "E":
            print ("Hello World!")
        elif user_language == "F":
            print ("Bonjour Le Monde")
        
    print("Thanks for playing!")
    sys.exit()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()