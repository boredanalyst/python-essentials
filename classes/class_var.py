
class Fruit():
    freshness = 100

    def __init__(self,name,price,weight,height):
        self.name = name
        self.price = price
        self.weight = weight
        self.height = height

    def decay(self):
        self.freshness -= 10
        print("-------")
        print(f'The fruit {self.name.upper()} decayed by 10 points!')
        print(f'The fruit {self.name.upper()} now has {self.freshness} freshness points!')

strawberry = Fruit("Strawberry",40,0.4,10)

strawberry.decay()

