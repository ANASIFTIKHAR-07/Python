#  Here we will learn about the dicitionaries


car_types = {
    "Ford": "Muscle car",
    "Ferrari" : "Sports car",
    "Ford" : "Trucks",
    "Buggati" : "Hyper car"
}

#  Two ways to access the keys of a dict
print(car_types["Buggati"])
print(car_types.get("Ferrari"))
#  Now, if we want to change the value of a key

car_types["Buggati"] = "Exclusive"
print(car_types)

#  Iteration on the dict

for cars in car_types :
    print(cars, car_types[cars])
#  Will print the keys as well as the values of the keys
#  Antoher way to iterate in the dict is :

for key, value in car_types.items() :
    print(key, value)

#  Here, the items() is specific for the dicts in the loops to print the key and valuse together
#  In a dict, a key and it's value together is called a item. So, the items() helps us to iterate each item as a whole
#  So that we don't have to use the previous method. I found this method easier and more convenient that the first one.

if "Buggati" in car_types :
    print("I have buggati")
    #  Conditional rendering

#  We can also find the length of the dict just like the list
print(len(car_types))

#  If we want to add a new item in the dict

car_types["Rolls Royce"] = "Luxury"
car_types["Porche"] = "Dream Car and a sports car"

#  We can also use the pop function in dict, but we have to give it a key because a dict doesn't have a sequence
# like lists

car_types.pop("Ford")
car_types.popitem()

#  In the popitem() we do not have to name the key. It will automatically remove the last item.
#  Now, there is a another method used in the dict, by which we can delete any of the unwanted item from the dict
#  And that is del

del car_types["Ferrari"]

#  To make a copy of the dict, just like the list

car_types_copy = car_types.copy

#  Another reference created for the copy. Although they have same itmes/Values. But in the memory they have 
#  different address.

#  Now, for the nested dict, just like the nested objects in js

car_shop = {
    "Mercedes" : {
        "Model" : "2026",
        "Name" : "G63 AMG",
        "Edition" : "Mansory",
        "Price" : "700K"
    },
    "Porsche" : {
        "Model" : "2026",
        "Name" : "911 GT3 RS",
        "Edition" : "Rs Chrono Package",
        "Price" : "470k"
    },
    
    "Lamborghini" : {
        "Model" : "2026",
        "Name" : "Urus Perfomante",
        "Edition" : "Carbon",
        "Price" : "420k"
    },
    
    "Lamborghini" : {
        "Model" : "2026",
        "Name" : "Revelto",
        "Edition" : "Mansory",
        "Price" : "770k"
    },
    "Toyota" : {
        "Model" : "2026",
        "Name" : "Land Cruiser",
        "Edition" : "Royal",
        "Price" : "120k"
    },
}

#  We can access them by the same .get() method or the [], There is an interesting thing also

car_shop["Lamborghini"]["Model"]
#  We can access the items of the sub-dict

#  Now, if we implement the list comprehension type syntax in dict, we can do that like this:

squredNums = {x: x**2 for x in range(6)}
#  Here we have to give the proper key and it's value unlike list.
#  Now, if we want to clear them

squredNums.clear()
# It will give us empty {}

#  Now, if we want to construct a new dictionary from a list or a variable

cars = ["Buggati" , "Porsche" , "Mercedes" , "BMW"]
default_value = "Love"

new_Dict = dict.fromkeys(cars, default_value)

#  Here we created a dict from two different data types and we can create a dict using this method. Even if we are
#  Not using the different datatypes. 

#  If we do this:

new_Dict = dict.fromkeys(cars, cars)
#  Now, what will happen in this case. In this case: Each key => cars will have all the keys as a value,
#  For example : {
#  "Buggati" : ["Buggati" , "Porsche" , "Mercedes" , "BMW"]
# }
#  This is just a illustration of how it will look when we do such kind of blunders or on purpose.
