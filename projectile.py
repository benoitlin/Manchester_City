import pygame, random

# class pour l'evenement des projectiles
class ProjectileEvent:
    def __init__(self, mode):
        self.all_asteroid = pygame.sprite.Group()
        self.time = pygame.time.get_ticks()
        self.cooldown = 2000

    def asteroid_add(self, mode):
        self.all_asteroid.add(Asteroid(self, mode))

    def projectile_attempt(self, mode):
        now = pygame.time.get_ticks()
        if now - self.time >= self.cooldown:
            self.asteroid_add(mode)
            self.time = now


# class pour l'asteroid
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, ProjectileEvent, mode):
        super().__init__()
        self.mode = mode
        self.image = pygame.image.load('assets/asteroid.png')
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = 1280
        self.rect.y = 300
        self.var_y = 0
        self.var_x = random.randint(3,5)
        self.var_z = random.randint(-3,3)
        self.var_spawn = random.randint(0,550)
        self.var_cloche = random.randint(5,8)
        self.var_trajectoire_type = random.randint(1,3)
        self.ProjectileEvent = ProjectileEvent
        # Initialisation pour le mode 2 :
        if self.mode == 2:
            self.var_x = random.randint(8, 12)
            self.var_z = random.randint(-6, 6)
        # Initialisation pour le mode 3 :
        elif self.mode == 3:
            self.image = pygame.image.load('assets/coeurs_newmode_1.png')
            self.image = pygame.transform.scale(self.image, (30, 25))

    def verif_collision(self):
        # vérifier si elle sort de l'écran et la supprimé si besoin
        if self.rect.x < 5:
            self.suppr_asteroid()
        if self.rect.y < 10:
            self.var_z = - self.var_z
        elif self.rect.y > 470:
            self.var_z = - self.var_z
        self.trajectoire_type()
    def trajectoire_type(self):
        # choix du type de trajectoire
        if self.var_trajectoire_type == 1 and self.mode == 1:
            self.image = pygame.image.load("assets/asteroid2.png")
            self.image = pygame.transform.scale(self.image, (30, 30))
            self.trajectoire_parabolique()
        elif self.var_trajectoire_type == 1 and self.mode == 3:
            self.trajectoire_parabolique()
        elif self.var_trajectoire_type == 1 and self.mode == 2:
            self.image = pygame.image.load("assets/asteroid2.png")
            self.image = pygame.transform.scale(self.image, (30, 30))
            self.trajectoire_parabolique_2()
        else:
            self.trajectoire_lineaire()
    def trajectoire_parabolique(self):
        # vélocité x :
        self.rect.x -= 5
        # vélocité y :
        # pour changer la vitesse du projectile, changer self.rect.x et self.var_X
        # pour changer la cloche, changer le multiplicateur de self.rect.y
        self.var_y += 0.1
        self.rect.y = self.var_spawn + (0.2 * self.var_y ** 2 - 5 * self.var_y) * self.var_cloche
        self.asteroid_rotation()
    def trajectoire_lineaire(self):
        self.rect.x -= self.var_x
        if self.var_y == 0:
            self.rect.y = self.var_spawn
            self.var_y = 1
        else:
            self.rect.y += self.var_z
    def suppr_asteroid(self):
        self.ProjectileEvent.all_asteroid.remove(self)
    def asteroid_rotation(self):
        pass
    def trajectoire_parabolique_2(self):
        # vélocité x :
        self.rect.x -= 10
        # vélocité y :
        # pour changer la vitesse du projectile, changer self.rect.x et self.var_y
        # pour changer la cloche, changer le multiplicateur de self.rect.y
        self.var_y += 0.2
        self.rect.y = self.var_spawn + (0.2 * self.var_y ** 2 - 5 * self.var_y) * self.var_cloche
        self.asteroid_rotation()

