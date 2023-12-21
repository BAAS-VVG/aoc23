import itertools


def removedoubledots(lst):
    nondots = [i for i, c in enumerate(lst) if c != '.']
    nondotsranges = [[t[0][1], t[-1][1] + 1] for t in (list(g) for k, g in itertools.groupby(
        enumerate(nondots), lambda l: l[0] - l[1]))]
    res = lst[nondotsranges[0][0]:nondotsranges[0][1]]
    for rng in nondotsranges[1:]:
        res.append('.')
        res.extend(lst[rng[0]:rng[1]])

    return res


def makespring(spring, unknowns, lengths, lut):
    unknowns = [i for i, ltr in enumerate(spring) if ltr == '?']
    dmgs = [i for i, c in enumerate(spring) if c == '#']
    if len(dmgs) > sum(lengths) or len(unknowns) + len(dmgs) < sum(lengths):
        return 0

    dmgrngs = [t[-1][1] - t[0][1] + 1 for t in
               (list(g) for k, g in itertools.groupby(enumerate(dmgs), lambda l: l[0] - l[1]))]
    if len(dmgrngs) == len(lengths) and all([dmgrng == ln for dmgrng, ln in zip(dmgrngs, lengths)]):
        return 1

    if len(unknowns) == 0:
        return 0

    dmgrngs = [[t[0][1], t[-1][1]] for t in (list(g) for k, g in itertools.groupby(
        enumerate([idx for idx in dmgs if idx < unknowns[0]]), lambda l: l[0] - l[1]))]
    if len(dmgrngs) > len(lengths):
        return 0
    remainingidcs = len(spring) - unknowns[0]
    numranges = len(dmgrngs)
    if numranges > 0:
        dmgszs = [d[1] - d[0] + 1 for d in dmgrngs]
        zp = [p for p in zip(dmgszs, lengths)]
        if spring[unknowns[0] - 1] == '#':
            if sum(lengths[numranges - 1:]) + len(lengths[numranges - 1:]) - 1 > remainingidcs + dmgszs[-1]:
                return 0
            for dmgrng, ln in zp[:-1]:
                if dmgrng != ln:
                    return 0
            if zp[-1][0] > zp[-1][1]:
                return 0
        else:
            if sum(lengths[numranges:]) + len(lengths[numranges:]) - 1 > remainingidcs:
                return 0
            for dmgrng, ln in zp:
                if dmgrng != ln:
                    return 0

    else:
        if sum(lengths) + len(lengths) - 1 > remainingidcs:
            return 0

    res = 0
    for c in ".#":
        newspring = removedoubledots(spring[:unknowns[0]] + [c] + spring[unknowns[0] + 1:])
        if (tuple(newspring), tuple(lengths)) not in lut:
            lut[(tuple(newspring), tuple(lengths))] = makespring(newspring, unknowns[1:], lengths, lut)
        res += lut[(tuple(newspring), tuple(lengths))]

    return res


def d12():
    inputfile = "d12.txt"
    # inputfile = "test.txt"

    lut = {}  # (spring, lengths) = npossibilities

    res = 0
    with open(inputfile) as f:
        for line in f.readlines():
            spring = list(line.split()[0])
            spring = removedoubledots(spring)
            lens = [int(v) for v in line.split()[1].split(',')]
            unknwns = [i for i, ltr in enumerate(spring) if ltr == '?']
            res += makespring(spring, unknwns, lens, lut)

    print(res)

    res = 0
    with open(inputfile) as f:
        for line in f.readlines():
            spring = list(line.split()[0])
            for i in range(4):
                spring.extend("".join("?" + line.split()[0]))
            spring = removedoubledots(spring)
            lens = [int(v) for v in line.split()[1].split(',')] * 5
            unknwns = [i for i, ltr in enumerate(spring) if ltr == '?']
            res += makespring(spring, unknwns, lens, lut)

    print(res)
