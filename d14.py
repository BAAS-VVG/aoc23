import itertools


def moveleft(grid):
    for x, row in enumerate(grid):
        dots = [i for i, c in enumerate(row) if c != '#']
        dtrngs = [[t[0][1], t[-1][1] + 1] for t in (list(g) for k, g in itertools.groupby(enumerate(dots), lambda l: l[0] - l[1]))]
        r = row[:]
        for rng in dtrngs:
            rocks = ['O'] * row[rng[0]:rng[1]].count('O')
            empt = ['.'] * row[rng[0]:rng[1]].count('.')
            r[rng[0]:rng[1]] = rocks + empt
        grid[x] = r


def transpose(grid):
    return [list(x) for x in zip(*grid)]


# Rotates the grid counterclockwise
def rotcc(grid):
    return [list(x) for x in zip(*grid)][::-1]


# Rotates the grid clockwise
def rotc(grid):
    return [list(x) for x in zip(*reversed(grid))]


def d14():
    inputfile = "d14.txt"
    # inputfile = "test.txt"
    cyclelen = 1000000000

    grid = []
    with open(inputfile) as f:
        for line in f.readlines():
            grid.append(line.strip())

    grid = rotcc(grid)
    moveleft(grid)
    grid = rotcc(grid)
    load = 0
    for i, row in enumerate(grid):
        load += row.count('O') * (i + 1)

    print(load)

    grid = []
    with open(inputfile) as f:
        for line in f.readlines():
            grid.append(line.strip())

    dct = {}  # dct[grid] == iter

    grid = rotcc(grid)
    itr = 0
    while itr < cyclelen:
        for _ in range(4):
            moveleft(grid)
            grid = rotc(grid)

        tgrid = tuple(map(tuple, grid))
        if tgrid in dct:
            cycle = itr - dct[tgrid]
            rem = (cyclelen - itr - 1) % cycle
            residx = itr + rem - cycle
            grid = list(map(list, next((grid for grid, itr in dct.items() if itr == residx))))
            break

        dct[tgrid] = itr
        itr += 1

    grid = rotcc(grid)
    load = 0
    for i, row in enumerate(grid):
        load += row.count('O') * (i + 1)

    print(load)





