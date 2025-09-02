# dict
marks = {
    "Alice": 88,
    "Bob": 75,
    "Charlie": 92,
    "David": 80
}
def get_dict_sort_by_key(data):
    result = {}
    for i in sorted(data):
        result[i] = data[i]
    return result
final_result = get_dict_sort_by_key(marks)
print(">>>>>>>1>>>>>>",final_result)