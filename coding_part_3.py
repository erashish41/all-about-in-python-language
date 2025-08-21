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

# with yield generator
def return_evens(lst):
    for l in lst:
        if l % 2 == 0:
            yield l

eggs = [x for x in range(20)]

print(list(return_evens(eggs)))

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