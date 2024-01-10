def part1(line):
    winning = set([int(n) for n in line.split('|')[0].split()])
    numbers = set([int(n) for n in line.split('|')[1].split()])

    amount = len(winning.intersection(numbers))
    return amount


def d4():
    print("d4")
    filename = "d4.txt"
    # filename = "test.txt"

    with open(filename) as f:
        print(sum([int(2 ** (part1(line.split(':')[1]) - 1)) for line in f.readlines()]))

    with open(filename) as f:
        temp = [line.split(':')[1] for line in f.readlines()]
        multiples = len(temp) * [1]
        for i, line in enumerate(temp):
            add = part1(line)
            for idx in range(add):
                multiples[i + idx + 1] += multiples[i]

        print(sum(multiples))
