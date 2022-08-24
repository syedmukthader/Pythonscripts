# String Build in Methods/Functions
print('')
message = "Python is a Great programming language."
print(message)
print(message.casefold())
Message = message.swapcase()
print(Message)
print(message.find('language'))
# dir() function it prints all the available built-in functions
print('')
print(dir(message))

# Looking @ .join function
date = ("12", '13', '0', '90')
print('.'.join(date)), print('/'.join(date)), print('"'.join(date)), print('~'.join(date))

# Looking @ LIST[] Customobility /adding,removing,merging.

restaurants = ['KFC', 'McD', 'Burger-king', "Nando's", 'Subway', "Dominos"]
print(restaurants)

restaurants.append("Pizza-Hut")
print(restaurants)
restaurants.extend(["In-and-out", 'Starbucks', "Taco bell"])
print(restaurants)
# insert at specific location in LIST
restaurants.insert(2, "Five-Guys")
print(restaurants)
# Delete each pop function deletes one string at a time / and at specific position
restaurants.pop()
restaurants.pop()
restaurants.pop()
restaurants.pop()
restaurants.pop()
print(restaurants)
print("")
restaurants.pop(2)
print(restaurants)

# Looking at the Dictionary
recruiter = {'name': 'dave', 'department': 'marketing', 'contact info': 74612324}
print(recruiter.keys())
print(recruiter.values())
recruiter.clear()
print(recruiter)
