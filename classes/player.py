
class Player:
    def __init__(self, hp=100,lvl=0,str=1,int=1):
        self.hp = hp
        self.lvl = lvl
        self.str = str
        self.int = int

firstPlayer = Player(100,10,10,2)

print(firstPlayer.int)
print(firstPlayer.str)

secondPlayer = Player(hp=200)
print(secondPlayer.hp)
