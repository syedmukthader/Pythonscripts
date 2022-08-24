# Arithmetic operators
a = 4
b = 8
total = a + b
print(total)
total = a - b
print(total)
total = a * b
print(total)
total = a / b
print(total)
total = a % b
print(total)

# Relational(COMPARISON) Operators

x = 92
y = 12

equals = x < y  # x less than y
print(equals)
equals = x > y  # x greater than y
print(equals)
equals = x == y  # x equal to y
print(equals)
equals = x != y  # x not equal to y
print(equals)
equals = x <= y  # x less than equal to y
print(equals)
equals = x >= y  # x greater than equal to y
print(equals)

# Assignment Operators
e = 1
f = 2
e += f
print(e)
e -= f
print(e)

# AND / OR LOGICAL OPERATORS

op = (a < b) or (e > f)
print(op)
op = (e < f) or (x < y)
print(op)

op = (a < b) and (e > f)
print(op)
op = (a < b) and (e < f)
print(op)

op = not (e < f)
print(op)

# Membership Operator
str1 = 'Membership'
flt1 = 6.9
tuple = (str1, flt1, 'food', 1.2, 37)
ans = str1 in tuple
print(ans)
ans = 'food' not in tuple
print(ans)

# Identity operator
p = 15
q = 15
ans = p is q
print(ans)
ans = p is not q
print(ans)
