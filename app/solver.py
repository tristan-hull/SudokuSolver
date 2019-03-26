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
                if any(puzzle.getColumn(i).count(num) > 1 for x in puzzle.getColumn(i)):
                    return False
                if any(puzzle.getSector(i).count(num) > 1 for x in puzzle.getSector(i)):
                    return False
        return True

    def bruteforceSolve(self, puzzle = 0, level = 0):
        if puzzle == 0: puzzle = self.puzzle
        if not 0 in puzzle:
            return puzzle
        # print(level + "\n" + puzzle.showPuzzle())
        for cell in puzzle.cells:
            if cell.value == 0:
                for value in range(1, 10):
                    possible = False
                    if self.checkValid(puzzle, cell, value):
                        puzzle.cells[cell.index].equals(value)
                        newPuzzle = self.bruteforceSolve(puzzle, level + 1)
                        if newPuzzle:
                            return puzzle
                        puzzle.cells[cell.index].equals(0)
                        
                return False
                        # else: tempPuzzle = puzzle          
        return False
    
    def checkValid(self, puzzle, cell, value):
        for j in puzzle.getColumn(cell.index):
            if j.value == value: return False
        for j in puzzle.getRow(cell.index): 
            if j.value == value: return False
        for j in puzzle.getSector(cell.index):
            if j.value == value: return False
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

    def removeImpossibleValues(self, cell, puzzle = 0):
        if puzzle == 0: puzzle = self.puzzle
        for j in puzzle.getColumn(cell.index):
            if j.isSolved:    
                cell.removePossibleValue(j.value)
        for j in puzzle.getRow(cell.index):
            if j.isSolved:
                cell.removePossibleValue(j.value)
        for j in puzzle.getSector(cell.index):
            if j.isSolved:    
                cell.removePossibleValue(j.value)

    def solve(self):
        while self.puzzle.numToSolve != 0:
            num = self.puzzle.numToSolve
            for i in self.puzzle.cells:
                if not i.isSolved:
                    self.removeImpossibleValues(i)
                    self.puzzle.numToSolve -= i.updateCell()

            if num == self.puzzle.numToSolve: self.advancedSolve()
            if num == self.puzzle.numToSolve: 
                tempPuzzle =  self.bruteforceSolve()
                if tempPuzzle:
                    if self.checkPuzzle(self.puzzle): return True
                else: return False
            if num == self.puzzle.numToSolve:
                return False
        return True


