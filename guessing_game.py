import random

secret = random.randint(1, 10)
guess = 0

while guess != secret:
    guess = int(input("guess a random number between 1 to 10: "))

    if guess < secret:
        print("try a higher number")
    elif guess > secret:
        print("try a lower number")
    else:
        print("congratulation🎉 you guessed it right")
