import map as m

calive = True
character_file = "characterSetting.txt"

class Character:
  """
  define the initial variable for character
  """
  
  def __init__(self, name, pos_x, pos_y, pos_z, hp):
    self.name = name
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.pos_z = pos_z
    self.hp = hp


class npc(Character):
  """
  define the initial variable for npc character
  """
  def __init__(self, name, pos_x, pos_y, pos_z, hp, speech):
    self.speech = speech
    Character.__init__(self, name, pos_x, pos_y, pos_z, hp)

  """
  This function allow npc to talk and define npc's location
  """
  def talk(self):
    print("\nYou meet " + self.name + "!")
    print(self.name + ':"' + self.speech + '"')
    self.pos_x = -1
    self.pos_y = -1


class player(Character):
  """
  define the initial variable for player
  """
  def __init__(self, name, pos_x, pos_y, pos_z, hp, backpack):
    self.backpack = backpack
    Character.__init__(self, name, pos_x, pos_y, pos_z, hp)

  def explore(self):
    """
    This function allow user to explore the things in the map 
    and decide if they want to pick up or not
    """
    result = m.sora_tower.map[self.pos_z][self.pos_x][self.pos_y].tool
    if result == "item":
        print("\nThere is nothing here")
    else:
        print("\nYou found " + result + "\n" +
             m.sora_tower.map[PlayerAn.pos_z][PlayerAn.pos_x][PlayerAn.pos_y].tool_description)
        print("\nScavengers, Do you want to pick up the tool?")
        pick_tool = input("Enter Yes/No: ")
        if pick_tool.lower() == "yes":
            self.backpack.append(result)
        elif pick_tool.lower() == "no":
            print("Respect your choice Scavnger!")
        else:
            print("Opps, Wrong input!") 

  
  def move(self):
    """
    This function allow player move and choose the direction they 
    want to go when they choose walk in last menu
    """
    print("\nChoose the direction from following list\n" +
          "Enter 'quit' if you want to quit")
    wrongInput = True
    while wrongInput:
      try:
        movement = input("Where do you want to go? ")
      except ValueError:
        print("Please enter in write form Scavanger.")
      else:
        if movement.lower() == "north":
          if self.pos_x == 0:
            print("You can't go North!")
          else:
            self.pos_x = self.pos_x - 1
            wrongInput = False
        elif movement.lower() == "south":
          if self.pos_x == m.sora_tower.map_length - 1:
            print("You can't go South!")
          else:
            self.pos_x = self.pos_x + 1
            wrongInput = False
        elif movement.lower() == "east":
          if self.pos_y == m.sora_tower.map_width - 1:
            print("You can't go East!")
          else:
            self.pos_y = self.pos_y + 1
            wrongInput = False
        elif movement.lower() == "west":
          if self.pos_y == 0:
            print("You can't go West!")
          else:
            self.pos_y = self.pos_y - 1
            wrongInput = False

def meet_npc(player):
  """
  This function allow player meet the npc when 
  they are in the specific position that the npc
  is locate
  """
  global calive
  for npc in npc_list:
      if player.pos_z == npc.pos_z and player.pos_x == npc.pos_x and player.pos_y == npc.pos_y:
          npc.talk()


PlayerAn = player("AnQi", 0, 0, 0, 5, [])
npc_list = [
    npc(
        "Zepjur", 1, 0, 0, 0,
        "In the early days, our people thrived here among the clouds, living in harmony with the winds and skies. I spent countless years documenting our history, carving our stories into the very clouds you see around us."
    ),
    npc(
        "Gale", 1, 0, 1, 0,
        "This plateau was once the training ground for our fiercest warriors. I defended our kingdom from countless threats, wielding the power of the wind to keep our enemies at bay and our people safe."
    ),
    npc(
        "Astra", 1, 0, 2, 0,
        "I have gazed into the cosmos from this sanctuary, reading the movements of the stars to guide our people. The constellations have long told the fate of Sora Kingdom, and I have seen both our rise and our fall within their patterns."
    ),
    npc(
        "Tempest", 1, 0, 3, 0,
        "I ventured through the fiercest storms of this tower, mapping the treacherous paths and uncovering lost relics of our ancestors. Each thunderclap and lightning strike tells a story of resilience and the relentless spirit of our people."
    ),
    npc(
        "Astra", 0, 1, 4, 0,
        "In this room of perpetual dawn, I have healed many wounds and mended countless hearts. The light of the Radiant Dawn has always symbolized hope and renewal for our kingdom, guiding us through our darkest times and into a brighter future."
    )
]

#Save the game
def save_game():
  global PlayerAn
  with open(character_file, 'w') as file:
    file.write(PlayerAn.name + "," + str(PlayerAn.pos_x) + "," 
               + str(PlayerAn.pos_y) + "," + str(PlayerAn.pos_z) + "," 
               + str(PlayerAn.hp))
  
    if PlayerAn.backpack != []:
      file.write("\n")
      for i in range(len(PlayerAn.backpack) - 1):
        file.write(PlayerAn.backpack[i] + ",")
  
      file.write(PlayerAn.backpack[len(PlayerAn.backpack) - 1])
  
#Read the game
def read_game():
  global PlayerAn
  with open(character_file, 'r') as file:
    player_info_str = file.readline()
    if player_info_str:
      player_info = player_info_str.strip().split(",")
      PlayerAn.name = player_info[0]
      PlayerAn.pos_x = int(player_info[1])
      PlayerAn.pos_y = int(player_info[2])
      PlayerAn.pos_z = int(player_info[3])
      PlayerAn.hp = int(player_info[4])
      player_backpack_str = file.readline()
      if player_backpack_str:
        PlayerAn.backpack = player_backpack_str.strip().split(",")
    else:
      print("There is nothing to load!")




