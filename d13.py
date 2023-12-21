def palindrome(lst, part2=False):
    if len(lst) % 2 == 1:
        return False
    if not part2:
        return all([x == y for x, y in zip(lst[:len(lst)//2], reversed(lst[len(lst)//2:]))])
    dif = 0
    for l1, l2 in zip(lst[:len(lst)//2], reversed(lst[len(lst)//2:])):
        for x, y in zip(l1, l2):
            if x != y:
                dif += 1
            if dif > 1:
                return False

    if dif == 1:
        return True
    return False


def calcline(grid, part2=False):
    for i in range(len(grid) - 1):
        if palindrome(grid[i:], part2):
            return 100 * (i + (len(grid) - i) // 2)

    for i in range(1, len(grid) - 1):
        if palindrome(grid[:len(grid) - i], part2):
            return 100 * ((len(grid) - i) // 2)

    grid = [list(x) for x in zip(*grid)]

    for i in range(len(grid) - 1):
        if palindrome(grid[i:], part2):
            return i + (len(grid) - i) // 2

    for i in range(1, len(grid) - 1):
        if palindrome(grid[:len(grid) - i], part2):
            return (len(grid) - i) // 2

    raise Exception("No mirror found!")


def d13():
    inputfile = "d13.txt"
    # inputfile = "test.txt"

    with open(inputfile) as f:
        res = 0
        for block in f.read().strip().split('\n\n'):
            grid = []
            for line in block.split('\n'):
                grid.append(line)
            res += calcline(grid)

    print(res)

    with open(inputfile) as f:
        res = 0
        for block in f.read().strip().split('\n\n'):
            grid = []
            for line in block.split('\n'):
                grid.append(line)
            res += calcline(grid, True)

    print(res)
