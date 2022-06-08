class Bunny:
    def __init__(self,n):
        self._n=n
    
    def __repr__(self):
        return f'repr:The number of bunnies is {self._n}'
    def __str__(self):
        return f'str:The number of bunnies is {self._n}'
    
x=Bunny(45)
print(x)
print(repr(x))
print(ascii(x))
print(chr(128406))
print(ord('A'))