import pygame

class Score:
    def __init__(self):
        self.score = pygame.font.Font(None, 50)
        self.time_sec = pygame.time.get_ticks()/1000
        self.time_min = 0
        self.print_time = pygame.font.Font.render(self.score, "00:00,000", True, (0, 0, 0))
    def affichage_time(self):
        self.time_sec = pygame.time.get_ticks() / 1000
        if self.time_sec >= 60 * (self.time_min + 1):
            self.time_min += 1
        self.print_time = pygame.font.Font.render(self.score, "{:0>2.0f} : {:4.3f}".format(self.time_min, self.time_sec - 60 * self.time_min), True, (0, 0, 0))