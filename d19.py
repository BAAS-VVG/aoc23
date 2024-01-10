import copy


def splitrange(remm, line):
    var = line[0]
    sign = line[1]
    val = int(line[2:])
    resm = copy.deepcopy(remm)
    if sign == '<':
        if val < remm[var][0]:
            resm[var] = tuple([0, 0])
            return resm
        if val >= remm[var][1]:
            remm[var] = tuple([0, 0])
            return resm
        resm[var] = tuple([remm[var][0], val - 1])
        remm[var] = tuple([val, remm[var][1]])
        return resm
    if val > remm[var][1]:
        resm[var] = tuple([0, 0])
        return resm
    if val <= remm[var][0]:
        remm[var] = tuple([0, 0])
        return resm
    resm[var] = tuple([val + 1, remm[var][1]])
    remm[var] = tuple([remm[var][0], val])
    return resm


def d19():
    print("d19")
    inputfile = "d19.txt"
    # inputfile = "test.txt"

    with open(inputfile) as f:
        manual, parts = f.read().split('\n\n')

        for rule in manual.split('\n'):
            name, body = rule.strip('}').split('{')

            if name == "in":  # to circumvent the keyword 'in'
                name = "innn"

            func = "def " + name + "(part):\n"
            func += " x, m, a, s = part\n"
            for line in body.split(','):
                if ':' in line:
                    func += " if " + line.split(':')[0] + ':\n' + "  return " + line.split(':')[1] + "(part)\n"
                else:
                    func += " return " + line + "(part)\n"
            exec(func, globals())

    func = "def A(part): return True"
    exec(func, globals())
    func = "def R(part): return False"
    exec(func, globals())

    res = 0
    for part in parts.strip().split('\n'):
        part = [int(i) for i in ''.join((c if c in '0123456789' else ' ') for c in part).split()]
        if innn(part):
            res += sum(part)

    print(res)

    with open(inputfile) as f:
        manual = f.read().split('\n\n')[0]
        for rule in manual.split('\n'):
            name, body = rule.strip('}').split('{')

            if name == "in":  # to circumvent the keyword 'in'
                name = "innn"

            func = "def " + name + "(mp):\n"
            func += " remm = copy.deepcopy(mp)\n"
            func += " total = 0\n"
            for line in body.split(','):
                if ':' in line:
                    func += " resm = splitrange(remm, \"" + line.split(':')[0] + '\")\n'
                    func += " total += " + line.split(':')[1] + "(resm)\n"
                else:
                    func += " return total + " + line + "(remm)\n"
            exec(func, globals())

    func = "def A(mp):\n"
    func += " res = 1\n"
    func += " for var in \"xmas\":\n"
    func += "  res *= mp[var][1] - mp[var][0] + 1\n"
    func += " return res\n"
    exec(func, globals())
    func = "def R(mp): return 0"
    exec(func, globals())

    mp = dict()
    mp["x"] = (1, 4000)
    mp["m"] = (1, 4000)
    mp["a"] = (1, 4000)
    mp["s"] = (1, 4000)

    print(innn(mp))

