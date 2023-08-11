

# (2) Extend to also output in reverse. (Submit for 1 point, so 3 points total)

# (3) Extend to convert the integer to a character by using the 'chr()' function,
# and output that character. (Submit for 2 points, so 5 points total).




# FIXME (1): Finish reading other items into variables, then
#  output the four values on a single line separated by a space

# (1) Prompt the user to input an integer between 32 and 126, a float, a character, and a string,
# storing each into separate variables. Then, output those four values on a
# single line separated by a space. (Submit for 2 points).

user_int = int(input('Enter integer (32 - 126):\n'))
user_float = float(input('Enter float:\n'))
user_char = input('Input character:\n')
user_string = input('Enter string:\n')

int_to_char = chr(user_int)

print(user_int, user_float, user_char, user_string)
print(user_string, user_char, user_float, user_int)
print(f'{user_int} converted to a character is {int_to_char}')


# FIXME (2): Output the four values in reverse

# FIXME (3): Convert the integer to a character, and output that character



