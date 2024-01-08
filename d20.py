import re
from math import prod
from queue import Queue


class Module:
    def __init__(self, name):
        self.dests = []
        self.name = name

    def pulse(self, queue, prevpulse):
        for dst in self.dests:
            queue.put((dst, self.name, prevpulse[2]))

    def addsrc(self, name):
        pass

    def reset(self):
        pass


class FlipFlop(Module):
    def __init__(self, name):
        super().__init__(name)
        self.state = False  # low

    def pulse(self, queue, prevpulse):  # True is high, False is low
        if prevpulse[2]:
            return

        self.state = not self.state  # Flip
        for dst in self.dests:
            queue.put((dst, self.name, self.state))  # send pulse.

    def reset(self):
        self.state = False


class Conjunction(Module):
    def __init__(self, name):
        super().__init__(name)
        self.inputs = {}

    def addsrc(self, name):
        self.inputs[name] = False  # low

    def pulse(self, queue, prevpulse):
        self.inputs[prevpulse[1]] = prevpulse[2]

        for dst in self.dests:
            queue.put((dst, self.name, not all(self.inputs.values())))

    def reset(self):
        for k in self.inputs:
            self.inputs[k] = False


def d20():
    inputfile = "d20.txt"
    # inputfile = "test.txt"

    modules = {}

    with open(inputfile) as f:
        for line in f.readlines():
            name, dests = [txt.strip() for txt in line.split('->')]
            dests = [d.strip() for d in re.split(',', dests)]

            if name[0] == '%':
                name = name[1:]
                modules[name] = FlipFlop(name)
                modules[name].dests.extend(dests)
            elif name[0] == '&':
                name = name[1:]
                modules[name] = Conjunction(name)
                modules[name].dests.extend(dests)
            else:
                modules[name] = Module(name)
                modules[name].dests.extend(dests)

    with open(inputfile) as f:
        for line in f.readlines():
            name, dests = [txt.strip() for txt in line.split('->')]
            dests = [d.strip() for d in re.split(',', dests)]

            if name[0] in '%&':
                name = name[1:]

            for dst in dests:
                if dst in modules:
                    modules[dst].addsrc(name)

    queue = Queue()
    low = 0
    high = 0
    for iter in range(1000):
        queue.put(("broadcaster", "button", False))
        while not queue.empty():
            pulse = queue.get()
            if pulse[2]:
                high += 1
            else:
                low += 1
            if pulse[0] in modules:
                modules[pulse[0]].pulse(queue, pulse)

    print(low * high)

    for module in modules.values():
        module.reset()

    iter = 0

    finalConj = [m.name for m in modules.values() if "rx" in m.dests][0]
    finalInputs = set([m.name for m in modules.values() if finalConj in m.dests])
    cycles = []

    while True:
        iter += 1
        queue.put(("broadcaster", "button", False))
        while not queue.empty():
            pulse = queue.get()
            if pulse[1] in finalInputs and pulse[2]:
                cycles.append(iter)
                finalInputs.remove(pulse[1])
            if pulse[0] in modules:
                modules[pulse[0]].pulse(queue, pulse)

        if not finalInputs:
            break

    print(prod(cycles))
