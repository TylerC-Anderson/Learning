# ----THE PROMPT----
# Write a program with total change amount as an integer input, and output the
# change using the fewest coins, one coin type per line. The coin types are Dollars,
# Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as
# appropriate, like 1 Penny vs. 2 Pennies.

# values of each denomination
dollar_val = 100
quarter_val = 25
dime_val = 10
nickel_val = 5
penny_val = 1

# getting input
coins = int(input())

# checking for edge cases of 0 or negative money
if coins <= 0:
   print('No change')

# remaining_coins tracks how much money we have to make change for
remaining_coins = coins

# Each block of if statements checks for the coin denominations and performs
# the required arithmetic and deducting it from the coins_remaining. Then,
# each block checks for whether there was a plurality of the denomination
# and outputs the grammatically correct response.
if remaining_coins >= dollar_val:
   dollars = remaining_coins // dollar_val
   remaining_coins -= dollars * dollar_val
   if dollars == 1:
      print(f'{dollars} Dollar')
   else:
      print(f'{dollars} Dollars')

if remaining_coins >= quarter_val:
   quarters = remaining_coins // quarter_val
   remaining_coins -= quarters * quarter_val
   if quarters == 1:
      print(f'{quarters} Quarter')
   else:
      print(f'{quarters} Quarters')

if remaining_coins >= dime_val:
   dimes = remaining_coins // dime_val
   remaining_coins -= dimes * dime_val
   if dimes == 1:
      print(f'{dimes} Dime')
   else:
      print(f'{dimes} Dimes')

# Point of interest: that there is no check for a plurality of
# nickels. Discovered that you only ever need 1 nickel
# as 2 nickels == 1 dime.
if remaining_coins >= nickel_val:
   nickels = remaining_coins // nickel_val
   remaining_coins -= nickels * nickel_val
   print(f'{nickels} Nickel')

if remaining_coins >= penny_val:
   pennies = remaining_coins // penny_val
   remaining_coins -= pennies * penny_val
   if pennies == 1:
      print(f'{pennies} Penny')
   else:
      print(f'{pennies} Pennies')
