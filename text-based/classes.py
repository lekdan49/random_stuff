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
