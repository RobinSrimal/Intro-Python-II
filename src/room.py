# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    n_to = None
    s_to = None
    w_to = None
    e_to = None
    
    def __init__(self, name, description,items):
        self.name = name
        self.description = description
        self.items = items

