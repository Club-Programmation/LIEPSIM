import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (100, 100))
        width, height = self.image.get_size()
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

"""class Wall(Object):
  def __init__(self, x, y):
    super().__init__()"""
