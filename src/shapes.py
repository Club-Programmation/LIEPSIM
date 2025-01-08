import pygame

class Shape:
  def __init__(self, color, position):
    self.color = color
    self.position = position

class Rectangle(Shape):
  def __init__(self, color, width, height):
    super().__init__(color)
    self.width = width
    self.height = height
    self.rect = pygame.Rect(position, width, height)

  def draw(self, screen):
    pygame.draw.rect(screen, self.color, self.rect)

class Circle(Shape):
  def __init__(self, color, radius):
    super().__init__(color)
    self.radius = radius