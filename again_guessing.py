import random

number = random.randrange(1, 11)
tries = 0

print('I have chosen a number between 1 and 10. Try to guess it!')
guess = int(input('Your guess: '))

guess == number

while False:
    print('That is incorrect. Try again!')
    guess = int(input('Your guess: '))
    tries += 1

    if guess == number:
        break

print('That\'s right! You\'re a good guesser!')
print(f'You only took {tries} tries!')
