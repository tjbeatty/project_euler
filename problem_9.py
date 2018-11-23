'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
# Answer = 31875000

goal = 1000

for c in range(goal - 3, 1, -1):
    for b in range(2, goal - c - 1):
        a = goal - c - b
        # print("A = {}, B = {}, C = {}".format(a, b, c))
        # print(a*b*c)
        if c**2 == a**2 + b**2:
            print("A = {}, B = {}, C = {}".format(a, b, c))
            print(a*b*c)



