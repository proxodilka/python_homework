class MoneyBox:
    def __init__(self, capacity):
        self.volume = capacity
        self.have = 0

    def can_add(self, v):
        return self.volume >= v + self.have

    def add(self, v):
        self.have += v