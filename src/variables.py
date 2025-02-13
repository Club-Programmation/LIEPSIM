import pygame

class Keys:
  def __init__(self):
    # Touches du clavier
    keys = pygame.key.get_pressed()
    self.enter = keys[pygame.K_RETURN]
    self.space = keys[pygame.K_SPACE]
    self.esc = keys[pygame.K_ESCAPE]

    self.up = keys[pygame.K_UP] or keys[pygame.K_z]
    self.down = keys[pygame.K_DOWN] or keys[pygame.K_s]
    self.left = keys[pygame.K_LEFT] or keys[pygame.K_q]
    self.right = keys[pygame.K_RIGHT] or keys[pygame.K_d]

class Colors:
  def __init__(self):
    self.black = (0, 0, 0)
    self.grey = (127, 127, 127)
    self.white = (255, 255, 255)

class Images:
  def __init__(self):
    images = "assets/images/"
    arrows = images + "arrows/"
    logos = images + "logos/"
    skins = images + "skins/"

    self.up_arrow = arrows + "up_arrow.png"
    self.down_arrow = arrows + "down_arrow.png"
    self.left_arrow = arrows + "left_arrow.png"
    self.right_arrow = arrows + "right_arrow.png"
    self.club_programmation = logos + "club_programmation.jpg"
    self.choqué = skins + "choqué.png"

def center(width, height):
  return [(800 - width) // 2, (600 - height) // 2]

def load_and_scale_image(image_path, size=(100, 100)):
    # Charge et redimensionne une image
    return pygame.transform.scale(pygame.image.load(image_path), size)