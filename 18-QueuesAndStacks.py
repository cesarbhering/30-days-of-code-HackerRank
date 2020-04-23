class Solution:
    def __init__(self):
        self.queue = []
        self.stack = []

    def pushCharacter(self, x):
        self.stack.append(x)

    def enqueueCharacter(self, x):
        self.queue.insert(0, x)

    def popCharacter(self):
        base = self.stack[0]
        self.stack.pop(0)
        return base

    def dequeueCharacter(self):
        base = self.queue[0]
        self.queue.pop(0)
        return base
