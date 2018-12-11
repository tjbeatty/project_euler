
"""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""

# Answer = 669171001

# Initialize box size
box_size = 1001

# Initialize count
total = 1
cur_num = 1

# Box size can't be an even number. It will be 1, 3, 5, 7....
# But, the first box is taken care of w/ just a single box/digit (1).
# For box of size 3, we go through the loop once. And each time, we add 2 to the previous number.
# For a box of size 5, we need to loop through twice and the third loop, add 4 to the previous number.
# Etc.
for i in range(2, int(box_size + 1 / 2), 2):

    # Add i four times to previous number
    for j in range(1, 5):
        cur_num += i
        total += cur_num

print(total)