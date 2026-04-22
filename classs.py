class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
p1 = person("Alice", 30)
print(p1.introduce())   

print(p1.name)
print(p1.age)   
