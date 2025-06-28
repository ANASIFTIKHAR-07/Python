#  Here we will learn about Python Functions


# 01 Basic function syntax: Find square of a num

from audioop import mul
from re import I


def square_num(number) :
    return number ** 2

# number_input = int(input("Enter you number: "))   

# Result = square_num(number_input)

# print("The square of your number is : ", Result)


#  02 Multiple parameters in the functions: Make a function that takes two numbers and return their sum

# def sum_of_nums(num1, num2):
#     return num1 + num2

# num1_input = int(input("Enter the first number: "))
# num2_input = int(input("Enter the second number: "))

# result = sum_of_nums(num1_input, num2_input)

# print("The sum of your numbers is:", result)


#  03 Polymorphism function: Write a function multiply that multiplies two numbers, but can also accept and multiply strings
#  Python handles polymorphism without any issue, even if it's a string value

def multiply(n1, n2) :
    return n1 * n2


# print(multiply(4, 6))
# print(multiply('5', 6))
# print(multiply(4, '6'))


#  04 Fucnction returning multiple values: The function will return both the area and circumference of the circle given its
#  radius
import math

def area_circumference(radius) :
    area =  math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area , circumference

input = int(input("Enter the radius to do the calculation: "))

a , c = area_circumference(input)

print(f"The Area is: {a:.2f}, The cirumference is: {c:.2f}" )







