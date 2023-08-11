x = 7
y = 10

if x > y:
   greater = x
else:
   greater = y

while (True):
   if (greater % x == 0) and (greater % y == 0):
      lcm = greater
      break
   greater += 1

print(lcm)