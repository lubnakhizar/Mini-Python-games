import random

top_of_range = input("Type a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number larger than 0 next time!')
        quit()
else:
    print('please type a number next time!')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:                      #  user_guess != random_number
    guesses += 1
    user_guess = input('Enter your guess : ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time!')
        continue

    if user_guess == random_number:
        print('\t\t----Yes! You got it :) ---- ')
        break
    elif user_guess > top_of_range:
        print('You entered above the input range of number guesser!')
    elif user_guess > random_number & user_guess < top_of_range:
        print('You were above the random number!')
    else:
        print('You were below the random number!')

print('You attempt total number of ', guesses, 'guesses .')
