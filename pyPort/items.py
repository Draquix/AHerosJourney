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
i5.consumable = True
i5.lowH = 4
i5.highH = 7

i6 = Item("garden", "Your Vegetable Garden", "You grow potatos, zucchini, carrots, and brocolli. All sorts of healthy peasant food.", False)
i6.locki = 666
i6.add_contents(i5)

i7 = Item("rake", "Garden Rake", "A long pole with metal tines at the end, used for gardening.", True)
i7.iskey = True
i7.locki = 666

i8 = Item("pail", "Milk Pail", "A metal bucket you use for milking the goats.", True)
i8.questref = 42

i9 = Item("milk", "Goat's Milk", "Nice and fresh, still a bit warm. Yummy goat's milk- you grew up on this stuff, it's a staple for you.", True)
i9.consumable = True
i9.lowH = 5
i9.highH = 8

i10 = Item("arrow", "Fred's lost arrow", "It's a straight willow shaft with feathers on one end and an iron point on the other. It looks like the ones Fred uses.", True)
i10.questref = 111

i11 = Item("jerky","Deer Jerky", "This aged and dried meat has a smokey flavor and a sweet taste. You buy it often from Fred as you're neighbors.", True)
i11.consumable = True
i11.lowH = 7
i11.highH = 12

i12 = Item("amulet", "Amulet of Jezran", "Hanging on a silver chord, the pupleish disc depicts two outstretched hands.", True)
i12.specref = 1
i12.equipSlot = 3 

i13 = Item("bun", "Hot Bun", "A flaky, fresh baked bun it's about the size of a third of a loaf and would help restore between 5 and 9 hp.", True)
i13.consumable = True
i13.lowH = 5
i13.highH = 9
i13b = Item("bun", "Hot Bun", "A flaky, fresh baked bun it's about the size of a third of a loaf and would help restore between 5 and 9 hp.", True)
i13b.consumable = True
i13b.lowH = 5
i13b.highH = 9

i14 = Item("bread", "Loaf of Bread", "This fluffy bread is plenty big to be a full meal.  It smells freshly baked. It restores between 9 and 15 health.", True)
i14.consumable = True
i14.lowH = 9
i14.highH = 15
i14b = Item("bread", "Loaf of Bread", "This fluffy bread is plenty big to be a full meal.  It smells freshly baked. It restores between 9 and 15 health.", True)
i14b.consumable = True
i14b.lowH = 9
i14b.highH = 15

i15 = Item("mushroom", "Spotted Red-Cap Shroom", "It's on a stalk the length of your hand with a big saucer shaped cap that has the iconic red with white spotted warts. It has value to some.", True)
i15.questref = 123

