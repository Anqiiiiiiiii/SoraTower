from _typeshed import Self

puzzle_right = False
class Room:
    def __init__(self, tool, name, description):
        """
        define object for Room
        """
        self.tool = tool
        self.name = name
        self.description = description

    def print_description(self):
        """
        This function help  print out player current
        place description
        """
        print(self.name)
        print(self.description)

class starting_room(Room):
    def __init__(self, level):
        self.level = level

    def start_introduction(self):
        print("Welcome,brave advanturer." 
              + "You have entered the legendary Sky Tower--a world long forgotten")
        print("You are now entered in " + str(self.level) + "\n")
        print("The room ahead seems to be shrouded in mist. Venture forth bravely!")

class puzzle_room(Room):
    def __init__(self, num, answer):
        self.num = num
        self.answer = answer

    
    def welcome_introduction(self):
        print("Welcome, you seem to be just one step away from the key to this level!")
        print("\nSolve the following puzzle to continue forward!")

    def npc_conversarion(self):
        pass

    def math1(self):
        puzzle_room.welcome_introduction(self)
        print("Dear adventure, here are a list of number, try to find the order," 
              + " and fill in the blank")
        print((2, 5, 11, 23, 47, "blank"))
        self.answer = input("please enter your answer in number form: ")
        if self.answer == "95":
            puzzle_right = True
        else:
            puzzle_right = False

    def math2(self):
        puzzle_room.welcome_introduction(self)
        print("Dear adventure, here is an not define intergral, try to solve for the answer!")
        print("\n" + "∫(2x+4)dx")
        self.answer = input("please enter your answer in euqtaion form: ")
        if self.answer.lower() == "x^2 + 4x + C" or "x^2+4x+c":
            puzzle_right = True
        else:
            puzzle_right = False

    def math3(self):
        puzzle_room.welcome_introduction(self)
        print("Dear adventure, here is a simple function, please sovlve for x")
        print("\n" + "2x+3 = 11")
        self.answer == input("please enter your answer in number form:")
        if self.answer == "4":
            puzzle_right = True
        else:
            puzzle_right = False

    def chem1(self):
        puzzle_room.welcome_introduction(self)
        print("Dear adventure, please choose from following element" 
              + "which two could form sulfuric acid?")
        print("H2  SO4  Cn  Cl  Zn\nS X C O NH4")
        self.answer == input("Please enter  your answer: ")
        if self.answer.lower() == "H2SO4":
            puzzle_right = True
        else:
            puzzle_right = False
    def chem2(self):
        puzzle_room.welcome_introduction(self)