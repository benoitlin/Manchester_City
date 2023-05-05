import pygame, sys

from game import Game
import interface
pygame.init()

# charger notre jeu
running = True
is_playing = False
game = Game()
# permet de maintenir la fenetre ouverte
while running:
    # regler les images/s
    pygame.time.Clock().tick(120)
    # lancer le jeu
    interface.main_menu()
    # update la fenetre
    pygame.display.flip()
    pygame.display.update()
    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # verifier si event est fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False