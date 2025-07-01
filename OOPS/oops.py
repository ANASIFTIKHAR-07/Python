"""
- ===============================
- OOP IN PYTHON – INTERVIEW NOTES
- ===============================
-
- 1. Class and Object
-    - Class: Blueprint for creating objects (instances).
-    - Object: Instance of a class.
-    Example:
-        class Car:
-            def __init__(self, brand, model):
-                self.__brand = brand
-                self.__model = model
-        my_car = Car("Toyota", "Corolla")
-
- 2. Encapsulation
-    - Hiding internal data by making attributes private (using __), and providing getter/setter methods.
-    Example:
-        class Car:
-            def __init__(self, brand, model):
-                self.__brand = brand
-            def get_brand(self):
-                return self.__brand
-            def set_brand(self, new_brand):
-                self.__brand = new_brand
-
- 3. Class Variables vs Instance Variables
-    - Class Variable: Shared by all instances (e.g., total_car).
-    - Instance Variable: Unique to each object.
-    Example:
-        class Car:
-            total_car = 0
-            def __init__(self, brand, model):
-                Car.total_car += 1
-
- 4. Inheritance
-    - Creating a new class from an existing class, inheriting its attributes and methods.
-    Example:
-        class ElectricCar(Car):
-            def __init__(self, brand, model, battery_size):
-                super().__init__(brand, model)
-                self.battery_size = battery_size
-
- 5. Polymorphism
-    - Methods with the same name behave differently in different classes.
-    Example:
-        class Car:
-            def fuel_type(self):
-                return "Petrol or Diesel"
-        class ElectricCar(Car):
-            def fuel_type(self):
-                return "Electric Charge"
-
- 6. Class Methods and Self
-    - self: Refers to the current object instance.
-    - Class methods: Functions defined inside a class that operate on its data.
-    Example:
-        class Car:
-            def fullname(self):
-                return f"{self.__brand} {self.__model}"
-
- 7. Static Methods
-    - Does not access instance or class data. Use @staticmethod decorator.
-    Example:
-        class Car:
-            @staticmethod
-            def general_description():
-                return "Cars are general mode of transmission"
-
- 8. @property Decorator
-    - Provides a Pythonic way to use getters/setters.
-    Example:
-        class Car:
-            @property
-            def model(self):
-                return self.__model
-
- 9. Multiple Inheritance
-    - A class can inherit from more than one parent class.
-    Example:
-        class Battery:
-            def battery_info(self):
-                return "This is the battery information"
-        class Engine:
-            def engine_info(self):
-                return "This is the Engine information"
-        class ElectricCar2(Battery, Engine, Car):
-            pass
-        my_new_tesla = ElectricCar2("Tesla", "Model S")
-        print(my_new_tesla.battery_info())
-        print(my_new_tesla.engine_info())
-
- 10. Instance Checking
-     - Use isinstance() to check if an object is an instance of a class.
-     Example:
-         my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
-         print(isinstance(my_tesla, Car))         # True
-         print(isinstance(my_tesla, ElectricCar)) # True
-
- ===============================
- SUMMARY TABLE
- ===============================
- | Concept             | Example/Usage                                  |
- |---------------------|------------------------------------------------|
- | Class/Object        | my_car = Car("Toyota", "Corolla")            |
- | Encapsulation       | self.__brand, get_brand(), set_brand()         |
- | Class Variable      | Car.total_car                                  |
- | Inheritance         | class ElectricCar(Car): ...                    |
- | Polymorphism        | Overriding fuel_type() in child class          |
- | Static Method       | @staticmethod                                  |
- | Property            | @property def model(self): ...                 |
- | Multiple Inheritance| class ElectricCar2(Battery, Engine, Car): ...  |
- | Instance Checking   | isinstance(obj, Class)                         |
-
- Best Practices:
- - Use class variables for data shared by all instances.
- - Use instance variables for data unique to each object.
- - Use encapsulation to protect data.
- - Use inheritance to reuse code.
- - Use polymorphism for flexible code.
- - Use static methods for utility functions.
- - Use properties for controlled attribute access.
- - Use multiple inheritance carefully to avoid complexity.
-
- ===============================
"""

# ===============================
#  Here we will learn about the OOP's in Python. 


#  01 Basic Class and Object : Create a Car class with attributes like brand and model. Then create an instance of this class.





class Car:
    total_car = 0  # Class variable

    def __init__(self, brand, model):
        self.__brand = brand  # Encapsulated (private) attribute
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"
    
    def set_brand(self, new_brand):
        self.__brand = new_brand

#  O2 Class method and Self:  Add a method to the Car that displays the fullname of the car(brand and model)

    def fullname(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are general mode of transmission"
    @property
    def model(self):
        return self.__model

# my_car = Car("Toyotta", "Corolla")

# print(my_car.fullname())
# print(my_car.get_brand())
# print(my_car.model)
# print(Car.general_description())
# Car("Ferrari", "Roma")
#  03 Inheritance : Create an ElectricCar class that inherits from the Car class and has an additional
# attribute battery_size

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) 
        self.battery_size = battery_size
    def specs(self):
        return f"Model: {self.fullname()} - Battery Size: {self.battery_size}"
        # return self.get_brand() For getting the __brand from the get_brand function 
    def fuel_type(self):
        return "Electric Charge"
        


# my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))


# print(my_tesla.fuel_type())
# print(my_tesla.get_brand()) # Output: Toyota
# my_car.set_brand("Honda")
# print(my_car.get_brand()) # Output: Honda
# print(Car.total_car) # Good practice always access these kind of variables by accessing the class directly.

#  04 Encapsulation : Modify the Car class to encapsulate the brand attribute, making it private, and proivde a
#  getter method for it. Have done it on the line no. 11 and 14.


#  05 Polymorphism: Demonstrate Polymorphism by defining a method fuel_type in both Car and ElectriCar classes
#  but with different behaviours 
#  06 Car Variable
#  07 Static Method: Add a static method to the Car class that returns a general description. 




class Battery:
    def battery_info(self):
        return "This is the battery information"

class Engine:
    def engine_info(self):
        return "This is the Engine information"


class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "Model S")

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())