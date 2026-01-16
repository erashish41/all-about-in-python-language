# 1. write python function that will reverse a string without using 
# slicing operation or reverse function (moving left → right through the string)
def reverse_string(data):
    result = ""
    for char in data:
        result = char + result
    return result
final_result = reverse_string(data="python")
print(final_result)

# or (moving right → left through the string)
def reverse_string_data(data):
    result = ""
    for char in range(len(data) - 1, -1, -1):
        result += data[char]
    return result
print(reverse_string_data("ashish"))

# new method
given_string = "Python is famous language !"
def reverse_string_left_right(given_string):
    given_list = list(given_string)
    left = 0
    right = len(given_list) - 1

    while left < right:
        given_list[left], given_list[right] = given_list[right], given_list[left]
        left += 1
        right -= 1
        return "".join(given_list)
result = reverse_string_left_right(given_string)
print(result)


# 2. write program to delete all consonants from given strings. "Python and Data Science"
def delete_consonants(data):
    result = ""
    for char in data:
        if char in "aeiouAEIOU" or char == " " or not char.isalpha():
            result += char
    return result
print(delete_consonants(data="Python and Data Science 3"))

# or
def contains_vowels(data):
    vowels = "aeiouAEIOU"
    result = ""
    for char in data:
        if char in vowels:
            result += char
    return result
print(contains_vowels(data="Python and Data Science Python and Data Science"))

# is.alpha() - keeps digits, punctuation, symbols, etc.