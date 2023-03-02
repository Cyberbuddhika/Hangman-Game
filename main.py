from replit import clear #Note that the `clear()` function used in this code is specific to Replit, and may not work on other IDEs. If you are running this code on a different IDE, you will need to use the appropriate command to clear the console screen, and adjust line 23 of the code accordingly.
import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
print("Welcome to the classic game of Hangman! In this game, you will need to guess a secret word by guessing one letter at a time. For each incorrect guess, a part of the hangman's body will be added to the gallows. If you can guess the word before the hangman is fully drawn, you win! But be careful, you only have a limited number of guesses before the game is over. Good luck and have fun playing! \n")
#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You already guess letter '{guess}''")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You choose letter '{guess}' and its not in the word. You loose a life ")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print()
            print(f"The word was '{chosen_word}'")
            print()
            print("Thanks for playing!\n")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Congratulations! You win.Thanks for playing!\n")

    print(stages[lives])