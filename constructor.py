class Person:
    def __init__(self, name, age):
        self.first_name = name
        self.my_age = age
        
    def show_info(self):
        return (f"I am {self.first_name} my age is {self.my_age}")
    
p1 = Person("Ashish", 31)
p2 = Person("Rajat", 29)

print(p1.show_info())
print(p2.show_info())
