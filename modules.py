def orderfood(order, *input):
    print(f"You have ordered : {order}")
    for item in input:
        print(f"Your Remaining Orders: {item}")

    print()
    print("The order will be soon delivered")
    print("<<<< Thanks for waiting >>>>")


import random


def activity(*time, **task):
    # print(time)
    # print(task)
    min = sum(time) + random.randint(0, 50)
    # print(min)
    choice = random.choice(list(task.keys()))  # converting into list
    # print(choice)
    print(f"Time you have spend {min}mins doing {task[choice]}.")


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