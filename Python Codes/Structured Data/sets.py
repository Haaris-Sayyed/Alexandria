#  A set is an unordered collection with no duplicate elements. 
# https://docs.python.org/3/tutorial/datastructures.html#sets

def main():
    a=set("this is a set data structure.")
    b=set("a set is an unordered collection with no duplicate elements.")
    print_set(a)
    print_set(b-a)
    print_set(a | b)
    print_set(a ^ b)

def print_set(o):
    print('{',end=' ')
    for ch in o:
        print(ch,end='')
    print('}')

if __name__ == '__main__':
    main()