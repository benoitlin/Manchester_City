import pygame
from player import Player
from projectile import ProjectileEvent, Asteroid
from plateforme import Plateforme

# creer une classe qui va representer notre jeu
class Game :

    def __init__(self):
        # generer notre joueur
        self.asteroid = Asteroid()
        self.player = Player()
        self.projectileEvent = ProjectileEvent()
        self.pressed = {}
        # savoir si le jeu est lancé ou non
        self.is_playing = False
        self.jump = False
        self.jumpCount = 0
        self.jumpMax = 15
        self.plateforme_liste_rect = [pygame.Rect(800, 300, 300, 50), pygame.Rect(0, 150, 300, 50)]

    def update(self, screen):
        # appliquer l'image du player
        screen.blit(self.player.image, self.player.rect)

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

        for p in self.plateforme_liste_rect:
            plat = Plateforme(p)
            plat.afficher(screen)
            if self.player.rect.midbottom[1] // 10 * 10 == plat.rect.top and self.player.rect.colliderect(p):
                self.player.resistance = -10
                jump = False
    def update_projectile(self, screen):
        self.projectileEvent.projectile_attempt()
        for asteroid in self.projectileEvent.all_asteroid:
            asteroid.trajectoire_type()
        self.projectileEvent.all_asteroid.draw(screen)