
from random import randint

def guess_the_number():
    """
    The User will guess 'num_to_guess' number between 1-20 correctly
    within a turn of 6 'tries' to win the game.
    """
    num_to_guess = randint(1, 20)
    tries = 0
    while user_input := int(input('HEY! Can you guess it? Enter a number: ')):
        tries += 1
        if user_input == num_to_guess:
            print('YOU WIN!')
            break
        if tries == 6:
            print(f'You failed, The number to guess was: {num_to_guess}')
            break
        elif user_input > num_to_guess:
            print('Too high!\n')
        elif user_input < num_to_guess:
            print('Too low!\n')
    print('Game Over!')

guess_the_number()
