def main():
    infile = open('D:/CODES/PYTHON/File IO/berlin.jpg', 'rb')
    outfile = open('D:/CODES/PYTHON/File IO/berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
