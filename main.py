import pygame, sys
from game import Game
from plateforme import Plateforme

pygame.init()

# Fenetre du jeu
pygame.display.set_caption("Dodge Game")
screen = pygame.display.set_mode((1280, 600))

# import du background
background = pygame.image.load('assets/Background_fire.png')

# charger notre jeu
game = Game()

running = True

# permet de maintenir la fenetre ouverte


jump = False
jumpCount = 0
jumpMax = 15
plateforme_liste_rect = [pygame.Rect(800, 300, 300, 50), pygame.Rect(0, 150, 300, 50)]

while running:
    pygame.time.Clock().tick(75)

    # appliquer le background dans la fenetre
    screen.blit(background, (0, 0))

    # appliquer l'image du player
    screen.blit(game.player.image, game.player.rect)

    game.update_projectile(screen)

    for p in plateforme_liste_rect:
        plat = Plateforme(p)
        plat.afficher(screen)
        if game.player.rect.midbottom[1] // 10 * 10 == plat.rect.top and game.player.rect.colliderect(p):
            game.player.resistance = -10
            jump = False


    # verifier si le joueur souhaite aller a gauche ou a droite ou sauter
    keys = pygame.key.get_pressed()
    if game.player.rect.x >= 0 and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.rect.x = (game.player.rect.x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5)
    elif game.player.rect.x > 800:
        game.player.rect.x = game.player.rect.x - 1
    else:
        game.player.rect.x = game.player.rect.x + 1

    if game.pressed.get(pygame.K_SPACE) and not (jump):
        jump = True
        jumpCount = jumpMax

    if jump:
        game.player.rect.y -= jumpCount
        if jumpCount > -jumpMax:
            jumpCount -= 1
        else:
            jump = False

            # mettre à jour la fenetre
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # verifier si envent est fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        pygame.display.flip()