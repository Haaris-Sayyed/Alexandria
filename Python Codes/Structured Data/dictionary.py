# dictionaries are mutable.
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

def main():
    d=dict(one='1',two='2',three='3',four='4',five='5')
    print_dictionary(d)
    print_dictionary1(d)

def print_dictionary(d):
    for i in d:
        print(f'k: {i} v:{d[i]}')

def print_dictionary1(d):
    for k,v in d.items():
        print(f'k: {k} v:{v}')

def print_keys(d):
    for k in d.keys():
        print(f'k: {k}')

def print_values(d):
    for v in d.values():
        print(f'v:{v}')
    
if __name__ == '__main__':
    main()