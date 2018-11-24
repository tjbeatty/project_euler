"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# Answer = 31875000

goal = 1000

# Since the sum has to be 1000 and each number has to be different, the other two would add up to at least 3,
# so start at 1000 - 3. Loop through numbers reducing by one each time
for c in range(goal - 3, 1, -1):

    # Since the sum has to be 1000 and they all have to be different, the least b can be is 2. Loop up from 2 to
    # 1000 - c - a (which starts at 1)
    for b in range(2, goal - c - 1):

        # Find a given constraints above
        a = goal - c - b

        # If the resulting three yield a pythagorean triplet, return the answer
        if (c**2 == a**2 + b**2) and a < b:
            print("A = {}, B = {}, C = {}".format(a, b, c))
            print(a*b*c)



