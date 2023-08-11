# ----- THE PROMPT -----
# Many documents use a specific format for a person's name.
# Write a program that reads a person's name in the following format:
# firstName middleName lastName (in one line)
# and outputs the person's name in the following format:
# lastName, firstInitial.middleInitial


# Taking input from user
name = input()

# Following are some checks to make sure that name is in valid characters and will output
# the correct casing and no extraneous spaces
alphaCheck = name.replace(' ', '')

# Checking for only alphabetic characters
if alphaCheck.isalpha():
   name = name.strip().title()
   nameSplit = name.split(' ')

   # Checking that there were no extra spaces between any of the names given as input,
   # since strip only does leading and trailing spaces
   if nameSplit.count('') == 0:

      # Performing the formatting assuming the above passes. Checks if 2 or 3 names were given
      # then outputs result in desired format
      if len(nameSplit) == 3:
         firstName = nameSplit[0]
         middleName = nameSplit[1]
         lastName = nameSplit[2]
         print(f'{lastName}, {firstName[0]}.{middleName[0]}.')

      else:
         firstName = nameSplit[0]
         lastName = nameSplit[1]
         print(f'{lastName}, {firstName[0]}.')

   # Error messages in case any of our input checks above flags soemthing undesired in the input
   else:
      raise ValueError("Name had extra spaces!")

else:
   raise ValueError("Name must only contain letters and single spaces between the names!")