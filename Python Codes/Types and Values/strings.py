# strings are objects.

x='seven'
print(f'x is {x.capitalize()}') # fstrings

print('seven {} {}'.format(8,9))
print('seven {1} {0}'.format(8,9)) # positional arguments
print('seven "{1:<9}" "{0:>9}"'.format(8,9))
print('seven "{1:<09}" "{0:>09}"'.format(8,9))
