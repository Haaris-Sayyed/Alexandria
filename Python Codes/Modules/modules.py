
import sys
import os
import datetime 

def main():
    v=sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    print(sys.platform)
    print(os.name)
    print(os.getcwd())
    print(datetime.datetime.now().year)

if __name__ == '__main__':
    main()