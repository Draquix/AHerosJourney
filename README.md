# AHerosJourney
A blend of HTML, CSS, and JavaScript creating a game reminiscant of 1980s text rpgs using modern technologies

# AHerosJourney
A blend of HTML, CSS, and JavaScript creating a game reminiscant of 1980s text rpgs using modern technologies,

More specifically it uses a blank HTML scaffold with several tags with id's or classes to allow the JavaScript engine to access page elements using the 
getElementById(element).innerHTML and post the game content and control structure. There is a css style sheet that creates the layout, colors, fonts. 
There are two JavaScript files. Script.js is the engine that displays the 'room' the player character is in, and handles the interactions with objects 
and characters. rooms.js contains the data structures that are arrays of objects containing room descriptions, NPCs, items and their uses.'

With the current engine the user can walk amongst all the rooms. You can examine, take, drop, and use items. You can examine, talk, and check for quest 
with all the NPCs, and also search special rooms that represent larger unmapped areas for random encounters including menu/turn based battles with enemy
characters.
Since that engine is mostly stable, game content can easily be added by making new object items in the arrays contained in rooms.js 
Literally the game could be made to be three times larger with twice as many items and quests just by adding objects to rooms.js without having to
make any alterations to the engine in script.js  .

This is my first personal attempt to work with github outside of school.


