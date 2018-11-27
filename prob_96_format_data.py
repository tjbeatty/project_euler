"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear,
but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called
Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in
such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical
starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary
to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The
complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it
can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""
import numpy as np


# Open the file
filename = "prob96_files/p096_sudoku.txt"
sudoku_puzzles_file = open(filename, "r")

# ---- Prep the data ---- #
lines_all = []

# Read file and break into lines, eliminating all the labels
for line in sudoku_puzzles_file:
    if not line[0:4] == "Grid":
        if line[-1] == '\n':
            lines_all.append(line[0:len(line) - 1])
        else:
            lines_all.append(line)


puzzle_rows_all = []
cur_puz = []

# If we're on a line divisible by 9, write to to all puzzles list
for i, line in enumerate(lines_all):

    cur_puz.append(list(line))

    if (i + 1) % 9 == 0:
        puzzle_rows_all.append(cur_puz)
        cur_puz = []

for i, puzzle in enumerate(puzzle_rows_all):
    file = open("prob96_files/puzzle_{}.csv".format(i), "w")
    for row in puzzle:
        for j in row:
            file.write(j)
            file.write(",")

        file.write("\n")

    file.close()

# for puzzle in puzzle_rows_all:
#     puzz = np.matrix(puzzle)
#     print(puzz)
#     print(puzz.transpose())







# puzzle_columns_all = []
# for puzzle in puzzle_rows_all:
#     cur_puzzle = []
#     for i in range(9):
#         cur_col = []
#         for j in range(9):

