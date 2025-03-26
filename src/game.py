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
                elif event.type == pygame.VIDEORESIZE:
                    # Redimensionner la fenêtre
                    if not Menu.fullscreen:
                        info = pygame.display.Info()
                        Menu.surface = pygame.display.set_mode((info.current_w, info.current_h), pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        Menu.fullscreen = not Menu.fullscreen  # Basculer l'état
                        if Menu.fullscreen:
                            # Passer en plein écran avec la résolution actuelle
                            info = pygame.display.Info()
                            Menu.width = info.current_w
                            Menu.height = info.current_h
                            Menu.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                            #Menu.surface = pygame.display.set_mode((Menu.surface.get_width(), Menu.surface.get_height()), pygame.FULLSCREEN)
                        else:
                            # Revenir en mode fenêtré
                            Menu.surface = pygame.display.set_mode((Menu.width, Menu.height), pygame.RESIZABLE)

            if Menu.main_menu.is_enabled():
                Menu.main_menu.update(events)
                Menu.main_menu.draw(Menu.surface)

            if Menu.start == 1:
                pygame.mixer.music.stop()
                self.player.update()
                self.draw() # Raffraichissement de l'écran

            pygame.display.update()
            self.clock.tick(60)
            #self.handle_events()
