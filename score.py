import pygame

class Score:
    def __init__(self):
        self.score = pygame.font.Font(None, 50)
        self.time = pygame.time.get_ticks()/1000
        self.print_time = pygame.font.Font.render(self.score, "00:00,000", True, (0, 0, 0))
        self.time_min = 0
    def affichage_time(self):
        self.time = pygame.time.get_ticks()/1000
        if self.time%100 > 60:
            self.time_min += 1
            print(self.time)
        self.print_time = pygame.font.Font.render(self.score, "{:0>2} : {:4.3f}".format(self.time_min, self.time), True, (0, 0, 0))
