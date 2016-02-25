import pygame
#Affichage du menu des villages
def Action(fen1):
    pygame.display.set_caption("Action")
    pygame.key.set_repeat(300, 300)
    fond = pygame.image.load("img/menuAction.png").convert()
    fen1.blit(fond, (0,0))
    pygame.display.flip()
    

