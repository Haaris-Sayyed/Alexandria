
x=45
y=90

print('The numbers are {} and {}.'.format(x,y))
print('The numbers are {a} and {b}.'.format(a=x,b=y))
print('{1} is twice of {0}.'.format(x,y))

# Formatting Instructions
print('The numbers are {0:<5} and {1:>5}.'.format(x,y))

x= 45 * 747 * 1000
print('The number is {:,}.'.format(x))
print('The number is {:.3f}'.format(x))

x=45
print('The number in hexadecimal is {:x}.'.format(x))
print('The number in octal is {:o}.'.format(x))
print('The number in binary is {:b}.'.format(x))
