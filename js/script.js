//Global Variable Declarations
var roomReturn = 0;
var bM = "Battle is math.";

//clearDisplay empties the page before the rewrites.
function clearDisplay() {
    document.getElementById('place-name').innerHTML = "";
    document.getElementById('left-display').innerHTML = "";
    document.getElementById('right-display').innerHTML = "";
    document.getElementById('nav-menu').innerHTML = "";
    document.getElementById('inventory').innerHTML = "";

}
//The Display function loads up the room object and writes it to the page.
function Display(index) {
    if (battleOn === false) {
        clearDisplay();
        roomReturn = index;
        var Name = rooms[index].roomName;
        document.getElementById('place-name').innerHTML = Name;
        var Desc = rooms[index].roomDesc;
        document.getElementById('left-display').innerHTML = Desc;
        var Exits = "Directions to go from here: <br>";
        var stuff = "Items for sale <br>";
        if (rooms[index].searchable === true) {
            Exits += "<a href='javascript:search("+index+")'> Search </a>";
        }
        if (rooms[index].store > -1){
            var shopNum = rooms[index].store;
            for (var i = 0; i < Shop[shopNum].items.length; i ++){
                console.log('shop items ran once.');
                stuff = Shop[shopNum].items[i].name+ " for "+Shop[shopNum].items[i].cost+" coins." + "<a href='javascript:shopLook("+shopNum+","+i+")'> Examine </a> <a href='javascript:buy("+shopNum+","+i+")'> Buy </a> <br>";
                document.getElementById('right-display').innerHTML += stuff;
            }
        }
        for (var i = 0; i < rooms[index].roomExits.length; i++){
            Exits += "<a href='javascript:Display("+ rooms[index].roomExits[i].link +")'>"+ rooms[index].roomExits[i].direction + "</a> ";
            document.getElementById('nav-menu').innerHTML = Exits;
        }
        for (var i = 0; i < Item.length; i++){
                if (Item[i].room === roomReturn) {
                    var itemName = Item[i].name + "<a href='javascript:lookAt("+i+")'> Examine </a><a href='javascript:take("+i+")'>Take</a><br>";
                    document.getElementById('right-display').innerHTML += itemName;
            }
        }
        for (var i =0; i < NPC.length; i++){
            if (NPC[i].room === roomReturn) {
                var NPCPrint = NPC[i].name + "<a href='javascript:glance("+i+")'> Examine</a> <a href='javascript:talk("+i+")'> Speak</a> <a href='javascript:quest("+i+")'>Quest</a><br>";
                document.getElementById('right-display').innerHTML += NPCPrint;
            }
        }
        characterSheet();
    }
}
function shopLook(shop,item){
    alert(Shop[shop].items[item].desc);
    Display(roomReturn);
}
function buy (shop,item){
    if (Player.coins > Shop[shop].items[item].cost-1) {
        Player.coins -= Shop[shop].items[item].cost;
        Shop[shop].items[item].onBuy();
        alert("You have bought the "+Shop[shop].items[item].name);
    } else {
        alert("You can't afford this right now.");
    }
    characterSheet();
}
function characterSheet(){
    var disp = Player.name+"'s Character Sheet<br>";
    disp += "Currently level "+Player.level+", with "+Player.xp+" experience points. Next level at "+Player.tNL+" points <br>";
    disp += "Hitpoints: "+Player.hp+" out of "+Player.maxHp+" <br>";
    disp += "Strength: "+Player.str+"  Dexterity: "+Player.dex+"  Defense: "+Player.def+ "<br>";
    disp += "You have "+Player.coins+" coins.<br>";
    disp += "------------------------------------<br>";
    disp += "Wearing: "+Player.armor+"<br>";
    disp += "Accessory: "+Player.acc+"<br>";
    disp += "Wielding: "+Player.weapon+"<br>";
    document.getElementById('stats').innerHTML = disp;
    for (var i = 0; i < Item.length; i++){
        if (Item[i].owned === true && Item[i].quantity > 0){
            var itemName = Item[i].name + "<a href='javascript:lookAt("+i+")'> Examine </a><a href='javascript:use("+i+")'>Use</a> <a href='javascript:drop("+i+")'>Drop</a><br>";
            document.getElementById('inventory').innerHTML += itemName;
        }
    }
}
function lookAt(index){
    var msg = Item[index].desc + "You have "+Item[index].quantity+" of them.";
    alert(msg);
}
function take(index){
    var msg = "You take the " +Item[index].name;
    alert(msg);
    Item[index].room = -1;
    Item[index].owned = true;
    Item[index].quantity ++;
    console.log(" You got the "+Item[index].name+' and own '+Item[index].quantity);
    Display(roomReturn);
}
function use(index){
    Item[index].use();
    characterSheet();
    Display(roomReturn);
}
function drop(index){
    Item[index].room = roomReturn;
    Item[index].owned = false;
    Item[index].quantity --;
    Display(roomReturn);
}
function glance(index){
    var msg = NPC[index].desc;
    alert(msg);
    Display(roomReturn);
}
function talk(index){
    var msg = NPC[index].talk;
    alert(msg);
    Display(roomReturn);
}
function quest(index){
    NPC[index].quest();
    Display(roomReturn);
}
function search(index) {
    rooms[index].search();
    Display(roomReturn);
}
function battleDisplay (){
    if (battleOn === true){
    clearDisplay();
    console.log("running battle display");
    var Name = Player.name+" fighting a "+Enemy.name;
    document.getElementById('place-name').innerHTML = Name;
    var Desc = "Enemy's Hp: "+Enemy.hp+ " / "+Enemy.maxHp+"<br>";
    Desc += "Strength: "+Enemy.str+"<br> Dexterity: "+Enemy.dex+"<br> Defense: "+Enemy.def;
    document.getElementById('right-display').innerHTML = Desc;
    document.getElementById('left-display').innerHTML = bM;
    var Nav = "<a href='javascript:pAttack(1)'> Aggressive Attack </a>";
    Nav += "<a href='javascript:pAttack(2)'> Precision Strike </a>";
    Nav += "<a href='javascript:pAttack(3)'> Defensive Blow </a><br>";
    Nav += "<a href='javascript:runAway()'> Run Away </a>";
    document.getElementById('nav-menu').innerHTML = Nav; 
    characterSheet();
    }
}
function pAttack(choice){
    bM = "You attack the enemy with your "+Player.weapon+"...";
    var toHit = Math.floor((Math.random() * 10) + Player.dex);
    console.log('to hit is '+ toHit);
    if (choice === 2){
        toHit += Math.floor(Math.random() * Player.dex);
        console.log("after precise its "+toHit);
    }
    var dodgeRoll = Math.floor((Math.random() * 10) + Enemy.def);
    console.log ('Dodge roll is '+dodgeRoll);
    if (toHit > dodgeRoll) {
        bM += "and you hit!";
        var damRoll = Math.floor((Math.random() * Player.str) + 1);
        console.log("Damage roll was "+ damRoll);
        if (choice === 1) {
            damRoll +=Math.floor((Math.random() * Player.str) + 1);
            console.log("Player aggressive adds to "+damRoll);
        }
        bM += " You inflict "+damRoll+" points of damage.<br>";
        Enemy.hp -= damRoll;
        if (Enemy.hp < 1) {
            battleOn = false;
            Loot();
        }
    } else {
        bM += "but unfortunately you miss. <br>";
    }
    document.getElementById('left-display').innerHTML = bM;
    var hitYou = Math.floor((Math.random() * 10) + Enemy.dex);
    bM += "The enemy attacks... ";
    var defRoll = Math.floor((Math.random() * 10) + Player.def);
    console.log("enemy hitroll is "+hitYou+" and your defRoll is "+ defRoll);
    if (choice === 3){
        defRoll += Math.floor((Math.random() * Player.def) + 1);
        console.log("defensive move brings up to "+defRoll);
    }
    if (hitYou > defRoll){
        var damRoll = Math.floor((Math.random() * Enemy.str) + 1);
        bM += "and hits you for "+damRoll+" points of damage!<br>";
        document.getElementById('left-display').innerHTML = bM;
        Player.hp -= damRoll;
        if (Player.hp < 1){
            alert('you lost the game');
        }
    } else {
        bM += "but it misses you.<br>";
    }
    document.getElementById('left-display').innerHTML = bM;
    battleDisplay();
}
function runAway (){
    alert("You flee the battle...");
    battleOn = false;
    Display(roomReturn);
}
function Loot(){
    alert("You have defeated the "+Enemy.name+"! You loot "+Enemy.coins+" and gain "+Enemy.xp+" experience points.");
    Player.coins += Enemy.coins;
    Player.xp += Enemy.xp;
    if (isCoyote === true) {
        isCoyote = false;
        coyoteCount ++;
        console.log("CoyoteCount is up to "+coyoteCount);
    }
    if (skeleton === true){
        skeleton = false;
        skeleCount ++;
        console.log("You've killed "+skeleCount+" skeletons.");
    }
    if (Player.xp > Player.tNL-1) {
        Player.level ++;
        Player.tNL = Math.floor(Player.tNL *2.5);
        Player.def ++;
        Player.dex ++;
        Player.str ++;
        Player.maxHp = Math.floor(Player.maxHp * 1.5);
    }
    Display(roomReturn);
}
Display(0);
