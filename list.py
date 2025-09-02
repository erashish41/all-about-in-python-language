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