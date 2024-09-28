#1. (Easy) Write a recursive function to calculate the factorial of a given number n.
def factorial(n: int):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n -1)
    
# 3. (Easy) Write a recursive function that returns the sum of the digits of a given number
sum_od = 0
def sum_of_digits(n: int):
    if n == 0:
        return 0
    else:
        return sum_od  + n%10 + sum_of_digits(n // 10)


# 4. (Easy) Write a recursive function to calculate x^n (x raised to the power of n).
def calculate_exponent(x: int, n: int):
    """
        pass a positive integer as 'x'l
    """
    if n == 0 or x == 1:
        return 1
    else:
        return x * calculate_exponent(x, (n -1))

# 5. (Easy) Write a recursive function to check if a given string is a palindrome
def is_palindrome(s: str):
    if len(s) == 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# 6. (Easy) Write a recursive function to reverse a string.
def reverse_string(s):
    if len(s) == 1 or len(s) == 0:
        return s
    else: 
        return s[-1] + reverse_string(s[:-1])

# 21. (Easy) Write a recursive function to calculate the sum of all elements in a list.
def sum_in_list(my_list: list):
    if len(my_list) == 0:
        return 0
    else:
        return my_list[0] + sum_in_list(my_list[1:])
mylist = [1,2,3,4]
print(sum_in_list(mylist))

# 24. (Easy) Write a recursive function to count the occurrences of a specific element in a list.
def num_occurences(my_list: list, el):
    if len(my_list) == 0:
        return 0
    else:
        if my_list[0] == el:
            return 1 + num_occurences(my_list[1:], el)
        else:
            return num_occurences(my_list[1:], el)

# 17. (Medium) Write a recursive function to calculate the following arithmetic operations: a+b
def addition(a, b):
    if b == 0:
        return 
    else:
        return addition(a + 1, b - 1)
    
# 19. Write a recursive function to replace each element of an array with the product of all
# other elements without using division operator.
def product_of_all(numbers: list):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] * product_of_all(numbers[1:])
    
def change_value(numbers: str):
    c = 0
    prod = product_of_all(numbers)
    while c < len(numbers):
        numbers[c] = prod
        c += 1
    return numbers
         
    
a = [1,2,3,4,5]
# print(change_value(a))

# 20. Write a recursive function to replace each element of an array with the product of its
# previous elements. Try using the same array.
def replace_with_previous(list: list):
    if len(list) == 1:
        return list[0]

