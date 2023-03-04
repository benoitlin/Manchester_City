import pygame, random

# class pour l'evenement des projectiles
class ProjectileEvent:
    def __init__(self):
        self.all_asteroid = pygame.sprite.Group()
        self.time = pygame.time.get_ticks()
        self.cooldown = 5000
    def asteroid_shoot(self):
            self.all_asteroid.add(Asteroid())
    def projectile_attempt(self):
        now = pygame.time.get_ticks()
        if now - self.time >= self.cooldown:
            self.asteroid_shoot()
            self.time = now

# class pour l'asteroid
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/asteroidtest.png')
        self.var_X = 0
        self.rect = self.image.get_rect()
        self.rect.x = 1280
        self.rect.y = 300
        self.var_spawn = random.randint(0,500)
    def trajectoire(self):
        # vélocité x :
        self.rect.x -= 5
        # vélocité y :
        # pour changer la vitesse du projectile, changer self.rect.x et self.var_X
        # pour changer la cloche, changer le multiplicateur de self.rect.y
        self.var_X += 0.1
        self.rect.y = self.var_spawn + (0.2 * self.var_X ** 2 - 5 * self.var_X)*5