# Basic Class And Object
class Car:

    total_car=0

    def __init__(self,model,brand):
        self.__brand=brand
        self.__model=model
        # Class variable
        Car.total_car += 1

# Encapsulation: It does some sort of object private and using def we can access that.
    def get_brand(self):
        return self.__brand + " !"
    
# Polymorphism:
    def fuel_type(self):
        return ("Petrol or Diesel")

# class method and Self
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
# Property Decorators:
    @property
    def model(self):
        return self.__model


# Inheritance
class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return ("Electric Charge")
    
my_machE=Electric_Car("Ford","Mustang_MachE","50kWh")
print(my_machE.full_name())
print(my_machE.fuel_type())
# Class Inheritance and isInstance() function
print(isinstance(my_machE,Car))
print(isinstance(my_machE,Electric_Car))

my_car=Car("Virtus","VW")
print(my_car.get_brand())
# my_car.model="City"
print(my_car.model)
print(my_car.full_name())
print(my_car.fuel_type())
print("Total No. of Cars: " + str(Car.total_car))


# Multiple Inheritance


class Engine:
    def Engine_info(self):
        return "Engine HorsePower is 200HP"


class Battery:
    def Battery_info(self):
        return "Battery Percentage is 60%"


class ElectricCarTwo(Battery, Engine, Car):
    pass

My_New_EV = ElectricCarTwo("Tesla", "Model S")
print(My_New_EV.Engine_info())
print(My_New_EV.Battery_info())