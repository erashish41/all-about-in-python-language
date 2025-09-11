nums = [10, 20, 30, 40, 500,900]
iter_nums = iter(nums)
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))

text = "Ashish"
iter_text = iter(text)
print(next(iter_text))
print(next(iter_text))
print(next(iter_text))
print(next(iter_text))
print(next(iter_text))
print(next(iter_text))

# Custom iterator with CBV 
class Counter:
    def __init__(self, count, end):
        self.first_count = count
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.first_count <= self.end:
            val = self.first_count
            self.first_count += 1
            return val
        else:
            raise StopIteration

for num in Counter(0,5):
    print("hi",num)