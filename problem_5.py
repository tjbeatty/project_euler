'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
# Answer = 232792560


# Seed
seed = 20
number = seed
flag = 0

while flag == 0:
    break_flag = 0
    for i in range(20, 1, -1):
        if number % i != 0:
            number += seed
            break_flag = 1
            break

    if break_flag == 0:

        print(number)
        flag = 1

