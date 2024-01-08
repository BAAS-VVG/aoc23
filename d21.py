from collections import defaultdict
from queue import Queue


def d21():
    inputfile = "d21.txt"
    # inputfile = "test.txt"

    grid = defaultdict(lambda: False)
    grid2 = {}

    with open(inputfile) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c == 'S':
                    start = (x, y)
                grid[(x, y)] = c != '#'
                grid2[(x, y)] = c != '#'

    height = y + 1
    width = x + 1

    visited = set()
    res = set()

    queue = Queue()

    queue.put((start, 0))
    while not queue.empty():
        pos, dist = queue.get()
        if pos in visited:
            continue
        visited.add(pos)

        if not grid[pos]:
            continue

        if not dist % 2:
            res.add(pos)

        dist += 1
        if dist > 64:
            continue
        queue.put(((pos[0] - 1, pos[1]), dist))
        queue.put(((pos[0] + 1, pos[1]), dist))
        queue.put(((pos[0], pos[1] - 1), dist))
        queue.put(((pos[0], pos[1] + 1), dist))

    print(len(res))

    visited = set()
    res = set()

    queue = Queue()
    queue.put((start, 0))
    while not queue.empty():
        pos, dist = queue.get()
        if pos in visited:
            continue
        visited.add(pos)

        if not grid2[(pos[0] % width, pos[1] % height)]:
            continue

        if dist % 2:
            res.add(pos)

        dist += 1
        if dist > 26501365:
            continue
        queue.put(((pos[0] - 1, pos[1]), dist))
        queue.put(((pos[0] + 1, pos[1]), dist))
        queue.put(((pos[0], pos[1] - 1), dist))
        queue.put(((pos[0], pos[1] + 1), dist))

    print(len(res))
