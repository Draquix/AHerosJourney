class Item:

    def __init__(self,ident,name,desc,mobile):
        self.ident = ident
        self.name = name
        self.desc = desc
        self.mobile = mobile
        self.consumable = False
        self.iskey = False
        self.locki = -1
        self.isopen = False
        self.contains = []
        self.lowH = 0
        self.highH = 0
        self.equipSlot = 0
        self.AC = 0
        self.DC = 0
        self.questref = 0
        self.quantity = 1

    def examine(self):
        print("You examine the "+self.ident+": "+self.desc)

    def add_contents(self,item):
        self.contains.append(item)
    
         


i0 = Item("apple", "Shiny Red Apple", "A shiny bright red apple that looks good to eat. Food aids in healing.", True)
i0.consumable = True
i0.lowH = 4
i0.highH = 6

i1 = Item("key", "Chest Key", "A small brass key that goes to your father's warchest.", True)
i1.iskey = True
i1.locki = 1234

i2 = Item("jerkin", "Leather Jerkin", "A hardened leather suit that offers a little protection in a fight. It belonged to your father.", True)
i2.equipSlot = 1
i2.AC = 1

i3 = Item("wooden", "Wooden Sword", "It's not meant to inflict much more damage than your fists, but it will help you train and do a little more damage.", True)
i3.equipSlot = 2
i3.DC = 1

i4 = Item("chest", "War Chest", "Your father was a soldier long ago... This chest holds some of his belongings. If it was open you could 'loot' it.", False)
i4.locki = 1234
i4.add_contents(i2)
i4.add_contents(i3)

i5 = Item("vegetables", "Fresh Vegetables", "There's two carrots, a zucchini, and a potato... with some meat and milk it'd make a good stew.",True) 

i6 = Item("garden", "Your Vegetable Garden", "You grow potatos, zucchini, carrots, and brocolli. All sorts of healthy peasant food.", False)
i6.locki = 666
i6.add_contents(i5)

i7 = Item("rake", "Garden Rake", "A long pole with metal tines at the end, used for gardening.", True)
i7.iskey = True
i7.locki = 666

i8 = Item("pail", "Milk Pail", "A metal bucket you use for milking the goats.", True)
i8.questref = 42
