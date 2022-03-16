import random
import time

from collectingloot import add_to_inv
from collectingloot import item_counter
from progressbar import ProgressBar

# Postaci uczestniczące w walce:

class Character:
    def __init__(self, attack, defence, power, hp):
        self.attack = attack
        self.defence = defence
        self.power = power
        self.hp = hp

    def __str__(self):
        return f"{self.__class__.__name__}"

    def attack_enemy(self, who):
        print(f"{self} attacks {who}.")
        who.hp = who.hp - ((self.power * self.attack) / who.defence)
        print(f"{who} left: {round(who.hp,2)} hp")

    def special_skill(self):
        pass


class Tank(Character):
    eq = {"gold coins": 58, "arrows": 120, "silver coins": 12, "dagger": 2, "boots": 4}

    def __init__(self, attack, defence, power, hp):
        super().__init__(attack, defence, power, hp)

    def special_skill(self):
        self.hp += 350
        return f"Knight treats the wounds. Hp: {round(self.hp, 2)}"


class Sorcerer(Character):
    def __init__(self, attack, defence, power, hp, special_meter):
        super().__init__(attack, defence, power, hp)
        self.special_meter = special_meter

    def special_skill(self):
        print("Mage's fireball deal 1000 damage.")
        enemy.hp = enemy.hp - 1000
        print(f" *** {enemy} left: {round(enemy.hp,2)} hp ***")


class Bowman(Character):
    def __init__(self, attack, defence, power, hp, special_meter):
        super().__init__(attack, defence, power, hp)
        self.special_meter = special_meter

    def special_skill(self):
        print("Archer's precision arrow deal 700 damage.")
        enemy.hp = enemy.hp - 700
        print(f" *** {enemy} left: {round(enemy.hp,2)} hp ***")


class Enemy(Character):
    eq = ["gold coins", "small sapphire", "gold coins",
                   "dragons tongue", "dragons scales", "gold coins", "dragons claws"]

    def __init__(self, attack, defence, power, hp):
        super().__init__(attack, defence, power, hp)


# Obiekty jako gotowa postać:

knight = Tank(100, 400, 200, 2500)
mage = Sorcerer(400, 200, 700, 800, 0)
archer = Bowman(200, 200, 400, 1100, 0)
enemy = Enemy(250, 500, 500, 5000)


# Jedna runda
def fight_round(hero_order, enemy):
    print(f"The next round begins.")

    hero_order[0].attack_enemy(enemy)
    hero_order[1].attack_enemy(enemy)
    hero_order[2].attack_enemy(enemy)
    mage.special_meter += 1
    archer.special_meter += 1

    if mage.special_meter == 3:
        mage.special_skill()
        mage.special_meter = 0

    if archer.special_meter == 4:
        archer.special_skill()
        archer.special_meter = 0

    a = random.randint(1, 20)
    if a in range(1, 18):
        enemy.attack_enemy(knight)
    elif a == 19:
        enemy.attack_enemy(mage)
    elif a == 20:
        enemy.attack_enemy(archer)

    print("\n")

# Rycerz potrafi się leczyć -> linie 28 - 30 :

    if knight.hp < 1500:
        knight.special_skill()

# Drużyna walczy w pętli tak długo aż jeden z bohaterów nie padnie

def game():

    kolejnosc = input("Select attack order. 1 - knight, 2 - mage, 3- archer. Ex. 3,1,2: ").split(",")
    time.sleep(1)
    hero_dict = {"1": knight, "2": mage, "3": archer}
    hero_order = []
    for elem in kolejnosc:
        hero_order.append(hero_dict[elem])

    while knight.hp > 0 and mage.hp > 0 and archer.hp > 0 and enemy.hp > 0:

        fight_round(hero_order, enemy)
        time.sleep(1)

    # Jeśli wygra drużyna, zabiera ekwipunek potwora

        if enemy.hp <= 0:
            print(f"The team won against {enemy} and collected his loot: {enemy.eq} \n")
            add_to_inv(enemy.eq, knight.eq)
            print(item_counter(knight.eq))
            break
        elif knight.hp < 1 or mage.hp < 1 or archer.hp < 1 or enemy.hp < 1:
            print("The enemy won")
            break

game()