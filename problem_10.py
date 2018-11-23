"""
PROBLEM:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


"""
RESEARCH: 
In mathematics, the sieve of Eratosthenes is a simple, ancient algorithm for finding all prime numbers up to any given 
limit.

It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the 
first prime number, 2. The multiples of a given prime are generated as a sequence of numbers starting from that 
prime, with constant difference between them that is equal to that prime.[1] This is the sieve's key distinction 
from using trial division to sequentially test each candidate number for divisibility by each prime.[2]

"""
# 20,000 rows = 0.33 seconds
# 200,000 rows = 32.6 seconds
# 400,000 rows = 254 seconds...

import time

start = time.time()

below_num = 400000
nums_to_check = range(2, below_num)
max_to_check = max(nums_to_check)
cur_num = min(nums_to_check)

prime_list = []
total = 0

while cur_num <= max_to_check:

    # print("To Check Pre {}".format(nums_to_check))

    # Add number to prime list
    prime_list.append(cur_num)
    # Create list of all multiples of current number
    more_not_prime = list(range(cur_num, below_num, cur_num))
    # print("More Not Prime = {}".format(more_not_prime))
    # Remove multiples of current number from numbers to check
    nums_to_check = list(set(nums_to_check) - set(more_not_prime))
    # print("To Check Post {}".format(nums_to_check))

    if not nums_to_check:
        break
    else:
        max_to_check = max(nums_to_check)
        cur_num = min(nums_to_check)
        # print(max_to_check)
        # print(cur_num)

end = time.time()

print(end - start)
print(sum(prime_list))
