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
        pygame.mixer.music.play(loops=-1)

        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(400, 300) # Le joueur
        self.menu = Menu()
        self.eventlistener = EventListener(self)
        self.arrow = Object(0, 0, self.assets.up_arrow)

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
                elif event.type == pygame.VIDEORESIZE:
                    # Redimensionner la fenêtre
                    if not self.menu.fullscreen:
                        info = pygame.display.Info()
                        self.menu.surface = pygame.display.set_mode((info.current_w, info.current_h), pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.menu.fullscreen = not self.menu.fullscreen  # Basculer l'état
                        if self.menu.fullscreen:
                            # Passer en plein écran avec la résolution actuelle
                            info = pygame.display.Info()
                            self.menu.width = info.current_w
                            self.menu.height = info.current_h
                            self.menu.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                            #Menu.surface = pygame.display.set_mode((Menu.surface.get_width(), Menu.surface.get_height()), pygame.FULLSCREEN)
                        else:
                            # Revenir en mode fenêtré
                            self.menu.surface = pygame.display.set_mode((self.menu.width, self.menu.height), pygame.RESIZABLE)

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
