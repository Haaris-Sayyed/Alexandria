
from decimal import DivisionByZero


def main(a):
    if a > 100:
        raise ValueError(f'Value {a} is not less than 100!')
    print(a)

def demo():
    try:
       x = 5/0
    except DivisionByZero as e:
        print(f'Caught Error: {e}')
    else:
        print(x)

if __name__ == '__main__':
    #main(105)
    demo()