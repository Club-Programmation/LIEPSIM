import pygame

class Variables:
  def __init__(self):
    self.keys = pygame.key.get_pressed()
    self.KEY_LEFT = self.keys[pygame.K_LEFT] or self.keys[pygame.K_q]
    self.KEY_RIGHT = self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]
    self.KEY_UP = self.keys[pygame.K_UP] or self.keys[pygame.K_z]
    self.KEY_DOWN = self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]