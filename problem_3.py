'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
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
number = 600851475143

for i in range(2, number):
    if number % i == 0:
        other_num = number / i
        if is_prime(other_num):
            print(other_num)
            break
