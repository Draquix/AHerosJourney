class NPC:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.questdone = False
        self.questdesc = ""
        self.dialogue = ""

    def talkTo(self):
        print(self.dialogue)

    def lookAt(self):
        print(self.desc)

    def onQuest(self):
        if self.questdone == False:
            print(self.questsdesc)
        if self.questdone == True:
            print(self.name + " doesn't require anything else of you.")

npc1 = NPC("Emmie", "Emmie is your female goat. You've had her for years, and practically grew up on her milk. She is a tan color with a white blaze on her chest.")
npc1.questdesc = "She bleats plaintively... she probably wants to be milked- if only you had your milk pail you could 'use' it."
npc1.dialogue = "Bleat, bleat!"
