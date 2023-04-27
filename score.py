import pygame
pygame.font.init()
class Score:
    def __init__(self):
        self.time_font = pygame.font.Font("assets/DigitaldreamFat.ttf", 40)
        self.score_font = pygame.font.Font("assets/RepetitionScrolling.ttf", 35)
        self.time_init = 0
        self.time_pause_tmp = 0
        self.time_pause = 0
        self.time_sec = 0
        self.time_min = 0
        self.print_time = pygame.font.Font.render(self.time_font, "00:00,000", True, (0, 0, 0))
        self.icone = pygame.image.load('assets/score_icone.png')
        self.icone = pygame.transform.scale(pygame.image.load('assets/score_icone.png'), (80, 80))
    def affichage_time(self):
        self.time_sec = (pygame.time.get_ticks() / 1000) - (self.time_init + self.time_pause)
        if self.time_sec >= 60 * (self.time_min + 1):
            self.time_min += 1
        self.print_time = pygame.font.Font.render(self.time_font, "{:0>2.0f}:{:4.3f}".format(self.time_min, self.time_sec - 60 * self.time_min), True, (255, 255, 255))
    def affichage_vie(self, player_health):
        self.print_vie = pygame.font.Font.render(self.score_font,"{}".format(player_health), True, (255, 255, 255))

    def affichage_time_fin(self):
        self.print_time = pygame.font.Font.render(self.time_font, "{:0>2.0f}:{:4.3f}".format(self.time_min, self.time_sec - 60 * self.time_min), True, (255, 255, 255))
