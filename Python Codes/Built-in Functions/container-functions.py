
x=(1,2,3,4,5)
y=len(x)
z=list(reversed(x))

print(x)
print(y)
print(z)
print(f'Sum is {sum(x)}')
print(f'Max: {max(x)}')
print(f'Min: {min(x)}')

p=(0,0,1,0,0)
print(f'any({p}) => {any(p)}')

p=(1,1,1,1,1)
print(f'all({p}) => {all(p)}')

x=(1,2,3,4,5)
y=(6,7,8,9,10)
z=zip(x,y)

for a,b in z:
    print(f'{a} - {b}')

animals=('Cat','Dog','Horse','Rabbit')
for index,value in enumerate(animals):
    print(f'{index}:{value}',end=' ')