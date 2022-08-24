# FOR Loop iterating in tuple
cars = ('Bwm', 'Audi', 'Opel', 'Seat', 'Ferrari', 'Toyota')
for car in cars:
    print(f"{car} is top car brand in today's era ")
# FOR Loop iterating in list
cars = ['Bwm', 'Audi', 'Opel', 'Seat', 'Ferrari', 'Toyota']
for car in cars:
    print(f"{car} is great car brand in today's era ")

# While loop
x = 0
while x <= 5:
    print(f'Value of X is :', x)
    x += 1
print(f'This is while loop in exited state')

# Nested for loop
carbrands = ["Bwm", "Audi", "Opel", "Seat", "Ferrari", "Toyota"]
for car in carbrands:
    print("")
    print("is top car brand in today's era ")
for i in car:
    print(i)

import time

x = 2
while x <= 42:
    print("is top car brand in today's era", x)
    print("loop")
    x += 2
    time.sleep(1)

# Break Statement
for i in "Devops":
    print(i)
    if i == "p":
        print('found my data')
        break
print('out of loop')

for i in 'Chocolate':
    print(i)
    if i == "l":
        print('skip this')
        continue
        print(f'{i} its called Chocolate')

print(' ')
print('EXITED LOOP')

# Break / Continue Statement
import random

carbrands = ["Bwm", "Audi", "Opel", "Seat", "Ferrari", "Toyota"]

random.shuffle(carbrands)
print(carbrands)

GOOD = random.choice(carbrands)
print(GOOD)

for car in carbrands:
    print(f"{car} searching for a good brand")
    if car == GOOD:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(f" {GOOD} is Legendary Brand")
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        break
    print("*******************************")
    print("Not a good brand")
    print("*******************************")
    print()


carbrands = ["Bwm", "Audi", "Opel", "Seat", "Ferrari", "Toyota"]

random.shuffle(carbrands)
print(carbrands)

GOOD = random.choice(carbrands)
print(GOOD)

for car in carbrands:
    print(f"{car} might be a good brand")
    if car == GOOD:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(f" {GOOD} is Legendary Brand")
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print()
        continue

    print("*******************************")
    print("Not a good brand")
    print("*******************************")
    print()
