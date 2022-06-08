# a decorator is a form of metaprogramming.
# it can be described as a special type of function which returns a wrapper function.

# def f1(f):
#     def f2():
#         print('This is before function call')
#         f()
#         print('This is after function call')
#     return f2 

# def f3():
#     print('This is f3')

# x=f1(f3)
# x()

def f1(f):
    def f2():
        print('This is before function call')
        f()
        print('This is after function call')
    return f2 

@f1
def f3():
    print('This is f3')

f3()
