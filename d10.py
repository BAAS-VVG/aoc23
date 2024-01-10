from queue import Queue


def getCoords(width, height):
    for x in range(width):
        for y in range(height):
            yield x, y


def getObstacles(coord):
    for x in range(coord[0]):
        yield x, coord[1]


def d10():
    print("d10")
    inputfile = "d10.txt"
    # inputfile = "test.txt"

    grid = {}
    with open(inputfile) as f:
        for y, line in enumerate(f.readlines()):
            for x, val in enumerate(line.strip()):
                grid[(x, y)] = val
                if val == "S":
                    start = (x, y)

    visited = set()
    q = Queue()
    q.put((start, 0))
    if 0 < start[0] < x and grid[(start[0] - 1, start[1])] in "LF-" and grid[(start[0] + 1, start[1])] in "7J-":
        grid[start] = "-"
    if start[0] > 0 and grid[(start[0] - 1, start[1])] in "LF-" and start[1] > 0 and grid[(start[0], start[1] - 1)] in "F7|":
        grid[start] = "J"
    if start[0] > 0 and grid[(start[0] - 1, start[1])] in "LF-" and start[1] < y and grid[(start[0], start[1] + 1)] in "LJ|":
        grid[start] = "7"
    if start[0] < x and grid[(start[0] + 1, start[1])] in "7J-" and start[1] > 0 and grid[(start[0], start[1] - 1)] in "F7|":
        grid[start] = "L"
    if start[0] < x and grid[(start[0] + 1, start[1])] in "7J-" and start[1] < y and grid[(start[0], start[1] + 1)] in "LJ|":
        grid[start] = "F"
    if 0 < start[1] < y and grid[(start[0], start[1] - 1)] in "F7|" and grid[(start[0], start[1] + 1)] in "LJ|":
        grid[start] = "|"
    while not q.empty():
        coord, dist = q.get()
        if coord in visited:
            continue
        visited.add(coord)

        if grid[coord] in "LF-":
            q.put(((coord[0] + 1, coord[1]), dist + 1))
        if grid[coord] in "J7-":
            q.put(((coord[0] - 1, coord[1]), dist + 1))
        if grid[coord] in "F7|":
            q.put(((coord[0], coord[1] + 1), dist + 1))
        if grid[coord] in "JL|":
            q.put(((coord[0], coord[1] - 1), dist + 1))

    print(dist - 1)

    width = x + 1
    height = y + 1

    inside = 0
    for coord in getCoords(width, height):
        if coord in visited:
            continue
        lines = 0
        for obstacle in getObstacles(coord):
            if obstacle not in visited:
                continue
            if grid[obstacle] == "|":
                lines += 1
            if grid[obstacle] in "JF":
                lines += 0.5
            if grid[obstacle] in "7L":
                lines -= 0.5

        if int(lines) % 2:
            inside += 1

    print(inside)


