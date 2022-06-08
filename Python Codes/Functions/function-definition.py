# immutable types are passed to function as a value so they dont actually change the original value. (int,string,bool,double)
# mutable types are passed to function as a reference so they actually change the original value.(list,tuple,dictionary)
def main():
    myFunction()


def myFunction():
    print('This is user defined function')


if __name__ == '__main__':
    main()

