


## Class methods + class variables

class Monster():
    category = "monster"
    affiliation = "enemy"
    catch_rate = 0.05
    
    def __init__(self,name,lvl,hp,mp):
        self.lvl = lvl
        self.hp = hp
        self.mp = mp
    
    @classmethod

    def weaken(cls):
        cls.catch_rate += 0.5
        print(f"The monster's catch rate increased by {0.1:.2%}.")
        print(f"The monster has a catch rate of {cls.catch_rate:.2%}!")

    def catch(cls):
        if cls.catch_rate >= 0.30:
            print("The enemy got caught!")
        else:
            print("The enemy did not get caught!")


slime = Monster('slime',5,100,300)

slime.weaken()

slime.catch()