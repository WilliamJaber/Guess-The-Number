from random import randint


def guess_the_number():
    """This is called a docstring. Every function should have one.
    It offers a summary description of the function the datatype value it returns.
    Erase this and write a good docstring.
    """

    # Generate a random number. We are creating a "memory location" of a random number.
    # In order of rit to be static, we must create it before the while loop.
    num_to_guess = randint(1, 20)
    tries = 0
    # Initialize the number of guesses (6)
    while tries < 6:
        tries = tries + 1
        # When asking for user input, you need to store the user's guess
        # in a memory location.Lets call it 'user_guess':
        # And because we are dealing with integers, we will wrap user input in the int() 
        user_guess = int(input('HEY! Can you guess the number?'))
        # If the guess is just right then print "you win!" and break
        if user_guess == num_to_guess:
            print('YOU WIN!')
            print(num_to_guess)
            break

        # Before you have n < num_to_guess. 
        # Now, it's user_guess!        
        if user_guess < num_to_guess:
            print('too low!\n')
            print(num_to_guess)

        # If the user_guess is too low then print  "too high"
        if user_guess > num_to_guess:
            print('too high!\n')
            print(num_to_guess)
        # If player doesn't guess in the given number of turns - print "Game over, " reveal number.
        if tries == 6:
            print('You lose')
            break  # We need to break this loop! Because...
        print('Game Over!')

# We no longer need a parameter for this function
guess_the_number()
