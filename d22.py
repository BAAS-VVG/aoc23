from collections import defaultdict
from queue import Queue


# AABB collision check on x and y axes.
def cansupport(b1, b2):
    return b1[0][0] <= b2[1][0] and b2[0][0] <= b1[1][0] and b1[0][1] <= b2[1][1] and b2[0][1] <= b1[1][1]


# Checks if b1 supports b2
def doessupport(b1, b2):
    return b1[1][2] + 1 == b2[0][2] and cansupport(b1, b2)


def checksupports(blocks):
    res = set()
    above = defaultdict(set)
    below = {}
    for i, block in enumerate(blocks):
        j = i - 1
        supports = []
        while j >= 0:
            if doessupport(blocks[j], block):
                supports.append(blocks[j])
                above[blocks[j]].add(block)
            j -= 1

        if len(supports) == 1:
            res.add(supports[0])

        below[block] = set([s for s in supports])

    return below, above, res


def fall(blocks):
    count = 0
    for i, block in enumerate(blocks):
        if block[0][2] == 1:
            continue

        z = 1
        for support in reversed(sorted(blocks[:i], key=lambda x: x[1][2])):
            if support[1][2] >= block[0][2]:
                continue

            if cansupport(support, block):
                z = support[1][2] + 1
                break

        if z == block[0][2]:
            continue

        height = block[1][2] - block[0][2]
        blocks[i][0][2] = z
        blocks[i][1][2] = z + height
        count += 1

    return count


def d22():
    print("d22")

    inputfile = "d22.txt"
    # inputfile = "test.txt"

    blocks = []
    with open(inputfile) as f:
        for line in f.readlines():
            blocks.append([[int(v) for v in c.split(',')] for c in line.strip().split('~')])

    blocks.sort(key=lambda x: x[0][2])
    fall(blocks)
    blocks = [tuple(tuple(c) for c in b) for b in blocks]
    blocks.sort(key=lambda x: x[0][2])
    below, above, supports = checksupports(blocks)

    print(len(blocks) - len(supports))

    # part 2
    queue = Queue()
    res = 0
    for supp in supports:
        fallen = set()
        for ab in above[supp]:
            queue.put(ab)
        fallen.add(supp)
        while not queue.empty():
            bl = queue.get()
            if below[bl].issubset(fallen):
                fallen.add(bl)
                for ab in above[bl]:
                    queue.put(ab)

        res += len(fallen) - 1

    print(res)







