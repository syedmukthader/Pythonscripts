# Defining the functions
def add(sum1, sum2):
    total = sum1 + sum2
    return total


sum = add(4, 5)
print(sum)
print(add(50, 50))

print('##################################')


# Without the return function
def add1(sum1, sum2):
    total = sum1 + sum2
    print(total)


print(add1(5, 6))

print('##################################')


# adding the functions in the list/tuple
def sum(arg):
    x = 0
    for i in arg:
        x = x + i
    return x


result = sum([5, 5, 5])
print(result)

print('##################################')


# Giving value to Default arguments
def money(msg='billionaire'):
    print(f"I am {msg}")
    print('Thanks for reminding me')


money()

print('##################################')


# Writing a code after understanding upper functions

def food(item, kcal):
    print(f"{item} kcal intake meter")
    if (kcal > 300) and (kcal <= 500):
        print("It's a healthy food")
    elif (kcal > 500) and (kcal < 600):
        print("This food is high in kcal")
    elif (kcal >= 600):
        print('THIS IS A HIGH KCAL FOOD AVOID IT')
    else:
        print("Can consume that much kcal intake")


food("Pizza", 620)
print()
food("Oats", 320)
print()
# Keywords argument
food(kcal=540, item="Burger")
print()
food(item="Redbull", kcal=120)
