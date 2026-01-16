# def my_generator(n):
#     for item in range(n):
#         yield item
# final = my_generator(5)
# print(next(final))
# print(next(final))
# print(next(final))
# print(next(final))
# print(next(final))
# print(">>>>1>>>")


# def new_generator(n):
#     for item in range(n):
#         yield item

# for e in new_generator(5):
#     print(e)
# print(">>>>2>>>")


# def generator1():
#     for i in range(0,5):
#         yield i
    
# for num in generator1():
#     print(num)
# print(">>>>>>>3>>>>>>>")



# # or
# def generator2():
#     print("hello ashish")
#     yield 4
    
#     print("hello rajat")
#     yield 6
    
#     print("hello Tom")
#     yield 8

# generator2()
# print(">>>>>>>4>>>>>>>")



# # a = 10
# # b = 0
# # print(a/b)

try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print(">>>> can't divide by zero")
finally:
    print(">>>> this always runs")


try:
    f = open("file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File Not Found")
finally:
    print("Closing operation done")