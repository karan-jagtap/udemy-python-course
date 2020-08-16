# declaration
x = {}
# or
x = dict()

print(type(x))

x = {
    1: 'one',
    '2': 2
}

print(x)
keys = x.keys()
print(keys)

# update
x[1] = 'ONE'
print(x)
x['2'] = 'TWO'
print(x)
print(len(x))

# add
x[3] = 'three'
print(x)

# delete
x.pop(1)  # deletes the specified item
print(x)

x.popitem()  # deletes the last item
print(x)
print(dir(x))
