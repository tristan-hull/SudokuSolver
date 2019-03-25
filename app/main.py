from puzzle import Puzzle
from solver import Solver
userInput = ""
userData = []
sudokuCSV = []

with open("SudokuSolver\Data\sudokushort.csv", 'r') as filestream:
        for line in filestream:
                currentline = line.split(",")
                sudokuCSV.append(currentline)

#Used to test a single line
# userInput = "000000050040002000087095000700040009905070310410300027054826790600700005802009000"
# for i in range(0, len(userInput)):
#         data = []
#         userData.append(int(userInput[i]))

# puzzle = Puzzle(userData)
# print(puzzle.showPuzzle())
# solver = Solver(puzzle)
# puzzle = solver.solve()
# print(puzzle.showPuzzle())

totalSolved = 0
totalUnsolved = 0
for i in sudokuCSV:
        print(totalSolved)
        input = []
        for j in i[0]:
                input.append(int(j))
        puzzle = Puzzle(input)
        solver = Solver(puzzle)
        puzzle = solver.solve()
        if puzzle.toString() == i[1][:-1]:
                totalSolved += 1
        else: totalUnsolved += 1

print("Total solved: " + str(totalSolved))
print("Total unsovled: " + str(totalUnsolved))

