  
# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room, items=[]):
        super().__init__()
        self.name = name
        self.current_room = current_room
        self.items = items
        
    def __str__(self):
        return f'Name: {self.name}, Room: {self.current_room}'
    
    def navigate(self, direction):
        self.current_room = getattr(self.current_room, f'{direction}_to')
    
    def get_item(self, item):
        self.items.append(item)