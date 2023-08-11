# ----- THE PROMPT ------

# Mad Libs are activities that have a person provide various words, which are then
# used to complete a short story in unexpected (and hopefully funny) ways.

# Write a program that takes a string and an integer as input, and outputs a sentence
# using the input values as shown in the example below. The program repeats until the
# input string is quit and disregards the integer input that follows.



# ---------------


# need input
user_str = input()

# now split input by the space and store the split results into 
# two different variables, one of which replaces the original input
# string
user_str, user_num = user_str.split(' ')

# check inputs, then provide output until user provides escape input.
while user_str.lower() != 'quit':
    print(f'Eating {user_int} {user_str} a day keeps the doctor away.')

    # reperform input check to see if user wants another MadLibs result
    # or is done
    user_str = input()
    user_str, user_int = user_str.split(' ')