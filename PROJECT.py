from random import randint

# Initialize the number of guesses (6)
def guess_the_number(n):
    tries = 0
    while tries < 6:
        tries = tries + 1
# Generate a random number (import random module)
        num_to_guess = randint(1, 20)

# Ask the user to guess number (use input functions)
        input('HEY! Can you guess the number?')
        # for turn in str(tries):
        #     print("try # " + turn)

# If the guess is just right then print "you win!" and break
        if n == num_to_guess:
            print('YOU WIN!')
            print(num_to_guess)
            break

# If the guess is too high then print "too low"
        if n < num_to_guess:
                print('too low!\n')

# If the guess is too low then print  "too high"
        if n > num_to_guess:
            print('too high!\n')

# If player doesn't guess in the given number of turns - print "Game over, " reveal number.
        if tries == 6:
            print('Game Over')

guess_the_number(5)
