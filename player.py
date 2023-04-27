import pygame

# creation d'une classe pour le personnage
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 0
        self.max_health = 50
        self.attack_animation = False
        self.attack_animation_right = False
        self.current_sprite = 0
        self.sprites_right = []
        # path = "assets/running/original_scale/"
        self.sprites_right.append(pygame.transform.scale(pygame.image.load('assets/running2.png'),(40,60)))
        self.sprites_right.append(pygame.transform.scale(pygame.image.load('assets/running3.png'),(40,60)))
        self.sprites_right.append(pygame.transform.scale(pygame.image.load('assets/running4.png'),(40,60)))
        self.sprites_left = []
        # path = "assets/running/original_scale/"
        self.sprites_left = self.sprites_right

        self.image = pygame.transform.scale(pygame.image.load('assets/running1.png'),(40,60))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.gravite = 10
        self.resistance = 0

    def graviter(self):
        self.rect.y += self.gravite + self.resistance

    def update_right(self, speed):
        if self.attack_animation_right is True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_right):
                self.current_sprite = 0
            self.image = self.sprites_right[int(self.current_sprite)]
        elif not self.attack_animation_right and not self.attack_animation:
            self.image = pygame.transform.scale(pygame.image.load('assets/running1.png'),(40,60))

    def update_left(self, speed):
        if self.attack_animation is True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_left):
                self.current_sprite = 0
            self.image = pygame.transform.flip(self.sprites_left[int(self.current_sprite)], True, False)
        elif not self.attack_animation_right and not self.attack_animation:
            self.image = pygame.transform.scale(pygame.image.load('assets/running1.png'),(40,60))
