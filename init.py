class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show_info(self):
        print(f"My name is  {self.name} and my age is {self.age}")
        
p1 = Person("Ashish", 31)
p2 = Person("Rajat", 29)

p1.show_info()
p2.show_info()