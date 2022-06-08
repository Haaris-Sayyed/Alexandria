
print('Hello World!'.upper())
print('Hello World!'.lower())
print('Hello World!'.capitalize())
print('Hello World!'.title())
print('Hello World!'.swapcase())
print('Hello World!'.casefold())

# proof of strings are immutable 
s1='Hello World!'
s2=s1.upper()
print(id(s1))
print(id(s2))
