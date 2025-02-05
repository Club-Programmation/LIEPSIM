import pygame
from player import Player
from events import EventListener

class Game:
    # Fonction de création de la fenêtre du jeu Résolution : 800x600 (digne d'un jeu des années 2000)
    def __init__(self):
        # Résolution de 800 x 600
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock() # Valentin wtf
        self.running = True
        self.player = Player(20, 250) # Le joueur
        self.eventlistener = EventListener(self)

    # Fonction pour gérer les événements
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.eventlistener.quit()
    
    # Raffraichissement de l'écran
    def update(self):
        self.player.update()

    # Fonction de dessin
    def draw(self):
        self.screen.fill((127, 127, 127))
        self.player.draw(self.screen)
        pygame.display.flip()

    # Boucle de jeu principale
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
