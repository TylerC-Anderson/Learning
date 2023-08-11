num_guesses = int(input())
user_guesses = []

num_guesses = str(num_guesses)
num_guesses.split(' ')

amt_guesses = num_guesses.pop(0)

for guesses in num_guesses:
    user_guesses.append(int(input()))
    guesses +=1


print('user_guesses:', user_guesses)