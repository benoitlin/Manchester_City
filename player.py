import pygame


# creation d'une classe pour le personnage
class Player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.possible = True
        self.health = 15
        self.max_health = 15
        self.velocity_x = 5
        self.velocity_y = 1
        self.image = pygame.image.load('assets/AmongUsBenoit.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 400

        self.saut = 0
        self.saut_montee = 0
        self.saut_descente = 2
        self.nombre_de_saut = 0
        self.a_sauter = False
        self.ground = True
    def move_right(self):
        self.rect.x += self.velocity_x
    def move_left(self):
        self.rect.x -= self.velocity_x
    def jump(self):
        if self.possible :
            if self.saut_montee >= 10 :

                self.saut_descente -= 1
                self.saut = self.saut_descente
            else:
                self.saut_montee += 1
                self.saut = self.saut_montee

            if self.saut_descente < 0:
                self.saut_montee = 0
                self.saut_descente = 5
                self.possible = False

        self.rect.y -= (10 * (12 / 2))
    def gravite(self):
        if self.ground and self.rect.y < 400:
            self.rect.y += (10 * (8 / 2))
            if self.rect.y > 400:
                self.ground = False
            self.ground = True
