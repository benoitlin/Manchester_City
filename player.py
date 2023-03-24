import pygame


# creation d'une classe pour le personnage
class Player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.possible = True
        self.health = 5
        self.max_health = 5
        self.attack_animation = False
        self.attack_animation_right = False
        self.current_sprite = 0
        self.sprites_right = []
        # path = "assets/running/original_scale/"
        self.sprites_right.append(pygame.transform.scale(pygame.image.load('assets/running2.png'), (100, 100)))
        self.sprites_right.append(pygame.transform.scale(pygame.image.load('assets/running3.png'), (100, 100)))
        self.sprites_right.append(pygame.transform.scale(pygame.image.load('assets/running4.png'), (100, 100)))
        self.sprites_left = []
        # path = "assets/running/original_scale/"
        self.sprites_left.append(pygame.transform.scale(pygame.image.load('assets/running2_left.png'), (100, 100)))
        self.sprites_left.append(pygame.transform.scale(pygame.image.load('assets/running3_left.png'), (100, 100)))
        self.sprites_left.append(pygame.transform.scale(pygame.image.load('assets/running4_left.png'), (100, 100)))
        self.image = pygame.transform.scale(pygame.image.load('assets/running1.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.velocity_x = 5
        self.velocity_y = 1
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
    def update_right(self, speed):
        if self.attack_animation_right is True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_right):
                self.current_sprite = 0
            self.image = self.sprites_right[int(self.current_sprite)]
        else:
            self.image = pygame.transform.scale(pygame.image.load('assets/running1.png'), (100, 100))

    def update_left(self, speed):
        if self.attack_animation is True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_left):
                self.current_sprite = 0
            self.image = self.sprites_left[int(self.current_sprite)]
        else:
            self.image = pygame.transform.scale(pygame.image.load('assets/running1.png'), (100, 100))