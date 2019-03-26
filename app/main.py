from puzzle import Puzzle
from solver import Solver
userInput = ""
userData = []
sudokuCSV = []

with open("SudokuSolver\data\sudokuhard.csv", 'r') as filestream:
        for line in filestream:
                currentline = line.split(",")
                sudokuCSV.append(currentline)

# userInput = "904060005068030400203500700350800640600009300009000500700000900000080000005000002"
# for i in range(0, len(userInput)):
#         data = []
#         userData.append(int(userInput[i]))

# puzzle = Puzzle(userData)
# print(puzzle.showPuzzle())
# solver = Solver(puzzle)
# solver.solve()
# # print(puzzle.cells[5].possibleValues)
# print(puzzle.showPuzzle())
# print(puzzle.toString())

totalSolved = 0
totalUnsolved = 0
for i in sudokuCSV:
        if totalSolved % 1 == 0:
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
                # print(puzzle.toString())
print("Total solved: " + str(totalSolved))
print("Total unsovled: " + str(totalUnsolved))

