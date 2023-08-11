# -----THE PROMPT-----
# Write a program whose input is a string which contains a character and a phrase,
# and whose output indicates the number of times the character appears in the phrase.

# Taking in user input- can be anything since we're just counting characters and inputs
# are always the string type in python until cast to a different Datatype.
user_input = input()

# Creates new variables from the user's input to determine the string being counted and
# what we are counting within the string
char_to_count = user_input[0]
string_being_counted = user_input[2:]

# Counts the character amount within the string, prints output, and done
print(string_being_counted.count(char_to_count))

