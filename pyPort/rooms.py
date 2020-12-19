class Room:
    name = ""
    desc = ""

roomdata = [
    ["Your Living Room",
    "This small room has a few chairs to sit at and a table by the fireplace. There is a door on the east wall adjoining to your bedroom. To the south is the front door that leads outside."],
    ["Your Bedroom",
    "Your bed takes up much of the space in here). The door to the living room is back towards the west. A dresser of drawers is along one wall to keep your clothes. A battered chest sits at the foot of your bed containing some belongings of your father's, who was a soldier."]
]
linkdata = [
    [-1,1,2,-1],
    [-1,-1,-1,0]
]
def Navigation(index):
    ToGo = "Exits: "
    if linkdata[index][0] > -1:
        ToGo = ToGo + "North "
    if linkdata[index][1] > -1:
        ToGo = ToGo +"East "
    if linkdata[index][2] > -1:
        ToGo = ToGo + "South "
    if linkdata[index][3] > -1:
        ToGo = ToGo + "West"
    return ToGo



