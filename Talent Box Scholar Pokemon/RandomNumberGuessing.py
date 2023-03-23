'''
Write a program that generates a random number between 1 and 100.
Have the user guess the number.
Provide feedback whether the number is too high or too low.
Count the number of guesses.

Hint:
To count the number of guesses, you can create a variable and initiate is with 0.
For each guess, you update this variable with the old value +1 using augumented assignment.
'''


import random

randomnumber = random.randint(1,100)

guesses = 0

while guesses < 10:
    guess = int(input("Guess a number!"))
    if guess > randomnumber:
        print("Your guess is too high. Guess again.")
        guesses += 1
        print(guesses)

    elif guess < randomnumber:
        print("Your guess is too low. Guess again.")
        guesses += 1
        print(guesses)

    else:
        print("Nice job! You guessed the number!")
        break