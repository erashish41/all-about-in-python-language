my_list = [1,2,3,4,5,6,7,8]
target = 7
result = []

def get_target_pairs(data,number):
    n = len(data)
    for i in range(n):
        for j in range(i+1, n):
            # print(f"Checking: {data[i]} + {data[j]} = {data[i] + data[j]}")
            print(f"Checking for loop: {data[i]} + {data[j]} = {data[i] + data[j]}")
            if (data[i] + data[j]) == number:
                result.append((data[i], data[j]))
    return result
final = get_target_pairs(my_list,target)
print(final)

# target = 10
# result = []
# def get_target_ten(data, number):
#     n = len(data)
#     for i in range(n):
#         for j in range(i+1, n):
#             if data[i] + data[j] == number:
#                 result.append((data[i], data[j]))
#     return result
# final = get_target_ten(my_list, target)
# print("2", final)