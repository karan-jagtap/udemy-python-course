x = 'abcd'
print(f'x: {x}')

y = ['a', 'b', 'c', 'd']
print(f'y: {y}')

y = ['a', 5, 'b', 5.7, 'c', 'd']
print(f'y: {y}')
print(len(y))
print(y[2])
print(y[-3])

# delete last item
print(y.pop())
print(y)

# add new item in the end
y.append(9)
print(y)

# remove item
y.remove('c')
print(y)

# all methods of list
print(dir(list))
# or
print(dir(x))


# delete list
del x
del y