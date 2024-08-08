
import random
low = int(input("Enter Lower Number: "))
high = int(input("Enter Higher Number: "))

x = random.randint(low,high)

print("You Have only 8 chances to guess the integer!")

i = 0 
attempt = 8             
while i < attempt:
    i += 1
    guess = int(input("Guess a number: "))
    if x == guess:
        print(f"Contratulations you did it in {i} attempt")
        break
    elif x < guess:
        print("You guessed high")
    elif x > guess:
        print("You guessed small")
