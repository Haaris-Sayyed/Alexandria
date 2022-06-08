def main():
    f = open('D:/CODES/PYTHON/File IO/lines.txt')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__':
    main()