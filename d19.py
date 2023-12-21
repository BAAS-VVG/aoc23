def A(part):
    return True


def R(part):
    return False


def d19():
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

        res = 0
        for part in parts.strip().split('\n'):
            part = [int(i) for i in ''.join((c if c in '0123456789' else ' ') for c in part).split()]
            if innn(part):
                res += sum(part)

        print(res)

        res = 0
        for x in range(1, 4001):
            for m in range(1, 4001):
                for a in range(1, 4001):
                    for s in range(1, 4001):
                        if innn((x, m, a, s)):
                            res += 1

        print(res)
