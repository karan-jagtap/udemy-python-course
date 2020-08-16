# --
x = 'abcd'
y = '567'
# both are strings
print(f'x: {type(x)}, y: {type(y)}')

# -- methods and strings
print(x)
x = x.upper()
print(x)

print(dir(x))
print(x.title())
print(x.lower())
x = x.replace('C', 'c')
print(x)

# -- Indexing and slicing
x = 'Fight.Club'
print(x[6])
print(x[2:7])
print(x[2:])
print(x[:6])
print(x[-1])
print(x[-5:-1])

# -- string formatting
x = "Fight"
y = "Club"
z = "Tyler Durden"
# method 1
sol = x + " " + y + " - " + z
print(sol)
# method 2
sol = "{} {} - {}".format(x, y, z)
print(sol)
# method 3
sol = f'{x} {y} - {z}'
print(sol)
# method 4
sol = "{2} {1} - {0}".format(x, y, z)
print(sol)
