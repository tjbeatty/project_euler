"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would
be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""


def find_num_div(number):

    # Every number is at least divisible by itself
    num_divisors = 1

    # Create upper limit to check whether its even or odd
    if number % 2 == 0:
        max_div = int(number / 2) + 1
    else:
        max_div = int((number - 1) / 2) + 1

    # Check all numbers from 1 to half of number to check
    for i in range(1, max_div):

        # If number is evenly divisible, add to the list
        if number % i == 0:
            num_divisors += 1

    return num_divisors


triangle_num = 0
j = 1
num_div = 0

# While number of divisors is less than 500, keep trying
while num_div <= 500:
    triangle_num += j
    num_div = find_num_div(triangle_num)
    j += 1


print(triangle_num)
