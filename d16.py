from queue import Queue


def energyfrompos(start, grid):
    visited = set()  # (x, y, dir)
    q = Queue()

    q.put(start)  # dir 0123 -> ESWN
    while not q.empty():
        light = q.get()
        x, y, d = light
        if x < 0 or x >= len(grid[0]):
            continue
        if y < 0 or y >= len(grid):
            continue

        if light in visited:
            continue
        visited.add(light)

        c = grid[y][x]

        if d % 2:  # N-S
            if c in '\\/':
                if c == '/':
                    d = (d + 1) % 4
                else:  # c == \
                    d -= 1
                q.put((x + 1 - d, y, d))
            elif c == '-':
                q.put((x + 1, y, 0))
                q.put((x - 1, y, 2))
            else:
                q.put((x, y + 2 - d, d))
        else:  # E-W
            if c in '\\/':
                if c == '\\':
                    d += 1
                else:  # c == /
                    d = (d - 1) % 4
                q.put((x, y + 2 - d, d))
            elif c == '|':
                q.put((x, y - 1, 3))
                q.put((x, y + 1, 1))
            else:
                q.put((x + 1 - d, y, d))

    return len(set([(x, y) for x, y, d in visited]))


def getstarts(grid):
    for x in range(len(grid[0])):
        yield x, 0, 1
        yield x, len(grid) - 1, 3

    for y in range(len(grid)):
        yield 0, y, 0
        yield len(grid[0]) - 1, y, 2


def d16():
    print("d16")
    inputfile = "d16.txt"
    # inputfile = "test.txt"

    grid = []
    with open(inputfile) as f:
        for line in f.readlines():
            grid.append(line.strip())

    print(energyfrompos((0, 0, 0), grid))

    print(max([energyfrompos(p, grid) for p in getstarts(grid)]))

