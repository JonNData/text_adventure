from room import Room
from player import Player
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
directions = ['n', 's', 'e', 'w']
player = Player("Archibald", room ['outside'])
print(f'Welcome!\nLocation: {player.current_room.name} \nDescription: {player.current_room.description}\n')
# Write a loop that:
#

while True:
    player_input = input("Choose a direction ['n', 's', 'e', 'w'] or 'q' to quit: ").lower()

    if player_input == 'q' or player_input == 'quit':
        print(f'Thanks for playing') 
        break

    if player_input in directions:
        try:
            player.navigate(player_input)
            print(f'Location: {player.current_room.name} \nDescription: {player.current_room.description}\n')
            print("_,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,_")
        except AttributeError:
            print("You cannot go that way")
    else:
        print('Error. Enter a direction (n, s, e, w)')