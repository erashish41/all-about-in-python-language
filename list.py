#       L I S T
# 1. Find the Maximum Number
number_list = [1111, 22, 386, 10345, 14, 95, 76, 707, 83, 99, 1, 415]

def get_max_number(number_list):
    max_number = number_list[0]
    for max in number_list:
        if max > max_number:
            max_number = max
    return max_number

result = get_max_number(number_list)
print(result)

# 2. Find all pairs with given sum
num_list = [1,5,2,7,9,4,6,5]
total_sum = 10
result = []
def get_all_pair_sum(data):
    n = len(data)
    for i in range(n):
        for j in range(i+1, n):
            if (data[i] + data[j]) == total_sum:
                result.append((data[i], data[j]))
    return result
final_result = get_all_pair_sum(num_list)
print(">>>>>2>>> : ", final_result)

# or without function
total_sum = 11
n = len(num_list)
for i in range(n):
    for j in range(i+1, n):
        if (num_list[i] + num_list[j]) == total_sum:
            print(num_list[i], num_list[j])
            
            
            
# sort list
ll = [[10,20,30], [40,50,60],[70,80,90]]
def nested_ll(data):
    for l in data:
        for x in l:
            print(x, end="  ")
result = nested_ll(ll)
print(">>>>2>>>>",result)

# sort list without using sort keyword
list = [5, 2, 9, 1, 7,345,21]
def get_sorted_list(list):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
result = get_sorted_list(list)
print(">>>>>>>3>>>>>> ace: ",result)



# 3. find sum of all prime number btw 0 and N
# data = [1,2,3,4,5,6,7,8,9,10]

def get_prime_number(data):
    for num in range(2, data):
        if (data % num == 0):
            return False
    return True

def add_prime(data):
    total = 0
    for num in range(2, data + 1):
        if (get_prime_number(num)):
            total += num
    return total
print(add_prime(data=10))

# or 
def get_prime(data):
    total = 0
    for num in range(2, data + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if (num % i == 0):
                is_prime = False
                break
        if is_prime:
            total += num
    return total
print(get_prime(12))

print(">>>>test111>>" )
# with list
def get_sum_of_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if (num % i == 0):
            return False
    return True

def get_sum(data):
    total = 0
    for sum in data:
        if (get_sum_of_prime(sum)):
            total += sum
    return total
data = [1,2,3,4,5,6,7,8,9,10,11]
print(get_sum(data))
      
      
# List comprehension
numbers = [1,2,3,4,56,15,2,4,61,9]
# add them
sq = [n**2 for n in numbers ]
print("list comprehension ",sq)

even_cube = [n**3 for n in numbers if n % 2 == 0 ]
print(even_cube)


list1 = [1,2,3]
list2 = [4,5,6]
result1 = list1 + list2
print("added list ",result1)

list1.extend(list2)
print("added new list ", list1)