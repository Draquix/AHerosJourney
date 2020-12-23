import rooms as r
import items as it
import random
import monsters as mobs

a = random.randint(1,10)
print(str(a))

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
        self.armor = "Clothes"
        self.armorSlot = []
        self.equip2 = False
        self.weapon = "Fists"
        self.weaponSlot = []
        self.equip3 = False
        self.accessory = "Nothing"
        self.accessorySlot = []

    def add_toInventory(self,item):
        self.inventory.append(item)

    def characterSheet(self):
        print(self.name+ "   ||  Level: "+str(self.lvl)+ " || Experience: "+str(self.xp)+ " of "+str(self.tNL))
        print("    Hitpoints: "+str(self.hp)+" of "+str(self.maxHp)+"  ||  Mana: "+str(self.mp)+" of "+str(self.maxMp) )
        print("Strength: "+str(self.strength)+"  ||  Dexterity: "+str(self.dexterity)+"  ||  Defense: "+str(self.defense))
        print("Wearing "+self.armor+", and wielding "+self.weapon+", and using "+self.accessory+"  with:")
        print(str(self.coins)+" coins in your purse.")

    def inventoryList(self):
        print("Wearing "+self.armor+", and wielding "+self.weapon+", and using "+self.accessory+"  with:")
        print(str(self.coins)+" coins in your purse.")
        print("You are carrying:")
        i = 0
        while i < len(self.inventory):
            print(self.inventory[i].name)
            i += 1

    def equipArmor(self,armor):
        self.armorSlot.append(armor)

    def equipWeapon(self, weapon):
        self.weaponSlot.append(weapon)
           
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

    # item use method
    def use(self,item, ind):
        #use of key
        if item.iskey == True:
            i = 0
            while i < len(self.rooms[self.index].items):
                if item.locki == self.rooms[self.index].items[i].locki:
                    while len(self.rooms[self.index].items[i].contains) > 0:
                        msg ="You use the "+item.name+" and the contents are available to take."
                        self.rooms[self.index].add_item(self.rooms[self.index].items[i].contains[0])
                        self.rooms[self.index].items[i].contains.pop(0)  
                i += 1
            print(msg)
            self.realign()              
        #using consumable 
        if item.consumable == True:
            heal = random.randint(item.lowH, item.highH)
            print("You eat the "+item.ident+" and gain back "+str(heal)+" health points.")
            self.people[0].hp += heal
            if self.people[0].hp > self.people[0].maxHp:
                self.people[0].hp = self.people[0].maxHp
            self.people[0].inventory.pop(ind)
            self.realign()
        # trying to 'use' armor, weapon, or accessory
        if item.equipSlot == 1:
            print("You can't exactly 'use' armor, perhaps 'wear' it?")
            self.realign()
        if item.equipSlot == 2:
            print("Rather than try to 'use' a weapon, you must 'wield' it...")
            self.realign()
        #using a quest item
        if item.questref > 0:
            if len(self.rooms[self.index].npcs) > 0:
                if item.questref == self.rooms[self.index].npcs[0].questref: 
                    self.rooms[self.index].npcs[0].questCount += 1
                    msg = "You give the "+item.name+" to "+self.rooms[self.index].npcs[0].name
                    msg += "That's "+str(self.rooms[self.index].npcs[0].questCount)+" so far and they need "+str(self.rooms[self.index].npcs[0].questamt)
                    print(msg)
                    if self.rooms[self.index].npcs[0].questamt == self.rooms[self.index].npcs[0].questCount:
                        msg = "You give the "+item.name+" to "+self.rooms[self.index].npcs[0].name
                        msg += self.rooms[self.index].npcs[0].name+", and in exchange they give you the "+self.rooms[self.index].npcs[0].reward[0].name+"." 
                        self.people[0].add_toInventory(self.rooms[self.index].npcs[0].reward[0])
                        self.rooms[self.index].npcs[0].reward.pop(0)
                        self.rooms[self.index].npcs[0].questdone = True
                        print(msg)
                        self.realign()
                else:
                    print("This item is used in a different quest...")
                    self.realign()
            else:
                print("There's no one here that needs that item.")
                self.realign()
        else:
            print("This is not a quest item.")
            self.realign()
        
# wear armor
    def wear(self, item):
        if len(self.people[0].armorSlot) == 0:
            if self.people[0].inventory[item].equipSlot == 1:
                self.people[0].defense += self.people[0].inventory[item].AC
                self.people[0].armor = self.people[0].inventory[item].name
                self.people[0].equipArmor(self.people[0].inventory[item])
                print("You wear the "+self.people[0].inventory[item].name+".")
                self.people[0].inventory.pop(item)
                self.realign()
            else:
                print("That's not a piece of armor, you can't wear it.")
                self.realign()
        else:
            print("You're already wearing some armor, you should 'remove' it.")
            self.realign()
#wield weapon
    def wield(self, item):
        if len(self.people[0].weaponSlot) == 0:
            if self.people[0].inventory[item].equipSlot == 2:
                self.people[0].strength += self.people[0].inventory[item].DC
                self.people[0].weapon = self.people[0].inventory[item].name
                self.people[0].equipWeapon(self.people[0].inventory[item])
                print("You wield the "+self.people[0].inventory[item].name+".")
                self.people[0].inventory.pop(item)
                self.realign()
            else:
                print("That's not a weapon, so you can't very well wield it.")
        else:
            print("You already have a weapon wielded. You should 'disarm' it before wielding another.")

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
                    #self.people[0].inventory.insert(0, self.people[0].inventory.pop(i))
                    print("about to go use: "+self.people[0].inventory[i].name)
                    self.use(self.people[0].inventory[i],i)
                    self.realign()
                i += 1
        # 'wear' command
        if "wear" in cmd.split():
            tag = cmd.split("wear ")
            i = 0
            while i < len(self.people[0].inventory):
                if tag[1] in self.people[0].inventory[i].ident:
                    self.wear(i)
                    self.realign()
                i += 1
        # 'wield' command
        if "wield" in cmd.split():
            tag = cmd.split("wield ")
            i = 0
            while i < len(self.people[0].inventory):
                if tag[1] in self.people[0].inventory[i].ident:
                    self.wield(i)
                    self.realign()
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
        if cmd == "talk":
            print("Who do you want to talk to?")
            self.realign()
        if "talk" in cmd.split():
            tag = cmd.split("talk ")
            i = 0
            while i < len(self.rooms[self.index].npcs):
                if tag[1] in self.rooms[self.index].npcs[i].name.lower():
                    self.rooms[self.index].npcs[i].talkTo()
                    self.realign()
                i += 1
        # 'quest' command
        if cmd == "quest":
            print("Quest who? Be more specific and name the NPC.")
            self.realign()
        if "quest" in cmd.split():
            tag = cmd.split("quest ")
            i = 0
            while i < len(self.rooms[self.index].npcs):
                if tag[1] in self.rooms[self.index].npcs[i].name.lower():
                    self.rooms[self.index].npcs[0].onQuest()
                    self.realign()
            i += 1
        # 'search command
        if cmd == "search":
            if self.rooms[self.index].searchable == True:
                self.goSearch(self.rooms[self.index].searchI)
            else:
                print("You find nothing more than you saw upon first entering...")  
        if cmd == "attack" and self.rooms[self.index].npcs[0].hostile == True:
            print("You attack aggressively by default, but you can also reposte to be defensive, or strike to be more precise.")     
            self.Attack(1)
        if cmd == "riposte" and self.rooms[self.index].npcs[0].hostile == True:
            print("When reposting you dodge roughly twice as well when the enemy strikes back.")
            self.Attack(2)
        if cmd == "strike" and self.rooms[self.index].npcs[0].hostile == True:
            print("You sacrifice a little power, and defensive abilty to strike with precision to be twice as likely to hit.")
            self.Attack(3) 
        else:
            print("Please enter a valid command (? for help")
        self.realign()
#Processes your attack and their hit back.
    def Attack(self, selector):
        msg = "You swing your "+self.people[0].weapon+" at your opponent and..."
        hitroll = random.randint(1,10)+random.randint(0, self.people[0].dexterity)
        dodgeroll = random.randint(1,10)+random.randint(0, self.rooms[self.index].npcs[0].defense)
        if selector == 3:
            hitroll += random.randint(0, self.people[0].dexterity)
        if hitroll > dodgeroll:
            damroll = random.randint(1,self.people[0].strength)
            if selector == 1:
                damroll += random.randint(1,self.people[0].strength)
            msg += "and you hit the enemy doing "+str(damroll)+" points of damage."
            self.rooms[self.index].npcs[0].hp -= damroll
            if self.rooms[self.index].npcs[0].hp < 1:
                print("You have defeated your opponent.")
                self.battleRewards()
        else:
            msg+= "you missed."
        print(msg)
        msg = "The "+self.rooms[self.index].npcs[0].name+" attacks you!  "
        hitroll = random.randint(1,10)+ random.randint(0,self.rooms[self.index].npcs[0].dexterity) 
        dodgeroll = random.randint(1,10)+random.randint(0, self.people[0].defense)
        if selector == 2:
            dodgeroll += random.randint(0, self.people[0].defense)
        if hitroll > dodgeroll:
            damroll = random.randint(1, self.rooms[self.index].npcs[0].strength)
            msg += "It hits you for "+str(damroll)+" points of damage."
            self.people[0].hp -= damroll
        else:
            msg += "..but it missed."
        print(msg)
        
        if self.people[0].hp < 1:
            print("YOU DIED!! Try again some time.")
            endGame()
#After battle, spoils of victory and popping out dead enemy object
    def battleRewards(self):
        self.people[0].xp += self.rooms[self.index].npcs[0].exp
        msg = "You gained "+str(self.rooms[self.index].npcs[0].exp)+" experience points, and "
        coin = random.randint(self.rooms[self.index].npcs[0].coinL,self.rooms[self.index].npcs[0].coinH)
        self.people[0].coins += coin
        msg += str(coin)+ "coins from the battle."
        print(msg)
        if self.people[0].xp >= self.people[0].tNL:
            self.people[0].tNL = self.people[0].tNL*2.6
            self.people[0].lvl += 1
            self.people[0].dexterity += 1
            self.people[0].strength += 1
            self.people[0].defense += 1
        self.mobRefresh(self.rooms[self.index].npcs[0].name)
        self.rooms[self.index].npcs.pop(0)
        self.realign()

    def mobRefresh(self,name):
        if name == "Coyote":
            mobs.coyote.hp = 9
        if name == "Jackalope":
            mobs.jack.hp = 7
#Searching area event handlers...
    def goSearch(self, searchI):
        #search possibilities for Raiken Woods
        if searchI == 1:
            enc = random.randint(1,5)
            self.rooms[self.index].searchCount += 1
            if enc == 1:
                fate = random.randint(1,3)
                print("You look about in the forest, searching for anything useful, or anything dangerous. You stumble and trip on a root...")
                if fate == 2:
                    print("You land against a chunk of stone causing a bruise and doing 1 point of damage.")
                    self.people[0].hp -= 1
                else:
                    print("But the undergrowth and fallen leaves cushion your landing.")
            if enc == 2:
                self.rooms[self.index].add_item(it.i10)
                print("As you follow a path throught the woods you come across an arrow stuck in a tree.")
            if enc == 3:
                print("A bush rustles, and then you hear the terrible chatter as the antlers hop into view. It's a jackalope!")
                self.rooms[self.index].add_npc(mobs.jack)
            if enc == 4:
                print("A mangy, hungry looking coyote slinks closer and growls at you.")
                self.rooms[self.index].add_npc(mobs.coyote)
            if enc == 5:
                print("A forest faery flits by on gossamer wings, and taps you on the shoulder, imbuing you with a little more health.")
                self.people[0].hp += 1
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
Game.add_room(r.r6)
Game.add_room(r.r7)
Game.add_room(r.r8)
Game.add_room(r.r9)
Game.index = 0
Game.rooms[Game.index].describe()
Game.parser()
def endGame():
    print("Thanks for playing!")
