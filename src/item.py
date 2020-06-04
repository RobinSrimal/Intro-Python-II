class Item:

    def __init__(self, name, description):

        self.name = name
        self.description = description


class Warg(Item):

    def tell_story(self):


        print("random story")


class Compass(Item):

    def show_way(self):

        print("right direction")


class Armor(Item):

    def put_on_armor(self):

        print("oh no you died")
