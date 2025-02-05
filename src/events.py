import pygame

class EventListener():
  def __init__(self, __game):
    self.game = __game
  
  def quit(self):
    self.game.running = False
    