import pygame, sys
from game import Game

pygame.init()
pygame.font.init()
# Fenetre du jeu
pygame.display.set_caption("Dodge Game")
screen = pygame.display.set_mode((1280, 600))

# import du background
background = pygame.image.load('assets/Background.png')
background = pygame.transform.scale(background,(1280,600))

# charger notre jeu
game = Game()

running = True

# permet de maintenir la fenetre ouverte
while running:
    pygame.time.Clock().tick(120)

    # appliquer le background dans la fenetre
    screen.blit(background, (0, 0))

    game.update(screen)
    game.update_projectile(screen)
    game.update_score(screen)
    game.player.update_right(0.5)
    game.player.update_left(0.5)

    # mettre à jour la fenetre
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # verifier si event est fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False