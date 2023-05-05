import pygame,sys,random
from player import Player
from projectile import ProjectileEvent, Asteroid
from plateforme import Plateforme
from score import Score

# creer une classe qui va representer notre jeu
class Game :
    def __init__(self):
        # generer nos variables
        # mode de jeu
        self.mode = 0
        self.asteroid = Asteroid(ProjectileEvent, self.mode)
        self.player = Player()
        self.projectileEvent = ProjectileEvent(self.mode)
        self.score = Score()
        self.plateforme_liste_rect = [pygame.Rect(0, 500, 1300, 10), pygame.Rect(10, 400, 100, 10),
                                pygame.Rect(500, 400, 300, 10), pygame.Rect(1000, 400, 100, 10),
                                pygame.Rect(300, 420, 100, 10)]

        self.plateforme_liste_rect.append(pygame.Rect(random.randint(0, 400), random.randint(280, 320) // 10 * 10, random.randint(100, 200), 10))
        self.plateforme_liste_rect.append(pygame.Rect(random.randint(450, 800), random.randint(280, 320) // 10 * 10, random.randint(100, 200), 10))
        self.plateforme_liste_rect.append(pygame.Rect(random.randint(840, 1200), random.randint(280, 320) // 10 * 10, random.randint(100, 200), 10))
        self.plateforme_liste_rect.append(pygame.Rect(random.randint(0, 400), random.randint(180, 230) // 10 * 10, random.randint(100, 200), 10))
        self.plateforme_liste_rect.append(pygame.Rect(random.randint(450, 800), random.randint(180, 230) // 10 * 10, random.randint(100, 200), 10))
        self.plateforme_liste_rect.append(pygame.Rect(random.randint(840, 1200), random.randint(180, 230) // 10 * 10, random.randint(100, 200), 10))
        self.plateforme = Plateforme(self.plateforme_liste_rect)
        self.pressed = {}
        # savoir si le jeu est lancee ou non
        self.is_playing = False
        # variable plateforme
        self.jump = False
        self.stopJump = False
        self.jumpCount = 0
        self.jumpMax = 15
        self.delay = 18
        self.counting = 15
        # Fenetre du jeu
        pygame.display.set_caption("Dodge Game")
        self.screen = pygame.display.set_mode((1280, 720))

        # import du background
        self.background = pygame.image.load('assets/Background.png')
        self.background = pygame.transform.scale(self.background, (1280, 720))

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
        self.game_over = pygame.transform.scale(self.game_over, (1280, 720))

    def update(self):
        self.is_playing=True
        # appliquer l'image du background
        self.screen.blit(self.background, (0, 0))
        # appliquer l'image du player
        self.screen.blit(self.player.image, self.player.rect)
        for p in self.plateforme_liste_rect:  # Permet de savoir si un joueur touche une plateforme et les afficher
            plat = Plateforme(p)
            plat.afficher(self.screen)
            if (self.player.rect.midbottom[1] // 10 * 10 == plat.rect.top) and self.player.rect.colliderect(p):
                self.player.resistance = -10
                self.stopJump = False
                self.counting = 15
            if self.counting == 0:
                self.player.resistance = 0
            else:
                self.counting -= 1
        # verifier si le joueur souhaite aller a gauche ou a droite ou sauter
        keys = pygame.key.get_pressed()
        if self.player.rect.x >= 0 and self.player.rect.x + self.player.rect.width < self.screen.get_width():
            self.player.rect.x = (self.player.rect.x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5)
            if keys[pygame.K_RIGHT]:
                self.player.attack_animation = False
                self.player.attack_animation_right = True
            elif keys[pygame.K_LEFT]:
                self.player.attack_animation_right = False
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
        if keys[pygame.K_SPACE] and not self.jump and self.player.resistance == -10 :
            self.jump = True
            self.stopJump = True
            self.jumpCount = self.jumpMax

        # verifier le saut sur la plateforme
        if self.jump:
            self.player.resistance = -10
            self.player.rect.y -= self.jumpCount
            if self.jumpCount > 0:
                self.jumpCount -= 1
                self.delay = 24
            elif self.jumpCount == 0 and self.delay != 0 and self.stopJump:
                self.player.resistance = 0
                self.delay -= 1
            else:
                self.jump = False
        self.player.graviter()
        self.update_projectile()
        self.update_score()
        self.fin()
    def update_projectile(self):
        # Initialisation pour le mode 2 :
        if self.mode == 2:
            self.projectileEvent.cooldown = 500
        # Initialisation pour le mode 3 :
        elif self.mode == 3:
            self.projectileEvent.cooldown = 1000
        self.projectileEvent.projectile_attempt(self.mode)
        for self.asteroid in self.projectileEvent.all_asteroid:
            self.asteroid.verif_collision()
        self.projectileEvent.all_asteroid.draw(self.screen)
    def update_score(self):
        if self.mode != 3:
            for self.asteroid in self.projectileEvent.all_asteroid:
                if self.player.rect.colliderect(self.asteroid.rect):
                    self.player.health -= 1
                    self.asteroid.suppr_asteroid()
                    print(self.player.health)
            # afficher les vies
            self.score.affichage_vie(self.player.health)
            self.screen.blit(self.score.icone, (0, 0))
            self.screen.blit(self.score.print_vie, (65, 35))
        else:
            for self.asteroid in self.projectileEvent.all_asteroid:
                if self.player.rect.colliderect(self.asteroid.rect):
                    self.player.hearth += 1
                    self.asteroid.suppr_asteroid()
                    print(self.player.hearth)
            # afficher les coeurs
            self.score.affichage_vie(self.player.hearth)
            self.screen.blit(self.score.icone, (0, 0))
            self.screen.blit(self.score.print_vie, (65, 35))
        self.score.affichage_time()
        self.screen.blit(self.score.print_time, (500, 0))
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
        elif self.player.hearth == 10:
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