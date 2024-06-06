mapFile = "map.txt"
class currentMap:
  def __init__(self, map):
    self.map = map
    self.mapLength = len(self.map[0])
    self.mapWidth = len(self.map)

class levelRoom:
  def __init__(self, tool):
    self.tool = tool

soraTower = currentMap(
  [["starting_room", 1, 2, "puzzle_room"],
   ["starting_room", 3, 4, "puzzle_room"],
   ["starting_room", 5, 6, "puzzle_room"],
   ["starting_room", 7, 8, "puzzle_room"]
  ] )

  