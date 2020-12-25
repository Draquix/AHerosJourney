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
        self.shop = False

    def reInit(self, name, desc, hp, strength, dexterity, defense, exp, coinL, coinH):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity
        self.defense = defense
        self.exp = exp
        self.coinL = coinL
        self.coinH = coinH
        self.shop = False

    def lookAt(self):
        print(self.desc)
        if self.hostile == True:
            print("The enemy's hitpoints are at: "+str(self.hp))


jack = Enemy("Jackalope", "It's basically a carnivorous rabbit with sharp teeth and antlers!", 7, 3, 3, 2, 4, 3, 7)
coyote = Enemy("Coyote", "Less dangerous than a wolf, still this canine poses some threat to a lone unarmed human...", 9, 3, 3, 3, 6, 4, 10)
badger = Enemy("Badger", "It's a furry mammal with sharp teeth and claws that tends to have an angry disposition.", 8,3,4,2,5,4,8)
frimp = Enemy("Forest Imp", "About 3 feet tall with batlike wings, this scaled creature is a form of minor demon that has adapted to live in forests.",12,4,3,4,9,7,14)
cougar = Enemy("Cougar", "This sleek feline is the size of a large dog, but far superior as it is a cat.",10,4,4,3,11,6,13)
bandit = Enemy("Bandit", "He's a grimy looking man who must have been camping out in the woods to hide from the authorities.",12,4,4,4,12,9,17)
spider = Enemy("Giant Spider", "This eight legged monstrosity is covered in course black hairs, it has a cluster of eyes staring at you, and fangs.",11,4,3,3,9,5,10)
skeleton = Enemy("Skeleton", "All bones and sinew it still wears a battered helm and a ragged chainmail shirt, though it no longer has flesh to protect.",14,4,5,4,13,9,20)
