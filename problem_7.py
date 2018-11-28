"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
# Answer = 104743


# Not the most efficient prime finding algorithm, but it works for this use case.
def is_prime(number):
    if number == 2:
        return True
    elif number % 2 == 0 or number == 0 or number == 1:  # By definition 0 and 1 are not prime
        return False
    else:
        for i in range(2, int((number - 1) / 2)):
            if number % i == 0:
                return False

        return True


count = 0
j = 0

# Run is_prime until it returns True 10,001 times
while count < 10001:
    j += 1
    if is_prime(j):
        count += 1

print(j)
