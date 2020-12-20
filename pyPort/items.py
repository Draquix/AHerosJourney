class Item:

    def __init__(self,name,desc,mobile):
        self.name = name
        self.desc = desc
        self.mobile = mobile
        self.iskey = False
        self.locki = -1
        self.isopen = False



Ckey = Item("Chest Key", "A small brass key that goes to your father's warchest.", True)
Ckey.iskey = True
Ckey.locki = 1

WarChest = Item("War Chest", "Your father was a soldier long ago... This chest holds some of his belongings.", False)


