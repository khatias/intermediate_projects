# import random

import random

def guess_word():
    print("Welcome!, it's a Hangman game, you have 10 attempts to guess the secret word, good luck!\n")
    # word list for random words
    words =["macaron", "paper", "stapler", "bush", "factory", "jumper", "candle", "microphone" ]
    # generate a random word
    secret_word = random.choice(words)
    # generate the number of attempts
    attempts = 10

    # Calculate the length of the secret word and create a string of underscores
    length = len(secret_word)
    guessed_letters = '_' * length

    print(f"There are {length} letters in the word")
    print(guessed_letters)

    
    while True:
        #  ask the user to enter a letter.
            user_input = input("Guess a letter: ")
        # check if the input is valid    
            if len(user_input) > 1:
                print("Please enter only one letter.")
            elif not user_input.isalpha():
                print("Please enter a valid letter from a to z.\n")

            else:     
                # Convert guessed_letters to a list for manipulation
                guessed_letters_list = list(guessed_letters)  

                letter_found = False 
                # Iterate over each index and letter in the secret_word
                for index, letter in enumerate(secret_word):
                    if letter == user_input:  
                        print("You've guessed a letter, Well done!")
                         # Update the guessed_letters_list with the guessed letter at the corresponding index
                        guessed_letters_list[index] = letter 
                        # Convert the guessed_letters_list back to a string
                        guessed_letters = ''.join(guessed_letters_list)  
                    
                        print(guessed_letters )
                        letter_found = True

                if not letter_found:
                    # If the guessed letter is not found in the secret word, decrement attempts and inform the player
                    attempts -= 1
                    print(f"Letter isn't in the word, you have {attempts} attempts left\n") 

   
                if attempts == 0:
                    # If attempts have reached 0, inform the player that the game is over and break out of the loop
                    print("Game over!")
                    break

                # Check if the player has guessed the entire secret word
                if secret_word == guessed_letters:
                    print("Congratulations! You've guessed the secret word!")        
                    break



guess_word()
