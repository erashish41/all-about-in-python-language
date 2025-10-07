# comprehensions - List, Dict, Set, Generator

my_list = [2, 3, 5, 7, 12]

# math operation
sqr_list = [i**2 for i in my_list]
print("list sqr math :", sqr_list)

sqr_dict = {x:x**2 for x in my_list}
print("dict 1 :",sqr_dict)

# filter operation
sqr_list_filter = [x**2 for x in my_list if x%2!=0]
print("list sqr filter :", sqr_list_filter)

sqr_dict_filter = {x:x**2 for x in my_list if x%2!=0}
print("dict filter :", sqr_dict_filter)


a = [1, 2, 3]
b = [7, 8, 9]

# parallel iterations
add_list = [(x+y) for (x,y) in zip(a,b)]
print("add 2 lists :", add_list)

# nested iterations
add_nested_list = [(x,y) for x in a for y in b]
print("nested list :",add_nested_list)
print(len(add_nested_list))

new_list = [[10,20,30],[40,50,60],[70,80,90]]
flatted_list = [x for temp in new_list for x in temp]
print("flatted list :", flatted_list)