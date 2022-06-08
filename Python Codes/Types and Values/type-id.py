# type() and id() built-ins
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)

print(f'x is {type(x)}')
print(f'y is {type(y)}')

# id() returns an unique identifier for each object
print(f'id of x {id(x)}')
print(f'id of y {id(y)}')

print(f'id of x[0] {id(x[0])}')
print(f'id of y[0] {id(y[0])}')

# to check type 

if isinstance(x,tuple):
    print('Yes')
else:
    print('No')
