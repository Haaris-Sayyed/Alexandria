# generators are special case of functions which serves as iterator.
# generator returns a stream of value.
def main():
    for i in inclusive_range(25):
        print(i,end=' ')
    print()

def inclusive_range(*args):
    numargs=len(args)
    start=0
    step=1

    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs==1:
        stop=args[0]
    elif numargs == 2:
        (start,stop)=args 
    elif numargs ==3:
        (start,stop,step)=args 
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')
    # generator
    i=start 
    while i<=stop:
        yield i
        i+=step 

if __name__ == '__main__':
    main()


# The yield call will return a value to the calling function, and then resume inside the generator.
def generator(start,stop):
    while (start<=stop):
        yield start
        print(f'start={start}')
        start+=1
for counter in generator(3,4):
    print(f'counter={counter}')

# counter=3
# start=3  
# counter=4
# start=4  