from collections import deque


class CircularList:
    def __init__(self, size):
        self.items = []
        self.index = 0
        self.max_size = size
        self.size = 0

    def append(self, item):
        self.index = (self.index + 1) % self.max_size
        if self.size == self.max_size:
            self.items[self.index] = item
        else:
            self.items.append(item)
        self.size = min(self.max_size, self.size + 1)

    def avg(self):
        return sum(self.items) / len(self.items)


class Analogue:
    def __init__(self, adc):
        self.adc = adc
        self.accumulator = CircularList(10)

    def read(self):
        sample = self.adc.read_u16()
        self.accumulator.append(sample)
        return self.accumulator.avg()
