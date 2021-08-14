

## Inheritance 繼承

class DOG:
    def __init__(self):
        self.name = "machi"
        self.age = 16

    def demo(self):
        self.age += 1
        return self.age

class Jack(DOG):
    pass


doggy = Jack()

print(doggy.demo())
print(doggy.name)
print(doggy.age)