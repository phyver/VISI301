import pygame


import pygame
from pygame.locals import *

# définition de quelques couleurs
BLACK = (0,0,0)
GREEN = (0,0,255)


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # taille de la fenêtre principale
    width = 480
    height = 640

    window = pygame.display.set_mode((width, height))

    # position initiale de la raquette
    x = width // 2      # milieu de l'écran
    y = height - 50     # attention, les coordonnées y partent du haut de la fenêtre

    while True:

        # on récupère les évènements clavier
        # pour un jeu en tour par tour, il semblerait qu'il faille utiliser
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_q:
        #             ...
        #         if event.key == K_LEFT:
        #             x += ...
        #             ...
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        # si la touche "q" est utilisée, on quitte
        if keys[K_q]:
            print(">> QUIT")
            break

        # les flèches changent la coordonnée x de la raquette
        if keys[K_LEFT]:
            print(">> LEFT")
            x += 3
        if keys[K_RIGHT]:
            print(">> RIGHT")
            x -= 3

        # on met la fenêtre à jour
        window.fill(BLACK)
        pygame.draw.rect(window, GREEN, (x, y, 80, 15))
        pygame. display.update()

        # on attend 1/10 de seconde (100 millièmes)
        clock.tick(100)
    pygame.quit()


if __name__ == "__main__":
    main()
