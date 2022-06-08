# List comprehension is a technique to generate an iterable using existing iterable
# by performing operations on original iterable.

def main():
    seq = range(11)
    seq2 = [x*2 for x in seq]
    seq3 = {x:x**2 for x in seq}
    print_seq(seq)
    print_seq(seq2)
    print(seq3)


def print_seq(seq):
    for x in seq:
        print(x, end=' ')
    print()


if __name__ == '__main__':
    main()
