import random

import pygame

class Player(pygame.sprite.Sprite):
    # Initialisation du joueur.
    # @param x - Coordonnées X du joueur ; en fonction du coin supérieur gauche.
    # @param y - Coordonnées Y du joueur ; en fonction du coin supérieur gauche.
    def __init__(self, x, y):
        super().__init__()
        # chokbarifié
        self.image = pygame.transform.scale(pygame.image.load("assets/images/choqué.png"), (200, 200))
        scaled_sprite = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # mettre le rectangle en x,y
        self.rect.topleft = (x,y)
        self.color = (255, 255, 255)
        self.speed = 5

    # Fonction UPDATE afin de mettre à jour les données du joueur
    # Actuellement :
    # - Mouvement ZQSD
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]: # Q ou left arrow
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: # D ou right arrow
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_z]: # Z ou up arrow
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: # S ou down arrow
            self.rect.y += self.speed

    # 
    def draw(self, screen):
        screen.blit(self.image, self.rect) # draw
        pygame.display.flip()
