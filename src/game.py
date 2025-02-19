import pygame
from player import Player
from menu import Menu

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(20, 250)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()

    def draw(self):
        Menu.surface.fill((127, 127, 127))
        self.player.draw(Menu.surface)
        pygame.display.flip()

    def run(self):
        while self.running:
            Menu.mainmenu.mainloop(Menu.surface)
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
