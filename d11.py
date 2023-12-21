def d11():
    inputfile = "d11.txt"
    # inputfile = "test.txt"

    glx = []
    with open(inputfile) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c == '#':
                    glx.append([x, y])

    width = x + 1
    height = y + 1

    emptyrows = []
    for row in range(height):
        if not any(v[1] == row for v in glx):
            emptyrows.append(row)

    emptycols = []
    for col in range(width):
        if not any(v[0] == col for v in glx):
            emptycols.append(col)

    emptyrows.reverse()
    emptycols.reverse()

    for row in emptyrows:
        for idx in range(len(glx)):
            if row < glx[idx][1]:
                glx[idx][1] += 1

    for col in emptycols:
        for idx in range(len(glx)):
            if col < glx[idx][0]:
                glx[idx][0] += 1
    res = 0
    for pair in [(a, b) for idx, a in enumerate(glx) for b in glx[idx + 1:]]:
        res += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

    print(res)

    glx = []
    with open(inputfile) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c == '#':
                    glx.append([x, y])

    for row in emptyrows:
        for idx in range(len(glx)):
            if row < glx[idx][1]:
                glx[idx][1] += 999999

    for col in emptycols:
        for idx in range(len(glx)):
            if col < glx[idx][0]:
                glx[idx][0] += 999999
    res = 0
    for pair in [(a, b) for idx, a in enumerate(glx) for b in glx[idx + 1:]]:
        res += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

    print(res)
