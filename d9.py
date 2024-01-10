import numpy as np


def nextValue(arr):
    if all([v == 0 for v in arr]):
        return 0

    return arr[-1] + nextValue(np.diff(arr))


def prevValue(arr):
    if all([v == 0 for v in arr]):
        return 0

    return arr[0] - prevValue(np.diff(arr))


def d9():
    print("d9")
    inputfile = "d9.txt"
    # inputfile = "test.txt"

    with open(inputfile) as f:
        res = 0
        res2 = 0
        for line in f.readlines():
            numbers = [int(x) for x in line.split()]
            res += nextValue(numbers)
            res2 += prevValue(numbers)

        print(res)
        print(res2)
