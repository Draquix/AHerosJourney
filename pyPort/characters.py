class NPC:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.questdone = False
        self.questdesc = ""
        self.dialogue = ""
        self.questref = 0
        self.questamt = 0

    def talkTo(self):
        print(self.dialogue)

    def lookAt(self):
        print(self.desc)

    def onQuest(self):
        if self.questdone == False:
            print(self.questdesc)
        if self.questdone == True:
            print(self.name + " doesn't require anything else of you.")

npc1 = NPC("Emmie", "Emmie is your female goat. You've had her for years, and practically grew up on her milk. She is a tan color with a white blaze on her chest.")
npc1.questdesc = "She bleats plaintively... she probably wants to be milked- if only you had your milk pail you could 'use' it."
npc1.dialogue = "Bleat, bleat!"
npc1.questref = 42
npc1.questamt = 1

npc2 = NPC("Fred", "Fred wears dark brown leathers, and a green cloak. He has red hair and a big bushy beard.")
npc2.questdesc = "I need some arrows... find me four, and I'll give you some deer jerky."
npc2.dialogue = "There's been a lot of coyotes in the woods lately, I keep getting attacked to the point that I've shot all my arrows!"
npc2.questref = 420
npc2.questamt = 4

