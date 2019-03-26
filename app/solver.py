from puzzle import Puzzle
import copy
class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
    

    def getOccurances(self, value, key, index):
        numOccurances = 0
        if key == 'row':
            for cell in self.puzzle.getRow(index):
                if value in cell.possibleValues:
                    numOccurances += 1

        if key == 'column':
            for cell in self.puzzle.getColumn(index):
                if value in cell.possibleValues:
                    numOccurances += 1

        if key == 'sector':
            for cell in self.puzzle.getSector(index):
                if value in cell.possibleValues:
                    numOccurances += 1
        return numOccurances

    def checkPuzzle(self, puzzle = 0):
        if puzzle == 0: puzzle = self.puzzle
        for i in range(9):
            if sum(puzzle.getRow(i)) != 45 or sum(puzzle.getColumn(i)) != 45 or sum(puzzle.getSector(i)) != 45:
                return False
        for num in range(1, 10):
            for i in range(0, 9):
                if any(puzzle.getRow(i).count(num) > 1 for x in puzzle.getRow(i)):
                    return False
            for i in range(0, 9):
                if any(puzzle.getColumn(i).count(num) > 1 for x in puzzle.getColumn(i)):
                    return False
            for i in range(0, 9):
                if any(puzzle.getSector(i).count(num) > 1 for x in puzzle.getSector(i)):
                    return False
        return True

    def advancedSolve(self):
        for num in range(1, 10):
            for index in range(9):
                if (self.getOccurances(num, 'column', index) == 1):
                    for i in self.puzzle.getColumn(index):
                        if num in i.possibleValues:
                            i.equals(num)
                            self.puzzle.numToSolve -= 1
                    return

                if (self.getOccurances(num, 'sector', index) == 1):
                    for i in self.puzzle.getSector(index):
                        if num in i.possibleValues:
                            i.equals(num)
                            self.puzzle.numToSolve -= 1
                    return

                if (self.getOccurances(num, 'row', index) == 1):
                    for i in self.puzzle.getRow(index):
                        if num in i.possibleValues:
                            i.equals(num)
                            self.puzzle.numToSolve -= 1
                    return

    def solve(self):
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
                self.advancedSolve()
            if num == self.puzzle.numToSolve:
                return False
        return True
