import random
import sys

print("Guess the number ^_^")
print("Give me a range [a, b] to choose from!")
try:
    a = int(input("a = "))
    b = int(input("b = "))
except ValueError:
    print("Try again lul.")
    sys.exit()

if a > b:
    print("Try again lul.")
else:
    secret = random.randint(a, b)
    incercari = 0
    guessed = False
    
    print(f"\nWhat number did I choose?=]")
    
    while not guessed:
        try:
            nr = int(input("Varianta ta: "))
            incercari += 1
            
            if nr < secret:
                print("Too smol :/")
            elif nr > secret:
                print("Too big :/")
            else:
                guessed = True
                print(f"Correct! Took you {incercari} tries btw!")
        except ValueError:
            print("Invalid number :|")