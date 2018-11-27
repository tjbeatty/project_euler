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


def format_sudoku_matrices(file):
    """
    Format data in three ndarrays - rows, columns, boxes
    :param file: File to be converted
    :return: sudoku_rows, sudoku_columns, sudoku_boxes
    """
    # Open the file

    puzzle_file = open(file, "r")

    sudoku_puzzle = []

    for line in puzzle_file:
        line = line[0:-2].split(",")
        sudoku_puzzle.append(line)

    sudoku_rows = np.matrix(sudoku_puzzle).astype(int)

    sudoku_columns = sudoku_rows.transpose()

    sudoku_boxes = np.ndarray(shape=(3,3), dtype=bytearray)

    for i in range(3):
        for j in range(3):
            sudoku_boxes[i, j] = sudoku_rows[3*i: 3*i + 3, 3*j: 3*j + 3]

    return [sudoku_rows, sudoku_columns, sudoku_boxes]


def init_possible_values():
    """Create a 9 x 9 array of lists 1-9"""
    possibles = np.ndarray(shape=(9, 9), dtype=bytearray)
    for i in range(9):  # Using np.ndarray.fill() didn't work. It would change every instance after
        for j in range(9):
            possibles[i, j] = list(range(1, 10))

    return possibles


def row2col_map(i, j):
    """Map row coordinates to column coordinates"""
    return [j, i]


def col2row_map(i, j):
    """Map column coordinates to row coordinates"""
    return [j, i]


def row2box_map(i, j):
    """Map row coordinates to box coordinates"""
    box_num_x = i // 3
    box_num_y = j // 3
    box_pos_x = i % 3
    box_pos_y = j % 3

    return [box_num_x, box_num_y, box_pos_x, box_pos_y]


def col2box_map(i, j):
    """Map column coordinates to box coordinates"""
    box_num_x = j // 3
    box_num_y = i // 3
    box_pos_x = j % 3
    box_pos_y = i % 3

    return [box_num_x, box_num_y, box_pos_x, box_pos_y]


def box2row_map(box_i, box_j, pos_i, pos_j):
    """Map box coordinates to row coordinates"""
    x_pos = box_i * 3 + pos_i
    y_pos = box_j * 3 + pos_j

    return [x_pos, y_pos]


def box2col_map(box_i, box_j, pos_i, pos_j):
    """Map box coordinates to column coordinates"""
    x_pos = box_j * 3 + pos_j
    y_pos = box_i * 3 + pos_i

    return [x_pos, y_pos]


def check_row(i, j, row_matrix, possibles_matrix):
    """ Check row for values. Remove values from possibles list, if present in row"""
    row_list = row_matrix[i].tolist()

    for item in row_list[0]:
        if item in possibles_matrix[i,j]:
            possibles_matrix[i, j].remove(item)


def check_col(i, j, col_matrix, possibles_matrix):
    """ Check column for values. Remove values from possibles list, if present in column"""
    col_list = col_matrix[j].tolist()

    for item in col_list[0]:
        if item in possibles_matrix[i, j]:
            possibles_matrix[i, j].remove(item)


def check_box(i, j, box_matrix, possibles_matrix):
    """ Check box for values. Remove values from possibles list, if present in box"""

    [box_x, box_y, box_pos_x, box_pos_y] = row2box_map(i, j)
    box_list = box_matrix[box_x, box_y].tolist()
    box_list = box_list[0] + box_list[1] + box_list[2]

    for item in box_list:
        if item in possibles_matrix[i, j]:
            possibles_matrix[i, j].remove(item)


def update_matrices(i, j, row_matrix, column_matrix, box_matrix, possibles):
    """Update all matrices if eliminated all other options"""

    if len(possibles[i, j]) == 1:
        row_matrix[i, j] = possibles[i, j][0]
        column_matrix[j, i] = possibles[i, j][0]

        [box_x, box_y, box_pos_x, box_pos_y] = row2box_map(i, j)
        box_matrix[box_x, box_y][box_pos_x, box_pos_y] = possibles[i, j][0]


def check_one_same(i, j, row_matrix, column_matrix, box_matrix, possibles):
    """"Check col, check row, check box."""
    if row_matrix[i, j] != 0:
        possibles[i, j] = row_matrix[i, j]
    else:
        check_row(i, j, row_matrix, possibles)
        check_col(i, j, column_matrix, possibles)
        check_box(i, j, box_matrix, possibles)

        update_matrices(i, j, row_matrix, column_matrix, box_matrix, possibles)


def check_all_same(row_matrix, column_matrix, box_matrix, possibles):
    """Loop through all rows and columns and check same col, same row, same box."""

    for i in range(9):
        for j in range(9):
            check_one_same(i, j, row_matrix, column_matrix, box_matrix, possibles)


filename = "prob96_files/puzzle_0.csv"

[rows, columns, boxes] = format_sudoku_matrices(filename)

possible_values = init_possible_values()

# print(rows)

print(rows)

while 0 in rows:

    check_all_same(rows, columns, boxes, possible_values)

    print(possible_values)
    print(rows)
