import random
import room as r
from tabulate import tabulate

map_file = "map.txt"
puzzle_file = "puzzle.txt"

room_order = []
sora_tower_map = []
sora_tower = None

class current_map:
  def __init__(self, map):
    self.map = map
    self.map_length = len(self.map[0][0])
    self.map_width = len(self.map[0])
    self.map_level = len(self.map)

  def __getitem__(self, index, index1, index2):
    return self.map[index][index1][index2]

def create_puzzle_order():
  global room_order
  i = random.randint(0, len(r.puzzle_room_list) - 1)
  
  for i in range(len(r.puzzle_room_list)):
      room_order.append(i)
  
  random.shuffle(room_order)

def write_puzzle_order():
  global room_order
  with open(puzzle_file, 'w') as file:
    for i in range(len(room_order) - 1):
      file.write(str(room_order[i]) + ",")

    file.write(str(room_order[len(room_order) - 1]))

def read_puzzle_order():
  global room_order
  try:
    with open(puzzle_file, 'r') as file:
      room_info_str = file.readline()
      room_info = room_info_str.strip().split(",")
      room_order=[]
      for i in range(len(room_info)):
        room_order.append(int(room_info[i]))
      initial_map()

  except ValueError:
    print("There is no map been saved!")
  else:
    print("Existing map loading")
  finally:
    print("Map loaded correctly!")
    

def initial_map():
  global sora_tower
  global sora_tower_map

  sora_tower_map = []

  sora_tower = current_map(
    [
      [[r.level_1st, r.wind_tunnel],
      [r.foggy_room, r.puzzle_room_list[room_order[0]]]],
      
      [[r.level_2st, r.celecstial_chamber],
      [r.echoing_hall, r.puzzle_room_list[room_order[1]]]],
      
      [[r.level_3st, r.misty_bridge],
      [r.glistening_cave, r.puzzle_room_list[room_order[2]]]],
      
      [[r.level_4st, r.sunlit_atrium],
      [r.whispering_grove, r.puzzle_room_list[room_order[3]]]],
      
      [[r.level_5st, r.celecstial_chamber],
      [r.puzzle_room_list[room_order[4]], r.final_room]]
    ])
  
  
  for i in range(len(sora_tower.map)):
    sora_tower_map.append([])
    for j in range(len(sora_tower.map[i])):
      sora_tower_map[i].append([])
      for k in range(len(sora_tower.map[i][j])):
        sora_tower_map[i][j].append(sora_tower.map[i][j][k].name)
      
  try:
    with open(map_file, 'w') as file:
      for i in sora_tower_map:
        file.write(tabulate(i, tablefmt='fancy_grid'))
        file.write("\n")
    with open(map_file, "r") as f:
        f2 = f.readlines()
  except FileNotFoundError:
    print("there is an error opening file!\n")
  else:
    for line in f2:
        print(line)
  finally:
    print("\n")