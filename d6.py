import math


def d6():
    inputfile = "d6.txt"
    # inputfile = "test.txt"

    with open(inputfile) as f:
        times = [int(x) for x in f.readline().split(':')[1].split()]
        distances = [int(x) for x in f.readline().split(':')[1].split()]

        print(math.prod([math.ceil((-time - math.sqrt(time * time - 4 * dist)) / -2) - math.floor((-time + math.sqrt(time * time - 4 * dist)) / -2) - 1 for time, dist in zip(times, distances)]))

    with open(inputfile) as f:
        time = int("".join(f.readline().split(':')[1].split()))
        dist = int("".join(f.readline().split(':')[1].split()))

        print(math.ceil((-time - math.sqrt(time * time - 4 * dist)) / -2) - math.floor((-time + math.sqrt(time * time - 4 * dist)) / -2) - 1)
