####################################################
# Name: Tamara Ozol and Nathan Mitchell
# Date: 3/30/2022
# Description: RPi Activity 1
####################################################
from tkinter import *

#the room class
class Room:
    #the constructor
    def __init__(self, name, image):
        # rooms have a name, an image (the name of a file),
        # exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table),
        # item descriptions (for each item), and grabbables
        # (things that can be taken into inventory)
        # enemies have a desc, health, damage, and a drop item
        # the enemy name is used to iterate over the list of enemies
        # with the functionality of the list
        # (the same is true with locked exits/ locked exit names)
        # locked items and locked exits both have descriptions
        # and key items to open them. Exits have the room they lead to
        # items have the grabbable they drop
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []
        self.enemyNames = []
        self.enemies = {}
        self.lockedItems = {}
        self.lockedExits = {}
        self.lockedExitNames = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):

        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    @property
    def enemies(self):
        return self._enemies

    @enemies.setter
    def enemies(self, value):
        self._enemies = value

    @property
    def enemyNames(self):
        return self._enemyNames
    
    @enemyNames.setter
    def enemyNames(self, value):
        self._enemyNames = value

    @property
    def lockedItems(self):
        return self._lockedItems
    
    @lockedItems.setter
    def lockedItems(self, value):
        self._lockedItems = value

    @property
    def lockedExits(self):
        return self._lockedExits
    
    @lockedExits.setter
    def lockedExits(self, value):
        self._lockedExits = value

    @property
    def lockedExitNames(self):
        return self._lockedExitNames
    
    @lockedExitNames.setter
    def lockedExitNames(self, value):
        self._lockedExitNames = value
    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate
        # dictionary
        self._exits[exit] = room

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is
    # made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate
        # dictionary
        self._items[item] = desc

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        if (item != None):
            self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)
    
    # adds an enemy to a specific room
    # the enemy name is added to the dict and the list
    # this functions as the key for the dictionary location
    # the desc and drop item, both str are added to dict
    # health and damage, both ints, are added to dict
    def addEnemy(self, enemy, desc, health, damage, dropItem):
        self._enemyNames.append(enemy)
        self._enemies[enemy] = [desc, health, damage, dropItem]
    
    # an enemy name is deleted from the list of enemies
    def delEnemy(self, enemy):
        self._enemyNames.remove(enemy)

    # a locked item is added to a room
    # everthing used for the dictionary is meant to be a string
    # item is the dictionary key
    def addLockedItem(self, item, desc, key, dropItem):
        self._lockedItems[item] = [desc, key, dropItem]

    # a locked exit is added to a room
    # exit is both the name and the key for the dict
    # it is added to both the list of names and dict
    # everything else is a str added to the dict
    def addLockedExit(self, exit, room, desc, key):
        self._lockedExitNames.append(exit)
        self._lockedExits[exit] = [room, desc, key]
    
    # a locked exit is removed
    # the name is removed from the list of exit names
    def delLockedExit(self, exit):
        self._lockedExitNames.remove(exit)
    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)
        # player Health Readout
        s += f"Player Health: {Game.healthReadout(Game)}\n"
        # next, the items in the room
        s += "You see: "
        for item in self.items.keys():
            s += item + " "
        
        # locked items also need to be displayed
        for item in self.lockedItems.keys():
            s += item + " "
        s += "\n"
            
        # next, the exits from the room
        s += "Exits: "

        for exit in self.exits.keys():
            s += exit + " "
        
        # and the locked exits
        for exit in self.lockedExitNames:
            s += exit + " "
        s += "\n"

        # next we need to display any enemies in the room
        s += "Enemies: "

        for enemy in self.enemyNames:
            s += enemy + " "
        s += "\n"


        return s



# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
    # Class variables are used for the player health, max player health, and damage for the player
    # these are all able to be changed, but generally, max health should be equal to 
    # player health at initialization
    playerHealth = 10
    maxHealth = 10
    playerDamage = 1
    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)

    # play the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")
        # processes the player's input

    # Creates the rooms
    def createRooms(self):
        # r1 through r4 are the four rooms in the mansion
        # currentRoom is the room the player is currently in (which
        # can be one of r1 through r4)
        # create the rooms and give them meaningful names and an

        # image in the current directory
        r1 = Room("Sitting Room", "SittingRoom.gif")
        r2 = Room("Living Room", "LivingRoom.gif")
        r3 = Room("Study", "Study.gif")
        r4 = Room("Brewery", "Brewery.gif")
        r5 = Room("Attic", "Attic.gif")
        r6 = Room("Basement", "Basement.gif")
        
        # add exits to room 1
        r1.addExit("east", r2) # to the east of room 1 is room 2
        r1.addExit("south", r3)
        # adds a locked exit to room 1
        r1.addLockedExit("north", True, "Oh look a locked room. The lock looks fAnCy.", "fancy_key")
        # add grabbables to room 1
        r1.addGrabbable("key")
        # add items to room 1
        r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
        r1.addItem("table", "It is made of oak. A golden key rests on it.")

        # add exits to room 2
        r2.addExit("west", r1)
        r2.addExit("south", r4)
        # add items to room 2
        r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
        r2.addItem("fireplace", "It is full of ashes.")
        
        # add exits to room 3
        r3.addExit("north", r1)
        r3.addExit("east", r4)
        r3.addExit("up", r5)
        # add grabbables to room 3
        r3.addGrabbable("book")
        # add items to room 3
        r3.addItem("bookshelves", "They are empty. Go figure.")
        r3.addItem("statue", "There is nothing special about it.")
        r3.addItem("desk", "The statue is resting on it. So is a book.")
        r3.addItem("book", "The book mentions something about being doomed by an exit. That's strange")

        # add exits to room 4
        r4.addExit("north", r2)
        r4.addExit("west", r3)
        r4.addExit("down", r6)
        r4.addExit("south", None) # DEATH!
        # add grabbables to room 4
        r4.addGrabbable("6-pack")
        # add items to room 4
        r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")

        #adds the exit to room 5
        r5.addExit("down", r3)
        #adds the item to room 5
        r5.addItem("throne", "A large throne with a goblin on it.")
            #adds the enemy to room 5
        r5.addEnemy("goblin", "A mean looking goblin who probably wants to kill you", 10, 2, "fancy_key")

        #adds exit to room 6
        r6.addExit("up", r4)
        #adds locked item to room 6
        r6.addLockedItem("safe", "It is locked... Maybe a key can open it?", "key", "dagger")
        # adds item to room 6
        r6.addItem("chains", "Maybe this was a dungeon?")
        
        # set room 1 as the current room at the beginning of the
        # game
        Game.currentRoom = r1

        # initialize the player's inventory
        Game.inventory = []


    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)
        
        # setup the player input at the bottom of the GUI

        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        
        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)
        
        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)



    # set the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
        # if dead, set the skull image
            Game.img = PhotoImage(file="Death.gif")
        elif (Game.playerHealth <= 0):
        # if killed by goblin, use death by gob image
            Game.img = PhotoImage(file="DeathByGob.gif")
        elif (Game.currentRoom == True):
        # if win use winning image
            Game.img = PhotoImage(file="Outside.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)
            
        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img


    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "Oh No!! You've gone through a bad door. The feds have discovered your trespassing and therefore you have been sentenced to death. sry.\n")
        elif(Game.playerHealth <= 0):
            # if you have been killed by the goblin, let the player know and give a hint
            Game.text.insert(END, "You have been killed by the goblin. Maybe you should find something to make you stronger?\n")
        elif(Game.currentRoom == True):
            # let the player know they've won and congratulate them
            Game.text.insert(END, "WOW!! Congrats! You made it out alive! That was super scary. Well, now what? Anyways. Have a good time finding your way home.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) + "\nYou are carrying: " + str(Game.inventory) + "\n\n" + status)
        Game.text.config(state=DISABLED)

    # combat is called to work out the enemy damage 
    # and player damage done to the player and enemy
    # respectively
    # it takes in the enemy that is being fought
    def combat(self, enemy):
        # calculates the damage towards the player
        Game.playerHealth += -(Game.currentRoom.enemies[enemy][2])
        
        # calculates the damage done by the player
        if("dagger" in Game.inventory):
            Game.playerDamage = 4
        Game.currentRoom.enemies[enemy][1] += -(Game.playerDamage)
        
        # if the enemy is dead, the enemy needs to drop it's item
        if (Game.currentRoom.enemies[enemy][1] <= 0):
            if(Game.currentRoom.enemies[enemy][3] != None):
                Game.currentRoom.addGrabbable(Game.currentRoom.enemies[enemy][3])
            Game.currentRoom.delEnemy(enemy)

    # enemy health is displayed in a visual bar like representation
    def enemyHealthReadout(self, enemy):
        visEnemyHealth = "@" * Game.currentRoom.enemies[enemy][1]
        visMaxHealth = "_" * (10 - Game.currentRoom.enemies[enemy][1])
        enemyHealth = f"[{visEnemyHealth + visMaxHealth}]"
        return enemyHealth

    # player health is displayed in a slightly different bar representation
    def healthReadout(self):
        visPlayerHealth = "#" * Game.playerHealth
        visMaxHealth = "_" * (Game.maxHealth - Game.playerHealth)
        playerHealth = f"[{visPlayerHealth + visMaxHealth}]"
        return(playerHealth)

    # processes the player's input
    def process(self, event):
        # grab the player's input from the input at the bottom of
        # the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to
        # compare the verb and noun to known values
        action = action.lower()
        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, take, attack, and use"

        # exit the game if the player wants to leave (supports quit,
        # exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye" or action == "sionara!"):
            exit(0)

        # if the player is dead if goes/went south from room 4
        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return

        # split the user input into words (words are separated by
        # spaces) and store the words in a list
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]

            # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "Invalid exit."
                # check for valid exits in the current room
                if (noun in Game.currentRoom.exits):
                    # if one is found, change the current room to
                    # the one that is associated with the
                    # specified exit
                    Game.currentRoom = Game.currentRoom.exits[noun]
                    # set the response (success)
                    response = "Room changed."
                # if a player tries to go through a locked exit
                # the player needs to be let know that it is locked
                elif(noun in Game.currentRoom.lockedExits):
                    response = Game.currentRoom.lockedExits[noun][1]
            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."

                # check for valid items in the current room
                if (noun in Game.currentRoom.items):
                    # if one is found, set the response to the
                    # item's description
                    response = Game.currentRoom.items[noun]
                # if there is no item matching the input, then it checks enemies
                # the enemy health and desc is returned
                elif(noun in Game.currentRoom.enemyNames):
                    response = f"Enemy Health: {Game.enemyHealthReadout(self, noun)} \n{Game.currentRoom.enemies[noun][0]}"
                # if there are no enemies or items, then it checks locked items
                # the description is given if not opened
                # otherwise explains that locked item has been opened
                elif(noun in Game.currentRoom.lockedItems):
                    if (Game.currentRoom.lockedItems[noun][2] == None):
                        response = f"The {noun} has been opened already."
                    else:
                        response = Game.currentRoom.lockedItems[noun][0]
            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "I don't see that item."
                # check for valid grabbable items in the current
                # room
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable):
                        # add the grabbable item to the player's
                        # inventory
                        Game.inventory.append(grabbable)
                        # remove the grabbable item from the
                        # room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable
                        # items
                        break
            # the verb attack is used to initiate combat with an enemy
            elif (verb == "attack"):
                # default response
                response = "No enemy in this room"
                for enemy in Game.currentRoom.enemyNames:
                    # if there is an enemy in the room that attacked by player
                    # then combat is called which deducts health from player and enemy
                    # and if the enemy is alive then health is shown
                    # otherwise the defeat message is returned
                    # the dropped item is also revealed
                    if (noun == enemy):
                        Game.combat(self, enemy)
                        enemyHealth = Game.enemyHealthReadout(self, enemy)
                        if (Game.currentRoom.enemies[enemy][1] > 0):
                            response = f"Enemy Health: {enemyHealth}"
                        else:
                            response = f"The {enemy} has been defeated! It dropped a {Game.currentRoom.enemies[enemy][3]}"
            # the verb use is for using items in the player's inventory
            elif (verb == "use"):
                # default response
                response = "Item not in inventory"
                for item in Game.inventory:
                    # checks to see if the item is in the player's inventory
                    if (noun == item):
                        # default response
                        response = "That item cannot be used here"
                        for item in Game.currentRoom.lockedItems:
                            # checks to see if there is a locked item that needs that use item
                            # if there is, then the locked item is opened and then the drop item 
                            # is removed from the locked item
                            if (noun == Game.currentRoom.lockedItems[item][1] and Game.currentRoom.lockedItems[item][2] != None):
                                response = f"The item has been used. A {Game.currentRoom.lockedItems[item][2]} has been dropped"
                                Game.currentRoom.addGrabbable(Game.currentRoom.lockedItems[item][2])
                                Game.currentRoom.lockedItems[item][2] = None
                        
                        for exit in Game.currentRoom.lockedExitNames:
                            # if there were no locked items using that item, then locked exits are checked
                            # if there is, and the exit has not already been unlocked, then the new exit is added to the room
                            # and the key is removed from being needed to open the door
                            if (noun == Game.currentRoom.lockedExits[exit][2] and Game.currentRoom.lockedExits[exit][2] != None):
                                response = f"The item has been used. The {exit} exit has been unlocked!"
                                Game.currentRoom.addExit(exit, Game.currentRoom.lockedExits[exit][0])
                                Game.currentRoom.delLockedExit(exit)
                                Game.currentRoom.lockedExits[exit][2] = None


            # display the response on the right of the GUI
            # display the room's image on the left of the GUI
            # clear the player's input
            self.setStatus(response)
            self.setRoomImage()
            Game.player_input.delete(0, END)



####################################################
#the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

#create the window
window = Tk()
window.title("Room Adventure")

#create the GUI as a Tkinter canvas inside the window
g = Game(window)
#play the game
g.play()

#wait for the window to close
window.mainloop()

