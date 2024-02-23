import random

def guess_secret_number():

    print("Welcome to the Game!")
    print("The game's rules are to guess my secret number, which will be in the range from 1 to 100\n")

    # Initialize the number of attempts and generate a secret number
    attempts = 7
    secret_number = random.randint(1, 100)

  
    while True:
        # ask user to enter number
        guess_number = input("Enter your number: ")

        # convert the input to an integer
        try:
            guess_number = int(guess_number)
        except ValueError:
            #  print an error message if input isn't valid
            print("Please enter a valid number, from 1 to 100")
            continue

        # after each attempt, reduce the number of attempts by one
        attempts -= 1
        
        # Check if player has enough attempts
        if attempts < 1:
            print(f"You have {attempts} attempts left")
            print("Game over!")
            break    

        #inform the user whether the number is high or low.
        if secret_number > guess_number:
            print(f"Number is low, try again, you have {attempts} attempts left\n")
        elif secret_number < guess_number:
            print(f"Number is high! Try again, you have {attempts} attempts left\n")
        else:
            print("Congratulations! You win!")
            print(f"It took you {attempts} attempts.")
            break

# Call the function to start the game
guess_secret_number()


