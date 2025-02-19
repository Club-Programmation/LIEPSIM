import pygame
from player import Player
from menu import Menu
from events import EventListener
from objects import *
from variables import *

class Game:
    # Fonction de création de la fenêtre du jeu
    # Résolution : 800x600
    def __init__(self):
        self.colors = Colors()
        self.images = Images()

        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(400, 300) # Le joueur
        self.eventlistener = EventListener(self)
        self.arrow = Object(0, 0, self.images.up_arrow)

    # Fonction pour gérer les événements
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or Keys().esc:
                self.eventlistener.quit()

    # Fonction de dessin
    def draw(self):
        Menu.surface.fill(self.colors.grey)
        self.player.draw(Menu.surface)
        self.arrow.draw(Menu.surface)
        pygame.display.flip()

    # Boucle de jeu principale
    def run(self):
        while self.running:
            Menu.mainmenu.mainloop(Menu.surface)
            self.handle_events()
            self.player.update()
            self.draw() # Raffraichissement de l'écran
            self.clock.tick(60)
