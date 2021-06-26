# importing module for random number generation
import random

# range of the values of a dice
low, high = 1,6

# to loop the rolling through user input
rolling = "1"

# looping
while rolling == "1" or rolling == "y":
    print("Rolling The Dices...")
    print("The Values are :")

    # generating and printing 1st random integer from 1 to 6
    print(random.randint(low, high))

    # generating and printing 2nd random integer from 1 to 6
    print(random.randint(low, high))

    # asking user to roll the dice again. Any input other than yes or y will terminate the loop
    rolling = input("Roll the Dices Again? ")