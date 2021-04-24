import random

n = random.randint(1,50)

chance = 1
try:
    while chance <= 5:
        guess = int(input("Guess number between 1-50: "))
        if guess < n:
            print("You guess smaller number, Guess greater number.")
        elif guess > n:
            print("You guess greater number, guess smaller number.")
        else:
            print("You guess correct number..")
            print("You Won!!!")
            break
        print(f"Number of chance you played {chance}")
        chance += 1
    if chance <= 5:
        pass
    else:
        print(f"The number is {n}")
        print("You loose the game!!! Bad Luck")
except:
    pass