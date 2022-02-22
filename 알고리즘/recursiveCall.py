#n! = n X(n-1)!
# def factorial(num):
#     if num>1:
#         return num * factorial(num - 1)
#     else:
#         return num
    
# for num in range(10):
#     print(factorial(num))


# def factorial(num):
#     if num >= 1:
#         return num
#     return num * factorial(num-1)

def multiple(num):
    if num <= 1:
        return num
    return num * multiple(num-1)

import random
from unittest import result
data = random.sample(range(100),10)


def sum_list(data):
    if len(data) == 1:
        return data[0]
    return data[0] + sum_list(data[1:])

def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

def molela(n):
    if n <= 1:
        return
    if n % 2 ==0:
        print(n)
        molela(n/2)
    else:
        print(n)
        molela(3*n+1)    

def func(data):
    if data ==1:
        return 1
    elif data ==2:
        return 2
    elif data ==3:
        return 4
    
    return func(data-1) + func(data-2) + func(data-3)