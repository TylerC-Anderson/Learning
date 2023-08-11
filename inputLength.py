# ----- The PROMPT ------ 
# Given a line of text as input, output the number of characters excluding
# spaces, periods, or commas.

user_text = input()

''' Type your code here. '''
# initializing counting variable
count = 0

for characters in user_text:
    
    # Ignoring the 3 characters specified in prompt.
    if characters == '.' or characters == ',' or characters == ' ':
        continue
    
    # Assuming above were not the current characters variable, tick the count up
    # by one
    count += 1

# print output to screen
print(count)