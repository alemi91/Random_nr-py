import random

a = int(input("a = "))
b = int(input("b = "))

if a > b:
    print("Try again lul")
else:
    nr = random.randint(a, b)
    print(f"Random number: {nr}")