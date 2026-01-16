# sort list
# is_palindrome

# sort list
def nested_loop():
    for i in range(1,3):
        j = 1
        while j < 3:
            print(i,j)
            j = j + 1
        print('Gfg')
result = nested_loop()
print(">>>>1>>>>",result)

# 
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

list = [5, 2, 9, 1, 7,345,21]
def get_sorted_list(list):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j] < list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
result = get_sorted_list(list)
print(">>>>>>>4>>>>>> dec: ",result)


# is_palindrome with for loop
def get_is_palindrome(str):
    n = len(str)
    for i in range(n//2):
        if str[i] != str[n-i-1]:
            return False
    return True
result = get_is_palindrome("MADAM")
print(">>>>>>>>5>>>>>>", result)

# is_palindrome with while loop
def is_palindrome(str):
    left, right = 0, len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
            left += 1
            right += 1
    return True
result = get_is_palindrome("malayalam")
print(">>>>>>>>6>>>>>>", result)


