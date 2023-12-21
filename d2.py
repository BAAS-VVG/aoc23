def possible(games):
    numred = 12
    numgreen = 13
    numblue = 14
    for game in games:
        colors = game.split(',')
        for color in colors:
            cubes = color.split()
            if cubes[1] == "red" and int(cubes[0]) > numred:
                return False
            if cubes[1] == "green" and int(cubes[0]) > numgreen:
                return False
            if cubes[1] == "blue" and int(cubes[0]) > numblue:
                return False

    return True


def d2():
    inputfile = "d2.txt"
    # inputfile = "test.txt"

    # part one
    with open(inputfile) as f:
        res = 0
        for line in f.readlines():
            idx = int(line.split(':')[0].split()[-1])
            games = line.split(':')[1].split(';')

            if possible(games):
                res += idx
        print(res)

    # part two
    with open(inputfile) as f:
        res = 0
        for line in f.readlines():
            games = line.split(':')[1].split(';')
            reds = [0]
            greens = [0]
            blues = [0]
            for game in games:
                colors = game.split(',')
                for color in colors:
                    cube = color.split()
                    if cube[1] == "red":
                        reds.append(int(cube[0]))
                    if cube[1] == "green":
                        greens.append(int(cube[0]))
                    if cube[1] == "blue":
                        blues.append(int(cube[0]))

            power = max(reds) * max(greens) * max(blues)
            res += power
        print(res)


