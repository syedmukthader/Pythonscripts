# Slicing

food = "best pizza is from italy"

print(food[14])
print(food[1])

print(food[-1])
print(food[-3])

# Slicing a string to get substring 4rm a string

print(food[0:4])
print(food[5:11])

# Slicing the tuple
foods = ("Pizza", "Chocolate", "Burger", "Brownie", "Ice-cream", "Fries")
print(foods[-1])
print(foods[3])
print(foods[-4])
print(foods[-5], foods[4], foods[-3])

print(foods[1:5])
print(foods[1:5][0])

print(foods[1:5][0][5:9])
print(foods[1:5][0][5:9][1:4])

# Slicing the list
foods = ["Pizza", "Chocolate", "Burger", "Brownie", "Ice-cream", "Fries"]
print(foods[-1])
print(foods[3])
print(foods[-4])
print(foods[-5], foods[4], foods[-3])

print(foods[1:5])
print(foods[1:5][0])

print(foods[1:5][0][5:9])
print(foods[1:5][0][5:9][1:4])

# Slicing the Dictionary

Eatery = {"foods": ("Pizza", "Chocolate", "Burger", "Brownie", "Ice-cream", "Fries"),
          "food": ['Chips', 'oats', 'protein shake', 'biscuits']}
print(Eatery)
print(Eatery['foods'])
print(Eatery['food'])

print(Eatery["food"][-2])
print(Eatery["food"][-2][8:13])

print(Eatery["foods"][3])
print(Eatery["foods"][3][0:5])
print(Eatery["foods"][3][0:5][-3:5])
