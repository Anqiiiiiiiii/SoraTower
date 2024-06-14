# import
import random

# global statement 
notWin = True


class Room:
    def __init__(self, name, description):
        """
        define object for Room
        """
        self.name = name
        self.description = description

    
    def print_description(self):
        """
        This function help  print out player current
        place description
        """
        print("\n************************************************")
        print(self.name + "\n")
        print(self.description)
        print("************************************************\n")
        return False


class starting_room(Room):
    def __init__(self, level, name, description, tool):
        """
        Define the object inside the starting_room class
        """
        self.level = level
        self.tool = tool
        Room.__init__(self, name, description)


    def print_description(self):
        """
        This function could print the description for each room
        """
        print("\n*************************************************")
        print(
            "You have entered the legendary Sky Tower--a world long forgotten")
        print("You are now entered in level: " + str(self.level))
        print("*************************************************\n")
        print(
            "The room ahead seems to be shrouded in mist. Venture forth bravely!"
        )
        print("\n*************************************************")
        print(self.name)
        print(self.description)
        print("*************************************************\n")
        return False


class ending_room(Room):
    def __init__(self, name, description, tool):
        """
        Define the object inside the ending_room 
        """
        self.tool = tool
        Room.__init__(self, name, description)


    def print_description(self):
        """
        This function help  print out player current
        place description for ending room
        """
        print(self.name)
        print(self.description)
        return False
        

class puzzle_room(Room):
    """
    Define the object inside the puzzle_room 
    """
    def __init__(self, name, description, description2, answer, tool):
        self.description2 = description2
        self.answer = answer
        self.tool = tool
        Room.__init__(self, name, description)


    def solve_puzzle(self):
        """
        THis function could help to justify if the puzzle answer from
        player is right or wrong
        """
        print(self.description2)
        player_answer = input("please enter your answer in number form: ")
        if self.answer == player_answer:
            print("You are Right!\n")
            puzzle_right = True
        else:
            print("You are Wrong!\n")
            puzzle_right = False
        return puzzle_right

    
    def print_description(self):
        """
        This function help  print out player current
        place description for puzzle room
        """
        print(
            "Welcome, you seem to be just one step away from the key to this level!"
        )
        print("\nSolve the following puzzle to continue forward!")
        print(self.name)
        print(self.description)
        return self.solve_puzzle()


class normal_room(Room):
    def __init__(self, name, description, tool, tool_description):
        """
        Define the object inside the normal_room
        """
        self.tool = tool
        self.tool_description = tool_description
        Room.__init__(self, name, description)

# all of the puzzle room settings
puzzle_room_list = [
    puzzle_room(
        "Puzzle1",
        "Dear adventure, here are a list of number, try to find the order," +
        " and fill in the blank", '2, 5, 11, 23, 47, "blank"', "95", "item"),
    puzzle_room(
        "Puzzle2", "Dear adventure, here is an not define intergral," +
        "try to solve for the answer!(make sure no space inside the answer",
        "∫(2x+4)dx", "x^2+4x+c", "item"),
    puzzle_room(
        "Puzzle3",
        "Dear adventure, here is a simple function, please sovlve for x",
        "2x+3 = 11", "4", "item"),
    puzzle_room(
        "Puzzle4",
        "Dear adventure, here is a simple function, please sovlve for x",
        "x^2 - 144 = 0 and x>0", "12", "item"),
    puzzle_room(
        "Puzzle5", "Dear adventure, please choose from following element" +
        "Form Sulfuric Acid by using two of the following element",
        "H2  SO4  Cn  Cl  Zn\nS X C O NH4", "H2SO4", "item")
]

# Define and setting rooms
level_1st = starting_room(
    1, "cloudy_realm",
    "The room is filled with a sea of swirling clouds, with ethereal light" 
    + "filtering through, creating a dreamlike atmosphere.",
    "item"
)
level_2st = starting_room(
    2, "windy_plateau",
    "The starting room is an open terrace with strong winds whipping around," 
    + "carrying the faint sounds of distant chimes.",
    "item"
)
level_3st = starting_room(
    3, "starry_sanctuary",
    "This room is illuminated by a celestial glow, with constellations" 
    + "twinkling on the walls and a serene, otherworldly ambiance.",
    "item"
)
level_4st = starting_room(
    4, "stormy_ascent",
    "The room is dark and turbulent, with flashes of lightning illuminating" 
    + "the stone walls and the sound of thunder echoing around.",
    "item"
)
level_5st = starting_room(
    5, "radiant_dawn",
    "The starting room is bathed in the golden light of a perpetual sunrise," 
    + "with warm rays piercing through the translucent windows and casting" 
    + "long shadows.",
    "item"
)

foggy_room = normal_room(
    "foggy_alcove", "A small, mist-filled chamber with soft, diffused light",
    "glowing compass",
    "glowing compass lies on a stone pedestal, ready to guide your way.")
wind_tunnel = normal_room(
    "wind_tunnel",
    " This narrow corridor is swept by constant, gentle breezes", "wind chime",
    "a wind chime hangs in the corner, its melody hinting at hidden paths.")
celecstial_chamber = normal_room(
    "Celestial Chamber", "A room adorned with murals of stars and galaxies",
    "starlight lantern",
    "a starlight lantern rests on a shelf, illuminating dark corners.")
glistening_cave = normal_room(
    "glistening_cave", "The walls shimmer with a crystalline sheen",
    "rope ladder",
    "a rope ladder is coiled near a rocky outcrop, perfect for reaching higher places."
)
echoing_hall = normal_room(
    "echoing_hall", "An expansive hall where every sound reverberates",
    "silver whistle",
    "a silver whistle is placed on a marble table, able to summon helpful echoes."
)
misty_bridge = normal_room(
    "misty_bridge", " A stone bridge spans a chasm filled with thick fog",
    "spool of enchanted thread",
    "a spool of enchanted thread is tied to the railing, useful for marking your path."
)
sunlit_atrium = normal_room(
    "sunlit_atrium",
    "A bright room with a high glass ceiling, flooding the area with sunlight",
    "reflective mirror",
    "a reflective mirror leans against the wall, capable of revealing hidden messages."
)
whispering_grove = normal_room(
    "whispering_grove",
    "This room is filled with gently rustling leaves and soft whispers",
    " wooden flute",
    "a wooden flute lies among the roots, its notes revealing secret passages."
)
final_room = ending_room(
    "crystal_room","In the center of the room stands a majestic pedestal,holding the" 
    + "Sky Crystal, its radiant energy pulsing gently, awaiting the touch of the" 
    + "one who has conquered the tower's challenges.",
    "item")


