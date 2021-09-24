from random import randint


def guess_number():
    turns = 0
    secret_number = randint(1, 20)
    # Introducing the walrus function
    while user_input := int(input('Enter a number: ')):
        turns += 1
        if turns == 6:
            print(f'You loose!, Secret number was {secret_number}')
            break

        if user_input == secret_number:
            print('You guessed correctly!')
            break

        elif user_input > secret_number:
            print('Too high!')
        elif user_input < secret_number:
            print('Too low!')
    print('Game over!')


print(guess_number())
