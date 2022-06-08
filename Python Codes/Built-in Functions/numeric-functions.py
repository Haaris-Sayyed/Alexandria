
x='47'
y=int(x)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'x is {type(y)}')
print(f'x is {y}')

x='47'
y=float(x)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'x is {type(y)}')
print(f'x is {y}')

x=-47
y=abs(x)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'x is {type(y)}')
print(f'x is {y}')

x=47
(quotient,remainder)=divmod(x,3)
print(f'quotient={quotient} remainder={remainder}')

c1=x+73j
c2=complex(x,73)

print(f'c1 is {type(c1)}')
print(f'c2 is {type(c2)}')