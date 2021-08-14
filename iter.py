# 請定義 Iterator 物件的類別，完成以下程式

class MyData:
    def __init__(self, max):
        self.n=0
        self.max=max
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.max*2:
            self.n += 2
            return self.n
        else:
            raise StopIteration

a = MyData(5)

print(next(a))
print(next(a))

# for x in MyData(5):
	# print(x)

# 程式要印出 2, 4, 6, 8, 10