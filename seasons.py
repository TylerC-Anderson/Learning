from collections import namedtuple

# defining named tuple category called month
month = namedtuple('month', [
   'month_name',
   'days_in_month',
   'numeric_month',
   'season_number',
   'has_end_of_season',
   'last_day_of_season'])

# list of seasons for indexing
seasons_list = [
   'Winter',
   'Spring',
   'Summer',
   'Autumn'
]

# defining the months' named tuples, their days, position in the year, season,
# and the last day of the year if it lands in that month, then creating a
# list of the months from that info

january = month('January', 31, 1, 0, False, None)
february = month('February', 28, 2, 0, False, None)
march = month('March', 31, 3, 0, True, 19)
april = month('April', 30, 4, 1, False, None)
may = month('May', 31, 5, 1, False, None)
june = month('June', 30, 6, 1, True, 20)
july = month('July', 31, 7, 2, False, None)
august = month('August', 31, 8, 2, False, None)
september = month('September', 30, 9, 2, True, 21)
october = month('October', 31, 10, 3, False, None)
november = month('November', 30, 11, 3, False, None)
december = month('December', 31, 12, 3, True, 20)

months_list = [
   january,
   february,
   march,
   april,
   may,
   june,
   july,
   august,
   september,
   october,
   november,
   december
]

months_as_strings = [
   'january',
   'february',
   'march',
   'april',
   'may',
   'june',
   'july',
   'august',
   'september',
   'october',
   'november',
   'december'
]

# accepting input here
input_month = input().lower()
input_day = int(input())

# checking if the user is inputting an incorrect month
if input_month not in months_as_strings:
   print('Invalid')

# upon valid entry, continue
else:
   # iteration variable to be used later
   iterate = 0

   # searching the months_as_strings list for the user's inputted month
   for months in months_as_strings:

      # if found, begin to use that month by assigning to month_requested
      if months == input_month:
         month_requested = months_list[iterate]

         # Check first for valid input day. Cannot be greater than days
         # in the month_requested, or be a negative number or 0
         if month_requested.days_in_month < input_day or input_day <= 0:
            print('Invalid')

         # now check if the month_requested contains the season's last day
         elif month_requested.has_end_of_season:

            # if the month_requested does contain last day in season, check if
            # the input day is before or on the last day in the season.
            # If so, output the month's season at the month's beginning per usual
            if input_day <= month_requested.last_day_of_season:
               season = month_requested.season_number
               print(seasons_list[season])

            # otherwise output the next season
            else:
               season = month_requested.season_number + 1
               print(seasons_list[season])

         # if the month does NOT contain the end of the season, output the season
         # as normal
         else:
            season = month_requested.season_number
            print(seasons_list[season])

      # if the current month we are looking at is not the input month, move on to
      # the next iteration. Repeat as needed.
      else:
         iterate += 1