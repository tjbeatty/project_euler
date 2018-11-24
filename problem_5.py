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

    # Start at 20 and go down, seeing if the number is divisible by all numbers 1 - 20
    for i in range(20, 1, -1):

        # If number is not divisible by a value, break the loop and start again on next number.
        if number % i != 0:

            # Number will have to be divisible by 20, so only check 20, 40, 60, etc.
            number += seed
            break_flag = 1
            break

    # If the test made it all the way through 20 -> 1, print the number and stop loop
    if break_flag == 0:

        print(number)
        flag = 1

