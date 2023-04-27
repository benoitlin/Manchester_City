import pygame,sys
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
        self.plateforme_liste_rect = [pygame.Rect(0, 500, 1300, 10), pygame.Rect(20, 150, 150, 10),
                                      pygame.Rect(10, 400, 100, 10), pygame.Rect(500, 400, 300, 10),
                                      pygame.Rect(1000, 400, 100, 10), pygame.Rect(300, 420, 100, 10),
                                      pygame.Rect(300, 150, 200, 10)]
        self.plateforme = Plateforme(self.plateforme_liste_rect)
        self.pressed = {}
        # savoir si le jeu est lancee ou non
        self.is_playing = False
        self.jump = False
        self.jumpCount = 0
        self.jumpMax = 15

        # Fenetre du jeu
        pygame.display.set_caption("Dodge Game")
        self.screen = pygame.display.set_mode((1280, 600))

        # import du background
        self.background = pygame.image.load('assets/Background.png')
        self.background = pygame.transform.scale(self.background, (1280, 600))

        self.bg_pause = pygame.image.load('assets/bg_pause.png')
        self.screen_width, self.screen_height = self.screen.get_size()
        self.bg_pause = pygame.transform.scale(self.bg_pause, (self.screen_width, self.screen_height))

        self.resume = pygame.image.load('assets/resume.png')
        self.resume = pygame.transform.scale(self.resume, (400, 150))
        self.resume_rect = self.resume.get_rect()
        self.resume_rect.x = self.screen.get_width() / 3
        self.resume_rect.y = 70

        self.exit = pygame.image.load('assets/exit.png')
        self.exit = pygame.transform.scale(self.exit, (400, 150))
        self.exit_rect = self.exit.get_rect()
        self.exit_rect.x = self.screen.get_width() / 3
        self.exit_rect.y = 380

        self.rules = pygame.image.load('assets/rules.png')
        self.rules = pygame.transform.scale(self.rules, (400, 150))
        self.rules_rect = self.rules.get_rect()
        self.rules_rect.x = self.screen.get_width() / 3
        self.rules_rect.y = 225

        self.game_over = pygame.image.load('assets/game_over.png')
        self.game_over = pygame.transform.scale(self.game_over, (1280, 600))

    def update(self):
        self.is_playing=True
        # verifier si le joueur souhaite aller a gauche ou a droite ou sauter
        keys = pygame.key.get_pressed()
        if self.player.rect.x >= 0 and self.player.rect.x + self.player.rect.width < self.screen.get_width():
            self.player.rect.x = (self.player.rect.x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5)
            if keys[pygame.K_RIGHT]:
                self.player.attack_animation_right = True

            elif keys[pygame.K_LEFT]:
                self.player.attack_animation = True
            else:
                self.player.attack_animation_right = False
                self.player.attack_animation = False
            # verifier si le joueur souhaite mettre sur pause
            if keys[pygame.K_ESCAPE]:
                self.pause()
        elif self.player.rect.x > 800:
            self.player.rect.x = self.player.rect.x - 1
        else:
            self.player.rect.x = self.player.rect.x + 1

        # verifier le saut
        if self.pressed.get(pygame.K_SPACE) and not self.plateforme.jump:
            self.plateforme.jump = True
            self.plateforme.stopJump = True
            self.plateforme.jumpCount = self.plateforme.jumpMax

        # verifier le saut sur la plateforme
        if self.plateforme.jump:
            self.player.resistance = -10
            self.player.rect.y -= self.plateforme.jumpCount
            if self.plateforme.jumpCount > 0:
                self.plateforme.jumpCount -= 1
                self.plateforme.delay = 24
            elif self.plateforme.jumpCount == 0 and self.plateforme.delay != 0 and self.plateforme.stopJump:
                self.player.resistance = 0
                self.plateforme.delay -= 1
            else:
                self.jump = False
        # appliquer l'image du background
        self.screen.blit(self.background, (0, 0))
        # appliquer l'image du player
        self.screen.blit(self.player.image, self.player.rect)
        self.plateforme_update()
        self.player.graviter()
        self.update_projectile()
        self.update_score()
        self.fin()
    def plateforme_update(self):
        for p in self.plateforme_liste_rect:  # Permet de savoir si un joueur touche une plateforme et les afficher
            plat = Plateforme(p)
            plat.afficher(self.screen)
            if self.player.rect.midbottom[1] // 10 * 10 == plat.rect.top and self.player.rect.colliderect(p):
                self.player.resistance = -10
                self.plateforme.stopJump = False
                self.plateforme.counting = 15
            if self.plateforme.counting == 0:
                self.player.resistance = 0
            else:
                self.plateforme.counting -= 1
    def update_projectile(self):
        self.projectileEvent.projectile_attempt()
        for self.asteroid in self.projectileEvent.all_asteroid:
            self.asteroid.verif_collision()
        self.projectileEvent.all_asteroid.draw(self.screen)
    def update_score(self):
        # afficher les vies
        self.score.affichage_vie(self.player.health)
        self.screen.blit(self.score.icone, (0, 0))
        self.screen.blit(self.score.print_vie, (65, 35))
        self.score.affichage_time()
        self.screen.blit(self.score.print_time, (500, 0))
        for self.asteroid in self.projectileEvent.all_asteroid:
            if self.player.rect.colliderect(self.asteroid.rect):
                self.player.health -= 1
                self.asteroid.suppr_asteroid()
                print(self.player.health)
    def pause(self):
        paused = True
        self.score.time_pause_tmp = pygame.time.get_ticks() / 1000
        self.screen.blit(self.bg_pause, (0, 0))
        self.screen.blit(self.resume, self.resume_rect)
        self.screen.blit(self.exit, self.exit_rect)
        self.screen.blit(self.rules, self.rules_rect)
        pygame.display.update()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.resume_rect.collidepoint(event.pos):
                        paused = False
                        self.score.time_pause += (pygame.time.get_ticks() / 1000) - self.score.time_pause_tmp
                    # elif rules_rect.collidepoint(event.pos):
                    # rules()
                    elif self.exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
    def fin(self):
        if self.player.health == 0:
            fin = True
            while fin:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.exit_rect.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()
                self.screen.blit(self.game_over, (0, 0))
                pygame.display.update()