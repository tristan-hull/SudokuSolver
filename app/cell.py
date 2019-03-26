class Cell:

    def __init__(self, value, index):
        self.value = 0
        self.possibleValues = []
        self.index = index
        self.isSolved = False
        if value > 0:
            self.value = value
            self.isSolved = True
        else: self.possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def equals(self, value):
        self.value = value
        self.isSolved = True
        self.possibleValues.clear()
    
    # def addValue(self, value):
    #     self.possibleValues.append(value)
    
    def int(self):
        return self.value

    def __radd__(self, other):
        return other + self.value

    def updateCell(self):
        if len(self.possibleValues) == 1 and self.isSolved is False:
            self.value = self.possibleValues[0]
            self.isSolved = True
            return 1
        elif len(self.possibleValues) == 0 and not self.isSolved: return -1
        else: return 0

    def removePossibleValue(self, value):
        if value in self.possibleValues:
            self.possibleValues.remove(value)
        return 0

        
    