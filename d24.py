import itertools
from geomdl.ray import Ray, intersect, RayIntersection


def d24():
    print("d24")

    inputfile = "d24.txt"
    boundary = (200000000000000, 400000000000000)

    # inputfile = "test.txt"
    # boundary = (7, 27)

    hailstones = []
    with open(inputfile) as f:
        for line in f.readlines():
            pos, vec = [[int(c) for c in v.split(',')[:2]] for v in line.strip().split('@')]
            hailstones.append(Ray(pos, [p + d for p, d in zip(pos, vec)]))

    res = 0
    for r1, r2 in itertools.combinations(hailstones, 2):
        t1, t2, status = intersect(r1, r2)
        if status != RayIntersection.COLINEAR and t1 >= 0 and t2 >= 0:  # future intersections
            if all(boundary[0] <= axis <= boundary[1] for axis in r1.eval(t1)):  # in test area
                res += 1

    print(res)

