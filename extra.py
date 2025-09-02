#generate Fibonacci number using generator

# def fibonacci():
#     a,b = 0,1
#     while True:
#         yield a
#         a, b = b, a + b
# result = fibonacci()
# print(next(result))
# print(next(result))



def get_fibonacci(n):
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

for num in get_fibonacci(5):
    print(num)

    