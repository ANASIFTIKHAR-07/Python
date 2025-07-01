#  Here we will learn about the OOP's in Python. 


#  01 Basic Class and Object : Create a Car class with attributes like brand and model. Then create an instance of this class.




class Car:
    total_car = 0

    def __init__(self ,brand, model):
        self.__brand = brand
        self.model = model
        # self.total_car += 1 For instance variable
        Car.total_car += 1 


    def get_brand(self):
        return self.__brand + "!"
    
    def set_brand(self, new_brand):
        self.__brand = new_brand

#  O2 Class method and Self:  Add a method to the Car that displays the fullname of the car(brand and model)

    def fullname(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are general mode of transmission"

my_car = Car("Toyotta", "Corolla")

print(my_car.fullname())
print(my_car.get_brand())
print(my_car.model)
print(Car.general_description())
Car("Ferrari", "Roma")
#  03 Inheritance : Create an ElectricCar class that inherits from the Car class and has an additional
# attribute battery_size

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) 
        self.battery_size = battery_size
    def specs(self):
        return f" Model : {self.fullname()} -Battery Size : {self.battery_size} "
        # return self.get_brand() For getting the __brand from the get_brand function 
    def fuel_type(self):
        return "Electric Charge"
        

porsche = Car("Porsche", "911 Gt3 Rs")
print(porsche.fuel_type())
my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
print(my_tesla.fuel_type())
print(my_tesla.get_brand()) # Output: Toyota
# my_car.set_brand("Honda")
# print(my_car.get_brand()) # Output: Honda
print(Car.total_car) # Good practice always access these kind of variables by accessing the class directly.

#  04 Encapsulation : Modify the Car class to encapsulate the brand attribute, making it private, and proivde a
#  getter method for it. Have done it on the line no. 11 and 14.


#  05 Polymorphism: Demonstrate Polymorphism by defining a method fuel_type in both Car and ElectriCar classes
#  but with different behaviours 
#  06 Car Variable
#  07 Static Method: Add a static method to the Car class that returns a general description. 


