#problem Solving Part 2
# 1. Happy Numbers a. https://en.wikipedia.org/wiki/Happy_number
# b. A happy number is a number defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1. An example of a happy number is 19
# c. Write a method that determines if a number is happy or sad

# 2. Prime Numbers
# a. A prime number is a number that is only divisible by one and itself.
# b. Write a method that prints out all prime numbers between 1 and 100

# 3. Fibonacci
# a. A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
# b. Write a method that does the Fibonacci sequence starting at 1
# c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs

# 1.
def get_input():
     return input("Please enter a number to check if its Happy: ")
def run_sequence(num):
    final_num = 0
    temp = None
    for i in range(len(num)):
        if int(num) < 10:
            final_num = int(num[i]) * int(num[i])
        else:
            temp = int(num[i]) * int(num[i])
            final_num += temp
    return final_num
def check_if_happy(final_number, user_number):
    while final_number != 1 and final_number != 4:
        final_number = run_sequence(str(final_number))
    if final_number == 1:
        print(f'{user_number} is a happy number')
    else:
        print(f'{user_number} is not a happy number')
def run_num1():
    user_input = get_input()
    results = run_sequence(user_input)
    check_if_happy(results, user_input)

run_num1()








# 3
def get_input():
    return input("Please enter a starting number to run the Fibonacci sequence")






