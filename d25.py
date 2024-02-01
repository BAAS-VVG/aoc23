import math
import random
import numpy as np
from numpy.linalg import eigh


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

    # Use spectral bisection to find answer. https://www.reddit.com/r/adventofcode/comments/18qbsxs/comment/kgxsxbz/
    # First build Laplacian matrix of graph
    Lmat = np.zeros((len(vertices.keys()), len(vertices.keys())))
    vertkeys = list(vertices.keys())
    for i, vert in enumerate(vertkeys):
        for edge in edges:
            if vert in edge:
                Lmat[i][i] += 1
                othervert = [v for v in edge if v != vert][0]
                j = vertkeys.index(othervert)
                Lmat[i][j] -= 1
                Lmat[j][i] -= 1

    # Compute eigenvalues and eigenvectors
    vals, vecs = eigh(Lmat)
    # Find index of second smallest eigenvalue
    i2 = sorted([(val, i) for i, val in enumerate(vals)])[1][1]

    # Count the signs of the elements of the corresponding eigenvector.
    # Positive is one side of the graph, negative is on the other.
    pos = 0
    neg = 0
    for num in vecs[i2]:
        if num < 0:
            neg += 1
        else:
            pos += 1

    print(pos * neg)

    # # Karger's algorithm. Found the answer just fine the first time in a couple seconds
    # # but sometimes takes 20 minutes to find the answer due to the randomness of the algorithm.
    # answer = 0
    # while answer != 3:
    #     v = vertices.copy()
    #     e = edges.copy()
    #
    #     while len(v.keys()) > 2:
    #         randedge = random.choice(e)
    #         v1, v2 = randedge
    #         v[v1 + v2] = v[v1] + v[v2]  # combine vertices into one
    #         del v[v1]  # remove old vertices
    #         del v[v2]
    #
    #         e = [[v1 + v2 if vert in randedge else vert for vert in edge] for edge in e]  # redirect edges
    #         e = [edge for edge in e if edge != [v1 + v2, v1 + v2]]  # remove edges between the same vertex
    #
    #     answer = len(e)
    # print(math.prod(list(v.values())))

