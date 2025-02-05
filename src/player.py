# Classe déstiné pour le joueur
import pygame

class Player(pygame.sprite.Sprite):
    # Initialisation du joueur.
    # @param x - Coordonnées X du joueur ; en fonction du coin supérieur gauche.
    # @param y - Coordonnées Y du joueur ; en fonction du coin supérieur gauche.    
    def __init__(self, x, y):
        super().__init__()

        # On créé les listes d'images pour chaque animation
        self.walk_right = [
            pygame.transform.scale(pygame.image.load("assets/images/choqué.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("assets/images/right_arrow.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("assets/images/up_arrow.png"), (100, 100))
        ]
        # Couleur de peau ???????? (RG)
        self.color = (255, 255, 255)

        # Là ça définit l'image de départ
        self.image = self.walk_right[0] # On commence à la première frame
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        
        self.frame_index = 0 
        self.animation_speed = 5  # Ca change de frame toutes les 5 boucles du jeu
        self.counter = 0  # Ca sert pour plus tard

        self.speed = 5 # Vitesse du joueur fixe
        self.direction = "right"  # On dit que le perso commence en regardant vers la droite

    def update(self):
        keys = pygame.key.get_pressed() # Quelles touches sont appuiyées
        moving = False # Le joueur ne bouge pas

        # Mécaniques de mouvement        
        if keys[pygame.K_LEFT] or keys[pygame.K_q]: 
            self.rect.x -= self.speed
            self.direction = "left"
            moving = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = "right"
            moving = True
        if keys[pygame.K_UP] or keys[pygame.K_z]: # Z ou up arrow
            self.rect.y -= self.speed
            self.direction = "up"
            moving = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: # S ou down arrow
            self.rect.y += self.speed
            self.direction = "down"
            moving = True
            
        # Fonction de l'animation
        if moving:
            self.counter += 1
            if self.counter >= self.animation_speed:
                self.counter = 0  # Reset le counter
                self.frame_index = (self.frame_index + 1) % len(self.walk_right)  # Permet de faire une boucle qui revient à la 1ère frame
        else:
            self.frame_index = 0  # Quand le perso bouge pas il est toujours à la 1ère frame

        # Ca affiche l'animation en fonction de la direction du personnage (WIP)
        # J'aurais mis un match-case statement si Python 3.10
        if self.direction == "right":
            self.image = self.walk_right[self.frame_index]

    # Fonction récurrente de dessin
    def draw(self, screen):
        screen.blit(self.image, self.rect) # draw
        pygame.display.flip()

