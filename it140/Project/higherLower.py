#Dominic Spucches
#Higher/Lower Game
import random

#this code will initialize the random number generator
#random number generator requires a value to generate a random number.
seedVal = int(input('What seed should be used?'))
random.seed(seedVal)

#ask for lower and upper values
lower = int(input('What is the lower bound?'))
upper = int(input('What is the upper bound?'))

random.randint(lower, upper)

