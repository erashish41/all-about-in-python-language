# LF is small anonymous function, define with any number of argument but only one expression.

# filter() - filter when you want to keep only certain elements from a list.
# map() - map when you want to change every element.
# reduce() - reduce when you want to merge all values into a single result.

# filter → even, odd, greater than, less than, etc.
# map → square, cube, add, subtract, multiply, etc.
# reduce → sum all numbers, multiply all numbers, combine all numbers

# basic lambda function
add = lambda a,b: a + b
print(add(5,3))


# Lambda with map
nums = [1,2,3,4]
squ_num = list(map(lambda x:x**2, nums))
print("squ_num: ",squ_num)

# lambda with filter
num = [1,2,3,4,5,6,7,8,9]
even_num = list(filter(lambda x:x%2==0, nums))
print("even_num: ",even_num)

str_length = lambda x: len(x)
print("len: ", str_length("I am Python Language"))

# product odd number
from functools import reduce
product_odd = reduce(lambda a,b: a*b, filter(lambda x: x%2!=0, num))
print(product_odd)

sum_num = reduce(lambda a,b: a+b, nums)
print("sum_num: ", sum_num)

# chained operator
chained_operator = reduce(lambda a,b: a+b, filter(lambda a: a>5, map(lambda a: a*a, num)))
print(chained_operator)
print("-------")


fruits = ['cherry','apple','watermelon','banana','kiwi']
result = sorted(fruits,key= lambda x: len(x),reverse=True)
print(result)


# longest fruit word
longest_fruit = reduce(lambda a,b: a if len(a) > len(b) else b, fruits)
print(longest_fruit)

# find max of list
max_num = reduce(lambda a,b : a if a > b else b, num)
print(max_num)

# add 5 in list
add_5 = list(map(lambda a: a + 5, num))
print(add_5)

# Count Odd Numbers
count_odd = list(filter(lambda a: a%2!=0,num))
print(len(count_odd))

# Convert to Uppercase
convert_Upper = list(map(lambda a: a.upper(), fruits))
print(convert_Upper)

# square only even
squ_even = list(map(lambda a: a**2,filter(lambda a: a%2==0, num)))
print(squ_even)

# sum only even
sum_even = reduce(lambda a,b: a + b, filter(lambda a:a%2==0, num))
print(sum_even)

# sort words
sort_word = sorted(fruits,key=lambda a: len(a), reverse=False)
print(sort_word)

# max
max_with_reduce = reduce(lambda a,b: a if a > b else b, num)
print(max_with_reduce)

# salary after 10% bonus
salaries = [20000, 30000, 25000]
salary_bounce = reduce(lambda a,b: a+b, map(lambda a: a * 1.10, salaries))
print(salary_bounce)
print("-----")


student_info = [
 {"name": "Aman", "marks": 35},
 {"name": "Riya", "marks": 78},
 {"name": "Karan", "marks": 55},
 {"name": "Neha", "marks": 40}
]
# pass students
pass_stud = list(filter(lambda a: a["marks"] >= 40, student_info))
print(len(pass_stud))

pass_student = [s for s in student_info if s["marks"] >= 40]
print("pass_student: ", pass_student)

# add 5 grace mark
add_grace_mark = list(map(lambda a: a["marks"] + 5,student_info))
print(add_grace_mark)

# total marks
total_marks = reduce(lambda a,b: a+b, map(lambda a: a["marks"], student_info))
print(total_marks)

# sort student by marks
sort_marks = sorted(student_info, key=lambda a: a["marks"], reverse=False)
print(sort_marks)