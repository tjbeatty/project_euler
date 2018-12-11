import numpy as np


a = [1, 2, 3, 4, 5]
b = [1, 4, 9, 16, 15]
c = list(set(b) - set(a))
print(c)

my_list = [2, list([1, 4, 5, 7, 9]), list([5, 7, 9]), list([4, 9]), 8, list([1, 4, 9]), 3, list([1, 5, 7]), list([1, 5, 6, 7])]

print(my_list)

k = 8

other_pos = []
for i, item in enumerate(my_list):
    if i == k:
        pass
    else:
        if type(item) is list:
            for j in item:
                other_pos.append(j)
        else:
            other_pos.append(item)

print(other_pos)
print(my_list[k])

poss = set(my_list[k]) - set(other_pos)
print(list(poss)[0])