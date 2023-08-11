# Pseudocode:

# Input: Upper and lower bounds, one variable each, a variable for the guess, and a variable for the random seed.
# Processing:

# 1   Import necessary modules, at least random is needed for number generation.
# 2   Print to screen the welcome message, such as ‘Welcome to the higher/lower
#    game, Bella! ’.
# 3   Get the random seedVal, print to screen the seed prompt, such as ‘What
#    seed should be used? ’
# 4   Get the lower and upper bounds, printing a prompt to screen for each and
#    casting the datatype to int (‘Enter the lower bound: ’ and ‘Enter the lower
#    bound: ’). Store in lower_bounds and upper_bounds
# 5   Generate number in between the bounds, store in num_generated
# 6   Get the guess, print the guessing prompt to screen (‘Great, now guess
#    a number between 10 and 30: ‘) and store into a variable
# 7    while True:
# 8        if user_guess == num_generated:
# 9            print to screen the success message, such as ‘You got it!’
# 10          break and STOP here.
# 11      else:
# 11           get user_guess again if number doesn’t match
# 12      Will repeat while user_guess is wrong. If User guesses correctly, the
# program will STOP within the while loop.

# import necessary modules
import random

# gather input seed
seedVal = int(input("What seed should be used? "))
random.seed(seedVal)

# get upper and lower bounds
lower_bound = int(input('What is the lower bound? '))
upper_bound = int(input('What is the upper bound? '))

# test upper and lower for tomfoolery
while lower_bound >= upper_bound:
    print('Lower bound must be less than upper bound.')
    lower_bound = int(input('What is the lower bound? '))
    upper_bound = int(input('What is the upper bound? '))

# generate number
num_generated = random.randint(lower_bound, upper_bound)

# initialize variable for later use
user_guess = 0

# this can just be an infinite loop, because we BREAK the loop within if the
# player succeeds
while True:
    # get guess
    user_guess = int(input(f'What is your guess? '))

    # check guess against num_generated
    if user_guess == num_generated:
        print('You got it!')
        break

    elif user_guess < num_generated:
        print('Nope, too low.')
    elif user_guess > num_generated:
        print('Nope, too high.')