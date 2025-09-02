# with pre-value or from user input

# 1. Add Two Numbers 
# num1 = float(input("enter first number: "))
# num2 = float(input("enter second number: "))

# sum = num1 + num2 
# print("sum of 2 number are: ", sum)

# 2. find square root(with exponencial)
num = 64
sr = num**(1/2)
print('square root is: ', sr)

# with math module
import math

num_1 = 81
sr_1 = math.sqrt(num_1)
print('square root is: ', sr_1)

# # 3. checks prime number
# num = int(input('enter the number: '))

# if num == 1:
#     print('number is not prime')
# if num > 1:
#     for i in range(2, num):
#         if num % 2 == 0:
#             print('it is not prime number')
#             break
#     else:
#         print('it is prime number')
        
# 4. random number
import random

num = random.randint(1,10)
# print('random number btw 1 to 10 is: ', num)

# # 5. find prime number btw some range(0-100)
# print(">>>>>>>>>>>>5>>>>>>>>>>>")
# lower = int(input('enter lower number: '))
# upper = int(input('enter upper number: '))

# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 print('number is not prime: ', num)
#                 break
#         else:
#             print('number is prime: ', num)
            
# # 6. find Factorial
# num = int(input("Enter number: "))

# if num < 0:
#     print("Factorial of negative numbers is not valid")
# elif num == 0:
#     print("Factorial of 0 is: 1")
# else:
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     print(f"Factorial of {num} is {fact}")

# # with recursion 
# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return ((num)*fact(num-1))
# num = int(input('enter number: '))
# result = fact(num)
# print('factorial of given number is: ', result)

# 7. Fibonacci sequence (0,1,1,2,3,5,8,13)
a = 0
b = 1
num = int(input('enter number: '))
if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,num+1):
        c = a + b
        a = b
        b = c
        print(c)


