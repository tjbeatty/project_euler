'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from math import sqrt


def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(2, int((number - 1) / 2)):
            if number % i == 0:
                return False

        return True


# Input
below_num = 2000000
total = 2

for num in range(3, below_num, 2):
    if is_prime(num):
        total += num

print(total)