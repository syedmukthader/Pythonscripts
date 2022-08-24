# Calling modules  /mentioning them individually
import modules

# print(dir(modules))

modules.orderfood('Biryani', 'Pasta', 'Noodles', 'Milk')
print()
modules.food('Pasta', 340)
print()
modules.activity(40, Dance='Hip-hop')

# Calling all the existing modules without mentioning it individually
print()
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print()
from modules import *

orderfood("Sweets", "Rice", "kebabs")
print()
food("steamed rice", 530)
print()
activity(10, outdoor='swimming')
