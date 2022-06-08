# python have two numeric types integer and float

a=2
print(f'a is {a} and its type is {type(a)}')
b=2.0
print(f'b is {b} and its type is {type(b)}')

print(f'7 / 3 = {7/3} and its type is {type(7/3)}')

print(f'{ 0.1 + 0.1 + 0.1 - 0.3 }') # 5.551115123125783e-17

from decimal import *

a=Decimal('0.10')
b=Decimal('0.30')
val= a + a + a - b
print(f'val={ val } and its type is {type(val)}') # 0.00