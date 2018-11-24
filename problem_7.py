'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''
# Answer = 104743


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


count = 0
i = 1

# Run is_prime until it returns True 10,001 times
while count < 10001:
    i += 1
    if is_prime(i):
        count += 1

print(i)