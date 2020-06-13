import random
import math


class Game():
    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence

    def take_damage(self, damage):
        damage_value = (self.health + damage) - self.health
        self.health = self.health - damage
        return(damage_value)


class Monsters():
    def __init__(self, name, health, attack, defence, scare, monster_id, monster_status):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.scare = scare
        self.monster_id = monster_id
        self.monster_status = monster_status    # 0 = dead, 1 = alive

    def take_damage(self, damage):
        damage_value = (self.health + damage) - self.health
        self.health = self.health - damage
        return(damage_value)


def initialize_character():
    # name = input("Please enter your name! ")
    name = 'Dan Gun'
    dan = Game(name, 100, 10, 5)
    return dan


def get_input():
    choice = input("Do you want to 'attack', 'defend' or try to 'flee'?\n")
    if choice == 'attack':
        return 0
    elif choice == 'defend':
        return 1
    elif choice == 'flee':
        return 2
    else:
        return 5


def combat_begin(monster):
    print("A", monster.name, "has appeared!")

    # round monster health up to whole number
    monster.health = math.ceil(monster.health)

    print("The", monster.name, "has", monster.health,
          'health and is about to attack!')

    result = combat_loop(player_char, monster)

    return result


def monster_encounter(player_char):
    monster = Monsters('slime', player_char.health * 2, 20, 40, 20, 1, 1)
    combat_begin(monster)


def monster_encounter_2(player_char):
    monster = Monsters('dragon', player_char.health * 1.2, 20, 40, 20, 2, 1)
    combat_begin(monster)


def combat_loop(player_char, monster):
    if player_char.health > 1 and monster.health > 0:
        player_move = get_input()
        if player_move == 0:
            attack(player_char, monster)
        elif player_move == 1:
            print("You defend! ")
            defend(player_char, monster)
        elif player_move == 2:
            flee(player_char, monster)
            print("You try to flee! ")
        else:
            combat_loop(player_char, monster)

    elif monster.health <= 0:
        print("Monster dead\n")
        monster.monster_status = 0
        return 1

    elif player_char.health <= 0:
        print("dead\n")
        return 0


def crit_test(player_char, monster, damage_given, damage_taken):
    player_crit = random.randrange(1, 10)
    monster_crit = random.randrange(1, 100)

    if player_crit > 5:
        print("You hit a critical strike! \n")
        damage_given = damage_given * 20

    if monster_crit > 80:
        print("The", monster.name, "hits a critical strike! \n")
        damage_taken = damage_taken * 2

    return damage_given, damage_taken


def attack(player_char, monster):
    # calculate damage given to monster
    damage_given = random.randrange(0, player_char.attack)
    # calculate damage taken from monster
    damage_taken = random.randrange(0, player_char.defence)

    damage_given, damage_taken = crit_test(
        player_char, monster, damage_given, damage_taken)    # check for crits
    # apply damage to class through method
    monster.take_damage(damage_given)
    # apply damage to class through method
    player_char.take_damage(damage_taken)

    print("You attack the", monster.name, "for", damage_given, "damage!\n")

    print("The", monster.name, "attacks you for", damage_taken, "damage!\n")
    print("You have", player_char.health, "health remaining.")
    print("The", monster.name, "has", monster.health, "health remaining.")
    combat_loop(player_char, monster)


def defend(player_char, monster):
    monster_choice = random.randrange(1, 100)
    if monster_choice >= 50:
        pass
    pass


def flee(player_char, monster):
    pass


if __name__ == '__main__':

    player_char = initialize_character()

    monster_encounter(player_char)

    monster_encounter_2(player_char)

    print(player_char.health)
