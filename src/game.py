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
        self.menu = Menu()
        self.eventlistener = EventListener(self)
        self.arrow = Object(0, 0, self.assets.up_arrow)

    # Fonction pour gérer les événements
    #def handle_events(self):
        # for event in pygame.event.get():
        #    if event.type == pygame.QUIT or Keys().esc:
        #        self.eventlistener.quit()

    # Fonction de dessin
    def draw(self):
        self.menu.surface.fill(self.colors.grey)
        self.player.draw(self.menu.surface)
        self.arrow.draw(self.menu.surface)
        pygame.display.flip()

    # Boucle de jeu principale
    def run(self):
        self.menu.menu_init()
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            if self.menu.main_menu.is_enabled():
                self.menu.main_menu.update(events)
                self.menu.main_menu.draw(self.menu.surface)

            if self.menu.start==1:
                pygame.mixer.music.stop()
                self.player.function_animation(self.menu.order)
                self.player.update()
                self.draw() # Raffraichissement de l'écran

            pygame.display.update()
            self.clock.tick(60)
            #self.handle_events()
