# Classe pour lister les événements
import pygame

class EventListener():
  # L'événement de démarrage du jeu
  def __init__(self, __game):
    self.game = __game
  
  # L'événement de fermeture du jeu
  def quit(self):
    self.game.running = False
    