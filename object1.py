


## Encapsulation 封裝 (使用2個底線)


class Person_age:
    def __init__(self, x, y):
        self.__age = x
        self.__height = y
    
    def add_age(self):
        self.__age += 1
        self.__height -= 1
        return [self.__age, self.__height]
    # def minus_height(self):
    #     self.__height -= 1
    #     return self.__height


new_age = Person_age(26, 170)
new_age.add_age()
# b = new_age.minus_height()
print(new_age.add_age())
