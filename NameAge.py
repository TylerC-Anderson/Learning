# importing ability to tell the current year from datetime module
from datetime import date

# get name as a string
name = input('What is your name? ')

# get age as an int
age = int(input('How old are you? '))

# Get current year, then use to calculate birth year
current_yr = date.today().year
birth_year = current_yr - age

# print greeting
print(f'Hello {name}! You were born in {birth_year}.')
