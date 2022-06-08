def main():
    infile = open('D:/CODES/PYTHON/File IO/lines.txt','rt')
    outfile = open('D:/CODES/PYTHON/File IO/lines-copy.txt','wt')
    for line in infile:
        print(line.rstrip(),file=outfile)
        print('.',end='',flush=True)
    outfile.close()
    print('\nDone.')

if __name__ == '__main__':
    main()