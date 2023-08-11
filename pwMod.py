# ----- THE PROMPT -----
# Many user-created passwords are simple and easy to guess. Write a program that
# takes a simple password and makes it stronger by replacing characters using the
# key below, and by appending "q*s" to the end of the input string.

# i becomes !
# a becomes @
# m becomes M
# B becomes 8
# o becomes .

word = input()
password = ''

for character in word:

    # i becomes !
    if character == 'i':
        password += '!'

    # a becomes @
    elif character == 'a':
        password += '@'
    
    # m becomes M
    elif character == 'm':
        password += 'M'
    
    # B becomes 8
    elif character == 'B':
        password += '8'
    
    # o becomes .
    elif character == 'o':
        password += '.'
    
    # if none of above, simply append the character and move on
    else:
        password += character

# after loop completes, append the extra characters requested
else:
    password += 'q*s'

# print output to screen
print(password)