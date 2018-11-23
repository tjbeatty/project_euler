'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
# Answer = 25164150

# Seed
max_num = 100
sum_of_sq = 0
sum_of_num = 0
sq_of_sum = 0

for i in range(1, max_num + 1):
    sum_of_sq += i ** 2
    sum_of_num += i


sq_of_sum = sum_of_num ** 2
diff = sq_of_sum - sum_of_sq

print(diff)