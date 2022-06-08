
from decimal import DivisionByZero


def main():
    try:
        x=5/3
    except ValueError:
        print('I caught a ValueError!')
    except DivisionByZero:
        print('I caught a DivisionByZero error!')
    else:
        print('No Error!')
        print(f'x = {x}')
    
if __name__ == '__main__':
    main()