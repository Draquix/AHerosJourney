import rooms as r

global location
global index
global move

print("              A Hero's Journey        ")
print("                   v.01")
print("        written by Daniel Rogahn")
print("")
print("")
index = 0
def drawBox(string):
    amt = len(string) + 4
    print("*" * amt)
    print("* " + string + " *")
    print("*" * amt)

def DisplayRoom(index):
    drawBox(r.roomdata[index][0])
    print(r.roomdata[index][1])
    print(r.Navigation(index))
    choice = input("What will you do?")
    ProcessInput(choice)


def ProcessInput(choice):
    global move
    print ("Now in Processing Function")
    if choice == "north" or choice == "n" or choice == "North" or choice == "N":
        if r.linkdata[index][0] > -1:
            print("You go North.")
            index = r.linkdata[index][0]
            print(move)
    if choice == "east" or choice == "e" or choice == "East" or choice == "E":
        if r.linkdata[index][1] > -1:
            print("You go East.")
            index = r.linkdata[index][1]
            print(move)
    if choice == "South" or choice == "south" or choice == "S" or choice == "s":
        if r.linkdata[index][2] > -1:
            print("You go South.")
            index = r.linkdata[index][2]
            print(move)
    if choice == "West" or choice == "west" or choice == "W" or choice == "w":
        if r.linkdata[index][3] > -1:
            print("You go West.")
            index = r.linkdata[index][3]
            print(move)
        else:
            choice = input("Please enter a valid choice.")
            ProcessInput(choice)
    DisplayRoom(index)

DisplayRoom(0)
