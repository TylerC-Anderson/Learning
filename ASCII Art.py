def main():
   i = 0
   while i < 50:
      i += 1

      if i == 1:
         print('    ^')
         continue

      elif i == 2:
         print('   / \\')
         continue

      elif i == 3:
         print('  / | \\')
         continue

      elif i == 45 or i == 46:
         print('==========')
         continue

      elif 47 <= i <= 50:
         print('   |||')

      else:
         print('  | | |  ')



# def skip():
#    if i % 2 != 0:
#       print('\n')
#       continue

main()