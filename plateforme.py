import pygame
class Plateforme(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.rect = rect
        self.jump = False
        self.stopJump = True
        self.plateforme_player = False
        self.jumpCount = 0
        self.jumpMax = 15
        self.delay = 18
        self.counting = 15
    def afficher(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.rect)