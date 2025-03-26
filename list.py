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