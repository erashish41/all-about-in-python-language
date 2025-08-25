# 1.write python function that will reverse a string without using slicing operation or reverse function
def reverse_string(data):
    result = ""
    for char in data:
        result = char + result
    return result
final_result = reverse_string(data="python")
print(final_result)

# or 
def reverse_string_data(data):
    result = ""
    for char in range(len(data) - 1, -1, -1):
        result += data[char]
    return result
print(reverse_string_data("ashish"))

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
        


