'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''
# Answer = 906609


def reverse_string(string):
    new_string = ""
    for i in range(len(string), 0, -1):
        new_string += string[i - 1]

    return new_string


# Seed values
num_1 = 999

# Calculated Seeds
num_2 = num_1
factor_less = round(num_1 / 10)
max_same = 0

while num_1 >= factor_less:
    num_2 = num_1
    product = num_1 * num_2
    prod_str = str(product)
    rev_prod = reverse_string(prod_str)
    while prod_str != rev_prod and num_2 > factor_less and product >= max_same:
        print("Num1 = {}, Num2 = {}, Product = {}".format(num_1, num_2, product))
        product = num_1 * num_2
        prod_str = str(product)
        rev_prod = reverse_string(prod_str)

        if prod_str == rev_prod:
            if product >= max_same:
                max_same = product
                print(max_same)
                print(num_1)
                print(num_2)

        num_2 -= 1

    num_1 -= 1
    num_2 = num_1

print(max_same)