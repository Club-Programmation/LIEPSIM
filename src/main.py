import pygame
from game import Game
from variables import *

def main():
    # Appel de la classe jeu (game.py) 
    # Démmarage du jeu
    pygame.init()
    logo = pygame.image.load(Images().club_programmation)
    pygame.display.set_caption('LIEPSIM')
    pygame.display.set_icon(logo)
    game = Game()
    game.run()
    # Fermeture du jeu
    pygame.quit()

if __name__ == "__main__":
    main()
