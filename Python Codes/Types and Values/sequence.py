
x = [1, 2, 3, 4, 5, 6]
print(f'{type(x)} is mutable')
for i in x:
    print('i is {}'.format(i))

x = (1, 2, 3, 4, 5, 6)
print(f'{type(x)} is immutable')
for i in x:
    print('i is {}'.format(i))

x = range(6)
print(f'{type(x)} is immutable')
for i in x:
    print('i is {}'.format(i))

x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
print(f'{type(x)} is mutable')
for k,v in x.items():
    print(' k: {} v: {}'.format(k,v))
