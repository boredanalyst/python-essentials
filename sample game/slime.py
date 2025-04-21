slime = {
    "lvl" : 12,
    "hp" : 120,
    "mp" : 5,
    "str" : 10,
    "int" : 1,
    "luc" : 5,
    "traits" : ["sticky","stuffed body","translucent"]
}

dmg = 0

def slimeAttack():
    dmg = (slime["str"] * 1.1)
    print(f'Slime inflicted {dmg} amount of damage!')

slimeAttack()