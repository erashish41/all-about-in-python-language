# # 1. find common letter btw 2 strings
# def get_common_letter():
#     str1 = input('enter str1: ')
#     str2 = input('enter str2: ')
#     s1 = set(str1)
#     s2 = set(str2)
#     # print(s1)
#     # print(s2)
#     print(s1&s2)
# get_common_letter()


# def common_letter():
#     result = ""
#     str1 = input("enter str1: ")
#     str2 = input("enter str2: ")
#     for char in str1:
#         if char in str2 and char not in result:
#             result += char
#     print(">>>>>>>", result)
# common_letter()


# # remove duplicate from letter
# def remove_duplicate():
#     str1 = input("enter letter: ")
#     result = ""
#     for letter in str1:
#         if letter not in result:
#             result +=letter
#     print(result)
#     return result
# remove_duplicate()


# def get_remove_duplicate():
#     str1 = input("enter letter: ")
#     str2 = input("enter letter: ")
#     combined = str1 + str2
#     result = ""
#     for letter in combined:
#         if letter not in result:
#             result +=letter
#     print(result)
#     return result
# get_remove_duplicate()

# # to get once letter
# def get_once_letter():
#     str1 = input("enter: ")
#     result = ""
#     for char in str1:
#         if str1.count(char) == 1:
#             result += char
#     print(">>>>>", result)
# get_once_letter()

# # 2. count the frequency of words appear in string
# def count_word_appear():
#     str = input("enter: ")
#     li = str.split()
#     dict = {}
    
#     for word in li:
#         if word not in dict.keys():
#             dict[word] = 0
#         dict[word] += 1
#     print(">>>dict>>>>",dict)
# count_word_appear()
    
# # 3. convert 2 list into dictionary
# def convert_list_to_dict():
#     list1 = ["Ashish", "Rajat", "Sahil"]            
#     list2 = [1234, 4567, 7890]
#     result = dict(zip(list1,list2))
#     print(result)
    
# convert_list_to_dict()

# def convert_dict_to_tuple():
#     dict1 = {'Ashish': 1234, 'Rajat': 4567, 'Sahil': 7890}
#     for i in dict1.items():
#         print(i)
# convert_dict_to_tuple()

# # Find missing number in array
# a = [1,2,6,7]
# def find_missing_number(a):
#     n = a[-1]
#     total = n*(n+1)//2
#     added = sum(a)
#     print(total - added)
# find_missing_number(a)

# def missing_number(a):
#     n = max(a)
#     missing = []
#     for num in range(1, n+1):
#         if num not in a:
#             missing.append(num)
#     return missing
# result = missing_number(a)
# print("result>>>>", result)

# 4. Find Out Pairs with given sum in an array in python of time complexity O(n log n)
def get_two_sum_digit(arr,sum):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while(left <= right):
        if (arr[left] + arr[right]) > sum:
            right = right - 1
        elif (arr[left] + arr[right]) < sum:
            left = left + 1
        elif (arr[left] + arr[right]) == sum:
            print("values of pair are ", arr[left], "&", arr[right])
            right = right - 1
            left = left + 1
        
arr = [5,7,3,4,9,8,19,21]
sum = 17
get_two_sum_digit(arr,sum)