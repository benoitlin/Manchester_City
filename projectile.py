import pygame, random

# class pour l'evenement des projectiles
class ProjectileEvent:
    def __init__(self):
        self.all_asteroid = pygame.sprite.Group()
        self.time = pygame.time.get_ticks()
        self.cooldown = 1000

    def asteroid_add(self):
        self.all_asteroid.add(Asteroid())

    def projectile_attempt(self):
        now = pygame.time.get_ticks()
        if now - self.time >= self.cooldown:
            self.asteroid_add()
            self.time = now


# class pour l'asteroid
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/asteroid.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 1280
        self.rect.y = 300
        self.var_y = random.randint(-2,2)
        self.var_x = 0
        self.var_spawn = random.randint(0,550)
        self.var_cloche = random.randint(5,8)
        self.var_trajectoire_type = random.randint(1,3)
    def trajectoire_type(self):
        if self.var_trajectoire_type == 1:
            self.trajectoire_parabolique()
        else:
            self.trajectoire_lineaire()
    def trajectoire_parabolique(self):
        # vélocité x :
        self.rect.x -= 5
        # vélocité y :
        # pour changer la vitesse du projectile, changer self.rect.x et self.var_X
        # pour changer la cloche, changer le multiplicateur de self.rect.y
        self.var_x += 0.1
        self.rect.y = self.var_spawn + (0.2 * self.var_x ** 2 - 5 * self.var_x) * self.var_cloche
        self.asteroid_rotation()
    def trajectoire_lineaire(self):
        self.rect.x -= 2
        if self.var_x == 0:
            self.rect.y = self.var_spawn
            self.var_x = 1
        else:
            self.rect.y += self.var_y
    def asteroid_rotation(self):
        pass