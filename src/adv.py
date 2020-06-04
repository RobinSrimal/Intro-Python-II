from room import Room
from player import Player
from item import Item, Warg, Compass, Armor


# declare all items

item = {
    "sword": Item("sword", """A sword with an ancient history. It is dark from all the blood 
that has been spilled with it. Its handle is decorated with a gem. Unstained and a gloomy light 
can be seen to fickle in it when the moon is at its peak."""),

    "armor": Armor("armor",  """The armor of an elven king, long lost in history. It is said that the beast
that killed him now lives inside it - a spirit snake ready to feast on a worthy successor. Type in "put on" if
you are daring enough.""" ),

    "book": Item("book",  """ A book written in the language of the dwarfes. It tells many stories but among
them is also the story of Gnob. Gnob was an obsessed collector of the most haunted items in the world. He placed
them in his secret vault. It is said that he will find and kill whoever will try to steal his beloed objects."""),

    "candle": Item("candle",  """ A handy candle emanating a warm and soothing light. It must have been burning
    for centuries... or did somebody light it on fire recently ???"""),

    "warg": Warg("warg", """ An ancient warg, too old to still be hunting. A spell binds his flesh to this world.
    Ask him to tell you a story by typing "tell story"  """),

    "compass": Compass("compass", """ Use this compass to show you the right way ... hopefully. 
    Type "show way"."""),

    "bow": Item("bow", """ A handy weapon, given to you by your mother.""")



}




# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[item["sword"], item["book"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item["warg"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[item["compass"]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[item["candle"], item["armor"]]),


}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']





#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


if __name__ == "__main__":

    print("Welcome, adventurer. You are at the beginning .... But great treasures await ....You can move through the maze")
    print("by typing n for North, s for South, w for West and e for East")
    
    name = input("But first please tell me your name: ")

    location = room['outside']
    
    player = Player(name, location, [item["bow"]])
    
    while True:
    
        player.status()

        #player.pick_or_drop()
    
        player.move()
    