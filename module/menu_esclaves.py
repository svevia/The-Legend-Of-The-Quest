import pygame, random
from module.compagnon import *
from module.statistiques import *

def menuEsclaves(fen1,personnage,comp,item):
    global IDesclave1,IDesclave2,IDesclave3,choix,esclave1,esclave2,esclave3
    pygame.display.set_caption("Menu Esclave")
    fondtext = pygame.font.SysFont(None, 22)
    fond = pygame.image.load("img/MenuEsclavagiste.png").convert()
    fen1.blit(fond, (0,0))
    
    choix = 0
    

    if personnage.vendeurEsclave == 0 :
        personnage.IDesclave1 = random.randint(1,12)
        personnage.IDesclave2 = random.randint(1,12)
        personnage.IDesclave3 = random.randint(1,12)
        personnage.esclave1 = compagnon(0,personnage.IDesclave1,personnage)
        personnage.esclave2 = compagnon(0,personnage.IDesclave2,personnage)
        personnage.esclave3 = compagnon(0,personnage.IDesclave3,personnage)
        personnage.vendeurEsclave = 4
        personnage.affichageEsclave1 = 0
        personnage.affichageEsclave2 = 0
        personnage.affichageEsclave3 = 0





    if personnage.affichageEsclave1 == 0 :
        imgcomp1 = pygame.image.load(personnage.esclave1.img)
        
        textNomEsclave1 = fondtext.render(str(personnage.esclave1.name),1,(0,0,0))
        textVieEsclave1 = fondtext.render("Vie : " + str(personnage.esclave1.vie),1,(0,0,0))
        textDegatMinEsclave1 = fondtext.render("Dégâts min. : " + str(personnage.esclave1.degatMin),1,(0,0,0))
        textDegatMaxEsclave1 = fondtext.render("Dégâts max. : " + str(personnage.esclave1.degatMax),1,(0,0,0))
        textEsquiveEsclave1 = fondtext.render("Esquive : " + str(personnage.esclave1.esquive) + "%",1,(0,0,0))
        textCritiqueEsclave1 = fondtext.render("Critique : " + str(personnage.esclave1.critique) + "%",1,(0,0,0))
        textPrixEsclave1 = fondtext.render("Prix : " + str(personnage.esclave1.prix) + " pièces d'or",1,(0,0,0))
        

        fen1.blit(textNomEsclave1,(200,330))
        fen1.blit(textVieEsclave1,(200,360))
        fen1.blit(textDegatMinEsclave1,(200,390))
        fen1.blit(textDegatMaxEsclave1,(200,420))
        fen1.blit(textEsquiveEsclave1,(200,450))
        fen1.blit(textCritiqueEsclave1,(200,480))
        fen1.blit(textPrixEsclave1,(200,510))
        fen1.blit(imgcomp1,(210,200))




    if personnage.affichageEsclave2 == 0 :
        imgcomp2 = pygame.image.load(personnage.esclave2.img)
    
        textNomEsclave2 = fondtext.render(str(personnage.esclave2.name),1,(0,0,0))
        textVieEsclave2 = fondtext.render("Vie : " + str(personnage.esclave2.vie),1,(0,0,0))
        textDegatMinEsclave2 = fondtext.render("Dégâts min. : " + str(personnage.esclave2.degatMin),1,(0,0,0))
        textDegatMaxEsclave2 = fondtext.render("Dégâts max. : " + str(personnage.esclave2.degatMax),1,(0,0,0))
        textEsquiveEsclave2 = fondtext.render("Esquive : " + str(personnage.esclave2.esquive) + "%",1,(0,0,0))
        textCritiqueEsclave2 = fondtext.render("Critique : " + str(personnage.esclave2.critique) + "%",1,(0,0,0))   
        textPrixEsclave2 = fondtext.render("Prix : " + str(personnage.esclave2.prix) + " pièces d'or",1,(0,0,0))


        fen1.blit(textNomEsclave2,(450,330))
        fen1.blit(textVieEsclave2,(450,360))
        fen1.blit(textDegatMinEsclave2,(450,390))
        fen1.blit(textDegatMaxEsclave2,(450,420))
        fen1.blit(textEsquiveEsclave2,(450,450))
        fen1.blit(textCritiqueEsclave2,(450,480))
        fen1.blit(textPrixEsclave2,(450,510))
        fen1.blit(imgcomp2,(460,200))  
    




    if personnage.affichageEsclave3 == 0 :
        imgcomp3 = pygame.image.load(personnage.esclave3.img)
        
        textNomEsclave3 = fondtext.render(str(personnage.esclave3.name),1,(0,0,0))
        textVieEsclave3 = fondtext.render("Vie : " + str(personnage.esclave3.vie),1,(0,0,0))
        textDegatMinEsclave3 = fondtext.render("Dégâts min. : " + str(personnage.esclave3.degatMin),1,(0,0,0))
        textDegatMaxEsclave3 = fondtext.render("Dégâts max. : " + str(personnage.esclave3.degatMax),1,(0,0,0))
        textEsquiveEsclave3 = fondtext.render("Esquive : " + str(personnage.esclave3.esquive) + "%",1,(0,0,0))
        textCritiqueEsclave3 = fondtext.render("Critique : " + str(personnage.esclave3.critique) + "%",1,(0,0,0))
        textPrixEsclave3 = fondtext.render("Prix : " + str(personnage.esclave3.prix) + " pièces d'or",1,(0,0,0))
        

        fen1.blit(textNomEsclave3,(705,330))
        fen1.blit(textVieEsclave3,(705,360))
        fen1.blit(textDegatMinEsclave3,(705,390))
        fen1.blit(textDegatMaxEsclave3,(705,420))
        fen1.blit(textEsquiveEsclave3,(705,450))
        fen1.blit(textCritiqueEsclave3,(705,480))
        fen1.blit(textPrixEsclave3,(705,510))
        fen1.blit(imgcomp3,(715,200))

    
    pygame.display.flip()
    

def infoEsclave1(fen1,personnage,comp,item):
    global nom, choix
    nom = personnage.esclave1.name
    comp.IDC = personnage.IDesclave1
    comp.prixFinal = personnage.esclave1.prix
    choix = 1
    
   
    
def infoEsclave2(fen1,personnage,comp,item):
    global nom, choix
    nom = personnage.esclave2.name
    comp.IDC = personnage.IDesclave2
    comp.prixFinal = personnage.esclave2.prix
    choix = 2


def infoEsclave3(fen1,personnage,comp,item):
    global nom, choix
    nom = personnage.esclave3.name
    comp.IDC = personnage.IDesclave3
    comp.prixFinal = personnage.esclave3.prix
    choix = 3




def verificationEsclave(fen1,personnage,comp,item,story):
    pygame.display.set_caption("Verification")
    fondtext = pygame.font.SysFont(None, 25)
    fond = pygame.image.load("img/Guivre.png").convert()
    fen1.blit(fond, (0,0))


    if (story.activation_quetes[5] == 1 or story.activation_quetes[5] == 2):
        textVerif1 = fondtext.render("Vous êtes en mission avec le scientifique et vous avez besoin de celui-ci.",1,(206,206,206))
        textVerif2 = fondtext.render("Ce n'est donc pas le moment d'acheter un esclave !",1,(206,206,206))
        textVerif3 = fondtext.render("1.Retour",1,(206,206,206))
        fen1.blit(textVerif1,(200,200)) 
        fen1.blit(textVerif2,(200,230))
        fen1.blit(textVerif3,(200,260))
        
    else :
        if comp.prixFinal > personnage.argent :
            textVerif1 = fondtext.render("Vous n'avez pas asser d'argent pour acheter cet eslave !",1,(206,206,206))
            textVerif4 = fondtext.render("1.Retour",1,(206,206,206))
            
        else :
            if comp.ami == 1 :
                textVerif1 = fondtext.render("Vous avez déjà un compagnon : " + str(comp.name) + " !",1,(206,206,206))
                textVerif2 = fondtext.render("Etes-vous sûr de vouloir remplacer " + str(comp.name) + " par " + str(nom) + " ?",1,(206,206,206))
                textVerif3 = fondtext.render("Cela vous coûtera la modique somme de " + str(comp.prixFinal) + " pièces d'or !",1,(206,206,206))
                textVerif4 = fondtext.render("1.Acheter et remplacer",1,(206,206,206))
                textVerif5 = fondtext.render("2.Retour",1,(206,206,206))


            else :
                textVerif1 = fondtext.render("Vous n'avez pas de compagnon !",1,(206,206,206))
                textVerif2 = fondtext.render("Etes-vous sûr de vouloir acheter " + str(nom) + " ?",1,(206,206,206))
                textVerif3 = fondtext.render("Cela vous coûtera la modique somme de " + str(comp.prixFinal) + " pièces d'or !",1,(206,206,206))
                textVerif4 = fondtext.render("1.Acheter",1,(206,206,206))
                textVerif5 = fondtext.render("2.Retour",1,(206,206,206))
                

            fen1.blit(textVerif2,(200,230))
            fen1.blit(textVerif3,(200,260))
            fen1.blit(textVerif5,(200,330))
            
        fen1.blit(textVerif1,(200,200))        
        fen1.blit(textVerif4,(200,300))

    pygame.display.flip()


def choixEsclave(fen1,personnage,comp,item):
    if choix == 1 : personnage.affichageEsclave1 = 1
    if choix == 2 : personnage.affichageEsclave2 = 1
    if choix == 3 : personnage.affichageEsclave3 = 1




    
    
