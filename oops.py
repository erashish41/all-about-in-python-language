# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
        
#         # init is also called constructor
        
#     def full_name(self):
#         return f"{self.brand} - {self.model}"
        
# # my_car = Car("Toyota", "Corolla")
# # print(my_car.brand)
# # print(my_car.model)
# # print(my_car.full_name())
# # print("-----")

# # my_new_car = Car("Maruti", "Baleno")
# # print(my_new_car.brand)
# # print(my_new_car.model)
# # print(my_new_car.full_name())
# # print("-----")

# # a. Inheritance
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size
        
# my_tesla = ElectricCar("Tesla","Model S","88 kWh")
# print(my_tesla.brand)
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.full_name())


# # b. Encapsulation
# class Car:
#     def __init__(self,brand,model):
#         self.__brand = brand
#         self.model = model
        
#     def full_name(self):
#         return f"{self.__brand} - {self.model}"
    
#     def get_brand(self):
#         return self.__brand + " !"
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.batter_size = battery_size
        
# my_electriccar = ElectricCar("Tesla", "Model S", "80kWh")
# print(my_electriccar.get_brand())


# # c. Polymorphism
# class Car:
#     total_car = 0
    
#     def __init__(self,brand,model):
#         self.__brand = brand
#         self.model = model
#         Car.total_car += 1
        
#     def full_name(self):
#         return f"{self.__brand} - {self.model}"
    
#     def get_brand(self):
#         return self.__brand + " !"
    
#     def fuel_type(self):
#         return ("Petrol or Diesel")
    
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery):
#         super().__init__(brand,model)
#         self.battery = battery
        
#     def fuel_type(self):
#         return ("Electrical Charger")
        
# my_electricCar = ElectricCar("Tesla","Model S", "80kWh")
# print(my_electricCar.get_brand())
# print(my_electricCar.full_name())
# print(my_electricCar.fuel_type())
# print(Car.total_car)
# print("----")

# my_car = Car("Maruti","Baleno")
# print(my_car.model)
# print(my_car.fuel_type())
# print(Car.total_car)

# # d. with general method with @staticmethod
# class Car:
#     def __init__(self,brand,model):
#         self.__brand = brand
#         self.model = model
        
#     def full_name(self):
#         return f"{self.__brand} - {self.model}"
    
#     def get_brand(self):
#         return self.__brand + " !"
    
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     @staticmethod
#     def general_description():
#         return "Car is mode of transport"
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery):
#         super().__init__(brand,model)
#         self.battery = battery
        
#     def fuel_type(self):
#         return "Electric Charge"
        
    
# my_car = Car("Toyota", "Corolla")
# print(my_car.model)
# print(my_car.get_brand())
# print(my_car.full_name())
# print(my_car.fuel_type())
# print(my_car.general_description())
# print("-------")


# my_electriccar = ElectricCar("Tesla","Model s","80kWh")
# print(my_electriccar.model)
# print(my_electriccar.get_brand())
# print(my_electriccar.battery)
# print(my_electriccar.full_name())
# print(my_electriccar.fuel_type())
# print(my_electriccar.general_description())


# # e. with general method with @property
# # property method is used that don't directly change any attribute property
# class Car:
#     def __init__(self,brand,model):
#         self.__brand = brand
#         self.__model = model
        
#     def full_name(self):
#         return f"{self.__brand} - {self.__model}"
    
#     def get_brand(self):
#         return self.__brand + " !"
    
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     @staticmethod
#     def general_description():
#         return "Car is mode of transport"
    
#     @property
#     def get_model(self):
#         return self.__model
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery):
#         super().__init__(brand,model)
#         self.battery = battery
        
    
#     def fuel_type(self):
#         return "Electric Charge"
        
    
# my_car = Car("Toyota", "Corolla")
# my_car.model = "LC"
# print(my_car.get_brand())
# print(my_car.full_name())
# print(my_car.fuel_type())
# print(my_car.general_description())
# print(my_car.get_model)
# print("-------")


# my_electriccar = ElectricCar("Tesla","Model s","80kWh")
# print(my_electriccar.get_brand())
# print(my_electriccar.battery)
# print(my_electriccar.full_name())
# print(my_electriccar.fuel_type())
# print(my_electriccar.general_description())
# print(my_electriccar.get_model)


# # f. class Inheritance and isinstance() function -- check ElectricCar is isinstance() of Car
# class Car:
#     def __init__(self,brand,model):
#         self.__brand = brand
#         self.__model = model
        
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery):
#         super().__init__(brand,model)
#         self.battery = battery
        

# my_electriccar = ElectricCar("Tesla","Model s","80kWh")


# print("-------")
# print(isinstance(my_electriccar,Car))
# print(isinstance(my_electriccar,ElectricCar))

# g. MultiInheritance
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        
        
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCar(Battery,Engine,Car):
    pass

my_electriccar = ElectricCar("Tesla", "Model S")
print(my_electriccar.battery_info())
print(my_electriccar.engine_info())