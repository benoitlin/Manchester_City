import pygame,sys
pygame.init()
from game import Game


game = Game()

# Fenetre du jeu
pygame.display.set_caption("Dodge Game")
screen = pygame.display.set_mode((1280, 720))

# import du menu 1
menu = pygame.image.load('assets/menu_1.png')


# importer charger notre boutton start, rules, exit et back
start_button = pygame.image.load("assets/play_button.png")
start_button = pygame.transform.scale(start_button,(380, 100))
start_button_rect = start_button.get_rect()
start_button_rect.x = screen.get_width()/2.9
start_button_rect.y = screen.get_width()/3.7

rules_button = pygame.image.load("assets/rules_button.png")
rules_button = pygame.transform.scale(rules_button,(60, 60))
rules_button_rect = rules_button.get_rect()
rules_button_rect.x = screen.get_width()/1.9
rules_button_rect.y = screen.get_width()/2.6

exit_button = pygame.image.load("assets/exit_button.png")
exit_button = pygame.transform.scale(exit_button,(60, 60))
exit_button_rect = exit_button.get_rect()
exit_button_rect.x = screen.get_width()/2.3
exit_button_rect.y = screen.get_width()/2.6

back_button = pygame.image.load("assets/Replay_button.png")
back_button = pygame.transform.scale(back_button,(60, 60))
back_button_rect = back_button.get_rect()
back_button_rect.x = screen.get_width()/2.1
back_button_rect.y = screen.get_width()/2


mode_1_button = pygame.image.load("assets/mode_1_button.png")
mode_1_button = pygame.transform.scale(mode_1_button,(250, 350))
mode_1_button_rect = mode_1_button.get_rect()
mode_1_button_rect.x = screen.get_width()/3.8
mode_1_button_rect.y = screen.get_width()/5

mode_2_button = pygame.image.load("assets/mode_2_button.png")
mode_2_button = pygame.transform.scale(mode_2_button,(250, 350))
mode_2_button_rect = mode_2_button.get_rect()
mode_2_button_rect.x = screen.get_width()/1.9
mode_2_button_rect.y = screen.get_width()/5


def start():

    # permet de maintenir la fenetre ouverte
    while True:

        # import du menu
        game_mode = pygame.image.load('assets/game_mode.png')

        # appliquer le fond 'game mode' dans la fenetre avec le bouton back
        screen.blit(game_mode, (0, 0))
        screen.blit(mode_1_button, mode_1_button_rect)
        screen.blit(mode_2_button, mode_2_button_rect)
        screen.blit(back_button, back_button_rect)

        # appliquer le fond 'game mode' dans la fenetre avec le choix des 2 modes
        for event in pygame.event.get():

            # verifier si on click bien sur le bouton back
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    main_menu()
                # verifier mode de jeu 1 ou 2
                if mode_1_button_rect.collidepoint(event.pos):
                    mode_1()
                if mode_2_button_rect.collidepoint(event.pos):
                    mode_2()

            # verifier si envent est fermeture de la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # verifier si on click bien sur le bouton back
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    main_menu()
        # mettre à jour la fenetre
        pygame.display.flip()
def rules():

    # permet de maintenir la fenetre ouverte
    while True:

        # import du fond avec les regles et le bouton back
        rules = pygame.image.load('assets/rules_interface.png')

        # appliquer le fond 'rule' et le bouton back
        screen.blit(rules, (0, 0))
        screen.blit(back_button, back_button_rect)

        for event in pygame.event.get():
            # verifier si envent est fermeture de la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # verifier si on click bien sur le bouton back
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    main_menu()
        # mettre à jour la fenetre
        pygame.display.flip()


def mode_1():
    import main

def mode_2():
    print("mode 2")

def main_menu():
    while True:
        # appliquer le background dans la fenetre
        screen.blit(menu, (0,0))

        # verifier si notre jeu a commencer ou pas
        if game.is_playing:

            # declencher les intructions de la partie
            game.update(screen)

        # verifier si notre jeu n'a pas commencé
        else:
            # afficher le menu 1 avec le fond + les bouttons
            screen.blit(start_button, (start_button_rect))
            screen.blit(rules_button, rules_button_rect)
            screen.blit(exit_button, exit_button_rect)
            screen.blit(back_button, back_button_rect)

        # verifier si le joueur ferme la fenetre
        for event in pygame.event.get():

            # verifier si event est fermeture de la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # detecter si un joueur click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # verrifier si on click bien sur le boutton start, rules, exit ou back
                if start_button_rect.collidepoint(event.pos):
                    start()
                if rules_button_rect.collidepoint(event.pos):
                    rules()
                if exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                if back_button_rect.collidepoint(event.pos):
                    # revenir sur le menu 1
                    main_menu()

        # mettre à jour la fenetre
        pygame.display.flip()


main_menu()