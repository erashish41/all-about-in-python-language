# Exceptional Handling - ZeroDivisionError, 

# divide by zero
def divide_by_zero(a,b):
    try:
        x = a / b
        return x
    except ZeroDivisionError:
        print("Divide by zero is not allowed")
        return None
print(">>>>1>>>>",divide_by_zero(10, 0))

# # Value Error
# def get_user_input():
#     user_input = input("Enter a number: ")
#     try:
#         num = int(user_input)
#         return num
#     except ValueError:
#         print("Error: can't convert string to integer")
# print(">>>>2>>>>",get_user_input())

def get_error():
    my_list = [1, 2, 3]
    try:
        my_list.remove(3)
    except ValueError:
        print("Item not found")
    return my_list

new_list = get_error()
print(">>>>3>>>> New list:", new_list)


# File Handling Error
def file_handling():
    try:
        with open("data.txt", "r") as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print("File not found")
        return None
    finally:
        print("file operation completed")
print(">>>>>>4>>>>",file_handling())
    
# Type Error
def get_type_error():
    try:
        result =  "hello" + 5
        return result
    except TypeError:
         print("Error: Cannot add string and integer together.")
print(get_type_error())