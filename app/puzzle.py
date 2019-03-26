from cell import Cell
class Puzzle:
    def __init__(self, numbers):
        self.numToSolve = 81
        self.cells = []
        for i in range(0, len(numbers)):
            self.cells.append(Cell(numbers[i], i))
            if self.cells[i].isSolved: self.numToSolve -= 1 

    def __contains__(self, value):
        for i in self.cells:
            if i.value == value: return True
        return False

    # Returns the index of the 3x3 sector the cell resides in
    def getSectorNumber(self, index):
        r = int(index / 27)     # The row in the grid of 3x3 cells
        c = int(index / 3) % 3  # The column in the grid of 3x3 cells
        return int(3 * r + c)

    # Returns the index of the column the cell is in 0-8
    def getColumnNumber(self, index):
        return int(index % 9)

    # Returns the index of the row the cell is in 0-8
    def getRowNumber(self, index):
        return int(index / 9) 

    # Returns the 3x3 sector the cell resides in
    def getSector(self, index):
        returnArray = []
        for i in range(9):
            returnArray.append(self.cells[27 * int(index / 27) + 3 * int((index % 9) / 3) + 9 * int(i / 3) + i % 3]) 
        return returnArray

    # Returns the number of the column the cell is in 0-8
    def getColumn(self, index):
        returnArray = []
        for i in range(9):
            # print(type(index))
            returnArray.append(self.cells[9 * i + self.getColumnNumber(index)]) 
        return returnArray

    # Returns the number of the row the cell is in 0-8
    def getRow(self, index):
        returnArray = []
        for i in range(9):
            returnArray.append(self.cells[9 * self.getRowNumber(index) + i]) 
        return returnArray


    # Prints the puzzle in a formatted manner
    def showPuzzle(self): 
        out = "" # Build a string
        for i in range(0, len(self.cells)):                                    # For every number
            out += " " + str(self.cells[i].value) + " "                              # Add it to the string
            if self.getColumnNumber(i) == 2 or self.getColumnNumber(i) == 5:    # If the number is in column 2 or 5 it needs a dividing line
                out += " | " 
            if self.getColumnNumber(i) == 8:                                    # If the number is in column 8 it needs a newline
                out += "\n"
                if self.getRowNumber(i) == 2 or self.getRowNumber(i) == 5:      # If the row was 2 or 5, a divider is needed before the next line
                    out += "---------------------------------\n"
        return out                                                              # Output the built string

    def toString(self):
        out = ""
        for i in self.cells:
            out += str(i.value)
        return out

