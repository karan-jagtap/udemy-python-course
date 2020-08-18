import random


def generate_face(x):
    if x == 1:
        print('===============')
        print('|             |')
        print('|      0      |')
        print('|             |')
        print('===============')
    elif x == 2:
        print('===============')
        print('|             |')
        print('|    0   0    |')
        print('|             |')
        print('===============')
    elif x == 3:
        print('===============')
        print('|   0         |')
        print('|      0      |')
        print('|         0   |')
        print('===============')
    elif x == 4:
        print('===============')
        print('|    0   0    |')
        print('|             |')
        print('|    0   0    |')
        print('===============')
    elif x == 5:
        print('===============')
        print('|   0     0   |')
        print('|      0      |')
        print('|   0     0   |')
        print('===============')
    elif x == 6:
        print('===============')
        print('|    0   0    |')
        print('|    0   0    |')
        print('|    0   0    |')
        print('===============')


choice = 'y'
while choice == 'y':
    num = random.randint(1, 6)
    generate_face(num)
    choice = input('press y to roll again...')
