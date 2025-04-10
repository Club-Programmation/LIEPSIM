import pygame
from variables import *
from menu import Menu

class Player(pygame.sprite.Sprite):
    # Initialisation du joueur
    # @param x - Coordonnées X du joueur ; en fonction du coin supérieur gauche.
    # @param y - Coordonnées Y du joueur ; en fonction du coin supérieur gauche.
    def __init__(self, x, y):
        super().__init__()
        self.assets = Assets()
        self.menu = Menu()

        self.animation = False

        #self.rect = pygame.Rect(center(width, height)[0], center(width, height)[1], width, height)
        
        self.frame_index = 0 
        self.animation_speed = 15 # Ca change de frame toutes les 15 boucles du jeu
        self.counter = 0 # Ca sert pour plus tard

        self.speed = 5 # Vitesse du joueur fixe
        self.direction = "right" # On dit que le perso commence en regardant vers la droite

    def function_animation(self, order):
        # Listes d'images pour chaque animation

        if self.animation == False:

            self.walk_up = [
                load_and_scale_image(self.assets, order),
                load_and_scale_image2(self.assets.up_arrow)
            ]
            self.walk_down = [
                load_and_scale_image(self.assets, order),
                load_and_scale_image2(self.assets.down_arrow)
            ]
            self.walk_left = [
                load_and_scale_image(self.assets, order),
                load_and_scale_image2(self.assets.left_arrow)
            ]
            self.walk_right = [
                load_and_scale_image(self.assets, order),
                load_and_scale_image2(self.assets.right_arrow)
            ]

            # Image de départ
            self.image = self.walk_right[0]  # On commence à la première frame
            width, height = self.image.get_size()
            x, y = center(width, height)
            self.rect = pygame.Rect(x, y, width, height)

            self.animation = True

    def update(self):
        moving = False
        keys = Keys()
        
        """if keys.up:
            self.rect.y -= self.speed
            self.direction = "up"
            moving = True
        if keys.down:
            self.rect.y += self.speed
            self.direction = "down"
            moving = True
        if keys.left: 
            self.rect.x -= self.speed
            self.direction = "left"
            moving = True
        if keys.right:
            self.rect.x += self.speed
            self.direction = "right"
            moving = True"""
        # Dictionnaire pour gérer les déplacements en fonction des touches
        directions = {
            'up': (0, -self.speed),
            'down': (0, self.speed),
            'left': (-self.speed, 0),
            'right': (self.speed, 0)
        }

        # Vérification des touches et mise à jour de la position
        for direction, (dx, dy) in directions.items():
            if getattr(keys, direction): # Vérifie si la touche correspondant à la direction est pressée
                self.rect.x += dx
                self.rect.y += dy
                self.direction = direction
                moving = True
                break
        
        if Keys().esc:
            Menu.start = 0
            pygame.mixer.music.play()
            self.menu.menu_init()
            self.menu.main_menu.force_surface_update()
        
        # Fonction de l'animation
        if moving:
            self.counter += 1
            if self.counter >= self.animation_speed:
                self.counter = 0  # Reset le counter
                self.frame_index = (self.frame_index + 1) % len(self.walk_right)  # Permet de faire une boucle qui revient à la 1ère frame
        else:
            self.frame_index = 0  # Quand le perso bouge pas il est toujours à la 1ère frame

        # Ca affiche l'animation en fonction de la direction du personnage (WIP)
        match self.direction:
            case "up":
                self.image = self.walk_up[self.frame_index]
            case "down":
                self.image = self.walk_down[self.frame_index]
            case "left":
                self.image = self.walk_left[self.frame_index]
            case "right":
                self.image = self.walk_right[self.frame_index]

    # Fonction récurrente de dessin
    def draw(self, screen):
        screen.blit(self.image, self.rect)
