import pygame
import sys
import os

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

    self.f11 = keys[pygame.K_F11]

class Colors:
  def __init__(self):
    self.black = (0, 0, 0)
    self.grey = (127, 127, 127)
    self.white = (255, 255, 255)

class Assets:
  def __init__(self):
    if getattr(sys, 'frozen', False):
      base_path = sys._MEIPASS  # Dossier temporaire PyInstaller
    else:
      base_path = os.path.abspath(".")

    assets_path = os.path.join(base_path, "assets")

    # Images
    images_path = os.path.join(assets_path, "images")
    arrows_path = os.path.join(images_path, "arrows")
    logos_path = os.path.join(images_path, "logos")
    skins_path = os.path.join(images_path, "skins")

    self.up_arrow = os.path.join(arrows_path, "up_arrow.png")
    self.down_arrow = os.path.join(arrows_path, "down_arrow.png")
    self.left_arrow = os.path.join(arrows_path, "left_arrow.png")
    self.right_arrow = os.path.join(arrows_path, "right_arrow.png")
    self.club_programmation = os.path.join(logos_path, "club_programmation.png")
    self.choqué = os.path.join(skins_path, "choqué.png")
    self.liep_background = os.path.join(images_path, "liep_background.png")

    # Fonts
    fonts_path = os.path.join(assets_path, "fonts")

    self.super_pixel = os.path.join(fonts_path, "SuperPixel.ttf")

    # Sounds
    sounds_path = os.path.join(assets_path, "sounds")

    self.fart = os.path.join(sounds_path, "fart.mp3")
    self.candyland = os.path.join(sounds_path, "Candyland.mp3")

class System:
  def __init__(self):
    self.MIN_WIDTH = 800
    self.MIN_HEIGHT = 450
  
def center(width, height):
  return [(800 - width) // 2, (450 - height) // 2]

def load_and_scale_image(image_path, size=(100, 100)):
    # Charge et redimensionne une image
    return pygame.transform.scale(pygame.image.load(image_path), size)