import random

while True:
    roll = input("Roll the dice? (yes/no): ").lower()
    if roll == 'yes':
        print("You rolled a", random.randint(1, 6))
    elif roll == 'no':
        print("Thanks for playing!")
        break
    else:
        print("Please type yes or no.")
# This is a simple dice game where the user can roll a dice or exit the game.