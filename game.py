import pygame
from player import Player
from projectile import ProjectileEvent, Asteroid

# creer une classe qui va representer notre jeu
class Game :

    def __init__(self):
        # generer notre joueur
        self.player = Player()
        self.projectile = ProjectileEvent()
        self.pressed = {}
        # savoir si le jeu est lancé ou non
        self.is_playing = False

        self.jump = False
        self.jumpCount = 0
        self.jumpMax = 15


    def update(self, screen):
        # appliquer l'image du player
        screen.blit(self.player.image, self.player.rect)

        self.player.update()

        # verifier si le joueur souhaite aller a gauche ou a droite ou sauter
        keys = pygame.key.get_pressed()
        if self.player.rect.x >= 0 and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.rect.x = (self.player.rect.x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5)
        elif self.player.rect.x > 800:
            self.player.rect.x = self.player.rect.x - 1
        else:
            self.player.rect.x = self.player.rect.x + 1

        if self.pressed.get(pygame.K_SPACE) and not (self.jump):
            self.jump = True
            self.jumpCount = self.jumpMax

        if self.jump:
            self.player.rect.y -= self.jumpCount
            if self.jumpCount > - self.jumpMax:
                self.jumpCount -= 1
            else:
                self.jump = False

    def update_projectile(self, screen):
        self.projectile.projectile_attempt()
        for asteroid in self.projectile.all_asteroid:
            asteroid.trajectoire()
        self.projectile.all_asteroid.draw(screen)