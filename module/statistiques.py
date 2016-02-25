import pygame
from pygame.locals import *
pygame.init()

class Stats: 

    def __init__(self,pseudo,classe,vie,viemax,principale,esquive,critique,constitution):
        self.pseudo = pseudo
        self.classe = classe
        self.niveau = 1
        self.xp = 0
        self.xpmax = 300
        self.xpbase = 300
        self.vie = vie
        self.viemax = viemax
        self.principale = principale
        self.esquive = esquive
        self.armure = 0
        self.constitution = constitution
        self.argent = 0
        self.competence = 0
        self.critique = critique
        self.cooldown = 0
        self.stunMonstre1 = 0
        self.stunMonstre2 = 0
        self.stunMonstre3 = 0
        self.toucherPerso = 0
        self.dgtMin = 0
        self.dgtMax = 0
        self.degat = 0
        self.chanceCrit = 0
        self.ennemi = 0
        self.up = 0
        self.temps_vitesse = 0
        self.temps_force = 0

        self.forgeron = 0
        self.alchimiste = 0
        
        self.vendeurEsclave = 0
        self.affichageEsclave1 = 0
        self.affichageEsclave2 = 0
        self.affichageEsclave3 = 0
        self.esclave1 = 0
        self.esclave2 = 0
        self.esclave3 = 0
        self.IDesclave1 = 0
        self.IDesclave2 = 0
        self.IDesclave3 = 0


        self.nouveauCompagnonID = 0
        self.nouveauCompagnonIDennemi = 0
        self.karus = 1
        self.iriszia = 1
        self.archimage = 1

       






        
