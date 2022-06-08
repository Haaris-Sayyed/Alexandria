
def main():
    x=dict(one='1',two='2',three='3')
    demo(**x) 

def demo(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('key: {} value: {}'.format(k,kwargs[k]))

if __name__ == '__main__':
    main()