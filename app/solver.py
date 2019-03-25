from puzzle import Puzzle
class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
    

    def getOccurances(self, value, key, index):
        numOccurances = 0
        # if key == 'row':
        #     for cell in self.puzzle.rows[index]:
        #         if value in cell.possibleValues:
        #             numOccurances += 1
        # if key == 'column':
        #     for cell in self.puzzle.columns[index]:
        #         if value in cell.possibleValues:
        #             numOccurances += 1

        if key == 'sector':
            for cell in self.puzzle.sectors[index]:
                if value in cell.possibleValues:
                    numOccurances += 1
        return numOccurances

    def advanvedSolve(self):
        for num in range(1, 10):
            for index in range(9):


                # if (self.getOccurances(num, 'column', index) == 1):
                #     for i in self.puzzle.columns[index]:
                #         if num in i.possibleValues:
                #             i.equals(num)
                #             self.puzzle.updateNums()


                if (self.getOccurances(num, 'sector', index) == 1):
                    for i in self.puzzle.sectors[index]:
                        if num in i.possibleValues:
                            i.equals(num)
                            self.puzzle.updateNums()
                            return

                # if (self.getOccurances(num, 'row', index) == 1):
                #     for i in self.puzzle.rows[index]:
                #         if num in i.possibleValues:
                #             i.equals(num)
                #             self.puzzle.updateNums()

    def solve(self, index = -1):
        while self.puzzle.numToSolve != 0:
            num = self.puzzle.numToSolve
            for i in self.puzzle.cells:
                if not i.isSolved:
                    for j in self.puzzle.getColumn(i.index):
                            self.puzzle.numToSolve -= i.removePossibleValue(j.value)
                    for j in self.puzzle.getRow(i.index):
                            self.puzzle.numToSolve -= i.removePossibleValue(j.value)
                    for j in self.puzzle.getSector(i.index):
                            self.puzzle.numToSolve -= i.removePossibleValue(j.value)

            if num == self.puzzle.numToSolve:
                print("--------Failed to solve this puzzle--------")
                return self.puzzle
        return self.puzzle
