import pygame
from player import Player
from menu import Menu
from events import EventListener
from objects import *
from variables import *

class Game:
    # Fonction de création de la fenêtre du jeu
    # Résolution : 800x450
    def __init__(self):
        self.colors = Colors()
        self.assets = Assets()

        pygame.mixer.music.load(self.assets.candyland)
        pygame.mixer.music.play()

        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(400, 300) # Le joueur
        self.eventlistener = EventListener(self)
        self.arrow = Object(0, 0, self.assets.up_arrow)

    # Fonction pour gérer les événements
    #def handle_events(self):
        # for event in pygame.event.get():
        #    if event.type == pygame.QUIT or Keys().esc:
        #        self.eventlistener.quit()

    # Fonction de dessin
    def draw(self):
        Menu.surface.fill(self.colors.grey)
        self.player.draw(Menu.surface)
        self.arrow.draw(Menu.surface)
        pygame.display.flip()

    # Boucle de jeu principale
    def run(self):
        Menu.menu_init(Menu())
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            if Menu.main_menu.is_enabled():
                Menu.main_menu.update(events)
                Menu.main_menu.draw(Menu.surface)

            if Menu.start==1:
                pygame.mixer.music.stop()
                self.player.update()
                self.draw() # Raffraichissement de l'écran

            pygame.display.update()
            self.clock.tick(60)
            #self.handle_events()
