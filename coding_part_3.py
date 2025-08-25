#  1.Fibonacci series - sum of the two preceding ones, starting from 0 and 1
# (a, b = b, a + b)

# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
# fibonacci(10)

def fibonacci(n):
    a = 0
    b = 1
    sequence = []
    for i in range(n):
        a, b = b, a + b
        sequence.append(a)
    return sequence
result = fibonacci(10)
print("fibonacci is: ",result)

# Generator (with yield keyword)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)

print(">>>>>> generator test >>>>>")
# with yield generator
def return_evens(lst):
    for l in range(lst + 1):
        if l % 2 == 0:
            yield l

for even in return_evens(10):
    print(even)
print(">>>> generator end >>>")

# Decorator
def my_decorator(func):
    def wrapper():
        print(" Transaction Initialed")
        func()
        print(" Transaction Completed")
        
    return wrapper

@my_decorator
def say_hello():
    print("Hello !")

say_hello()

# Real-world Example: Authentication in Django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def my_view(request):
    return HttpResponse("Hello, this is my first Django response")

print(">>>>>decorator two>>>>")
# or 
def decorator_name(func):
    print("hi decorator")
    def wrapper(*args, **kwargs):
        print("before execute")
        result = func(*args, **kwargs)
        print("after execute")
        return result
    return wrapper

@decorator_name
def add(a,b):
    return a+ b
print(add(9,2))