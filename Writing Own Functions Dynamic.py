# VARIABLE Function writing(NONE KEYWORD ARGUMENTS) *args (will be stored in tuple)

def orderfood(order, *input):
    print(f"You have ordered : {order}")
    for item in input:
        print(f"Your Remaining Orders: {item}")

    print()
    print("The order will be soon delivered")
    print("<<<< Thanks for waiting >>>>")


orderfood('pizza', 'burger', 'pasta', 'soup', 'cheese sticks')

print()
print('###########################################################')
print()
# VARIABLE Function writing(WITH KEYWORD ARGUMENTS) **kwargs (will be stored in dictionary)
import random


def activity(*time, **task):
    # print(time)
    # print(task)
    min = sum(time) + random.randint(0, 50)
    # print(min)
    choice = random.choice(list(task.keys()))  # converting into list
    # print(choice)
    print(f"Time you have spend {min}mins doing {task[choice]}.")


activity(5, 10, 20, work='coding', playing='sudo', doing='nothing', gaming='CSGO')
