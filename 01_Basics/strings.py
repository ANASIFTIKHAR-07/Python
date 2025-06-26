# Here we will learn about the strings in Python.

from shlex import join


chai = 'Masala Chai'
first_char = chai[0] 
print(first_char)

nums = '0123456789'
nums[:]
nums[:7]
nums[0:6]
nums[0:6:2]
# In the last variation the third parameter is to set the hop in the order

userName = "     Muhammad Anas  "
print(userName.strip())
#  Used to remove the unwanted spaces
#  lower(), upper(), replace(), split() used to make a string into a list with actual list like behaviour, find(),
#  count()

chai_Type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"

print(order.format(quantity, chai_Type))

# This works exactly like the string interpolation in javascript. Here it is called order formatting
#  And we can do that using the format method and give the variables in the correct order.  


chai_Variety = ["Masala chai", "Doodh patti", "Ginger chai", "Lemon chai"]

print(" ", join(chai_Variety))
# Join is used to convert the list into an string and the first " " is used to seperate the indexes of list based on
# spaces because i gave a space in it but you can add something else as a seperator for example a "-"

print(len(chai))
# Used to calculate the lenght of the variable a string 

for letter in chai :
    print(letter)
    # Will print the letters of the chai string

chai_Comment = "He said, \"Masala Chai is awesome\" " 
#  OUTPUT: 'He said, "Masala Chai is awesome" '

# chai = r"Masala\nchai" Here the r is used to make the string raw meaning it will print exactly like this.
# Many times used in paths and the URL's
#  chai = r"c:\user\pwd"
# print(chai) Output will be exactly same => 'c:\user\pwd'
#  Window's paths are problematic especially because of the forward slashes\

# print("Masala" in chai) Containing condition for string
