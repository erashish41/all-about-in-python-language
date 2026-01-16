# shallow copy- copy.copy()
import copy

given_list = [[1,2], [3,4]]
shallow = copy.copy(given_list)

shallow[0][0] = 99
print("given_list: ",given_list)
print("shallow list",shallow)


# deep copy- copy.deepcopy()

# import copy
given_input_list = [[1,2], [3,4]]

deep = copy.deepcopy(given_input_list)
deep[0][0] = 99

print("given_input_list: ", given_input_list)
print("deep: ", deep)