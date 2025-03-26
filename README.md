# fantasygame
"""
Turn based rpg game with story progression, challenging side quests, and hidden secrets

Party system:
5 hero slots
Low man mode: per each fewer party member on purpose (doesn't account for yet to be unlocked slots and dead characters) you get a bonus to stats
unique hero classes, looks, and skill trees
prebuilt npc allies avialable
build your own team
max party size is 10 people

battle system:
battle size is max size of 5 at a time, but enemy count is not limited, as enemy dies next will come on
each character (heroes and enemies) will have an initiative or speed rating that will determine their attack order
there are items, attack, abilities, and specials
some battles will have special events or triggers that must be done to change the fight into its next stage

leveling system:
xp based leveling, combats earn xp
each character template has base stats that get updated per level (not always the same stat every level)
preset templates provide base skills and abilities but additional skills and abilities will be based on level unlocks and then players choices
certain items will have level requirements attached

skill system:
skill tree where each choice has branching options that expand upon the base node
you don't have to keep going down a path
some nodes have an either or choice, once you select one path the other path gets locked
some skills level up to become stronger, some skills evolve into a new skill that replaces the old (retains original skill but adds some new feature to it)

Game starts prompted with 'new game','load game','settings'.
New game opens a second menu:
    - single or multi players
        - multiplayer online or LAN
    - difficulty
    - expansion
    - story 
    - name
    - race 
    - class 
    - background
load game opens a list of saved games with savename, duration played, and your main character name
settings
    - color and brightness
    - sound levels
    - subtitles
    - 

Once game is started depending on the background a specific opening will play and some questions and options will help you determine your early proficiency points 
(create a natural story based approach to leveling)
character will appear in the starting setting and so begins the path line, each story has 1000's of ways it can go and the ending is also not predetermined, your choices matter a lot.

experience will scale with leveling, so a lvl 1 mob is always a lvl 1 mob and as you get further away (higher level) mob gives less exp, but will always give 1.
spawned Child mobs (creatures spawned in a fight, NOT creatures that come in from elsewhere and join) will not give exp, also no rewards. 
a mob must give exp to drop items, to prevent low level farming for levels the exp need per each level greatly increases

crafting exists to make potions, poisons, ammo, and gear.
Crafted gear will be categorized by basic or enchanted, enchanted crafting is the addition of a a compound to add a benefit depending on where its added. 
Basic gear is basic armor types, weapon types, and shield types.


"""