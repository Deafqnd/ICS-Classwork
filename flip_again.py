import random


again = 'y'

while True:
    flip = random.randrange(2)  # 0-1

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print("You flip a coin and it is... " + coin)

    again = input("Would you like to flip again (y/n)? ")

    if again == 'n':
        break

# It no longer works since the true/false condition cannot be fulfilled in for the while statement to run
