'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
# Answer = 1366

# Inputs
number = 2 ** 1000

# Initialize
total = 0

# Convert to string so we can loop through digits
num_str = str(number)

# For each digit, convert to int, then add to total
for i in range(len(num_str)):
    total += int(num_str[i])

print(total)