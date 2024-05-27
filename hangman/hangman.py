import random
from graphics import Canvas
import math

WORDS = ["python", "alien", "javascript", "juicy", "belonging", "random", "barbarian", "plebeian", "philistine", "education", "ambition", "gross", "horse", "mouse", "house", "dog", "cat", "dictionary", "definition", "spaceship", "flower", "plant"]

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

MISTAKES_LIMIT = 7

HANGMAN_COLOR = 'green'
LETTER_WIDTH_WORD_DISPLAY = 36

def draw_hangman(canvas, mistakes):
    #draws the entire hangman in 7 steps. number of steps to be drawn depends on mistakes count, which has been sent in as a parameter
    steps_to_draw = MISTAKES_LIMIT - mistakes #for example when starting out, result is 0 and only the gallows will be drawn

    #step 0 draw the gallows
    if steps_to_draw == 0:
        #draw the base
        canvas.create_rectangle(200, 340, 450, 360, 'black')
        #draw the column
        canvas.create_rectangle(400, 50, 420, 360, 'black')
        #draw the crossbeam
        canvas.create_rectangle(250, 50, 420, 70, 'black')
        #draw the hangbeam
        canvas.create_rectangle(250, 50, 270, 110, 'black')
    
    #step 1 draw the head
    elif steps_to_draw == 1:
        #draw circle for the head
        canvas.create_oval(230, 90, 290, 150, HANGMAN_COLOR)

    #step 2 draw the neck
    elif steps_to_draw == 2:
        #draw horizontal rectangle for the neck
        canvas.create_rectangle(255, 140, 265, 170, HANGMAN_COLOR)

    #step 3 draw the right arm
    elif steps_to_draw == 3:
        #draw angled rectangle for the arm (or a thick line)
        canvas.create_rectangle(180, 160, 260, 170, HANGMAN_COLOR)

    #step 4 draw the left arm
    elif steps_to_draw == 4:
        #draw angled rectangle for the arm (or a thick line)
        canvas.create_rectangle(260, 160, 340, 170, HANGMAN_COLOR)
    
    #step 5 draw the body
    elif steps_to_draw == 5:
        #draw vertical rectangle for the body
        canvas.create_rectangle(255, 170, 265, 300, HANGMAN_COLOR)

    #step 6 draw the left leg
    elif steps_to_draw == 6:
        #draw angled rectangle for the leg (or a thick line)
        canvas.create_rectangle(260, 290, 340, 300, HANGMAN_COLOR)

    #step 7 draw the right leg
    elif steps_to_draw == 7:
        #draw angled rectangle for the leg (or a thick line)
        canvas.create_rectangle(180, 290, 260, 300, HANGMAN_COLOR)

def draw_smiley_face(canvas):
    #draw mouth
    canvas.create_oval(240, 100, 280, 140, 'black')
    canvas.create_rectangle(240, 100, 280, 126, HANGMAN_COLOR)
    #draw happy eyes
    canvas.create_oval(240, 110, 252, 122, 'black')
    canvas.create_rectangle(240, 116, 252, 122, HANGMAN_COLOR)
    canvas.create_oval(268, 110, 280, 122, 'black')
    canvas.create_rectangle(268, 116, 280, 122, HANGMAN_COLOR)

def draw_dead_face(canvas):
    #draw mouth with hanging tongue
    canvas.create_rectangle(240, 126, 280, 130, 'black')
    canvas.create_oval(246, 125, 256, 139, 'black')
    canvas.create_rectangle(240, 122, 280, 126, HANGMAN_COLOR)
    
    #draw cross eyes
    canvas.create_line(243, 110, 255, 122, 'black')
    canvas.create_line(255, 110, 243, 122, 'black')
    canvas.create_line(265, 110, 277, 122, 'black')
    canvas.create_line(277, 110, 265, 122, 'black')

def clear_word(canvas):
    canvas.create_rectangle(1, 390, 500, 450, 'white')

def clear_alphabet(canvas):
    canvas.create_rectangle(1, 440, 500, 490, 'white')

def clear_mistakes(canvas):
    canvas.create_rectangle(1, 1, 500, 36, 'white')

def draw_word(canvas, word_display):
    #clear the previous alphabet from the canvas
    clear_word(canvas)
    #draw the word
    x = (CANVAS_WIDTH - (len(word_display) * LETTER_WIDTH_WORD_DISPLAY)) // 2 #center the word horizontally on the canvas
    y = 410
    for letter in word_display:
        canvas.create_text(
            x, 
            y, 
            text = letter,
            font = 'Arial', 
            font_size = 30, 
            color ='blue'
        )
        x += LETTER_WIDTH_WORD_DISPLAY

def draw_word_missing_letters(canvas, word_display, chosen_word):
    #draw the missing letters of the word
    x = (CANVAS_WIDTH - (len(word_display) * LETTER_WIDTH_WORD_DISPLAY)) // 2 #center the word horizontally on the canvas
    y = 410
    index = 0
    for letter in word_display:
        if letter == "_":
            canvas.create_text(
                x, 
                y, 
                text = chosen_word[index],
                font = 'Arial', 
                font_size = 30, 
                color ='red'
            )
        index += 1
        x += LETTER_WIDTH_WORD_DISPLAY

def draw_alphabet(canvas, alphabet):
    #clear the previous alphabet from the canvas
    clear_alphabet(canvas)
    #draw the alphabet
    x = 20
    y = 460
    for letter in alphabet:
        canvas.create_text(
            x, 
            y, 
            text = letter,
            font = 'Arial', 
            font_size = 18, 
            color ='black'
        )
        x += 18

def draw_mistakes(canvas, mistakes):
    #clear the previous mistakes from the canvas
    clear_mistakes(canvas)
    #draw the alphabet
    x = 20
    y = 20
    canvas.create_text(
        x, 
        y, 
        text = "mistakes left: ",
        font = 'Arial', 
        font_size = 18, 
        color ='black'
    )
    canvas.create_text(
        x + 120, 
        y, 
        text = str(mistakes),
        font = 'Arial', 
        font_size = 18, 
        color ='red'
    )

def draw_announcement(canvas, announcement):
    #clear the previous mistakes from the canvas
    #clear_mistakes(canvas)
    #draw announcement
    x = 20
    y = 200
    canvas.create_text(
        x, 
        y, 
        text = announcement,
        font = 'Arial', 
        font_size = 36, 
        color ='black'
    )


def main():
    #initialize user_input to something so it enters the loop
    user_input = "something."
    won = 0
    lost = 0

    #make the entire game loop, until user presses just enter or q to quit
    while user_input not in ["", "q", "n"]:
        #initialize the canvas variable
        canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
        #initialize the alphabet
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        #randomly choose a word from the list
        chosen_word = random.choice(WORDS)

        word_display = ['_' for underscore in chosen_word]
        #set default attempts count to 8
        mistakes = MISTAKES_LIMIT

        #draw hangman gallows initial state
        draw_hangman(canvas, mistakes)

        #draw chosen_word with underscores inital state
        draw_word(canvas, word_display)

        #draw alphabet initial state
        draw_alphabet(canvas, alphabet)

        #draw mistakes initial state
        draw_mistakes(canvas, mistakes)

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

            #draw the updated hangman's gallows
            draw_hangman(canvas, mistakes)

            #draw chosen_word with underscores updated state
            draw_word(canvas, word_display)

            #draw alphabet updated state
            draw_alphabet(canvas, alphabet)

            #draw mistakes updated count
            draw_mistakes(canvas, mistakes)

        #game ending
        if '_' not in word_display:
            print("You did it. You correctly guessed the word! " + (' '.join(word_display)))
            print()
            #draw smiley face only if head has already been drawn, meaning at least one mistake was made
            if MISTAKES_LIMIT - mistakes > 0:
                draw_smiley_face(canvas)
            draw_announcement(canvas, "You Won!")
            won += 1
        else:
            print("You made too many mistakes. The word was: " + chosen_word)
            print("So sorry. You died. Be smarter in your next life.")
            print()
            draw_dead_face(canvas)
            draw_announcement(canvas, "You Lose.")
            #update the canvas with missing letters
            draw_word_missing_letters(canvas, word_display, chosen_word)
            print(chosen_word[0], chosen_word[2])   
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





#todo add sound effects