class Cell:

    def __init__(self, value, index):
        self.value = 0
        self.possibleValues = []
        self.index = index
        self.isSolved = False
        if value > 0:
            self.value = value
            self.isSolved = True
        else:
            for i in range(1, 10):
                self.possibleValues.append(i)
    
    def equals(self, value):
        self.value = value
        self.isSolved = True
        self.possibleValues.clear()
    
    # def addValue(self, value):
    #     self.possibleValues.append(value)
        
    def updateCell(self):
        if len(self.possibleValues) == 1 and self.isSolved is False:
            self.value = self.possibleValues[0]
            self.isSolved = True
            return 1
        else: return 0

    def removePossibleValue(self, value):
        if value in self.possibleValues:
            self.possibleValues.remove(value)
            return self.updateCell()
        else: return 0

        
    