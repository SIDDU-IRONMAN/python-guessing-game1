# this the guessing games project

import random
print("-------welcoe to our guessing game-----")
print("-------guess a number from 1 to 10 ---------")


secreat = random.randint(1,10)

while True:
    number = int(input("enter a number as your wish from 1 to 10 : "))
      
    if secreat == number:
        print("the guess number is correct you won the game")
        break
    elif secreat < number:
        print("the given number is too high")
    elif secreat > number:
        print("the given value is too low")
       