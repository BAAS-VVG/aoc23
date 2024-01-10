import math


def d8():
    print("d8")
    inputfile = "d8.txt"
    # inputfile = "test.txt"

    with open(inputfile) as f:
        dirs = f.readline().strip()
        f.readline()

        dct = {}
        for line in f.readlines():
            dct[line.split('=')[0].strip()] = [s.strip() for s in line.split('=')[1].strip("( )\n").split(',')]

    dirlen = len(dirs)
    pos = "AAA"
    steps = 0
    while pos != "ZZZ":
        pos = dct[pos][0 if dirs[steps % dirlen] == 'L' else 1]
        steps += 1

    print(steps)

    positions = [s for s in dct.keys() if s.endswith("A")]
    steps = 0
    solutiondct = {}
    while len(solutiondct.keys()) != len(positions):
        newpos = []
        idx = 0 if dirs[steps % dirlen] == 'L' else 1
        for i, pos in enumerate(positions):
            if pos.endswith("Z"):
                solutiondct[i] = steps
            newpos.append(dct[pos][idx])
        positions = newpos
        steps += 1

    gcd = math.gcd(*solutiondct.values())
    print(math.prod([v // gcd for v in solutiondct.values()]) * gcd)
