from shapely.geometry import Polygon


def d18():
    inputfile = "d18.txt"
    # inputfile = "test.txt"

    points = [(0, 0)]
    with open(inputfile) as f:
        for i, line in enumerate(f.readlines()):
            d, l, _ = line.split()
            l = int(l)

            if d == "R":
                points.append((points[i][0] + l, points[i][1]))
            elif d == "D":
                points.append((points[i][0], points[i][1] + l))
            elif d == "L":
                points.append((points[i][0] - l, points[i][1]))
            else:
                points.append((points[i][0], points[i][1] - l))

    pgon = Polygon(points).buffer(0.5, join_style="mitre")

    print(int(pgon.area))

    points = [(0, 0)]
    with open(inputfile) as f:
        for i, line in enumerate(f.readlines()):
            c = line.split()[2].strip('(#)')
            l = int(c[:5], 16)
            d = int(c[5])

            if d == 0:
                points.append((points[i][0] + l, points[i][1]))
            elif d == 1:
                points.append((points[i][0], points[i][1] + l))
            elif d == 2:
                points.append((points[i][0] - l, points[i][1]))
            else:
                points.append((points[i][0], points[i][1] - l))

    pgon = Polygon(points).buffer(0.5, join_style="mitre")

    print(int(pgon.area))
