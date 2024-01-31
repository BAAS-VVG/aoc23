from collections import defaultdict
from copy import copy
from queue import Queue, LifoQueue


def d23():
    print("d23")

    inputfile = "d23.txt"
    # inputfile = "test.txt"

    # Observation 1: slippery slopes occur only on intersections.
    # Observation 2: slippery slopes always point south or east.
    def makegraph():
        def isintersection():
            walls = 0
            for offset in offsets:
                if grid[(pos[0] + offset[0], pos[1] + offset[1])] == '#':
                    walls += 1
                    if walls == 2:
                        return False

            return True

        stack = LifoQueue()
        stack.put(((1, 1), (1, 0), (1, 0), 1, 1))  # (currpos, prevpos, prevnode, prevdir, dist)
        visited = {(1, 0)}
        while not stack.empty():
            pos, prevpos, prevnode, prevdir, dist = stack.get()
            if grid[pos] == '#' or pos == prevnode:
                continue

            dist += 1

            # if at goal add node to graph
            if pos[1] == height - 1:
                graph[prevnode][prevdir] = (pos, dist)
                graph[pos][3] = (prevnode, dist)
                continue

            # if at intersection add node to graph
            if isintersection():
                graph[prevnode][prevdir] = (pos, dist)
                if pos[0] - prevpos[0] > 0:
                    graph[pos][2] = (prevnode, dist)
                elif pos[1] - prevpos[1] > 0:
                    graph[pos][3] = (prevnode, dist)
                elif pos[0] - prevpos[0] < 0:
                    graph[pos][0] = (prevnode, dist)
                else:
                    graph[pos][1] = (prevnode, dist)

                for offset, direction in zip(offsets, [1, 0, 2, 3]):
                    stack.put(((pos[0] + offset[0], pos[1] + offset[1]), pos, pos, direction, 0))
                continue

            if pos in visited:
                continue
            visited.add(pos)

            for offset in offsets:
                stack.put(((pos[0] + offset[0], pos[1] + offset[1]), pos, prevnode, prevdir, dist))

    def solvegraph(part2=False):
        maxdist = 0
        queue = LifoQueue()
        queue.put((graph[start][1][0], {start}, graph[start][1][1]))  # pos, visited, dist
        while not queue.empty():
            pos, visited, dist = queue.get()

            if pos in visited:
                continue
            visited.add(pos)

            if pos[1] == height - 1:
                maxdist = max(maxdist, dist)
                continue
            ## TODO: optimisation doesnt produce correct answer!
            for dir in range(4 if part2 and not any([p is None for p in graph[pos]]) else 2):  # optimisation in https://www.reddit.com/r/adventofcode/comments/18oy4pc/comment/kfyvp2g/
                if graph[pos][dir] is None:
                    continue
                node, curdist = graph[pos][dir]
                if not part2 and (pos, curdist) not in graph[node][2:]:
                    continue
                queue.put((node, copy(visited), dist + curdist))

        print(maxdist - 1)

    # def solve(part2=False):
    #     dist = 0
    #     queue = Queue()
    #     queue.put(((1, 1), {start}))
    #     while not queue.empty():
    #         pos, visited = queue.get()
    #         if grid[pos] == '#':
    #             continue
    #         if pos in visited:
    #             continue
    #
    #         visited.add(pos)
    #
    #         if pos[1] == height - 1:
    #             dist = len(visited)
    #             continue
    #
    #         if not part2 and grid[pos] in signs:
    #             currentoffsets = [offsets[signs.index(grid[pos])]]
    #         else:
    #             currentoffsets = offsets
    #
    #         newpositions = [(pos[0] + offset[0], pos[1] + offset[1]) for offset in currentoffsets]
    #         for newpos in newpositions:
    #             if grid[newpos] == '#' or newpos in visited:
    #                 newpositions.remove(newpos)
    #
    #         if len(newpositions) == 0:
    #             continue
    #         queue.put((newpositions[0], visited))  # don't copy set if not necessary
    #         if len(newpositions) > 1:
    #             for newpos in newpositions[1:]:
    #                 queue.put((newpos, copy(visited)))
    #
    #     print(dist - 1)

    grid = {}

    with open(inputfile) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                grid[(x, y)] = c

    height = y + 1
    width = x + 1
    start = (1, 0)  # consistent in test and real data

    signs = ["v", ">", "<", "^"]
    offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    graph = defaultdict(lambda: [None, None, None, None])  # ESWN
    makegraph()
    # solve()
    solvegraph()
    # solve(True)
    solvegraph(True)







