
class Creature():
    def __init__(self,name,lvl,hp,mp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.mp = mp


class Player(Creature):
    def __init__(self,name,lvl,hp,mp,happiness,attribute):
        super().__init__(name,lvl,hp,mp)
        self.happiness = happiness
        self.attribute = attribute
    
    def self_heal(self):
        self.hp += 10
        print(f"{self.name} restored {self.hp} HP!")
    
    def check_ko(self):
        if self.hp <= 0:
            print(f"{self.name} fainted!")

    def self_destruct(self):
        self.hp = 0
        print(f"{self.name} self-destructed!")

class Opponent(Creature):
    
    def __init__(self,name,lvl,hp,mp,category,attribute):
        super().__init__(name,lvl,hp,mp)
        self.category = category
        self.attribute = attribute
    
    def self_ko(self):
        self.hp = 0
        print(f"{self.name} self-destructed!")

slime = Opponent("Slime",5,100,30,"Amorphous","Water")

print(slime.attribute)
print(slime.hp)
print(slime.mp)

slime.self_ko()
print(slime.hp)