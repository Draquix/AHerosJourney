import items as it

class NPC:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.questdone = False
        self.questdesc = ""
        self.dialogue = ""
        self.reward = []
        self.questref = 0
        self.questamt = 1
        self.questCount = 0
        self.hostile = False
        self.shop = False

    def add_item(self, item):
        self.reward.append(item)

    def talkTo(self):
        print(self.dialogue)

    def lookAt(self):
        print(self.desc)
        if self.hostile == True:
            print("The enemy's hitpoints are at: "+self.hp)

    def onQuest(self):
        if self.questdone == False:
            print(self.questdesc)
                
        if self.questdone == True:
            print(self.name + " doesn't require anything else of you.")

class Shopkeeper(NPC):
    def __init__(self, name, desc, salespitch):
        self.name = name
        self.desc = desc
        self.salespitch = salespitch
        self.wares = []
        self.prices = []
        self.shop = True
        self.reward = []

    def stock(self,item):
        self.wares.append(item)

npc1 = NPC("Emmie", "Emmie is your female goat. You've had her for years, and practically grew up on her milk. She is a tan color with a white blaze on her chest.")
npc1.questdesc = "She bleats plaintively... she probably wants to be milked- if only you had your milk pail you could 'use' it."
npc1.dialogue = "Bleat, bleat!"
npc1.questref = 42
npc1.questamt = 1
npc1.add_item(it.i9)

npc2 = NPC("Fred", "Fred wears dark brown leathers, and a green cloak. He has red hair and a big bushy beard.")
npc2.questdesc = "I need some arrows... find me four, and I'll give you some deer jerky."
npc2.dialogue = "There's been a lot of coyotes in the woods lately, I keep getting attacked to the point that I've shot all my arrows!"
npc2.questref = 111
npc2.questamt = 4
npc2.add_item(it.i11)

npc3 = Shopkeeper("Father Brennan", "A devotee of the goodess of healing, Jezran, he wears yellow robes and has a holy icon hanging around his neck.", "I would be happy to heal you, my child, if you could donate some coins to sustain this chapel...")
npc3.questdesc = "The dead have been restless in the catacombs below.. If you slayed 3 skeletons for me I'd gift to you an amulet of healing."
npc3.dialogue = "I found Jezran when I was but a boy... I'd fallen and skinned my knee and I pedged my soul to make the pain stop and Jezran was there for me."
npc3.questamt = 3
npc3.add_item(it.i12)
npc3.wares = ["Light Healing", "Medium Healing", "Full Healing"]
npc3.prices = [5, 10, 15]
npc3.priest = True

npc4 = Shopkeeper("Margaret Thatcher", "She's a smiling, jovial, rotound woman always wearing her apron with the big heart on it. Her arms are coated in a fine layer of flour.", "I've got today's selection in the case on the counter. I can only bake so much in a day so what's there is all there is.")
npc4.questdesc = "Oh i've no mind for adventures, i just bake and sell my bread."
npc4.stock(it.i13)
npc4.stock(it.i13b)
npc4.stock(it.i14)
npc4.stock(it.i14b)
npc4.prices = [7,7,14,14]