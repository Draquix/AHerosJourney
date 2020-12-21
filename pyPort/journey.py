import rooms as r


print("              A Hero's Journey        ")
print("                   v.01")
print("        written by Daniel Rogahn")
print("")
print("")

class World:
    def __init__(self):
        self.index = 0
        self.rooms = []

    def add_room(self,room):
        self.rooms.append(room)

    def walk(self,link):
        self.index = link
        self.rooms[Game.index].describe()
        self.parser()

    def realign(self):
        a = input("press enter")
        self.rooms[Game.index].describe()
        self.parser()


    def parser(self):
        cmd = input("What will you do?")
        cmd = cmd.lower()
        if cmd == "?":
            print("Type the name of a direction to move through an exit to another room. Type 'get' followed by the name of the item to pick something up. You can 'peek' in a direction. In large areas that are searchable you can type 'search' to trigger an encounter.")
        if cmd == "q" or cmd == "quit":
            endGame()
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
        else:
            print("Please enter a valid command (? for help")
        self.realign()


def endGame():
    print("Thanks for playing!")
      
Game = World()
Game.add_room(r.r0)
Game.add_room(r.r1)
Game.add_room(r.r2)
Game.add_room(r.r3)
Game.add_room(r.r4)
Game.add_room(r.r5)
Game.index = 0
Game.rooms[Game.index].describe()
Game.parser()

