# Program that prompts the user to guess a number
# The program needs to tell the user if their guess is too high or too low, each time they guess. 
# Hint - put an if statement inside the while loop

# Author : Michelle O'Connor

numberToGuess = 30

guess = int(input ("Please guess the number : "))

while guess != numberToGuess:
    if guess < numberToGuess:
        print ("Too low")
    else: print ("Too High")
    guess = int(input ("Please guess again : "))

print ("Well done! Yes the number was", numberToGuess)