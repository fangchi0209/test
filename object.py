'''
    物件導向 ＝ 封裝 Encapusulation, 繼承 Inheritance, 多型 Polymorphism
'''

'''
    class Person:
        def __init__(self): # 賦予初始化, 將大類別定義
            self.name = "Adam" # 賦予的值就是屬性 attribute
            self.age = 30

        def demoFunction(self): # 方法 method
            self.age += 1

    # new_person = 實體化
    new_person = Person() #Person() 類別實體化
    new_person.demoFunction()
    print(new_person.age)
'''

class Person:
    def __init__(self, x, y): # 賦予初始化, 將大類別定義
        self.name = x # x 或是賦予的值就是屬性 attribute
        self.age = y

    def demoFunction(self): # 方法 method
        self.age += 1

# new_person = 實體化
# 先有實體才能使用屬性&方法
new_person = Person("demo", 20) #Person() 類別實體化
new_person.demoFunction() # 給予方法

print(new_person.age)