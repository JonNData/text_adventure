  
# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        super().__init__()
        self.name = name
        self.description = description
        self.items = items
    
    def room_items(self):
        print("You see {self.items} in the room")

    
    def __str__(self):
        return f'{self.name} - {self.description}'