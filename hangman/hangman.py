import random

WORDS = ["python", "alien", "javascript", "juicy", "belonging", "random", "barbarian", "plebeian", "philistine", "education", "ambition", "gross", "horse", "mouse", "house", "dog", "cat", "dictionary", "definition", "spaceship", "flower", "plant"]

def main():
    #initialize user_input to something so it enters the loop
    user_input = "something."
    won = 0
    lost = 0

    #make the entire game loop, until user presses just enter or q to quit
    while user_input not in ["", "q", "n"]:
        #initialize the alphabet
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        #randomly choose a word from the list
        chosen_word = random.choice(WORDS)

        word_display = ['_' for underscore in chosen_word]
        #set default attempts count to 8
        mistakes = 8

        print()
        print("Welcome to Hangman by Darion D'Anjou")
        print()

        #loop the gameplay until attempts run out or user solves the word
        while mistakes > 0 and '_' in word_display:
            print("\n" + ' '.join(word_display))
            print()
            print("\n" + ' '.join(alphabet))
            print()

            #create a check for 1 mistake to ensure the grammar of the prompt is correct
            if mistakes == 1:
                guess = input(str(mistakes) + " mistake left. Guess a letter: ").lower()
            else:
                guess = input(str(mistakes) + " mistakes left. Guess a letter: ").lower()

            print()
            #implement a valudation loop to be sure the letter guessed isn't a letter player has already guessed
            while guess not in alphabet:
                guess = input("Be sure to choose from available letters. Guess a letter: ").lower()

            if guess in chosen_word:
                for index, letter in enumerate(chosen_word):
                    if letter == guess:
                        word_display[index] = guess #updates the display word with the correctly guessed letter/s in the right place
            else:
                print()
                print("The letter " + guess + " is NOT in the word.")
                print()
                mistakes -= 1
            
            #update the available alphabet letters
            if guess in alphabet:
                for index, letter in enumerate(alphabet):
                    if letter == guess:
                        alphabet[index] = " "

        #game ending
        if '_' not in word_display:
            print("You did it. You correctly guessed the word! " + (' '.join(word_display)))
            print()
            won += 1
        else:
            print("You made too many mistakes. The word was: " + chosen_word)
            print("So sorry. You died. Be smarter in your next life.")
            print()
            lost += 1
        
        #ask user to play again
        print('Games won: ' + str(won) + " Games lost: " + str(lost))
        print("Play again? Y to play again. ENTER or Q or N to quit")
        user_input = input().lower()

    #Bye!
    print()
    print("This has been a Darion D'Anjou game, written in Python. Thanks for playing. Hope you had fun!")
    print()

if __name__ == "__main__":
    main()

