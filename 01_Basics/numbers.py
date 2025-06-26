#  Python is the language with the most number precisiion capability and it is highly powerful in numbers

x = 2
y = 4
z = 6

# x + y * z   This syntax is not used and appreciated in production code you can proritize some action using the 
# () to that action for example: x + (y * z)
# Another point is that we should operate the same type of datatype of numbers while calculations
# Although they are all numbers but we should use the same type like : float against float. int against int
# And also we can transform one type into another using the built in methods like round int etc
# We also learn about the operator overloading in which if we concatenate some values the language will autmatically
# detect the datatype of one value and autmotically predict the same datatype of the other value 
# Example: 'Anas' + 'Iftikhar' 

#  Individually stored and showed

# If we assign the variable together x , y , z Like this. There result will be shown like the tuples. But you can 
# work with them individually as they are individual variables

# repr() => It is a method of sting representation for the debugging. Show oficial string represntation
#   E.G : print(repr('Anas')) => OUTPUT : 'Anas' With actual quotes
# str() => It is a method of user friendly string representation. For the end users
#   E.G : print(str('Hello')) => OUTPUT : Hello with no quotes
# print() => Simply outputs to the console 
# We can also handle the complex, imaginary numbers in python.


#  Comparions operators (<, > , <=, >=)
#  These return the result in True or False And in python the True is treated as 1 and False as 0. Internally they
# Are treated as numbers
# Chained comparisons : x < y < z "Not a good practice"
#  x < y and y < z "Usually a good pratice than before" Although the first approach is used by the engineers 
# at several instances but the second increase the code readability.  And the second approach is using the 
# logical operator 

#  ALso learnt about the octal, binary, hexa, hexadecimal numbers

# int('64', 8)  Octal 
# int('64', 16)  Hexa decimal
# int('64', 6)  Hex

#  Also got to know about the bitwise operators

#  Now we will jump to the import statements

import random

random.randint(1, 10) 
# Will give us the random number between 1 and 10. Unlike js in which we have to add logic to get a suitable number
l1 = ['lemon', 'Ginger', 'Masala', 'Mint', 'Doodh Patti']
random.choice(l1)
# This random method will give us the random choice from this list or any other values stored
random.shuffle(l1)
#  Use to shuffle the order of values.

# Decimal precision is  problematic in python too for that we import
from decimal import Decimal
#  Decimal('0.1') + Decimal('0.1') + Decimal('0.1') 

from fractions import Fraction
#  We can also import the fractions 
myFra = Fraction(2,7)

#  Sets => {1, 2, 3, 5} => Works in unique values
#  Can perform all the set calculations like union, interection, superset, difference
#  One thing to remember that when we subtract the the set with it's own values it will not give us empty
#  parenthesis, instead it will give us the set() method with now values.
#  Why that happens? Because empty parenthesis => () is dictionary, If you check the type of () you will see yourself
