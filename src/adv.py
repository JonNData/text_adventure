from room import Room
from player import Player
import sys
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

# Room items
room['outside'].add_item("Dagger")
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
    player_input = input("Choose a direction ['n', 's', 'e', 'w'] or 'q' to quit: ").lower().split()
    # 1 word command
    if len(player_input) == 1:
        if player_input[0] == 'q' or player_input[0] == 'quit':
            print(f'Thanks for playing') 
            break

        if player_input[0] in directions:
            try:
                player.navigate(player_input[0])
                print(f'Location: {player.current_room.name} \nDescription: {player.current_room.description}\n')
                print("_,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,_")
            except AttributeError:
                print("You cannot go that way")
    # 2 word commands
    elif len(player_input) == 2:
        if player_input[0] == 'get':
            if player_input[1] not in room.items:
                print("Can only get items currently in the room")
            elif player_input[1] in room.items:
                player.get_item(player_input[1])
                room.grabbed_item()
            else:
                print("Invalid command")
                # check item in list of items, add to inventory, remove from room

    else:
        print('Error. Enter a direction (n, s, e, w)')