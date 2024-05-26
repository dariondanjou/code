# code
 This console based version of hangman has the following features:
chooses a word randomly from a hard coded list of about 15 words in the main code file
prints underscores representing the letters of the randomly chosen word to be guessed
initializes a mistakes counter
prints the number of mistakes left, before each guess
prints a list of available letters to be guessed
updates and prints the available letters to be guessed list, with each new guess, taking away a latter each time
validates the guess against the available letters. prompts the player to guess again, until an available letter is guessed
avaialable letter validation keeps player from wasting guesses by keeping them from guessing the same wrong letters repeatedly
available letter validation also prevents non letter characters from being guessed
once player has guessed the complete word or used up all mistakes without doing so, appropriate statement is printed
entire game exists in a giant loop that prompts the user to play again if they want (any character besides q n or enter), or quit (q, n, or enter)

potential next steps:
add a graphics interface for the game


