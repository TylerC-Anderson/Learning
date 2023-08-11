# Accepting user input here

integer1 = int(input())
integer2 = int(input())
integer3 = int(input())

# Outer-most block of if statements are testing for which of the 3 integers is
# smaller of the pair

if 0 < (integer1 - integer2):
   # Interior if statements check the remaining integer pair for which is
   # smallest of those, then outputs answer
   if integer2 < integer3:
      print(integer2)
   else:
      print(integer3)

# Repeat above logic for remaining combinations

elif 0 < (integer1 - integer3):
   if integer3 < integer2:
      print(integer3)
   else:
      print(integer2)

else:
   print(integer1)