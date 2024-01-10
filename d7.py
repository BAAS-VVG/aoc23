def d7():
    print("d7")
    inputfile = "d7.txt"
    # inputfile = "test.txt"

    class Card:
        def __init__(self, c, part2=False):
            self.c = c
            self.p2 = part2

        def __repr__(self):
            return self.c

        def __gt__(self, other):
            order = "AKQJT98765432"
            if self.p2:
                order = "AKQT98765432J"
            return order.find(self.c) < order.find(other.c)

        def __eq__(self, other):
            return self.c == other.c

        def __ge__(self, other):
            return self > other or self == other

        def __ne__(self, other):
            return not self == other

        def __lt__(self, other):
            return not self >= other

        def __le__(self, other):
            return not self > other

    class Hand:
        def __init__(self, txt, part2=False):
            self.p2 = part2
            self.cards = [Card(c, part2) for c in txt]
            self.dct = {}
            for c in txt:
                if c in self.dct:
                    self.dct[c] += 1
                else:
                    self.dct[c] = 1
            jokers = 0
            if part2:
                if "J" in self.dct:
                    jokers = self.dct["J"]
                    self.dct["J"] = 0

            self.h = list(reversed(sorted(list(self.dct.values()))))
            if part2:
                self.h[0] += jokers

        def __lt__(self, other):
            for s, o in zip(self.h, other.h):
                if s < o:
                    return True
                elif s > o:
                    return False

            for s, o in zip(self.cards, other.cards):
                if s < o:
                    return True
                elif o < s:
                    return False

            return False

        def __repr__(self):
            return "".join([c.c for c in self.cards])

        def __eq__(self, other):
            return self.h == other.h and self.cards == other.cards

        def __le__(self, other):
            return self < other or self == other

        def __ne__(self, other):
            return not self == other

        def __gt__(self, other):
            return not self <= other

        def __ge__(self, other):
            return not self < other

    with open(inputfile) as f:
        dct = {}
        hands = []
        hands2 = []
        for line in f.readlines():
            dct[line.split()[0]] = int(line.split()[1])
            hands.append(Hand(line.split()[0]))
            hands2.append(Hand(line.split()[0], True))

        hands.sort()

        res = 0
        factor = 1
        for hand in hands:
            res += factor * dct[str(hand)]
            factor += 1

        print(res)

        hands2.sort()
        res = 0
        factor = 1
        for hand in hands2:
            res += factor * dct[str(hand)]
            factor += 1

        print(res)

