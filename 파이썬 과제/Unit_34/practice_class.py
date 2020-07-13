class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print("베기")
            
x = Knight(542.4, 210.3, 38)
print(x.health, x.mana, x.armor)
x.slash()
