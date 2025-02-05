# Classe principale
import pygame
from game import Game

def main():
    # Appel de la classe jeu (game.py) Démmarage du jeu
    pygame.init()
    game = Game()
    game.run()
    # Fermeture du jeu
    pygame.quit()

# RG n'as rien compris là
if __name__ == "__main__":
    main()