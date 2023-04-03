import pygame
from player import Player
from projectile import ProjectileEvent, Asteroid
from plateforme import Plateforme
from score import Score



# creer une classe qui va representer notre jeu
class Game :

    def __init__(self):
        # generer notre joueur
        self.asteroid = Asteroid(ProjectileEvent)
        self.player = Player()
        self.projectileEvent = ProjectileEvent()
        self.score = Score()
        self.pressed = {}
        # savoir si le jeu est lancÃ© ou non
        self.is_playing = False
        self.jump = False
        self.jumpCount = 0
        self.jumpMax = 15
        self.plateforme_liste_rect = [pygame.Rect(800, 385, 300, 50), pygame.Rect(0, 150, 300, 50)]

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
            asteroid.verif_collision()
        self.projectileEvent.all_asteroid.draw(screen)

    def update_score(self, screen):
        # afficher les vies
        font = pygame.font.SysFont('Verdana', 25, 0)
        score_text = font.render(f"{self.player.health}", 1, (255, 0, 0))
        screen.blit(score_text, (60, 35))
        screen.blit(self.player.image, self.player.rect)

        screen.blit(self.score.print_time, (500, 0))
        self.score.affichage_time()
        icone = pygame.image.load('assets/score_icone.png')
        icone = pygame.transform.scale(pygame.image.load('assets/score_icone.png'), (80, 80))
        screen.blit(icone, (0, 0))


        for self.asteroid in self.projectileEvent.all_asteroid:
            if self.player.rect.colliderect(self.asteroid.rect):
                self.player.health -= 1
                self.asteroid.suppr_asteroid()
                print(self.player.health)
