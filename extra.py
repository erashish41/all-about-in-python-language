def decorator(func):
    def wrapper():
        print("T I")
        func()
        print(("T C"))
    return wrapper
@decorator
def hello():
    print("T E")
hello()