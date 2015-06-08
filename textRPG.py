"""
The Interactive Python Text RPG.
Created by Mike Burgess

TODO: better input interface
TODO: more monsters
TODO: better leveling
TODO: monster leveling
TODO: rest ability for all classes to heal small amount of hp
TODO: improve debugging
TODO: add comments to Mage class
TODO: error handling for map functions
TODO: treasure list and drop rate

Notes: Camelcase is use for all function and variables names.
All class objects are single word and capitalized.  Double quotes are
used for all strings and comments.  Please utilize proper gramer for
all comments for better readability.  
"""

#imports
from random import randint
import simplegui

# globals

# Enable debugging by setting to True.
# To be used to print out variables and alter gameplay
# to all for easier debugging.
debug = False

# ??
tile = 20
width = tile * 11
height = tile * 15
char_name = ""
profession = ""

# classes

class Die:
    """
    Generate a random number in the range of the number of sides to the die.
    """
    def __init__(self, sides=6, numDie=1):
        """
        Takes the number of sides and number of die.
        Defaults to 6 side.
        Defaults to 1 die.
        """
        self.sides = sides
        self.numDie = numDie
        
    def roll(self):
        """
        Roll the die and get a random integer between one and the die maximum.
        """
        x = 0
        roll = 0
        while(x < self.numDie):
            x += 1
            roll += randint(1,self.sides)
        return roll
    
class Character(object):
    """
    Object to hold the player character's (PC) statistics
    """
    def __init__(self,char_name,hp,thaco,ac,inventory,exp):
        """
        Set the PC attributes for later use.
        """
        self.char_name = name
        self.hp = hp
        self.thaco = thaco
        self.ac = ac
        self.inventory = inventory
        self.exp = exp
        
class Player(Character):
    """
    Create the PC.
    """
    def __init__(self):
        pass
    
    def fight():
        """
        Player attacks on the command 'f'.
        This command is available to all classes.
        """
        playerAttack()
        
    def sheet():
        """
        Fetch the PC's character sheet.
        Contains the character's current attributes.
        """
        print "Name: %s Class: %s Level: %s HP: %s Thac0: %s AC:%s XP:%s"% (sprite.hero.char_name,sprite.hero.prof,sprite.hero.level,sprite.hero.hp,sprite.hero.thaco,sprite.hero.ac,sprite.hero.exp)
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        # Call the class commands function after printing the character sheet.
        commands()
       
class Fighter(Player):
    """
    The figher class.
    Brute melee attacker.
    Highest HP, melee attack, and defense
    """
    
    # Class
    prof = "fighter"
    # Maximum health points.
    # Starts at 10 for the fighter.
    maxhp = 10
    # Current level.
    # Each character starts at level 1.
    level = 1
    # Health die.
    # Determines health increase on a level up.
    hd = 10
    # Experience needed for the next level.
    next_level = 15
    # Die rolled to determine the damage done when the PC hits.
    attackDie = 10
    # PC's current health points.
    hp = 10
    # Current experience (exp) level.
    # Exp is gained by killing enemies.
    exp = 10
    # PC's offense is sprite.hero.thaco - sprite.mob.ac.
    thaco = 20
    # PC's defense is sprite.mob.thaco - sprite.hero.ac.
    ac = 10  
        
    def fight():
        """
        Attack the enemy.
        """
        # Call the fight function in the Player class.
        Player.fight()
        
    def sheet():
        """
        Retrieve the PC's character sheet.
        """
        # Call the sheet function in the Player class.
        Player.sheet()
    
    # The fighter class commands available.
    COMMANDS={
        'f':('fight',fight),
        'i':('info',sheet),
        'q':('quit',quit),
        }
    
class Cleric(Player):
    """
    The cleric class.
    Can attack; can heal.
    Moderate HP and melee attack.
    """
    
    # Class
    prof = "cleric"
    # Maximum health points.
    # Starts at 8 for the cleric.
    maxhp = 8
    # Current level.
    # Each character starts at level 1.
    level = 1
    # Health die.
    # Determines health increase on a level up.
    hd = 8
    # Experience needed for the next level.
    next_level = 20
    # Die rolled to determine the damage done when the PC hits.
    attackDie = 6
    # PC's current health points.
    hp = 8
    # Current experience (exp) level.
    # Exp is gained by killing enemies.
    exp = 8
    # PC's offense is sprite.hero.thaco - sprite.mob.ac.
    thaco = 20
    # PC's defense is sprite.mob.thaco - sprite.hero.ac.
    ac = 10
       
    def fight():
        """
        Attack the enemy.
        """
        # Call the fight function in the Player class.
        Player.fight()
    
    def sheet():
        """
        Retrieve the PC's character sheet.
        """
        # Call the sheet function in the Player class.
        Player.sheet()
    
    def heal():
        """
        The cleric's heal ability.
        Can be cast until at full health.
        The enemy still gets an attack while PC is healing.
        Can only heal self.
        """
        if sprite.hero.hp < sprite.hero.maxhp:
            sprite.hero.hp += Die(8).roll()                
            if sprite.hero.hp > sprite.hero.maxhp:
                sprite.hero.hp = sprite.hero.maxhp
            print "You now have: %s/%s hp"% (sprite.hero.hp,sprite.hero.maxhp)
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        else:
            print "Your health points are full"
            print "You have: %s/%s hp"% (sprite.hero.hp,sprite.hero.maxhp)
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

            # Call the class commands function if the PC's health is at full already.
            commands()
            
    # The cleric class commands available.
    COMMANDS={
        'f':('fight',fight),
        'h':('heal',heal),
        'i':('info',sheet),
        'q':('quit',quit),
        }

class Mage(Player):
    """
    The mage class.
    Casts spells.
    Weak HP and melee attack.
    Master of the arcane.  Wields powerful magicks.
    """    
    
    # Class
    prof = "mage"
    # Resource for casting spells
    # Mage only
    mana = 1
    # Maximum mana
    maxmana = 1
    # Maximum health points.
    # Starts at 4 for the mage.
    maxhp = 4
    # Current level.
    # Each character starts at level 1.
    level = 1
    # Health die.
    # Determines health increase on a level up.
    hd = 4
    # Experience needed for the next level.
    next_level = 10
    # Die rolled to determine the damage done when the PC hits.
    attackDie = 4
    # PC's current health points.
    hp = 4
    # Current experience (exp) level.
    # Exp is gained by killing enemies.
    exp = 4
    # PC's offense is sprite.hero.thaco - sprite.mob.ac.
    thaco = 20
    # PC's defense is sprite.mob.thaco - sprite.hero.ac.
    ac = 10
    
    def fight():
        """
        Attack the enemy.
        """
        # Call the fight function in the Player class.
        Player.fight()
    
    def sheet():
        """
        Retrieve the PC's character sheet.
        """
        # Call the sheet function in the Player class.
        Player.sheet()

    def rest():        
        if sprite.hero.mana < sprite.hero.maxmana:
            sprite.hero.mana += 1
            print("You have",sprite.hero.mana,"mana.")
        elif sprite.hero.mana >= sprite.hero.maxmana:
            print("Your mana is full.")
            print("You have",sprite.hero.mana,"mana.")
            commands()
        
    def castSpell():
        
        def sleep():
            print "You put the monster to sleep it is easy to kill now"
            sprite.mob.hp -= sprite.mob.hp
            sprite.hero.mana -= 1
            
        def magicMissile():
            dam = Die(4).roll() * sprite.hero.mana
            sprite.mob.hp -= dam
            print "You use all your mana! and do",dam,"damage!"
            sprite.hero.mana -= sprite.hero.mana
            
        def fireball():
            print "You are temporarily blinded by a feiry flash of light."
            dam = Die(6,3).roll()
            
            sprite.mob.hp -= dam
            print "You did",dam,"points of damage."            
            sprite.hero.mana -= 3

        def rewind():                    
            commands()
           
        print "You have",sprite.hero.mana,"mana."
        if sprite.hero.mana >= 1 and sprite.hero.mana < 3:
            spells={
                's':('sleep',sleep),
                'm':('magic missile',magicMissile),
                }
        elif sprite.hero.mana >= 3:
             spells={
                's':('sleep',sleep),
                'm':('magic missile',magicMissile),
                'f':('fireball',fireball),
                }
        else:
            spells={
                'e':('rewind',rewind),
                }
            print "You are out of mana!"
            
            
        for command, action in spells.items():
            print "Press %s to cast %s"% (command,action[0])
        print "Press Enter to skip."
        
        while True:
            print "~~~~~~~~~Press a key to Continue.~~~~~~~"
            command=input("Choose a command.\n>>>")
            if command and command not in spells:
                print "Not a valid command"
                continue
            break
        if command:
            spells[command][1]()
            
    # The mage class commands available.
    COMMANDS={
        'f':('fight',fight),
        's':('spells',castSpell),
        'r':('generate mana',rest),
        'i':('info',sheet),
        'q':('quit',quit),
        }
    
class Monster(Character):
    """
    A low level roaming monster template.
    """
    def __init__(self):
        pass
    # Monster name.
    mob_name = "NAME"
    # Monster health points.
    hp = 9999
    # Monster's offense is sprite.mob.thaco - sprite.hero.ac.
    thaco = 9999
    # Monster's defense is sprite.hero.thaco - sprite.mob.ac.
    ac = 9999
    # Items that the creature could drop on death.
    inventory={}
    # Experience awarded to the PC for killing the monster.
    exp = 9999
    # Die rolled to determine the damaage when the monster hits the PC.
    attackDie = 9999
    pass

class Goblin(Character):
    """
    A low level roaming monster.
    """
    def __init__(self):
        pass
    # Monster name.
    mob_name = "goblin"
    # Monster health points.
    hp = 7
    # Monster's offense is sprite.mob.thaco - sprite.hero.ac.
    thaco = 20
    # Monster's defense is sprite.hero.thaco - sprite.mob.ac.
    # PC auto hits with at level 42.
    ac = 6
    # Items that the creature could drop on death.
    inventory={}
    # Experience awarded to the PC for killing the monster.
    exp = 7
    # Die rolled to determine the damaage when the monster hits the PC.
    attackDie = 4

class Orc(Character):
    """
    A low level roaming monster.
    """
    def __init__(self):
        pass
    # Monster name.
    mob_name="orc"
    # Monster health points.
    hp=8
    # Monster's offense is sprite.mob.thaco - sprite.hero.ac.
    thaco=18
    # Monster's defense is sprite.hero.thaco - sprite.mob.ac.
    # PC auto hits with at level 42.
    ac=6
    # Items that the creature could drop on death.
    inventory={}
    exp=8
    # Die rolled to determine the damaage when the monster hits the PC.
    attackDie=6

# functions and event handlers    
    
def prof_label():
    """
    PC class options are Fighter, Cleric, and Mage.  Multi-line label.
    """
    choice = {
        "f": Fighter,
        "c": Cleric,
        "m": Mage,
        }
    
    label = ""
    for letter in choice.keys():        
        label += "Enter \'%s\' for %s " % (letter, choice[letter].__name__)
    return label
    
def char_prof(char_prof):
    """
    PC class options are Fighter, Cleric, and Mage.  Takes in a letter from the user.
    Outputs the PC's choosen profession.
    """
    global profession
    
    choice = {
        "f": Fighter,
        "c": Cleric,
        "m": Mage,
        }
    
    # Only allow a single class per PC.
    if profession == "":
        # Get the class from the user.
        if char_prof == "f":
            print "You choose the %s class."% (choice[char_prof].__name__)
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            profession = choice[char_prof]()
        elif char_prof == "c":
            print "You choose the %s class."% (choice[char_prof].__name__)
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            profession = choice[char_prof]()
        elif char_prof == "m":
            key = "m"
            print "You choose the %s class."% (choice[char_prof].__name__)
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            profession = choice[char_prof]()
        else:
            print "You entered an invalid class."
            return
    else:
        # The PC already has a choosen class
        return
    
def ranmob():
    """
    Roll a 2 sided die (D2) to determine which monster is encountered by the PC.
    """
    # A Goblin appears if a 1 is rolled.
    # An Orc appears if a 2 is rolled.
    mob = Goblin() if Die(2).roll() < 2 else Orc()
    return mob
    
class sprite:
    """
    Main class object to generate the PC and monster.
    """
    hero = profession
    mob = ranmob()    
    
def playerAttack():
    """
    The PC attacks the monster currently engaged in combat.
    """
    # Roll a twenty sided (D20) die.
    # A roll greater than the difference between the PC's THAC0 and the monster's AC equates to a hit.
    # Anything lower is a miss.
    roll = Die(20).roll()   
    if roll >= sprite.hero.thaco-sprite.mob.ac:
        print "You hit"
        # Roll the PC's attack die to determine damage.
        rollD = Die(sprite.hero.attackDie).roll()
        print "for",rollD,"damage"
        sprite.mob.hp -= rollD
        print "the",sprite.mob.mob_name,"has",sprite.mob.hp,"hp left"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    else:
        print"You miss"
        print"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        
def monsterAttack():
    """
    The monster attacks the PC.
    """
    # Roll a twenty sided (D20) die.
    # A roll greater than the difference between the monsters's THAC0 and the PC's AC equates to a hit.
    # Anything lower is a miss.
    roll = Die(20).roll()   
    if roll >= sprite.mob.thaco-sprite.hero.ac:
        print "The monster hit"
        # Roll the monster's attack die to determine damage.
        rollD = Die(sprite.mob.attackDie).roll()
        print "for",rollD,"damage"
        sprite.hero.hp -= rollD
        print sprite.hero.char_name,"has",sprite.hero.hp,"hp left"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    else:
        print "Monster misses"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"    
       
def levelUp():
    """
    Determine if the PC has enough experience to increase in level.
    HP and mana are improved every level.
    Thac0 is improved every thrid level up to level 18.
    """
    levelGain = False
    # Check if the experience gained is higher than the experience needed to gain the next level.
    while sprite.hero.exp >= sprite.hero.next_level:
        # Increase the PC's level
        sprite.hero.level += 1
        levelGain = True
        # Double the previous amount of experience needed and set it for the next level.
        sprite.hero.next_level = sprite.hero.next_level * 2
        if levelGain == True:
            # Roll the PC's hit die and add it to the maximum health.
            # Boost the PC's health to the new maximum.
            sprite.hero.maxhp += Die(sprite.hero.hd).roll()
            sprite.hero.hp = sprite.hero.maxhp
            # Increase the Mage class maximum mana by 1.
            # Boost the Mage's mana to the new maximum.
            if sprite.hero.prof == "mage":
                sprite.hero.maxmana += 1
                sprite.hero.mana = sprite.hero.maxmana
            print "You Gained a level","\n",'hp:',sprite.hero.hp,"\n",'level:',sprite.hero.level
            print "Congragulations!"
            # Reduce the PC's Thaco by one every three levels.
            if sprite.hero.level % 3 == 0:
                sprite.hero.thaco -= 1
                print "Your new thaco:",sprite.hero.thaco
            levelGain = False
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    
def commands():
    """
    Get the users input on the command to execute.
    """
    for command, action in sprite.hero.COMMANDS.items():
        print "Press %s to %s"% (command,action[0])
    print "press Enter to skip"
    while True:
        print "~~~~~~~~~Press a key to Continue.~~~~~~~"
        command = input("Choose a command.\n>>>")
        command = command.lower()
        if command and command not in sprite.hero.COMMANDS:
            print "Not a valid command"
            continue
        break
    # Pass the user command to the Class specific command list.
    if command:
        sprite.hero.COMMANDS[command][1]()
    
def  encounter(mob1,hero1):
    """
    Generate combat encounters with monsters.
    User will be prompted to select an action.
    The monster will attack.
    """
    sprite.mob = mob1
    sprite.hero = hero1
    print "%s encountered a wild %s."% (sprite.hero.char_name,sprite.mob.mob_name)
    print "The %s has %s hp."% (sprite.mob.mob_name,sprite.mob.hp)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    if sprite.hero.hp > 0:
        commands()
    if sprite.mob.hp > 0:  
        monsterAttack()
          
def checkDead(mob1,hero1):
    """
    Check to see if the monster or PC is dead.
    Death occurs when the health points reach zero or are below zero.
    A set amount of experience is awarded on a monster kill.
    """
    sprite.mob = mob1
    sprite.hero = hero1
    # Is the monster dead?
    if sprite.mob.hp <= 0:
        print "The",sprite.mob.mob_name,"is dead!"     
        sprite.hero.exp += sprite.mob.exp        
        print sprite.hero.char_name + " gained %s xp"% (sprite.mob.exp)
        print "%s xp remaining until the next level."% (sprite.hero.next_level - sprite.hero.exp)
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        sprite.mob = ranmob()
        # Call the function to see if the PC has increased in level.
        levelUp()
        return True
    # Is the PC dead?
    if sprite.hero.hp <= 0:
        sprite.mob.exp += sprite.hero.exp
        print "mob xp:",sprite.mob.exp
        print "Your hero",sprite.hero.char_name,"died!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        sprite.hero.char_name = input("What is your characters name?\n>>>")
        sprite.hero = profession()
        #print "Name: %s HP: %s Thac0: %s AC:%s XP:%s"% (sprite.hero.char_name,sprite.hero.hp,sprite.hero.thaco,sprite.hero.ac,sprite.hero.exp)
        return True
    else:
        return False

def combat():
    """
    FIGHT!
    """
    # Call the encounter function as long as the PC and monster are still alive.
    while checkDead(sprite.mob,sprite.hero)==False:
        encounter(sprite.mob,sprite.hero)

def gameLoop():
    """
    Main game function.
    The game will loop throught he below functions until the user quits.
    """
    # Main combat
    combat()
    # Loop back through itself until terminated by the user.
    gameLoop()
    
def char_name(char_name):
    """
    Get the PC's name from the user.
    """ 
    # char_name is used instead of name.

    char_name = char_name
    print "Welcome %s to the Interactive Python Text RPG!"% (char_name)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    
def draw_handler(canvas):
    """
    Event handler to drawn the player on the canvas.
    """
    canvas.draw_image(player,(10,10),(tile,tile),player_pos,(tile,tile))
    
def move(key):
    """
    Event handler allow the player to move around the canvas.
    """
    global player_pos
    
    if key == simplegui.KEY_MAP['down'] and player_pos[1]<height-tile:
        player_pos[1] += tile
    elif key == simplegui.KEY_MAP['up'] and player_pos[1]>0+tile:
        player_pos[1] -= tile
    elif key == simplegui.KEY_MAP['right'] and player_pos[0]<width-tile:
        player_pos[0] += tile
    elif key == simplegui.KEY_MAP['left'] and player_pos[0]>0+tile:
        player_pos[0] -= tile    
    
# Main game function call
#gameLoop()

# create frame
frame = simplegui.create_frame("Text RPG",width,height)
player = simplegui.load_image("http://6mlove.com/avatars/avatar-megaman.png")
player_pos = [tile * 5 + 10, tile * 14 + 10]
frame.set_canvas_background("black")

# register event handlers
frame.add_input("Characters name", char_name, 100)
frame.add_input("Characters class",char_prof, 100)
frame.add_label(prof_label(), 150)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(move)

# start frame
frame.start()