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

    # part 2

    hailstones = []
    with open(inputfile) as f:
        for line in f.readlines():
            pos, vec = [[int(c) for c in v.split(',')] for v in line.strip().split('@')]
            hailstones.append(Ray(pos, [p + d for p, d in zip(pos, vec)]))

    offset = 0
    while True:
        for xOffset in range(offset + 1):
            yOffset = offset - xOffset
            for negX in (-1, 1):
                X = negX * xOffset
                for negY in (-1, 1):
                    Y = negY * yOffset
                    h0 = Ray(hailstones[0].p[:2], [p + o for p, o in zip(hailstones[0].points[1][:2], [X, Y])])
                    intersection = None
                    Z = None
                    times = []
                    for n, hN in enumerate([Ray(h.p[:2], [p + o for p, o in zip(h.points[1][:2], [X, Y])]) for h in hailstones[1:4]]):
                        t1, t2, status = intersect(h0, hN)
                        currIntersection = None
                        currZ = None
                        if len(times) == 0:
                            times.append(t1)
                        times.append(t2)
                        if status == RayIntersection.COLINEAR or t1 < -0.0 or t2 < -0.0:
                            break
                        currIntersection = [round(x) for x in hN.eval(t2)]
                        currZ = round((hailstones[0].p[2] - hailstones[n + 1].p[2] + t1 * hailstones[0].d[2] - t2 * hailstones[n + 1].d[2]) / (t1 - t2))
                        if intersection is None:
                            intersection = currIntersection
                            Z = currZ
                            continue
                        if currIntersection != intersection or Z != currZ:
                            break
                    if currIntersection is None or intersection != currIntersection or Z != currZ:
                        continue

                    h0 = Ray(hailstones[0].p, [p + o for p, o in zip(hailstones[0].points[1], [X, Y, -Z])])
                    intersection = [round(x) for x in h0.eval(t1)]
                    print(sum(intersection))
                    return
        offset += 1







