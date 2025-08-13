# with pre-value or from user input
# 1. Add Two Numbers 
# num1 = float(input("enter first number: "))
# num2 = float(input("enter second number: "))

# sum = num1 + num2 
# print("sum of 2 number are: ", sum)

# 2. find square root(with exponensional)
num = 64
sr = num**(1/2)
print('square root is: ', sr)

# with math module
import math

num_1 = 81
sr_1 = math.sqrt(num_1)
print('square root is: ', sr_1)

# 3. checks prime number
num = int(input('enter the number: '))

if num == 1:
    print('number is not prime')
if num > 1:
    for i in range(2, num):
        if num % 2 == 0:
            print('it is not prime number')
            break
    else:
        print('it is prime number')