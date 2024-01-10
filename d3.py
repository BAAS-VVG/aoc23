def neighbours(grid, posx, posy):
    for x in range(posx - 1, posx + 2):
        if x < 0:
            continue
        if x >= len(grid[0]):
            continue
        for y in range(posy - 1, posy + 2):
            if y < 0:
                continue
            if y >= len(grid):
                continue
            if x == posx and y == posy:
                continue

            yield x, y, grid[y][x]


def findleft(grid, x, y):
    while x > 0 and grid[y][x - 1].isdigit():
        x -= 1
    return x


def findright(grid, x, y):
    while x < len(grid[0]) and grid[y][x].isdigit():
        x += 1
    return x


def d3():
    print("d3")
    inputfile = "d3.txt"
    # inputfile = "test.txt"

    with open(inputfile) as f:
        visited = {}
        grid = [row.strip() for row in f]
        total = 0
        asts = {}
        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if not grid[y][x].isdigit():
                    continue
                neighboursymbols = [s for s in neighbours(grid, x, y) if s[2] != '.' and not s[2].isdigit()]
                if len(neighboursymbols) == 0:
                    continue
                left = findleft(grid, x, y)
                s = neighboursymbols[0]
                if s[2] == '*':
                    if (s[0], s[1]) in asts:
                        asts[s[0], s[1]].add((left, y))
                    else:
                        asts[s[0], s[1]] = {(left, y)}

                if (left, y) in visited:
                    continue
                right = findright(grid, x, y)
                number = int(grid[y][left:right])
                visited[(left, y)] = number
                total += number

        print(total)

        total = 0
        for v in asts.values():
            if len(v) == 2:
                l = list(v)
                n1 = visited[l[0]]
                n2 = visited[l[1]]
                total += n1 * n2

        print(total)

    # with open(inputfile) as f:
    #     asts = {}
    #     grid = [row.strip() for row in f]
    #     for y, row in enumerate(grid):
    #         for x, char in enumerate(row):
    #             if not grid[y][x] != '*':
    #                 continue
    #
    #
    #
    #
    #
