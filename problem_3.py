"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
# Answer = 6857


def is_prime(number):
    if number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(2, int((number - 1) / 2)):
            if number % i == 0:
                return False

        return True


# Seed
seed_number = 600851475143


# Start from 2 and try to divide. If number is evenly divisible, find other factor. If factor is prime, return.
for j in range(2, seed_number):

    if seed_number % j == 0:
        other_num = seed_number / j

        if is_prime(other_num):
            print(other_num)
            break
