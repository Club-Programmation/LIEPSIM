# boite de collisions
class Hitbox:
  def __init__(self, pos1, pos2):
    self.pos1 = pos1
    self.pos2 = pos2
  def update(self, pos1, pos2):
    self.pos1 = pos1
    self.pos2 = pos2

def checkCollision(h1,h2):
  # on verifie si la h2 est dans la h1
  if h2.pos2[0]-h1.pos2[0] <= 0 and h2.pos1[0]-h1.pos1[0] >= 0 and h2.pos1[1]-h1.pos1[1] <= 0 and h2.pos2[1]-h1.pos2[1] >= 0 or h2.pos2[0]-h1.pos1[0] >= 0 and h2.pos1[0]-h1.pos2[0] <= 0 and h2.pos1[1]-h1.pos2[1] <= 0 and h2.pos2[1]-h1.pos1[1] >= 0: 
     return True
  return False

H1 = Hitbox((0,0),(10,10))
H2 = Hitbox((10,10),(15,15))
if checkCollision(H1,H2):
  print("vamos a ir al instituto") # True
  