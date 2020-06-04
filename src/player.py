# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:


    def __init__(self, name, location, items):

        self.name = name
        self.location = location
        self.items = items

    def status(self):
        
        print(f"You are currently here: {self.location.name}")

        print("---------------------------")
        print(self.location.description)

        print("---------------------------")
        
        print(f"these items are in the room: {self.location.items}")
        print(f"currently you carry these items: {self.items}")

        print("---------------------------")

    def pick_or_drop(self):

        decision = input("""would you like to pick up or drop an item?
        type "yes" or "no": """)

        if decision == "yes":

            if len(self.items) == len(self.location.items) == 0:

                print("I am sorry but this is currently not possible")

            elif len(self.items) == 0:

                decision = input("""please type in what item you would like to pick up: """)

            elif len(self.location.items) == 0:

                decision = input("""please type in what item you would like to drop: """)

            else:

                decision = input("""would you like to pick something up or drop something?: """)


        elif decision == "no":

            pass

        else:
            print("""please type "yes" or "no" """)
            pick_or_drop()

    def move(self):
        
        move = input("Where would you like to go next?: ")

        if move == "q":

            exit()
        
        if move in ["n", "s", "w", "e"]:
            
            if move == "n":
                
                if self.location.n_to == None:
                    
                    print("Unfortunately you cannot go this way")
                    self.move()
                else:
                    self.location = self.location.n_to
                
            elif move == "s":
                
                if self.location.s_to == None:
                    
                    print("Unfortunately you cannot go this way")
                    self.move()
                else:
                    self.location = self.location.s_to
                
            elif move == "w":
                
                if self.location.w_to == None:
                    
                    print("Unfortunately you cannot go this way")
                    self.move()
                else:
                    self.location = self.location.w_to
                    
            else:
                
                if self.location.e_to == None:
                    
                    print("Unfortunately you cannot go this way")
                    self.move()
                else:
                    self.location = self.location.e_to
                  
        else:
            print("Please type n, s, w or e to indicate the direction you want to go")
            self.move()
        
