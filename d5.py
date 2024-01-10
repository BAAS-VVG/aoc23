def mp(lst, val):
    for line in lst:
        if 0 <= val - int(line[1]) < int(line[2]):
            return int(line[0]) + val - int(line[1])
    return val


def mpr(lst, ranges):
    resranges = []
    for line in lst:
        line = [int(v) for v in line]
        idx = 0
        while len(ranges) > idx:
            if 0 <= ranges[idx][0] - line[1] < line[2] and 0 <= ranges[idx][1] - line[1] < line[2]:  # range is fully in map range
                resranges.append((line[0] + ranges[idx][0] - line[1], line[0] + ranges[idx][1] - line[1]))
                del ranges[idx]
                idx -= 1
            elif 0 <= ranges[idx][0] - line[1] < line[2]:  # range starts in map range but exceeds it
                start = line[1] + line[2]
                ranges.append((start, ranges[idx][1]))
                resranges.append((line[0] + ranges[idx][0] - line[1], line[0] + (start - 1) - line[1]))
                del ranges[idx]
                idx -= 1
            elif 0 <= ranges[idx][1] - line[1] < line[2]:  # range ends in map range but starts before it
                start = line[1]
                ranges.append((ranges[idx][0], start - 1))
                resranges.append((line[0] + start - line[1], line[0] + ranges[idx][1] - line[1]))
                del ranges[idx]
                idx -= 1
            elif ranges[idx][0] - line[1] < line[2] and 0 <= ranges[idx][1] - line[1]:  # map range is fully inside range, but with excess
                start = line[1]
                end = line[1] + line[2] - 1
                ranges.append((ranges[idx][0], start - 1))
                ranges.append((end + 1, ranges[idx][1]))
                resranges.append((line[0] + start - line[1], line[0] + end - line[1]))
                del ranges[idx]
                idx -= 1

            idx += 1

    resranges.extend(ranges)

    return resranges


def seedranges(seeds):
    it = iter(seeds)
    for s in it:
        r = next(it)
        yield s, s + r


def d5():
    print("d5")
    inputfile = "d5.txt"
    # inputfile = "test.txt"

    with open(inputfile) as f:
        seeds = [int(n) for n in f.readline().split(':')[1].split()]
        f.readline()
        f.readline()
        seedsoil = []
        line = f.readline()
        while line != '\n':
            seedsoil.append(line.split())

            line = f.readline()
        f.readline()
        soilferti = []
        line = f.readline()
        while line != '\n':
            soilferti.append(line.split())

            line = f.readline()
        f.readline()
        fertiwater = []
        line = f.readline()
        while line != '\n':
            fertiwater.append(line.split())

            line = f.readline()
        f.readline()
        waterlight = []
        line = f.readline()
        while line != '\n':
            waterlight.append(line.split())

            line = f.readline()
        f.readline()
        lighttemp = []
        line = f.readline()
        while line != '\n':
            lighttemp.append(line.split())

            line = f.readline()
        f.readline()
        temphumid = []
        line = f.readline()
        while line != '\n':
            temphumid.append(line.split())

            line = f.readline()
        f.readline()
        humidloca = []
        line = f.readline()
        while line != '':
            humidloca.append(line.split())

            line = f.readline()

    print(min([mp(humidloca, mp(temphumid, mp(lighttemp, mp(waterlight, mp(fertiwater, mp(soilferti, mp(seedsoil, s))))))) for s in seeds]))

    ranges = list(seedranges(seeds))

    resranges = mpr(humidloca, mpr(temphumid, mpr(lighttemp, mpr(waterlight, mpr(fertiwater, mpr(soilferti, mpr(seedsoil, ranges)))))))
    resranges.sort()
    print(resranges[0][0])




