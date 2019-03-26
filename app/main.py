from puzzle import Puzzle
from solver import Solver
userInput = ""
userData = []
sudokuCSV = []

with open("SudokuSolver\data\sudokushort.csv", 'r') as filestream:
        for line in filestream:
                currentline = line.split(",")
                sudokuCSV.append(currentline)

# userInput = "906008070012700080038600024081000209090030007370020640000560401000094800060100050"
# for i in range(0, len(userInput)):
#         data = []
#         userData.append(int(userInput[i]))

# puzzle = Puzzle(userData)
# print(puzzle.showPuzzle())
# solver = Solver(puzzle)
# solver.solve()
# print(puzzle.showPuzzle())

totalSolved = 0
totalUnsolved = 0
for i in sudokuCSV:
        if totalSolved % 1000 == 0:
                print(totalSolved)
        input = []
        for j in i[0]:
                input.append(int(j))
        puzzle = Puzzle(input)
        solver = Solver(puzzle)
        solver.solve()
        if puzzle.toString() == i[1][:-1]:
                totalSolved += 1
        else: 
                totalUnsolved += 1
                print(puzzle.cells[14].possibleValues)
                print(puzzle.showPuzzle())
print("Total solved: " + str(totalSolved))
print("Total unsovled: " + str(totalUnsolved))

