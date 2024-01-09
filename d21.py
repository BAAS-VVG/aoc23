from collections import defaultdict
from queue import Queue


def d21():
    def solve(step, startpos):
        visited = set()
        res = set()

        queue = Queue()

        queue.put((startpos, step))
        while not queue.empty():
            pos, dist = queue.get()
            if pos in visited:
                continue
            visited.add(pos)

            if not grid[pos]:
                continue

            if not dist % 2:
                res.add(pos)

            dist -= 1
            if dist < 0:
                continue
            queue.put(((pos[0] - 1, pos[1]), dist))
            queue.put(((pos[0] + 1, pos[1]), dist))
            queue.put(((pos[0], pos[1] - 1), dist))
            queue.put(((pos[0], pos[1] + 1), dist))

        return len(res)

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

    print(solve(64, start))

    # part 2
    # Solution is a diamond. Input is 131 x 131. Start is in center. 65 steps to the edge;
    # ('steps' - 65) % 131 == 0 -> solution is one big diamond.
    steps = 26501365

    if width == height and start[0] == start[1] and start[0] == width // 2 and all(
            [grid[(start[0], y)] for y in range(height)]) and all([grid[(x, start[1])] for x in range(width)]) and (
            steps - width // 2) % width == 0:
        d = width
        r = width // 2

        x = (steps - r) // d

        odd = x * x - 2 * x + 1
        even = x * x
        small = x
        big = x - 1

        centersquare = solve(steps, start)
        offsquare = solve(steps - 1, start)
        left = solve(d - 1, (width - 1, start[1]))
        right = solve(d - 1, (0, start[1]))
        top = solve(d - 1, (start[0], height - 1))
        bottom = solve(d - 1, (start[0], 0))
        bigr = d + r - 1
        smallr = r - 1
        topleftbig = solve(bigr, (width - 1, height - 1))
        topleftsmall = solve(smallr, (width - 1, height - 1))
        toprightbig = solve(bigr, (0, height - 1))
        toprightsmall = solve(smallr, (0, height - 1))
        bottomrightbig = solve(bigr, (0, 0))
        bottomrightsmall = solve(smallr, (0, 0))
        bottomleftbig = solve(bigr, (width - 1, 0))
        bottomleftsmall = solve(smallr, (width - 1, 0))

        total = odd * centersquare + even * offsquare + left + right + top + bottom + \
                big * topleftbig + small * topleftsmall + big * toprightbig + small * toprightsmall + \
                big * bottomrightbig + small * bottomrightsmall + big * bottomleftbig + small * bottomleftsmall

        print(total)
        return

    visited = set()
    res = set()

    queue = Queue()
    queue.put((start, steps))
    while not queue.empty():
        pos, dist = queue.get()
        if pos in visited:
            continue
        visited.add(pos)

        if not grid2[(pos[0] % width, pos[1] % height)]:
            continue

        if not dist % 2:
            res.add(pos)

        dist -= 1
        if dist < 0:
            continue
        queue.put(((pos[0] - 1, pos[1]), dist))
        queue.put(((pos[0] + 1, pos[1]), dist))
        queue.put(((pos[0], pos[1] - 1), dist))
        queue.put(((pos[0], pos[1] + 1), dist))

    print(len(res))
