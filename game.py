import random

secret_num = random.randint(1, 100)

chances = 1
while chances <= 5:
    num = int(input("enter ur no : "))

    if num < secret_num:
        print("greater")

    elif num > secret_num:
        print("smaller")
    elif num == secret_num:
        print("congrats you find the no ! ")
        break
    chances += 1
else:
    print(" you lose game over !! ")
