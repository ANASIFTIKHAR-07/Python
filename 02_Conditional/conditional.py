#  Here we will practice 10 conditional problems. I will try to solve these problems all by myself.
#  Let's start


#  No 1 : Age Group Categorization

#  CHILD (<13), TEENAGER(13-19), ADULT(20-59), SENIOR(60+)




# age = int(input("Enter your age : "))

# if age < 0 or age == 0:
#     print("Age cannot be less than or equal to 0")

# elif  age > 0  and  age < 13 :
#     print("You are a child")
# elif age >=13 and age<=19:
#     print("Your are a teenager")
# elif age >= 20 and age <= 59:
#     print("You are an adult")
# elif age >=60 :
#     print("You are a senior citizen")
# else:
#     print("❌ Invalid input. Please enter numeric digits only.")


#  No 2: Movie Ticket pricing and Wednesday discount

#  Age < 18 : 8$ , Age > 18 : 12$

#  2$ Discount on wednesday for everyone


age = int(input("Enter your age: "))

day = input("Enter the day")

price = 12 if age >= 18 else 8

if day == "Wednesday" :
    price -= 2

print("Ticket price for you is $", price)