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
# Answer = 142913828922

# Instantiate variables
below_num = 2000000
cur_num = 0
total = 0

# Create a list of length below_num with all switched to "True"
prime_list = [True for i in range(below_num)]

# 0 and 1 are not prime (for final addition)
prime_list[0] = prime_list[1] = False

# Check every position in list
while cur_num < below_num:

    # If a number is prime, every multiple of that will not be. Switch those to "False"
    if prime_list[cur_num]:
        for i in range(cur_num * 2, below_num, cur_num):
            prime_list[i] = False

    cur_num += 1

# Add up all positions with "True"
for i in range(below_num):
    if prime_list[i]:
        total += i

print(total)
