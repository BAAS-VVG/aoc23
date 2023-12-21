from queue import PriorityQueue


def findpath(grid, slim, clim):
    height = len(grid)
    width = len(grid[0])
    visited = set()  # (x, y, d, l), d: 0123 -> ESWN
    goal = (width - 1, height - 1)

    q = PriorityQueue()
    q.put((0, 0, 1, 0, 0, 0))
    q.put((0, 0, 0, 1, 1, 0))

    while not q.empty():
        pos = q.get()
        prio, loss, x, y, d, l = pos
        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        if (x, y, d, l) in visited:
            continue
        visited.add((x, y, d, l))

        loss += grid[y][x]
        l += 1

        if (x, y) == goal and l >= clim:
            print(loss)
            break

        if d % 2:  # N-S
            if l >= clim:
                q.put((loss + abs(x - 1 - goal[0]) + abs(y - goal[1]), loss, x - 1, y, 2, 0))
                q.put((loss + abs(x + 1 - goal[0]) + abs(y - goal[1]), loss, x + 1, y, 0, 0))
            if l < slim:
                q.put((loss + abs(x - goal[0]) + abs(y + 2 - d - goal[1]), loss, x, y + 2 - d, d, l))
        else:  # E-W
            if l >= clim:
                q.put((loss + abs(x - goal[0]) + abs(y - 1 - goal[1]), loss, x, y - 1, 3, 0))
                q.put((loss + abs(x - goal[0]) + abs(y + 1 - goal[1]), loss, x, y + 1, 1, 0))
            if l < slim:
                q.put((loss + abs(x + 1 - d - goal[0]) + abs(y - goal[1]), loss, x + 1 - d, y, d, l))


def d17():
    inputfile = "d17.txt"
    # inputfile = "test.txt"

    grid = []
    with open(inputfile) as f:
        for line in f.readlines():
            grid.append([int(v) for v in line.strip()])

    findpath(grid, 3, 0)
    findpath(grid, 10, 4)
