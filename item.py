class item:
  def __init__(self, name, description, pos_x, pos_y, pos_z):
    self.name = name
    self.description = description
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.pos_z = pos_z

tool = [item("feather", "", 2, 0),
        item("old_note", "", 3, 0), 
        item("crystal_ball", "", 2, 1), 
        item("star_clues", "", 3, 2), 
        item("branches", "", 2, 3)]