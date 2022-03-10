import random
from collectingloot import add_to_inv
from collectingloot import item_counter


# Postaci uczestniczące w walce:

class Character:
    def __init__(self, attack, defence, power, hp):
        self.attack = attack
        self.defence = defence
        self.power = power
        self.hp = hp

    def attack_enemy(self, who):
        print(f"{self} attacks {who}.")
        who.hp = who.hp - ((self.power * self.attack) / who.defence)
        print(f"{who} left: {round(who.hp,2)} hp")

    def special_skill(self):
        pass


class Tank(Character):
    eq = {"gold coins": 58, "arrows": 120, "silver coins": 12, "dagger": 2, "boots": 4}

    def __str__(self):
        return f"{self.__class__.__name__}"

    def __init__(self, attack, defence, power, hp):
        super().__init__(attack, defence, power, hp)

    def special_skill(self):
        self.hp += 350
        return f"Knight treats the wounds. Hp: {round(self.hp, 2)}"




class Sorcerer(Character):
    def __str__(self):
        return f"{self.__class__.__name__}"

    def __init__(self, attack, defence, power, hp, special_meter):
        super().__init__(attack, defence, power, hp)
        self.special_meter = special_meter

    def special_skill(self):
        print("Mage's fireball deal 1000 damage.")
        monster.hp = monster.hp - 1000
        return f"{monster} left: {round(monster.hp,2)} hp"


class Bowman(Character):
    def __str__(self):
        return f"{self.__class__.__name__}"

    def __init__(self, attack, defence, power, hp, special_meter):
        super().__init__(attack, defence, power, hp)
        self.special_meter = special_meter

    def special_skill(self):
        print("Archer's precision arrow deal 700 damage.")
        monster.hp = monster.hp - 700
        return f"{monster} left: {round(monster.hp,2)} hp"


class Monster(Character):
    eq = ["gold coins", "small sapphire", "gold coins",
                   "dragons tongue", "dragons scales", "gold coins", "dragons claws"]

    def __str__(self):
        return f"{self.__class__.__name__}"

    def __init__(self, attack, defence, power, hp):
        super().__init__(attack, defence, power, hp)



# Obiekty jako gotowa postać:

knight = Tank(100, 400, 200, 2500)
mage = Sorcerer(400, 200, 700, 800, 0)
archer = Bowman(200, 200, 400, 1100, 0)
monster = Monster(250, 500, 500, 5000)


# Jedna runda
def fight():

    print(f"The next round begins.")

    knight.attack_enemy(monster)
    mage.attack_enemy(monster)
    mage.special_meter += 1
    archer.attack_enemy(monster)
    archer.special_meter += 1

    if mage.special_meter == 3:
        mage.special_skill()
        mage.special_meter = 0

    if archer.special_meter == 4:
        archer.special_skill()
        archer.special_meter = 0

    a = random.randint(1, 20)
    if a in range(1, 18):
        monster.attack_enemy(knight)
    elif a == 19:
        monster.attack_enemy(mage)
    elif a == 20:
        monster.attack_enemy(archer)

    print("\n")

# Rycerz potrafi się leczyć -> linie 28 - 30 :

    if knight.hp < 1500:
        knight.special_skill()

# Drużyna walczy w pętli tak długo aż jeden z bohaterów nie padnie


while knight.hp > 0 and mage.hp > 0 and archer.hp > 0 and monster.hp > 0:

    fight()

# Jeśli wygra drużyna, zabiera ekwipunek potwora

    if monster.hp <= 0:
        print(f"The team won against {monster} and collected his loot: {monster.eq} \n")
        add_to_inv(monster.eq, knight.eq)
        print(item_counter(knight.eq))
        break
    elif knight.hp < 1 or mage.hp < 1 or archer.hp < 1 or monster.hp < 1:
        print("The enemy won")
        break