#-----THE PROMPTS-----

# (1) Prompt the user to enter two words and a number, storing each into separate variables. Then, output those three values on a single line separated by a space. (Submit for 1 point)
# (2) Output two passwords using a combination of the user input. Format the passwords as shown below. (Submit for 2 points, so 3 points total).
# (3) Output the length of each password (the number of characters in the strings). (Submit for 2 points, so 5 points total).

# Gathering input block
word1 = input()
word2 = input()
number = input()

# Block for transforming inputs into passwords
firstPass = f'{word1}_{word2}'
secondPass = f'{number}{word1}{number}'

# Output block
print(f"You entered: {word1} {word2} {number}")

print(f'\nFirst password: {firstPass}')
print(f'Second password: {secondPass}')

print(f'\nNumber of characters in {firstPass}: {len(firstPass)}')
print(f'Number of characters in {secondPass}: {len(secondPass)}')

