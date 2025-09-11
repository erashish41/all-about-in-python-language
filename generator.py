def generator1():
    for i in range(0,5):
        yield i
    
for num in generator1():
    print(num)
print(">>>>>>>1>>>>>>>")



# or
def generator2():
    print("hello ashish")
    yield 4
    
    print("hello rajat")
    yield 6
    
    print("hello Tom")
    yield 8

generator2()