from random import randint


def guess_number() -> None:
    """
    Player has 6 'turns' to guess a secret_number number between 1-20 correctly.
    """
    turns = 0
    secret_number = randint(1, 20)
    while user_input := int(input('Enter a number: ')):
        turns += 1
        if user_input == secret_number:
            print('You guessed correctly!')
            break

        if turns == 6:
            print(f'You loose!, Secret number was {secret_number}')
            break

        elif user_input > secret_number:
            print('Too high!', secret_number)
        elif user_input < secret_number:
            print('Too low!', secret_number)

    print('Game over!')


# # If the program is run (instead of imported), run the game
if __name__ == "__main__":
    print(guess_number())
