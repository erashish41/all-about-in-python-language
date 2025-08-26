# swap the 2 number
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a, b
print("1:",swap(1,2))
# order of degree: o(1) because of consonant

# swap list
def swap_list(a):
    n = len(a)
    for i in range(n//2):
        temp = a[i]
        a[i] = a[n-i-1]
        a[n-i-1] = temp
    return a
print(swap_list([1, 2, 3, 4, 5]))# order of degree: 0(n)

# add 
def add(a):
    s = 0
    for i in a:
        s = s + i
    return s
a = [1,2,3,45,6]
result = add(a)
print("2:",result)
# order of degree: 0(n)