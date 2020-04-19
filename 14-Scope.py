class Difference:
    def __init__(self, a):
        self.__elements = a
        self.elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        self.elements.sort()
        self.maximumDifference = self.elements[-1]-self.elements[0]
