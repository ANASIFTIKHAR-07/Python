#  Here we will learn about Python Functions


# 01 Basic function syntax: Find square of a num


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
# import math

# def area_circumference(radius) :
#     area =  math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area , circumference

# input = int(input("Enter the radius to do the calculation: "))

# a , c = area_circumference(input)

# print(f"The Area is: {a:.2f}, The cirumference is: {c:.2f}" )


# 05 Defaule Parameter value: Write a function that greets a user. If no name is provided, it should greet with a defaule
# name


# def greet(name = "Anas"):
#     return "Hello, " + name

# print(greet("Ali"))


# 06 Lamda function: Create a lambda function to compute the cube of a number
#  Lamda functions are also known as anonymous function, one liners.

# cube = lambda c: c** 3
# print(cube(5))


#  07 Variable length arguements:

# def sum_all(*args) :
#     print(args) # Returns the arguments in tuple object type
#     for i in args:
#         print(i * 2)
#     return sum(args)

# print(sum_all(1,2,3,4,5))


#  08 ** kwargs multiple keyword values:
#  Create a function that accepts any number of keywoard arguements and prints them in the format key : value.


# def print_kwargs(**kwargs) :
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
    
# print_kwargs(name = "Benten", power = "Omnitrix", enemy = "Wilgax")


#  09 Generate a function with yield
#  Write a generator function thay yields even numbers up to a specified limit


def even_generator(limit) :
    for i in range(2 , limit + 1 , 2):
        yield i
 
for num in even_generator(10):
    print(num)



#  10 Recursive function :  Create a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



