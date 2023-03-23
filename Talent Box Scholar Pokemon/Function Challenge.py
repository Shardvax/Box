'''
Write a Python function that takes in a list of integers and returns the sum of all the even numbers in the list.
For example, sum_even_numbers([1, 2, 3, 4, 5, 6]) should return 12, because 2 + 4 + 6 = 12.
'''

def sum_even_numbers():
    sum = 0
    numbers = [1, 10, 64, 65, 75, 100, 125, 130, 135, 150]
    print("The even numbers are: ")
    for i in numbers: # running through each element in list
        if i %2 == 0: # checking if even
            sum = i+sum
            print(i)

    print("Their sum is " + str(sum))


sum_even_numbers()

# for loop to go through each item

# check if even by using %. % determines remainder. 7%3 = 1 remainder. 6%3 = no remainder

# also use / by 2 to find remainder for each number

# true: add to sum
