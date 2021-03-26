# Program that prompts the user to guess a number
# The program needs to keep prompting the user to guess the nummber until it the user gets it right

# Author : Michelle O'Connor

numberToGuess = 30

guess = int(input ("Please guess a number between 1 and 40 : "))

while guess != numberToGuess:
    print ("Wrong")
    guess = int(input ("Please guess again, a number between 1 and 40 : "))

print ("Well done! Yes the number was", numberToGuess)