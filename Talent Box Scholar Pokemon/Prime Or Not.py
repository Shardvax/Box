'''
Write a Python program that takes a number as input from the user
and checks if it is a prime number or not.
A prime number is a number that is only
divisible by 1 and itself.
'''
import math

def is_it_prime(n):
    for i in range(2, int(math.sqrt(n))+1): # 2, 3, 4
        if n %i == 0:
            print("The number you entered was not a prime number.")
        else:
            print("The number you entered was a prime number.")

is_it_prime(15)
