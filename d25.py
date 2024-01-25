import math
import random


def d25():
    print("d25")
    inputfile = "d25.txt"
    # inputfile = "test.txt"

    vertices = {}
    edges = []
    with open(inputfile) as f:
        for line in f.readlines():
            left, rights = line.strip().split(':')
            vertices[left] = 1
            for right in rights.strip().split():
                vertices[right] = 1
                edges.append([left, right])

    answer = 0
    while answer != 3:
        v = vertices.copy()
        e = edges.copy()

        while len(v.keys()) > 2:
            randedge = random.choice(e)
            v1, v2 = randedge
            v[v1 + v2] = v[v1] + v[v2]  # combine vertices into one
            del v[v1]  # remove old vertices
            del v[v2]

            e = [[v1 + v2 if vert in randedge else vert for vert in edge] for edge in e]  # redirect edges
            e = [edge for edge in e if edge != [v1 + v2, v1 + v2]]  # remove edges between the same vertex

        answer = len(e)
    print(math.prod(list(v.values())))

