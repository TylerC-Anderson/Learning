# ----- THE PROMPT -----
# This program will output a right triangle based on user specified height
# triangle_height and symbol triangle_char.

# (1) The given program outputs a fixed-height triangle using a * character. Modify
# the given program to output a right triangle that instead uses the user-specified
# triangle_char character. (1 pt)

# (2) Modify the program to use a loop to output a right triangle of height
# triangle_height. The first line will have one user-specified character, such as
# % or *. Each subsequent line will have one additional user-specified character
# until the number in the triangle's base reaches triangle_height. Output a space
# after each user-specified character, including a line's last user-specified character. (2 pts)


# --------------------------------------

# initialising variables and generate whitespace to build the
# triangle

triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

# need to start count at 1 because we want the first level to
# have 1 character
level = 1

while level <= triangle_height:
    
    # "Take the triangle character, add a space to it, then repeat
    # as many times as the value of the current level"
    print((f'{triangle_char}' + ' ') * level)
    
    # build the next layer and end loop when done
    level += 1
