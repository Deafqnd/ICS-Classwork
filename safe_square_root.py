import math

print('SQUARE ROOT!')
number = int(input('Enter a number: '))

while number < 0:
    print('You can\'t take the square root of a negative number, silly.')
    number = int(input('Try again: '))
    if number > 0:
        break

print(f'The square root of {number} is {math.sqrt(number)}')
