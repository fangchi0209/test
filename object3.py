


## Ploymorphism 多形
## overriding 改寫 & overloading 擴充
## super() 上級的實體化

class CARS:
    def __init__(self):
        self.name = "newnew"
        self.age = 10

    def demo(self):
        self.age += 1

class myCar(CARS):
    def __init__(self, brand):
        # super().__init__()  ##實體化父類別
        self.brand = brand

    # def demo(self):
    #     self.age -= 1

newCar = myCar("toyota")
# newCar.demo()

# print(newCar.brand)
print(newCar.age)