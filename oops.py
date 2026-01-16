# Inheritance
class Animal:
    def eat(self):
        print(">>> eating")
        
class Dog(Animal):
    def bark(self):
        print(">>> Barking")
        
        
inheritance_result = Dog()
inheritance_result.eat()
inheritance_result.bark()

# Polymorphism
class Animal:
    def sound():
        pass
    
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")
        
        
# animals = [Dog(), Cat()]

# for animal in animals:
#     print(animal.sound())
        
polymorphism_result = Cat()
polymorphism_result.sound()
polymorphism_result.sound()



# Encapsulation
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def data(self):
        print(self.first_name)
     
p = Person("Ashish", "Bhardwaj")
print(p.first_name)