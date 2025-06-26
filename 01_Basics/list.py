#  We will learn about the lists in this file

food_varieties = ['Desi', 'Italian', 'British', 'American', 'Chinese']

food_varieties[1:2] = ["Mexican"]
# Used to replace the value of index using the slicing, dicing method. If we simply give the value in ""
#  Then each character will be seperately stored as a list as a list.   
# Although this is a confusing syntax to do this task, simply you can use the replace method

for food in food_varieties:
    print(food) 
    print(food, end="-")

if "arabian" in food_varieties:
    print("Arabian food bhi dastyab hy!")

# Because there is no arabian food in the list print will not be shown in the result. To add the arabian in the 
# list we can use the append() method just like in the javascript. It will add in the last
food_varieties.append("Arabian")

food_varieties.pop()
# It wil remove the last value of the list. If we want to remove any specific value in the list we use remove

# food_varieties.remove("British")

food_varieties.insert(1, 'japaneses') 
#  The dedicated method to add the value in the list instead of slicing dicing hack we can use this method.

#  Now the list comprehension
squared_Nums = [x**2 for x in range(10)]
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] So basically we can generate list also like this.
#  This method is used to generate the values in the list using loop

cube_Nums = [y**3 for y in range(10)]
# This will generate cubes of the digits till 9. Why not 10 that's a question and the answer is the exclusivity.