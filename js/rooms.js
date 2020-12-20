var battleOn = false;
var cataQuest = false;
var skeleCount = 0;
var woodsExplore = 0;
var woodsExploreDeep = 0;
var skeleton = false;
var chestOpen = false;
var coyoteQuest = false;
var coyoteCount = 0;
var isCoyote = false;
var deeperSwitch = false;
/*The rooms array contains the display data of the various rooms in the
game, such as the room name, it's description, and it's exits. */
let rooms = [
    {// room index 0 object
        roomName:"Your House - Living Room",
        searchable: false,
        store: -1,
        roomDesc:"This small room has a few chairs to sit at and a table by the fireplace. There is a door on the east wall adjoining to your bedroom. To the south is the front door that leads outside.",
        roomExits: [
            {
                link:1,
                direction: "East"
            },
            {
                link:2,
                direction: "South"
            }
        ]
    },
    {// room index 1 object
        roomName:"Your House - Bedroom",
        searchable: false,
        store: -1,
        roomDesc:"Your bed takes up much of the space in here. The door to the living room is back towards the west. A dresser of drawers is along one wall to keep your clothes. A battered chest sits at the foot of your bed containing some belongings of your father's, who was a soldier.",
        roomExits: [
            {
                link:0,
                direction: "West"
            }
        ]
    },
    {// room index 2 object
        roomName:"Yard - Outside Your House",
        searchable: false,
        store: -1,
        roomDesc:"The yard outside your house has a stone path running north and south from your front door to the road to the south. A goat pen is to the east, and a small garden takes up the western side of your property.",
        roomExits: [
            {
                link:0,
                direction: "North"
            },
            {
                link:3,
                direction: "East"
            },
            {
                link: 4,
                direction: "West"
            },
            {
                link:6,
                direction: "South"
            }
        ]
    },
    { // room index 3 object -- Goat Pen
        roomName:"Yard - Goat Pen",
        searchable:false,
        store: -1,
        roomDesc:"Enclosed in a wooden fence is a patch of ground that is home to your two goats, Emmie and Mealy. They bleet happily to see you and nose at your hand looking to get pet, or perhaps just seeing if you have food for them.",
        roomExits: [
            {
                link: 2,
                direction: "West"
            }
        ]
    },
    {// room index 4 object -- Garden
        roomName: "Yard - Garden",
        searchable: false,
        store: -1,
        roomDesc: "A silly scarecrow stands in the center of the patch of soil and several rows of vegetables grow here. The weeds are starting to encroach upon the crops... To the north stands your small toolshed, and to the east is the rest of your yard.",
        roomExits: [
            {
                link:5,
                direction: "North"
            },
            {
                link: 2,
                direction: "East"
            }
        ]
    },
    { // room index 5 object -- The tool shed
        roomName: "Tool Shed",
        searchable: false,
        store: -1,
        roomDesc: "This cluttered little shack contains a number of useful items for maintaining your residence and its yard. The tools are either hung on a rack on one side, or leaning up in a corner, or lying on the workbench.",
        roomExits: [
            {
                link:4,
                direction: "South"
            }
        ]
    },
    {   // room index 6 object -- The street
        roomName: "The Main Street - In front of your House",
        searchable:false,
        store: -1,
        roomDesc: "This street has very little activity. To the north is your residence and to the south is your neighbor, Fred, who is a hunter. The road runs west towards the town square and east towards Raiken Woods.",
        roomExits: [
            {
                link:2,
                direction: "North"
            },
            {
                link:9,
                direction: "East"
            },
            {   
                 link:10,
                direction: "West"
            },
            {
                link:7,
                direction: "South"
            }
        ]
    },
    { // room index 7 -- Fred's Yard
        roomName: "Fred's House - The Front Yard",
        searchable: false,
        store: -1,
        roomDesc: "This yard is somewhat unkempt with random shrubberies growing haphazardly. A smokehouse takes up one corner, there is a tanning rack for deerskins. The door to Fred's house is to the south, and the main street is to the north.",
        roomExits: [
            {
                link:6,
                direction: "North"
            },
            {
                link:8,
                direction: "South"
            }
        ]
    },
    { // room index 8 - Fred's House
        roomName: "Fred's House - Main Room",
        searchable: false,
        store: -1,
        roomDesc: "This one room building holds Fred's bed, a small table to have meals at, and a fireplace. A bow is propped up in the corner by an empty quiver.",
        roomExits: [
            {
                link: 7,
                direction: "North"
            }
        ]
    },
    { // room index 9 - Raiken Forest
        roomName: "Raiken Woods",
        searchable: true,
        store: -1,
        roomDesc: "This thick copse of oak trees is home to many forms of wildlife. It is a favorite spot for hunters, as rabbits and deer are plentiful here. Lately a pack of dangerous coyotes have moved in, hassling both the game and the hunters. You can search around if you wish to encounter anything. You have explored here "+woodsExplore+" times.",
        roomExits: [
            {
                link:6,
                direction: "Back to Town"
            }
        ],
        search: function(){
            var rando = Math.floor(Math.random() * 4);
            woodsExplore ++;
            console.log("Woods explored "+woodsExplore+" times.");
            if (woodsExplore > 9 && deeperSwitch === false){
                rooms[9].roomExits.push({ link:13, direction: "Deeper Woods"});
                deeperSwitch = true;
            }
            if (rando === 0) {
                var rando = Math.floor(Math.random() * 4);
                if (rando === 1){
                    alert('You search around the area and find nothing. You think you see a flash of movement and speed off in that direction but end up tripping over a tree root and hurting yourself a little bit.  You take 1 damage.');
                    Player.hp -= 1;
                } else{
                    alert('You wander around the forest looking intently at the perimeter of your vision and misstep, tripping over a root. But you catch your fall on the soft leaves.');
                }
            }
            if (rando === 1) {
                alert("As you walk through the woods you come upon an arrow that has been left here.");
                Item[9].room = 9;
            }
            if (rando === 2) {
                alert("A dangerous jackalope rushes out of the trees! Basically it's a bunny with antlers and sharp teeth. Prepare to fight!");
                Enemy = new Monster("jackalope", 9, 2, 2, 2, 4, 9, 4);
                console.log("Enemy created...");
                var bM = "The "+Enemy.name+" looks at you menacingly, giving you a chance to attack first!";
                battleOn = true;
                battleDisplay();
            }
            if (rando === 3) {
                alert("Oh no! As you come around a tree you find yourself faced by a growling coyote. It stalks towards you.");
                Enemy = new Monster("coyote", 11, 3, 3, 3, 5, 12, 6);
                isCoyote = true;
                console.log("Enemy generated");
                var bM = "The "+Enemy.name+" looks at you menacingly, giving you a chance to attack first!";
                battleOn = true;
                battleDisplay();
            }
            Display(roomReturn);
        }
    },
    { //room index 10 - Along the main street.
        roomName: "The Main Street - Nearing Town Square",
        searchable: false,
        store: -1,
        roomDesc: "A villager walks past going east towards the edge of town, where the woods are. To the north is a quaint chapel. To the south is the baker's store. Your house is further to the east and the town's square is to the west.",
        roomExits: [
            {
                link: 11,
                direction: "North"
            },
            {
                link: 15,
                direction: "West"
            },
            {
                link:6,
                direction: "East"
            },
            {
                link: 12,
                direction: "South"
            }
        ]
    },
    {  // room index 11 - The chapel
        roomName: "Father Brennan's Chapel",
        searchable: false,
        store: 0,
        roomDesc: "A roow of benches for the congretion to sit and listen to sermons fills the southern part of the room. The alter to Jezran, goddess of healing, takes up space in the north end of the room. Many come here to pray or be healed of their injuries.",
        roomExits: [
            {
                link: 10,
                direction: "South"
            },
            {
                link: 14,
                direction: "Down"
            }
        ],
    },
    { // room index 12 - The baker
        roomName: "The Bakery",
        searchable: false,
        store: 1,
        roomDesc: "The smell of baking bread is ever present here. A counter divides the room in half and an oven dominates the southern wall. A display of bread is sitting on the counter.",
        roomExits: [
            {
                link: 10,
                direction: "North"
            }
        ],
    },
    { // room index 13 - Deeper in the Woods
        roomName: "Deeper into Raiken Wood",
        searchable: true,
        store: -1,
        roomDesc: "The undergrowth is much thicker here than the forest's outskirts you first entered. Strange cries can be heard in the distance and the hairs on the back of your neck are standing up as if you sense danger.",
        roomExits: [
            {
                link: 9,
                direction: "Back Towards the Forest Outskirts"
            }
        ]  ,
        search: function () {
            var rando = Math.floor(Math.random() * 6);
            woodsExploreDeep ++;
            if (woodsExplore > 9){
                rooms[9].roomExits.push({ link:13, direction: "Deeper Woods"});
            }
            if (rando === 0) {
                var rando = Math.floor(Math.random() * 4);
                if (rando === 1){
                    alert('You search around the area and find nothing. You think you see a flash of movement and speed off in that direction but end up tripping over a tree root and hurting yourself a little bit.  You take 1 damage.');
                    Player.hp -= 1;
                } else{
                    alert('You wander around the forest looking intently at the perimeter of your vision and misstep, tripping over a root. But you catch your fall on the soft leaves.');
                }
            }
            if (rando === 1) {
                alert("As you walk through the woods you come upon an apple tree. It has a single apple hanging within reach of you that catches your eye.");
                Item[0].room = 13;
            }
            if (rando === 2) {
                alert("A dangerous jackalope rushes out of the trees! Basically it's a bunny with antlers and sharp teeth. Prepare to fight!");
                Enemy = new Monster("Forest Imp", 14, 4, 3, 3, 7, 15, 8);
                console.log("Enemy created...");
                var bM = "The "+Enemy.name+" looks at you menacingly, giving you a chance to attack first!";
                battleOn = true;
                battleDisplay();
            }
            if (rando === 3) {
                alert("Oh no! As you come around a tree you find yourself faced by a growling coyote. It stalks towards you.");
                Enemy = new Monster("coyote", 11, 3, 3, 3, 5, 12, 6);
                isCoyote = true;
                console.log("Enemy generated");
                var bM = "The "+Enemy.name+" looks at you menacingly, giving you a chance to attack first!";
                battleOn = true;
                battleDisplay();
            }
            if (rando === 4) {
                alert("Oh! Just under a fallen log, some spotted red-cap mushrooms grow. Perhaps you've met someone who can use these?");
                Item[15].room = 13;
            }
            if (rando === 5) {
                alert("A very angry badger was disturbed by your poking about and it attacks you for invading it's territory.");
                Enemy = new Monster("Angry Badger", 12, 4, 3, 3, 6, 11, 7);
                battleOn = true;
                battleDisplay();
            }
            Display(roomReturn);

        }
    },
    { // room index 14 - Catacombs under the Chapel
        roomName: "Chapel Catacombs",
        searchable: true,
        store: -1,
        roomDesc: "Torches of Everburning are lit in sconces set into the pillars that hold up the roof of this underground area. Sarcophagi are placed at intervals and also set into the walls are places for the dead whose family didn't have the means to buy sarcophogi for.",
        roomExits: [
            {
                link: 11,
                direction: "Up"
            }
        ],
        search: function(){
            var rando = Math.floor(Math.random() * 3);
            if (rando === 0){
                alert("You search about the catacombs. Just outside your perimeter of vision you hear movement but can't see into the shadows.");
                Display(roomReturn);
            }
            if (rando === 1) {
                alert("Oh how nice, you've found a lucky coin heads up on the ground!");
                Player.coins ++;
                Display(roomReturn);
            }
            if (rando == 2) {
                skeleton = true;
                Enemy = new Monster("Skeleton", 15, 4, 4, 3, 8, 14, 7);
                battleOn = true;
                battleDisplay()
            }
        }
    },
    { // room index 15 - Town Square
        roomName: "Town Square",
        searchable: false,
        store: -1,
        roomDesc: "Here is a large expanse of green grass. The open area is often used for festivities as a place for the villagers to congregate. To the north is the house of the mayor. The main street leads east and west. To the south, across the open grass is gate to the Great Highway.",
        roomExits: [
            {
                link: 16,
                direction: "North"
            },
            {
                link: 10,
                direction: "East"
            },
            {
                link: 18,
                direction: "West"
            }
        ]
    },
    { // Room Index 16 -- The mayor's house
        roomName: "Mayor's House - Greeting Room",
        searchable: false,
        store: -1,
        roomDesc: "A massive fireplace takes up the west wall. Several comfortable armchairs are seated close to the heat. The bedrooms are up on the second story, which is off limits to guests. The mayor's office is to the east.",
        roomExits: [    
            { 
                link: 17,
                direction: "East"
            },
            {
                link: 15,
                direction: "South"
            }
        ]
    },
    { // Room Index 17 -- Mayor's office
        roomName: "Mayor's House - Office",
        searchable: false,
        store: -1,
        roomDesc: "A large desk dominates the center of the room and the mayor can often be found behind it. It's cluttered with papers and maps. The door to the main room is to the west.",
        roomExits: [
            {
                link: 16,
                direction: "West"
            }
        ]
    },
    { // Room Index 18 -- Craftsman's Street
        roomName: "Craftsman's Street",
        searchable: false,
        store: -1,
        roomDesc: "You're to the west of the town's square. The various craftsman have their shops on this street. To the north is the weaponsmith and to the south is the armorer. The street continues to the west.",
        roomExits: [
            {
                link: 19,
                direction: "North"
            },
            {
                link: 15,
                direction: "East"
            },
            {
                link: 20,
                direction: "South"
            }
        ]
    },
    { // Room Index 19 -- Weaponsmith
        roomName: "The Bloody Blade",
        searchable: false,
        store: 2,
        roomDesc: "A wood and glass display case makes up for the counter. The walls are lined with examples of the bladesmith's work. The sounds of an active forge drift from the yard out behind the shop.",
        roomExits: [
            {
                link: 18,
                direction: "South"
            }
        ]
    },
    { // Room Index 20 -- Armorer
        roomName: "The Armor Shop",
        searchable: false,
        store : 3,
        roomDesc: "Several mannequins are positioned throughout the store displaying various sets of armor. At first glance it seems to be a very crowded shop, and a good day for business, but... nope its a room full of mannequins. The street is back to the north.",
        roomExits: [
            {
                link : 18,
                direction: "North"
            }
        ]

    }
]
let Shop = [
    { // Shop index 0 -- Healing services at the Chapel
        items: [
            {
                name: "Healing Services",
                desc: "The priest will pray for your wounds to be healed.",
                cost: 6,
                onBuy: function () {
                    Player.hp = Player.maxHp;
                }
            }
        ]
    },
    { // Shop index 1 -- The baker
        items: [
            {
                name: "Hot Bun",
                desc: "You can take a hotbun with you that will restore 4-6 health.",
                cost: 4,
                onBuy: function () {
                    take(12);
                }
            },
            {
                name: "Loaf of Bread",
                desc: "This loaf of bread will heal 6-9 health.",
                cost: 7,
                onBuy: function () {
                    take(13);
                }
            },
            {
                name: "Pot Pie",
                desc: "Beef and vegetables baked into a flaky crust, it will fully restore you.",
                cost: 12,
                onBuy: function () {
                    take(14);
                }
            }
        ]
    },
    { // shop index 2 -- the weaponsmith
        items: [
            {
                name: "Iron Dagger",
                desc: "A plain hilt with a sharp blade, nearly a foot long.",
                cost: 50,
                onBuy: function (){
                    take(16);
                }
            }
        ]

    },
    {  // shop index 3 -- The armorer
            items: [
                {
                    name: "Studded Leather Armor",
                    desc: "This hardened leather jacket and pants is fitted with little metal studs meant to afford some extra protection from sharp, pointy things trying to pierce you.",
                    cost: 65,
                    onBuy: function () {
                        take(17);
                    }
                }
            ]
    }
]
/* the Item array contains all the objects in the game as objects, with
such properties as name, description, quanity, room index found within,
a boolean as to whether the player has it in it's inventory, and a function
that executes upon use of the object. */
let Item = [
    {// item index 0 apple
        name: "Apple",
        desc: "A shiny red apple. It looks tasty and perhaps eating it will restore some health.",
        room: 0,
        quantity: 0,
        owned: false,
        use: function (){
            var restore = Math.floor(Math.random()*(4-4+2))+4;
            alert('You eat the apple and it restores '+ restore +'health.');
            Player.hp += restore;
            Item[0].quantity --;
            if (this.quantity < 1) {
                this.owned = false;
            }
        }
    },
    {// item index 1 chest key
        name: "Chest Key",
        desc: "This small brass key will open the chest in your room.",
        room: 0,
        quantity: 0,
        owned: false,
        use: function (){
            if (roomReturn === 1 && chestOpen === false){
                alert("You unlock the chest and remove it's items.");
                chestOpen = true;
                Item[2].room = 1;
                Item[3].room = 1;
            } else {
                alert("There's nothing here that this key will unlock...");
            }
            Display(roomReturn);
        }
    },
    {// item index 2 leather jerkin
        name: "Leather Jerkin",
        desc: "It was once your father's, but it's about your size and would offer a little bit of defense.",
        room: -1,
        quantity: 0,
        owned: false,
        worn: false,
        use: function (){
            var wielded = false;
            for (var i = 0; i < Item.length; i++){
                if (Item[i].worn === true) {
                    wielded = true;
                }
            }
            if (this.worn === false && wielded === false) {
                Player.armor = "Leather Jerkin";
                Player.def += 1;
                this.worn = true;
                alert("You wear the leather jerkin and feel slightly more defended.");
            } else if (this.worn === true) {
                alert("You stop using the leather jerkin.");
                Player.armor = "Clothes";
                Player.def -= 1;
                this.worn = false;
            }
            Display(roomReturn);
        }
    },
    { //Item index 3 wooden sword
        name: "Wooden Practice Sword",
        desc: "It's not meant to inflict much more damage than your fists, but it will help you train and do a little more damage.",
        room: -1,
        quantity: 0,
        owned: false,
        equipped: false,
        use: function (){
            var wielded = false;
            for (var i = 0; i < Item.length; i++){
                if (Item[i].equipped === true) {
                    wielded = true;
                }
            }
            if (this.equipped === false && wielded === false) {
                Player.weapon = "Wooden Practice Sword";
                Player.str += 1;
                this.equipped = true;
                alert("You wield the wooden practice sword and feel like your attacks will be slightly stronger.");
            } else if (this.equipped === true) {
                alert("You stop using the wooden practice sword.");
                Player.weapon = "Fists";
                Player.str -= 1;
                this.equipped = false;
            }
            Display(roomReturn);
        }
    },
    {//Item index 4 milk bucket
        name: "Milk Bucket",
        desc: "This bucket holds milk when you milk the goats. The goat milk is a major source of daily nourishment for you.",
        room: 5,
        quantity: 0,
        owned: false,
        use: function () {
            if (roomReturn === 3 && this.quantity === 1) {
                this.quantity=0;
                take(5);
                alert("You milk the goat and obtain a pail of goat's milk");
            } else {
                alert("You see nothing here that you can milk.");
            }
        }
    },
    { //Item index 5  -- Goat milk
        name: "Goat Milk",
        desc: "It's a little more bitter, yet more rich, than traditional cow milk. It's part of a balanced meal, and it's always good to have food along.",
        room: -1,
        quantity: 0,
        owned: false,
        use: function () {
            alert("It's part of a balanced meal. Find all four food groups to make a meal to go.");
            Display(roomReturn);
        }
    },
    { //Item index 6  -- Rake
        name: "Rake",
        desc: "A long pole with tines on the end that can moove and smooth soil, or pull up weeds by their roots.",
        room: 5,
        quantity: 0,
        owned: false,
        use: function () {
            if (roomReturn === 4 && this.quantity > 0) {
                this.quantity = 0;
                rooms[4].roomDesc = "A silly scarecrow stands in the center of the patch of soil and several rows of well tended vegetables grow here. The weeds have been cleared away by the labor of a good gardener. To the north stands your small toolshed, and to the east is the rest of your yard.";
                alert("You rake the garden and take care of the weeds. In the process you harvest a few vegetables.");
                take(7);
            } else {
                alert("You see nothing here to rake...");
            }
        }
    },
    { // Item index 7  -- Vegetables
        name:"Vegetables",
        desc: "A zucchini, a carrot, and a potato. If you had some milk and a bit of dried meat you could pack a meal to take with you.",
        room: -1,
        quantity: 0,
        owned: false,
        use: function () {
            alert("If you had vegetables, milk, and some meat you could pack up a meal.");
        }
    },
    { // Item index 8 -- Meat
        name: "Deer Jerky",
        desc: "A dried strip of beef. One of the three parts of a meal to go...",
        room: -1,
        quantity: 0,
        owned: false,
        use: function () {
            alert("If you use this with vegatables and milk, you can pack a meal to go.");
        }
    },
    { // Item index 9 -- Arrow
        name: "Arrow",
        desc: "A wooden shaft with a bronze tip and feather fletching at the other side.",
        room: -1,
        quantity: 0,
        owned: false,
        use: function (){
            alert("You're not much use with a bow... perhaps you know someone who needs some of these");
        }
    },
    {  // Item index 10 -- The Stew
        name: "Hearty Stew",
        desc: "It's a combination of roasted vegetables and hearty venison in a goat milk sauce.",
        room:-1,
        quantity:0,
        owned: false,
        use: function () {
            Player.hp = Player.maxHp;
            this.quantity --;
            this.owned = false;
            alert("You eat the stew and recover all your health.");
        }
    },
    { // Item index 11 -- Amulet of Protection
        name: "Amulet of Protection",
        desc: "A silver circle inset with a copper square that hangs on a strip of leather.",
        room: -1,
        quantity: 0,
        owned: false,
        use: function () {
            Player.acc = "Amulet of Protection";
            this.quantity --;
            this.owned = false;
            Player.def ++;
            alert("You slip the amulet over your head.");
        }
    },
    {  // Item Index 12 -- Hot Bun
        name: "Hot Bun",
        desc: "A round flaky wheat roll, it looks tasty and may can restore some health.",
        room: -1,
        quantity:0,
        owned: false,
        use: function (){
            var restore = Math.floor(Math.random()*(6-4+1))+4;
            alert('You eat the hot bun and it restores '+ restore +'health.');
            Player.hp += restore;
            Item[12].quantity --;
            if (this.quantity < 1) {
                this.owned = false;
            }
        }
    },
{ // Item index 13 -- loaf of bread
    name: "Loaf of Bread",
    desc: "Baked fresh today, this loaf of bread smells delicious. Food helps heal wounds on the go.",
    room: -1,
    quantity: 0,
    owned: false,
    use: function (){
        var restore = Math.floor(Math.random()*(9-5+1))+5;
        alert('You eat the apple and it restores '+ restore +'health.');
        Player.hp += restore;
        Item[13].quantity --;
        if (this.quantity < 1) {
            this.owned = false;
        }
    }
},
{  // Item index 14 -- Pot Pie
    name: "Pot Pie",
    desc: "Beef and vegetables have been baked into a flakey crust. This kind of meal would fully restore you.",
    room: -1,
    quantity: 0,
    owned: false,
    use: function () {
        Player.hp = Player.maxHp;
        Item[14].quantity --;
        if (this.quantity < 1) {
            this.owned = false;
        }
    }
},
{ // Item index 15 -- Spotted Red Cap mushroom
    name: "Spotted Red-Cap Mushroom",
    desc: "Some use these mushrooms to journey astrally or go into a divinatory trance. You personally don't have much use for this item, but someone else might.",
    room: -1,
    quantity: 0,
    owned: false,
    use: function () {
        alert("You eat the mushroom and start to feel funny. You wake up three hours later having had some amazing dreams.");
        this.quantity --;
        if (this.quantity < 1){
            this.owned = false;
        }
    }
},
{ //Item index 16 -- Iron Dagger
    name: "Iron Dagger",
    desc: "A simple hilt wrapped in leather with a sharp blade just under a foot long.",
    room: -1,
    quantity: 0,
    owned: false,
    equipped: false,
    use: function (){
        var wielded = false;
        for (var i = 0; i < Item.length; i++) {
            if (Item[i].equipped = true) {
                var wielded = true;
            }
        }
        if (this.equipped === false && wielded === false) {
            Player.weapon = "Iron Dagger";
            this.equipped = true;
            Player.str += 2;
            alert("You wield the iron dagger.");
        } else if (this.equipped === true) {
            alert("You stop using the iron dagger.");
            Player.weapon = "Fists";
            Player.str -= 2;
            this.equipped = false;
        } else if (wielded === true){
            alert("You already hold a weapon.");
        }
        Display(roomReturn);
    }
},
{ // Item index 17 -- Studded Leather armor.
    name: "Hard Studded Leather",
    desc:"This hardened leather jacket and pants is fitted with little metal studs meant to afford some extra protection from sharp, pointy things trying to pierce you.",
    room: -1,
    quantity: 0,
    owned: false,
    worn: false,
    use: function (){
        var wielded = false;
        for (var i = 0; i < Item.length; i++){
            if (Item[i].worn === true) {
                wielded = true;
            }
        }
        if (this.worn === false && wielded === false) {
            Player.armor = "Hard Studded Leather",
            Player.def += 2;
            this.worn = true;
            alert("You wear the leather jerkin and feel slightly more defended.");
        } else if (this.worn === true) {
            alert("You stop using the leather jerkin.");
            Player.armor = "Clothes";
            Player.def -= 1;
            this.worn = false;
        } else if (this.worn === false && wielded === true) {
            alert("You should remove the armor you're already wearing before putting this on.");
        }
        Display(roomReturn);
    }
}
]
/* The NPC array contains objects that represent the characters you meet
on your quest. They all have a message that displays upon looking at them,
or talking to them, or trying to fulfill a quest for them. */
let NPC = [
    { //NPC index 0 -- Fred the hunter
        name: "Fred",
        desc: "He wears a set of green and brown hunter's fatigues. His keen blue eyes dart about as if looking for a target to shoot with his bow. His liveliehood is being a hunter, mostly trapping rabbits or stalking deer in Raiken Woods.",
        room: 8,
        talk: "Oh hey there...  I used up my whole quiver last hunting run cuz I kept running into rabid dogs. The dang things would run off when hit with an arrow before I could kill them completely and collect my shaft back. If you brought me 4 arrows back I'd trade you some jerky for it.",
        quest: function (){
            if (Item[9].quantity > 3) {
                alert("Ah you found me four arrows.  Here's some deer jerky for you.");
                Item[9].quantity -= 4;
                take(8); 
            } else {
                alert("I still need more arrows to go hunting again. Four should do enough that I could spare a piece of jerkey for you.")
            }
            Display(roomReturn);
        }
    },
    { // NPC index 1 -- Emmie the Goat
        name: "Emmie",
        desc: "A grey and white goat that you've owned since you were young. She's a great milk producer and eats vegetable refuse or weeds.",
        room: 3,
        talk: "Bleet! Bleet! (she's trying to tell you she's either hungry or needs milk.",
        quest: function () {
            if (Item[4].owned === true && Item[4].quantity > 0) {
                Item[4].owned = false;
                take(5);
                alert("You milk the goat and obtain a pail of goat's milk");
            } else {
                alert("You have nothing with which to milk.");
            }
        }
    },
    { // NPC index 2 -- Meally the Goat
        name: "Meally",
        desc: "A brownish red, almost ginger colored goat that keeps Emmie company and loves carrots.",
        room: 3,
        talk: "Maaaah, maaaah! (He must want food...)",
        quest: function(){
            alert("Meally doesn't ever want much more than food...");
        }
    },
    { // NPC index 3 -- The Stove
        name: "The Cook Pot",
        desc: "A blackened metal cauldron hangs over the fire. You often use it to make stews... Right now the embers of a fire are still hot enough to cook on.",
        room: 0,
        talk: "You talk to yourself as you think of cooking, 'If I had some meat, some vegetables, and some goat's milk, I could make a wonderful stew.",
        quest: function () {
            if (Item[5].quantity > 0 && Item[7].quantity > 0 && Item[8].quantity > 0){
                Item[5].quantity --;
                Item[5].owned = false; 
                Item[7].quantity --;
                Item[7].owned = false;
                Item[8].quantity --;
                Item[8].owned = false;
                take(10);
                alert("You cook up a nice stew.");   
            } else {
                alert("You don't have enough ingredients to cook a stew.");
            }
        }
    },
    { // NPC index 4 -- Father Brennan
        name: "Father Brennan",
        desc: "A thin, ruddy faced man of tall stature. He wears yellow robes and an icon of Jezran hangs around his neck on a chord of leather.",
        room: 11,
        talk: "I can heal you brother, but my services would become scarce were it not for the 'donations' of my parishoners. I'd only take 6 coins from you if you wish to have your health restored.",
        quest: function() {
            if (Player.level > 2 && cataQuest === false){
                alert("I fear there is unrest in the catacombs below here. Several of the dead have risen and I would bestow upon you an amulet of protection if you killed 3.");
            } else if (Player.level < 3 && cataQuest === false) {
                alert("Come back when your level is higher and I may have a job for you.");
            } else if (cataQuest === true) {
                alert ("Thankyou for your services in ridding us of the undead.")
            }else if (skeleCount > 2 && cataQuest === false){
                alert ("Ahh thankyou, my son. The undead were more than I myself could handle. As agreed I give you this amulet of protection.");
                take(11);
                cataQuest = true;
            }
        }
    },
    { // NPC index 5 -- Margaret the Baker
        name: "Margaret the Baker",
        desc: "A broad shouldered woman of considerable girth, Margaret smiles at you. Her arms are coated in flour as is her apron.",
        room: 12,
        shop: true,
        talk: "I don't have much time to spare for chit-chat. I've got loaves to bake!",
        quest: function () {
            alert("There's nothing i be needing right now.");
        }
    },
    { // NPC index 6 -- Your Chest
        name: "Your Father's Chest",
        desc: "Your father was a soldier, and a few of his belongings have been stored here.",
        room: 1,
        shop: false,
        talk: "You talk to yourself about the key you keep in the other room that opens this chest...",
        quest: function () {
            if (chestOpen === false && Item[1].owned === true){
                chestOpen = true;
                Item[2].room = 1;
                Item[3].room = 1;
            } else if (chestOpen === true) {
                alert("The chest has already been looted.");
            } else if (Item[1].owned === false) {
                alert("You need the key for this chest.");
            }
        }
    },
    { // NPC index 7 -- The Mayor
        name: "Mayor Collin",
        desc: "A short balding man with a keen eye. He wears well cut trousers and a coat. He looks at you appraisingly.",
        room: 17,
        talk: "Ahh yes, good to see you. I've heard tell there are too many coyotes in the forest and it's putting the hunters and gatherers in danger.",
        quest: function(){
            if (coyoteCount < 8 && coyoteQuest === false) {
                alert("If you would kill 8 coyotes for our fair village I'd see you rewarded with a sum of coins");
            }
            if (coyoteCount > 7 && coyoteQuest === false) {
                coyoteQuest = true;
                Player.coins += 35;
                alert("Thankyou for your hunting! Here is 35 coins for your trouble.");
            }
            if (coyoteQuest === true) {
                alert("I have no further jobs for you.");
            }
        }
    },
    { // NPC index 8- Bradford the Blacksmith
        name: "Bradford",
        desc: "A barrel chested stocky man, his head is shaved completely bald except for a small patch of hair just below his lip.",
        room: 19,
        talk: "If you be looking for a better weapon, you did come to the right place!",
        quest: function () {
            alert('I have no special tasks for you...');
        }
    },
    {  // NPC index 9 - Avraam the Armorer
        name: "Avraam",
        desc: "A lean, tall man with spectacles. He doesn't look much like an armorer... but you do wonder, what's an armorer supposed to look like?",
        room: 20,
        talk: "Ahh yes, protection is the name of my game. But i like to forge my wares from a place of power... so I make a potion from the Spotted Red Caps mushrooms to quaff before I start a piece.",
        quest: function () {
            alert("If you brought me 5 Spotted Redcap mushrooms, I'd pay you 45 coins.");
            if (Item[15].quantity > 4 && avraamQ === false){
                avraamQ = true;
                Item[15].quantity -= 5;
                Player.coins += 45;
                alert('"Thankyou so much", says Avraam as he gives you the coins and takes the mushrooms.');
            } else if (avraamQ === true){
                alert("I don't need anything more at this moment... But thankyou.");
            }
        }
    }
]
console.log('NPC array loaded');
var Player = {
    name: "Player",
    level: 1,
    hp: 10,
    maxHp: 10,
    str: 3,
    dex: 3,
    def: 3,
    coins: 10,
    xp: 0,
    tNL: 10,
    armor: "Cotton Clothes",
    acc: "none",
    weapon: "fists"
}
function Monster(name, hp, str, dex, def, coinL, coinH, xp) {
    this.name = name;
    this.hp = hp;
    this.maxHp = hp;
    this.str = str;
    this.dex = dex;
    this.def = def;
    this.coins = Math.floor(Math.random()*(coinH-coinL+1))+coinL;
    this.xp = xp;
}