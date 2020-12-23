class Enemy:
    def __init__(self, name, desc, hp, strength, dexterity, defense, exp, coinL, coinH):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity
        self.defense = defense
        self.exp = exp
        self.coinL = coinL
        self.coinH = coinH
        self.hostile = True

    def lookAt(self):
        print(self.desc)
        if self.hostile == True:
            print("The enemy's hitpoints are at: "+str(self.hp))


jack = Enemy("Jackalope", "It's basically a carnivorous rabbit with sharp teeth and antlers!", 7, 3, 3, 2, 4, 3, 7)
coyote = Enemy("Coyote", "Less dangerous than a wolf, still this canine poses some threat to a lone unarmed human...", 9, 3, 3, 3, 6, 4, 10)
