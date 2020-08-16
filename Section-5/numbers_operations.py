# -- operator precedence
# **
# * /
# + -

# -- numbers
x = 4
print(type(x))

# output is float
y = x / 3
print(f'y = {y}, type = {type(y)}')

# output is int
y = x // 3
print(f'y = {y}, type = {type(y)}')

# -- arithmetic operators
x = 3 + 5 * 6
print(x)
x = (3 + 5) * 6
print(x)

# -- power operator
x = 4 ** 2
print(x)
