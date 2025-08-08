#Read first n lines of a file
def read_first_n_lines(fname, nlines):
    from itertools import islice
    with open(fname) as f:
            for line in islice(f, nlines):
                    print(line)
read_first_n_lines('text.txt',2)
