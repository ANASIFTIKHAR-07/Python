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




# age = int(input("Enter your age: "))

# day = input("Enter the day: ").strip().lower()

# price = 12 if age >= 18 else 8

# if day == "wednesday" :
#     price -= 2

# print("Ticket price for you is $", price)

#  No 3: Grade Calculator 

#  A(90-100), B(80-89), C(70-79), D(60-69), F(Below 60)

# nums = int(input("Enter your numbers: "))

# if nums > 100 or nums < 0 :
#     print("Please Enter valid numbers")
#     # exit() => Can also use this method to exit from the program in some cases.
# else:
#     if nums >= 90 and nums <= 100:
#         print("A Grade")
#     elif nums >= 80 and nums <= 89:
#         print("B Grade")
#     elif nums >= 70 and nums <= 79:
#         print("C Grade")
#     elif nums >= 60 and nums <= 69:
#         print("D Grade")
#     else:
#         print("F : You are fail")


#  No 4: Determine if the banana is ripe, overripe or unripe based on it's color:
#   Banana : Green = unripe, Yellow = ripe, Brown = overripe


# color = input("Enter the color of banana: ").strip().lower()

# if color == "yellow":
#     print("The Banana is ripe")
# elif color == "brown":
#     print("The Banana is overripe")
# elif color == "green":
#     print("The Banana is unripe")
# else:
#     print("I think you have entered a wrong color, Please Try Again!")



#  No 5: Weather Activity suggestion

#  Sunny = Go for a walk or Play sports, Rainy = Spend quality or productive time at home, Snowy = Buld a snowman

# weather = input("How's the weather today: ").strip().lower()

# if weather == "sunny":
#     print("Go for a walk or play sports")
# elif weather == "rainy" or weather == "raining":
#     print("Spend some quality or productive time at home")
# elif weather == "snowy" or weather == "snowfall":
#     print("Build a snowman")




#  No 6: Transport suggestion


# distance = int(input("Enter the distance: "))

# if distance <= 3:
#     transport = "walk"
# elif distance > 3 and distance <= 15:
#     transport = "bike"
# else :
#     transport = "car or bus"

# print("AI recommend you the transport of:", transport)


#  No 7: Pet food recommendation based on specie and age of the pet.

pet = input("Which pet do you have: ").strip().lower()
pet_age = float(input("What is the age of you pet: "))

if pet == "dog":
    if pet_age < 2:
        print("Give your dog Farmina N&D Puppy Starter")
    elif pet_age >= 2:
        print("Give your dog Pedigree Adult Dog Dry Food")
elif pet == "cat":
    if pet_age < 2:
        print("Give your cat Tiki cat food or Nature's variety food, To fulfil it's nutrition")
    elif pet_age >=2:
        print("Give your cat Himalya Healthy CAT food adult")
else:
    print("I don't have data for your pet specie")



#  No 8L Leap year finder


year = int(input("Enter the year: "))


if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "Is a leap year")
else:
    print(year, "Is not a leap year")

