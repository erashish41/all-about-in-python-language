# LF is small anonymous function, define with any number of argument but only one expression.

# basic lambda function
add = lambda a,b: a + b
print(add(5,3))


# Lambda with map
nums = [1,2,3,4]
square = list(map(lambda x:x**2, nums))
print(square)

# lambda with filter
num = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda x:x%2==0, nums))
print(even)