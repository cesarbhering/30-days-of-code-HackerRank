class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        if (sum(scores)/len(scores)) >= 90:
            return('O')
        elif (sum(scores)/len(scores)) >= 80:
            return('E')
        elif (sum(scores)/len(scores)) >= 70:
            return('A')
        elif (sum(scores)/len(scores)) >= 55:
            return('P')
        elif (sum(scores)/len(scores)) >= 40:
            return('D')
        else:
            return('T')
            