def add(x=0, y=0):
    return x + y


print(add(4, 6))

# -- getting user input
a = int(input('Enter Num1 : '))
b = int(input('Enter Num2 : '))
print(add(a, b))

# -- uses default values if no arguments are passed
print(add())
print(add(5))
