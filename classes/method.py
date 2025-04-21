class Animal:
    def __init__(self,feet,name='cutie'):
        self.feet = feet
        self.name = name
    
    def walk(self):
        print(f'{self.name.title()} walked!')

dog = Animal(4)

print(dog.feet)
print(dog.name)
dog.walk()