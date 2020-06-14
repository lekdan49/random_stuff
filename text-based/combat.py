class Combat():
    #player_crit_rate = 20
    def __init__(self, player_char, monster, player_crit_rate):
        self.player_char = player_char
        self.monster = monster
        

    def get_combat_input(self):
        choice = input("Do you want to 'attack', 'defend' or try to 'flee'?\n")
        if choice == 'attack':
            self.combat_input = 0
        elif choice == 'defend':
            self.combat_input = 1
        elif choice == 'flee':
            self.combat_input = 2
        else:
            self.combat_input = 5

    
    #@classmethod
    #def set_player_crit(cls, player_crit_rate):
        #cls.player_crit_rate = player_crit_rate
    
