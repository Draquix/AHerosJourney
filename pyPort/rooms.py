import items as it
import characters as ch

def drawBox(string):
    amt = len(string) + 4
    print("*" * amt)
    print("* " + string + " *")
    print("*" * amt)

class Room:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.exits = []
        self.items = []
        self.npcs = []
        self.searchable = False
        self.searchi = 0

    def add_exit(self,exit):
        self.exits.append(exit)

    def add_item(self,item):
        self.items.append(item)

    def add_npc(self,npc):
        self.npcs.append(npc)

    def describe(self):
        drawBox(self.name)
        print(self.description)
        if len(self.items) > 0:
            i = 0
            while i < len(self.items):
                print("A "+self.items[i].name+" is here.")
                if self.items[i].isopen == True:
                    print("It is open... you can 'loot' it.")
                i += 1        
        if len(self.npcs) > 0:
            i = 0
            while i < len(self.npcs):
                print(self.npcs[i].name+" stands here.")
                i += 1
        nav ="Exits: "
        i = 0
        while i < len(self.exits):
            nav += self.exits[i].dir + " "
            i += 1
        if self.searchable == True:
            nav += "*Search*"
        print(nav)


class Exit:
    def __init__(self,dir,link,peek):
        self.dir = dir
        self.link = link
        self.peek = peek

    def lookpeek(self):
        print("You look through the exit and see "+ self.peek)
    

r0 = Room("Your House - Living Room","This small room has a few chairs to sit at and a table by the fireplace. There is a door on the east wall adjoining to your bedroom. To the south is the front door that leads outside.")
r0.add_item(it.i0)
r0.add_item(it.i1)
r0e1 = Exit("East", 1, "Bedroom")
r0e2 = Exit("South", 2, "Yard Outside")
r0.add_exit(r0e1)
r0.add_exit(r0e2)

r1 = Room("Your House - Bedroom","Your bed takes up much of the space in here. The door to the living room is back towards the west. A dresser of drawers is along one wall to keep your clothes. A battered chest sits at the foot of your bed containing some belongings of your father's, who was a soldier.")
r1.add_item(it.i4)
r1e1 = Exit("West", 0, "Living Room")
r1.add_exit(r1e1)

r2 = Room("Yard - Outside Your House","The yard outside your house has a stone path running north and south from your front door to the road to the south. A goat pen is to the east, and a small garden takes up the western side of your property.")
r2e1 = Exit("North", 0, "Living Room")
r2e2 = Exit("East", 3, "Goat Pen")
r2e3 = Exit("West", 4, "Garden")
r2e4 = Exit("South", 6, "Street")
r2.add_exit(r2e1)
r2.add_exit(r2e2)
r2.add_exit(r2e3)
r2.add_exit(r2e4)

r3 = Room("Yard - Goat Pen", "Enclosed in a wooden fence is a patch of ground that is home to your two goats, Emmie and Mealy. They bleet happily to see you and nose at your hand looking to get pet, or perhaps just seeing if you have food for them.")
r3.add_npc(ch.npc1)
r3e1 = Exit("West", 2, "Yard")
r3.add_exit(r3e1)

r4 = Room("Yard - Garden", "A silly scarecrow stands in the center of the patch of soil and several rows of vegetables grow here. The weeds are starting to encroach upon the crops... To the north stands your small toolshed, and to the east is the rest of your yard.")
r4.add_item(it.i6)
r4e1 = Exit("North", 5, "Tool Shed")
r4e2 = Exit("East", 2, "Yard")
r4.add_exit(r4e1)
r4.add_exit(r4e2)

r5 = Room("Tool Shed", "This cluttered little shack contains a number of useful items for maintaining your residence and its yard. The tools are either hung on a rack on one side, or leaning up in a corner, or lying on the workbench.")
r5.add_item(it.i7)
r5.add_item(it.i8)
r5e1 = Exit("South", 4, "Garden")
r5.add_exit(r5e1)

r6 = Room("The Main Street - By Your House","This street has very little activity. To the north is your residence and to the south is your neighbor, Fred, who is a hunter. The road runs west towards the town square and east towards Raiken Woods.")
r6e1 = Exit("North", 2, "Your Yard")
r6e2 = Exit("East", 9, "Raiken Woods")
r6e3 = Exit("West", 10, "Main Street")
r6e4 = Exit("South", 7, "Fred's Yard")
r6.add_exit(r6e1)
r6.add_exit(r6e2)
r6.add_exit(r6e3)
r6.add_exit(r6e4)

r7 = Room("Fred's House - The Front Yard", "This yard is somewhat unkempt with random shrubberies growing haphazardly. A smokehouse takes up one corner, there is a tanning rack for deerskins. The door to Fred's house is to the south, and the main street is to the north.")
r7e1 = Exit("North", 6, "Main Street")
r7e2 = Exit("South", 8, "Fred's House")
r7.add_exit(r7e1)
r7.add_exit(r7e2)

r8 = Room("Fred's House - Interior", "This one room building holds Fred's bed, a small table to have meals at, and a fireplace. A bow is propped up in the corner by an empty quiver.")
r8.add_npc(ch.npc2)
r8e1 = Exit("North", 7, "Fred's Yard")
r8.add_exit(r8e1)

r9 = Room("Raiken Woods - Outskirts", "This thick copse of oak trees is home to many forms of wildlife. It is a favorite spot for hunters, as rabbits and deer are plentiful here. Lately a pack of dangerous coyotes have moved in, hassling both the game and the hunters. You can search around if you wish to encounter anything.")
r9e1 = Exit("West", 6, "Main Street")
r9.add_exit(r9e1)
r9.searchable = True
r9.searchi = 1