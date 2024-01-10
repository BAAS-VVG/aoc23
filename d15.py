import functools
import re


def d15():
    print("d15")
    inputfile = "d15.txt"
    # inputfile = "test.txt"

    with open(inputfile) as f:
        print(sum([functools.reduce(lambda a, b: (a + ord(b)) * 17 % 256, val, 0) for val in f.read().split(',')]))

    with open(inputfile) as f:
        boxes = [{} for _ in range(256)]
        for val in f.read().strip().split(','):
            label, lens = re.split('-|=', val)
            h = functools.reduce(lambda a, b: (a + ord(b)) * 17 % 256, label, 0)

            if len(lens) < 1:  # '-'
                boxes[h].pop(label, None)
            else:  # '='
                boxes[h][label] = int(lens)

        print(sum([(i + 1) * (j + 1) * l for i, d in enumerate(boxes) for j, l in enumerate(d.values())]))
    