import rooms as r
import items as it


print("              A Hero's Journey        ")
print("                   v.01")
print("        written by Daniel Rogahn")
print("")
print("")

class Player:
    def __init__(self):
        self.name = ""
        self.hp = 10
        self.maxHp = 10
        self.mp = 2
        self.maxMp = 2
        self.lvl = 1
        self.coins = 10
        self.xp = 0
        self.tNL = 10
        self.strength = 3
        self.dexterity = 3
        self.defense = 3
        self.inventory = []
        self.equip1 = False
        self.weapon = "your Fists"
        self.equip2 = False
        self.armor = "Clothes"
        self.equip3 = False
        self.accessory = "Nothing"

    def add_toInventory(self,item):
        self.inventory.append(item)

    def characterSheet(self):
        print(self.name+ "   ||  Level: "+str(self.lvl)+ " || Experience: "+str(self.xp)+ " of "+str(self.tNL))
        print("    Hitpoints: "+str(self.hp)+" of "+str(self.maxHp)+"  ||  Mana: "+str(self.mp)+" of "+str(self.maxMp) )
        print("Strength: "+str(self.strength)+"  ||  Dexterity: "+str(self.dexterity)+"  ||  Defense: "+str(self.defense))
        print("Wearing "+self.armor+", and wielding "+self.weapon+", and using "+self.accessory+"  with:")
        print(str(self.coins)+" coins in your purse.")

    def inventoryList(self,):
        print("Wearing "+self.armor+", and wielding "+self.weapon+", and using "+self.accessory+"  with:")
        print(str(self.coins)+" coins in your purse.")
        print("You are carrying:")
        i = 0
        while i < len(self.inventory):
            print(self.inventory[i].name)
            i += 1
           
class World:
    def __init__(self):
        self.index = 0
        self.rooms = []
        self.people = []

    def add_room(self,room):
        self.rooms.append(room)

    def add_player(self,player):
        self.people.append(player)

    def walk(self,link):
        self.index = link
        self.rooms[Game.index].describe()
        self.parser()

    def realign(self):
        a = input("press enter")
        self.rooms[Game.index].describe()
        self.parser()

    def get_item(self,ind):
        if self.rooms[self.index].items[ind].mobile == True: 
            self.people[0].add_toInventory(self.rooms[self.index].items[ind])
            self.rooms[self.index].items.pop(ind)
        else:
            print("That cannot be picked up or moved.")
        

    def drop_item(self,ind):
        self.rooms[self.index].add_item(self.people[0].inventory[ind])
        self.people[0].inventory.pop(ind)

    def use(self,item):
        if self.people[0].inventory[item].iskey == True:
            i = 0
            while i < len(self.rooms[self.index].items):
                if self.people[0].inventory[item].locki == self.rooms[self.index].items[item].locki:
                    if self.rooms[self.index].items[item].isopen == False:
                        self.rooms[self.index].items[item].isopen = True
                        print("You turn the key and unlock it.")
                        self.realign()
                    else:
                        print("It's already unlocked.")
                        self.realign()
                i += 1
            self.realign()

    def parser(self):
        cmd = input("What will you do?")
        cmd = cmd.lower()
        if cmd == "?":
            print("Type the name of a direction to move through an exit to another room. Type 'get' followed by the name of the item to pick something up. You can 'look' in a direction or at items and characters. In large areas that are searchable you can type 'search' to trigger an encounter. Type 'stats' to see your character or 'inv' to list your inventory.")
            self.realign()
        if cmd == "q" or cmd == "quit":
            endGame()
        if cmd == "stats":
            self.people[0].characterSheet()
            self.realign()
        if cmd == "inv":
            self.people[0].inventoryList()
            self.realign()
        #movement
        if cmd == "east" or cmd == "e":
            i = 0
            while i < len(self.rooms[self.index].exits):
                if "East" in self.rooms[self.index].exits[i].dir:
                    print("You go East.")
                    self.walk(self.rooms[self.index].exits[i].link)
                i += 1
        if cmd.lower() == "south" or cmd.lower() == "s":
            i = 0
            while i < len(self.rooms[self.index].exits):
                if "South" in self.rooms[self.index].exits[i].dir:
                    print("You go South.")
                    self.walk(self.rooms[self.index].exits[i].link)
                i += 1
        if cmd.lower() == "west" or cmd.lower() == "w":
            i = 0
            while i < len(self.rooms[self.index].exits):
                if "West" in self.rooms[self.index].exits[i].dir:
                    print("You go West.")
                    self.walk(self.rooms[self.index].exits[i].link)
                i += 1
        if cmd.lower() == "north" or cmd.lower() == "n":
            i = 0
            while i < len(self.rooms[self.index].exits):
                if "North" in self.rooms[self.index].exits[i].dir:
                    print("You go North.")
                    self.walk(self.rooms[self.index].exits[i].link)
                i += 1
        # 'take' command
        if "take" in cmd.split():
            tag = cmd.split("take ")
            i = 0
            while i < len(self.rooms[self.index].items):
                if tag[1] in self.rooms[self.index].items[i].ident:
                    self.get_item(i)
                    self.realign()
                i += 1
        # 'drop' command    
        if "drop" in cmd.split():
            tag = cmd.split("drop ")
            i = 0
            while i < len(self.people[0].inventory):
                if tag[1] in self.people[0].inventory[i].ident:
                    self.drop_item(i)
                    self.realign()
                i += 1
        # 'use' command
        if "use" in cmd.split():
            tag = cmd.split("use ")
            i = 0
            while i < len(self.people[0].inventory):
                if tag[1] in self.people[0].inventory[i].ident:
                    self.use(i)
                    self.realign()
                i += 1
        # 'loot' command
        if "loot" in cmd.split():
            i = 0
            while i < len(self.rooms[self.index].items):
                if self.rooms[self.index].items[i].isopen == True:
                    x = 0
                    while len(self.rooms[self.index].items[i].contains) > 0:
                        self.rooms[self.index].add_item(self.rooms[self.index].items[i].contains[0])
                        self.rooms[self.index].items[x].contains.pop(0)
                i += 1
        # 'look' command
        if cmd == "look":
            self.realign()
        if "look" in cmd.split():
            tag = cmd.split("look ")
            if "north" in tag[1]:
                i = 0
                while i < len(self.rooms[self.index].exits):
                    if "North" in self.rooms[self.index].exits[i].dir:
                        self.rooms[self.index].exits[i].lookpeek()
                        self.realign()
                    i += 1
                self.realign()
            if "east" in tag[1]:
                i = 0
                while i < len(self.rooms[self.index].exits):
                    if "East" in self.rooms[self.index].exits[i].dir:
                        self.rooms[self.index].exits[i].lookpeek()
                        self.realign()
                    i += 1
                self.realign()
            if "west" in tag[1]:
                i = 0
                while i < len(self.rooms[self.index].exits):
                    if "West" in self.rooms[self.index].exits[i].dir:
                        self.rooms[self.index].exits[i].lookpeek()
                        self.realign()
                    i += 1
                self.realign()
            if "south" in tag[1]:
                i = 0
                while i < len(self.rooms[self.index].exits):
                    if "South" in self.rooms[self.index].exits[i].dir:
                        self.rooms[self.index].exits[i].lookpeek()
                        self.realign()
                    i += 1
                self.realign()
            i = 0
            while i < len(self.rooms[self.index].items):
                if tag[1] in self.rooms[self.index].items[i].ident:
                    self.rooms[self.index].items[i].examine()
                    self.realign()
                i += 1
            i = 0
            while i < len(self.rooms[self.index].npcs):
                if tag[1] in self.rooms[self.index].npcs[i].name.lower():
                    self.rooms[self.index].npcs[i].lookAt()
                    self.realign()
                i += 1
        # 'talk' command
        if "talk" in cmd.split():
            tag = cmd.split("talk ")
            i = 0
            while i < len(self.rooms[self.index].npcs):
                if tag[1] in self.rooms[self.index].npcs[i].name.lower():
                    self.rooms[self.index].npcs[i].talkTo()
                    self.realign()
                i += 1
        # 'quest' command
        if "quest" in cmd.split():
            tag = cmd.split("quest ")
            i = 0
            while i < len(self.rooms[self.index].npcs):
                if tag[1] in self.rooms[self.index].npcs[i].name.lower():
                    self.rooms[self.index].npcs[i].onQuest()
                    self.realign()
                i += 1
        else:
            print("Please enter a valid command (? for help")
        self.realign()

playerName = input("What is your name?:")
You = Player()
You.name = playerName
Game = World()
Game.add_player(You)
Game.add_room(r.r0)
Game.add_room(r.r1)
Game.add_room(r.r2)
Game.add_room(r.r3)
Game.add_room(r.r4)
Game.add_room(r.r5)
Game.index = 0
Game.rooms[Game.index].describe()
Game.parser()
def endGame():
    print("Thanks for playing!")
