class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print(f"My name: {self.name} and my age: {self.age}")

p1 = person("Ahmed", 34)

p1.age += 1

p1.myfunc()