#  No 1: Count how many of the values are positive

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_nums_count = 0

for num in numbers:
    if num > 0:
        # print(num)
        positive_nums_count += 1
# print("The positive number count is: ", positive_nums_count)


#  No 2: Sum of even numbers
# n = int(input("Enter the number: "))

# sum_even = 0

# for i in range(1, n + 1):
#     if i%2 == 0:
#         sum_even += i

# print("Sum of even numbers:", sum_even)

# No 3:  Print a numbers table, but remove the 5th iteration.

# num = int(input("Enter your number: "))

# for i in range(1, 11) :
#     if i == 5:
#         continue # skips the 5th iteration 

#     print(num, 'x' ,i, '=', num * i )


#  No 4: Reverse a string using loop


# name = "Python"
# reverse_name = ""

# for char in name:
#     reverse_name = char + reverse_name

# print(reverse_name)

# #  No 5: Find the first non-repeated character

# input_str = "teeter"

# for char in input_str:
#     if input_str.count(char) == 1:
#         print("char is : ", char)
        # break

#  No 6: Find the factorial of a numbers using while loop 

# number = int(input("Enter the number to find the factorial: "))
# factorial = 1

# while number > 0:
#     # factorial = factorial * number
#     factorial *= number
#     number -= 1
# print("The factorial of your number is : ", factorial)


#  No 7: Keep asking the user for input until they enter the value between 1 and 10

while True:
    number= int(input("Enter the number between 1 and 10: "))
    if 1 <= number <= 10 :
        print("Thanks for entering the right number")
        break
    else:
        print("Invalid number try Again!!")

#  No 8: Prime number checker


prime_num = int(input("Enter your number: "))
is_prime = True

if prime_num > 1:
    for i in range(2, prime_num):
        if (prime_num % i) == 0:
            is_prime = False
            break

print(is_prime)

#  No 9: Check if all the elements in the list are unique. If a duplicate is found,exit the loop
# and print the duplicate

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate item :", item)
        break
    unique_item.add(item)

#  No 10: Exponential backoff strategy

import time

max_retries = 5
wait_time = 1
attempts = 0

while attempts < max_retries:
    print("Attempts", attempts + 1, "-wait time", wait_time)
    time.sleep
    wait_time += 2
    attempts += 1





