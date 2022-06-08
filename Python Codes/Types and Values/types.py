# python follows dynamic typing also known as 'Duck Typing' 
# where the type of value is determined by value itself. 
x=7
print(f'{x} => {type(x)}')
x=7.0
print(f'{x} => {type(x)}')
x='7'
print(f'{x} => {type(x)}')
x=True
print(f'{x} => {type(x)}')
x=None
print(f'{x} => {type(x)}')