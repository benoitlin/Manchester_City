import pygame, sys
from game import Game
from plateforme import Plateforme
import score
pygame.init()
pygame.font.init()

# variables utilisées

jump = False
stopJump = True
plateforme_player = False
jumpCount = 0
jumpMax = 15
delay = 18
plateforme_liste_rect = [pygame.Rect(800, 290, 100, 50), pygame.Rect(0, 150, 300, 50), pygame.Rect(0,400,1000,50)]
counting = 15

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

    game.update_projectile(screen)
    game.update_score(screen)
    game.player.update(0.5)

    game.player.update_right(1)
    game.player.update_left(1)


    # appliquer l'image du player
    screen.blit(game.player.image, game.player.rect)

    for p in plateforme_liste_rect:  # Permet de savoir si un joueur touche une plateforme et les affiche
        plat = Plateforme(p)
        plat.afficher(screen)
        if game.player.rect.midbottom[1] // 10 * 10 == plat.rect.top and game.player.rect.colliderect(p):
            game.player.resistance = -10
            stopJump = False
            counting = 5
        if counting == 0:
            game.player.resistance = 0
        else:
            counting -= 1

    # verifier si le joueur souhaite aller a gauche ou a droite ou sauter
    keys = pygame.key.get_pressed()
    if game.player.rect.x >= 0 and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.rect.x = (game.player.rect.x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5)
        if keys[pygame.K_RIGHT] :
            game.player.attack_animation_right = True

        elif keys[pygame.K_LEFT] :
            game.player.attack_animation = True
        else :
            game.player.attack_animation_right = False
            game.player.attack_animation = False
    elif game.player.rect.x > 800:
        game.player.rect.x = game.player.rect.x - 1
    else:
        game.player.rect.x = game.player.rect.x + 1

    if game.pressed.get(pygame.K_SPACE) and not (jump):
        jump = True
        stopJump = True
        jumpCount = jumpMax

    if jump:
        game.player.resistance = -10
        game.player.rect.y -= jumpCount
        if jumpCount > 0:
            jumpCount -= 1
            delay = 24
        elif jumpCount == 0 and delay != 0 and stopJump:
            game.player.resistance = 0
            delay -= 1
        else:
            jump = False


    game.player.graviter()

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