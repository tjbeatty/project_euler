"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
# Answer = 1074

input_str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# --- Prepping the strings to do analysis

# Convert large string to list of lists
input_list = []

# Break up string at new line chars
for item in input_str:
    items = input_str.split("\n")

# Break up string at spaces
for term in items:
    input_list.append(term.split(" "))

# Convert all strings to integers
for i, row in enumerate(input_list):
    for j, col in enumerate(row):
        input_list[i][j] = int(col)

# --- End prepping of string

# Starting at second to last row and working your way backwards...
for i in range(len(input_list) - 2, -1, -1):

    # Move along each item in row and compare the two options to determine which is greater. Save greater value in row.
    for j in range(len(input_list[i])):

        # If moving right is better, save that total sum in this row
        if input_list[i+1][j] > input_list[i+1][j+1]:
            input_list[i][j] += input_list[i+1][j]
        # If moving left is better, save that total sum in this row
        else:
            input_list[i][j] += input_list[i+1][j+1]

# After you have folded the entire triangle into a single value in top row, return value.
print(input_list[0][0])


