'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''
# Answer = 906609


def reverse_string(string):
    """
    Function to return the reverse of the string
    :param string: Any string you want to find the reverse of
    :return: Reversed string
    """
    new_string = ""
    for i in range(len(string), 0, -1):
        new_string += string[i - 1]

    return new_string


# Seed value - Start with the largest three digit number
num_1 = 999
max_same = 0

# Want to stay in three digit numbers. This will serve as the floor to stop
factor_less = round(num_1 / 10)

# Start with two numbers the same. Loop through number 2 until you identify a palindromic number and return. The reduce
# number one and start process over, reversing through number 2. If palindomic number is larger than previous, save new.

while num_1 >= factor_less:

    # Reset two numbers
    num_2 = num_1

    # Initiate product for each loop of num1. Make product a string, and reverse the string.
    product = num_1 * num_2
    prod_str = str(product)
    rev_prod = reverse_string(prod_str)

    # Loop through number 2 until find a palindromic number. Return that palindromic number
    while prod_str != rev_prod and num_2 > factor_less and product >= max_same:
        # print("Num1 = {}, Num2 = {}, Product = {}".format(num_1, num_2, product))
        product = num_1 * num_2
        prod_str = str(product)
        rev_prod = reverse_string(prod_str)

        # If number is palindrome, see if its larger than all the previous ones.
        if prod_str == rev_prod:
            if product >= max_same:

                # If product is larger than previous, save as the largest.
                max_same = product
                # print(max_same)
                # print(num_1)
                # print(num_2)

        # If value is not palindromic, reduce number 2 and try again
        num_2 -= 1

    # Reduce number 1 by one
    num_1 -= 1

print(max_same)