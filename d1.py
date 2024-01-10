def d1():
    print("d1")
    inputfile = "d1.txt"
    # inputfile = "test.txt"

    digits = ["one",
              "two",
              "three",
              "four",
              "five",
              "six",
              "seven",
              "eight",
              "nine"]

    # part one
    with open(inputfile) as f:
        total = 0
        for line in f.readlines():
            numbers = [int(x) for x in line if x.isnumeric()]
            total += 10 * numbers[0] + numbers[-1]

    print(total)

    # part two
    with open(inputfile) as f:
        total = 0
        for line in f.readlines():
            lindices = [line.find(x) for x in digits]
            rindices = [line.rfind(x) for x in digits]
            nindices = [i for i, c in enumerate(line) if c.isdigit()]
            if len(nindices) == 0:
                nindices = [len(line), 0]
            lindices.insert(0, nindices[0])
            rindices.insert(0, nindices[-1])
            lindices = [idx if idx >= 0 else len(line) for idx in lindices]
            left = lindices.index(min(lindices))
            if left == 0:
                left = int(line[lindices[0]])
            left *= 10
            right = rindices.index(max(rindices))
            if right == 0:
                right = int(line[rindices[0]])
            total += left + right

    print(total)
