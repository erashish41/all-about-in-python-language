# dict
marks = {
    "Alice": 88,
    "Bob": 75,
    "Charlie": 92,
    "David": 80
}

# sort with keys
def get_dict_sort_by_key(data):
    result = {}
    print("hi",sorted(data))
    for i in sorted(data):
        result[i] = data[i]
    return result
final_result = get_dict_sort_by_key(marks)
print(">>>>>>>1>>>>>>",final_result)

# sort using dict comprehension(keys)
sort_by_key = {k: marks[k] for k in sorted(marks)}
print("hi1>>> : ", sort_by_key)

# sort with values
# item[1] - takes the second element/value from each tuple and sort using that.
def get_dict_sort_by_value(data):
    sorted_items = sorted(data.items(), key= lambda item: item[1])
    result = {}
    for k,v in sorted_items:
        result[k] = v
    return sorted_items
final_result = get_dict_sort_by_value(marks)
print(">>>>>>>2>>>>>>",final_result)

# sort using dict comprehension(values)
sort_by_values = {k: v for k,v in sorted(marks.items(), key=lambda item:item[1])}
print("hi2>>> : ",sort_by_values)

# add 2 dict
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 1, "d": 2}

dict1.update(dict2)
print("add dict ",dict1)

merged = {**dict1, **dict2}
print("merged dict ", merged)

added = dict1 | dict2
print(added)