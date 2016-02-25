'''Aléatoirement au cours du jeu, le joueur va se retrouver confronter à divers évenements aléatoires
pouvant être de diférents types:
-Messgaer regénerant la carte
-Déclenchement de combats accompagnés d'animations
-Présentation d'un partenaire potentiel
-...
l'ensemble de ces evenements est défini et lancé aléatoirement depuis ce programme
En effet, la fonction Choix_Event() Tire aléatoirement un évenments, le déclenche puis le retire de
la liste carte.liste_event, afin que les evenements ne soient représentés que lorsque tous sont déjà passés'''



import pygame,random,time
from module.menu_classe import *
from module.combat import *
from module.compagnon import *
import module.bind
pygame.init()

def Choix_Event(fen1,carte,personnage,item,comp,story):
    carte.debutEvent = random.randint(200000,500000)
    event = random.choice(carte.liste_event)  
    carte.liste_event.remove(event)
    
    if len(carte.liste_event) == 0:
       carte.liste_event = [1,2,3,4,5,6,7]

    if event == 1 : event_taxe(fen1,carte,personnage,item,comp)
    if event == 2 : event_messager(fen1,carte,personnage,item,comp)
    if event == 3 : event_boss_alea(fen1,carte,personnage,item,comp)
    if event == 4 : event_compagnon_paladin(fen1,carte,personnage,item,comp,story)
    if event == 5 : event_compagnon_assassin(fen1,carte,personnage,item,comp,story)
    if event == 6 : event_compagnon_sorcier(fen1,carte,personnage,item,comp,story)
    if event == 7 : EventAttaqueSorcier(fen1,carte,personnage,item,comp)


#-----------------------------------------------------event 1 :taxe----------------------------------------------------------------#

def event_taxe(fen1,carte,personnage,item,comp):
    global position_inconnu
    font = pygame.font.SysFont(None, 32)
    pygame.display.set_caption("Event taxe")
    fichier = []
    pos =0
    if carte.positiony > carte.taille[1] - 1000: #pour éviter que le personnage arrive en marchant sur l'eau
        carte.perso = carte.fichier[25]
        if personnage.classe != "mage":
            taxeur = pygame.image.load("img/monstre/HeretiqueFightGauche.png")
            for i in range(1,9):
                fichier.append(pygame.image.load("img/heretique/Heretique"+str(i)+".png").convert_alpha())
                texte1 = font.render("Bonjour voyageur, je suis le mage de ces lieux.",1,(206,206,206))

        if personnage.classe == "mage":
            taxeur = pygame.image.load("img/monstre/PaladinFightGauche.png")
            for i in range(1,9):
                fichier.append(pygame.image.load("img/paladin/Paladin"+str(i)+".png").convert_alpha())
                texte1 = font.render("Bonjour voyageur, je suis le gardien de ces lieux.",1,(206,206,206))

        inconnu = fichier[pos]
        position_inconnu = inconnu.get_rect()
        position_inconnu = position_inconnu.move(512, -10)
    
    else:
        carte.perso = carte.fichier[1]
        if personnage.classe != "mage":
            taxeur = pygame.image.load("img/monstre/HeretiqueFightGauche.png")
            for i in range(25,33):
                fichier.append(pygame.image.load("img/heretique/Heretique"+str(i)+".png").convert_alpha())
            texte1 = font.render("Bonjour voyageur, je suis le mage de ces lieux.",1,(206,206,206))

        if personnage.classe == "mage":
            taxeur = pygame.image.load("img/monstre/PaladinFightGauche.png")
            for i in range(25,33):
                fichier.append(pygame.image.load("img/paladin/Paladin"+str(i)+".png").convert_alpha())
            texte1 = font.render("Bonjour voyageur, je suis le gardien de ces lieux.",1,(206,206,206))
            

        inconnu = fichier[pos]
        position_inconnu = inconnu.get_rect()
        position_inconnu = position_inconnu.move(512, 780)

    deplacement = 0

    while deplacement < 370:
        pos += 1
        if carte.positiony > carte.taille[1] - 1000:
            position_inconnu = position_inconnu.move(0,4)
        else:
            position_inconnu = position_inconnu.move(0,-4)
        deplacement +=4
        if pos not in range(0,8):
            pos = 0

            
        carte.affichage(fen1,personnage,item,comp)
        inconnu = fichier[pos]


#pour éviter la superposition du personnage et de l'inconnu
        if carte.positiony > carte.taille[1] - 1000:
            fen1.blit(inconnu, position_inconnu)
            fen1.blit(carte.perso, (512,384))
        else:
            fen1.blit(carte.perso, (512,384))
            fen1.blit(inconnu, position_inconnu)


        carte.contour(fen1,personnage)
        
        pygame.display.flip()
        time.sleep(0.03)

    pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))



    texte2 = font.render("Nul ne passe ici sans me payer une taxe, pour toi ce sera... 200 d'or !",1,(206,206,206))
    if personnage.argent >= 200:
        texte3 = font.render("1.Payer (-200 or)",1,(206,206,206))
        texte4 = font.render("2.Défendre sa bourse !",1,(206,206,206))
    else:
        texte3 = font.render("Vous n'avez pas assez d'argent...",1,(206,206,206))
        texte4 = font.render("2.Se battre !",1,(206,206,206))

    
    fen1.blit(texte1,(10,580))
    fen1.blit(taxeur,(800,600))
    pygame.display.flip()
    time.sleep(1)
    fen1.blit(texte2,(10,610))
    fen1.blit(texte3,(10,640))
    fen1.blit(texte4,(10,670))
    pygame.display.flip()
    pygame.display.set_caption("Event-taxe")



def Payer_taxe(fen1,personnage,item,carte,comp):
    global position_inconnu
    personnage.argent -= 200
    deplacement = 0
    fichier = []
    pos = 1
    if carte.positiony > carte.taille[1] - 1000:
        if personnage.classe != "mage":
            for i in range(25,33):
                fichier.append(pygame.image.load("img/heretique/Heretique"+str(i)+".png").convert_alpha())


        if personnage.classe == "mage":
            for i in range(25,33):
                fichier.append(pygame.image.load("img/paladin/Paladin"+str(i)+".png").convert_alpha())


    else:
        if personnage.classe != "mage":
            for i in range(1,9):
                fichier.append(pygame.image.load("img/heretique/Heretique"+str(i)+".png").convert_alpha())

        if personnage.classe == "mage":
            for i in range(1,9):
                fichier.append(pygame.image.load("img/paladin/Paladin"+str(i)+".png").convert_alpha())

                
    while deplacement < 400:
        pos += 1
        if carte.positiony > carte.taille[1] - 1000:
            position_inconnu = position_inconnu.move(0,-4)
        else:
            position_inconnu = position_inconnu.move(0,4)
        deplacement +=4
        if pos not in range(0,8):
            pos = 0
            
        carte.affichage(fen1,personnage,item,comp)
        inconnu = fichier[pos]
        
        if carte.positiony > carte.taille[1] - 1000:
            fen1.blit(inconnu, position_inconnu)
            fen1.blit(carte.perso, (512,384))
        else:
            fen1.blit(carte.perso, (512,384))
            fen1.blit(inconnu, position_inconnu)

        carte.contour(fen1,personnage)
        
        
        pygame.display.flip()
        time.sleep(0.03)
    carte.reprise(fen1,personnage,item)

    
#------------------------------------------------------------------- event 2 : messager --------------------------------------------------------------#

        
def event_messager(fen1,carte,personnage,item,comp):
    global position_inconnu
    font = pygame.font.SysFont(None, 32)
    pygame.display.set_caption("Event messager")
    fichier = []
    pos =0
    if carte.positionx < carte.taille[0] - 1000: #pour éviter que le personnage arrive en marchant sur l'eau
        carte.perso = carte.fichier[9]  
        for i in range(7,16):
            fichier.append(pygame.image.load("img/event/messager/Messager"+str(i)+".png").convert_alpha())


        inconnu = fichier[pos]
        position_inconnu = inconnu.get_rect()
        position_inconnu = position_inconnu.move(1034,390)
    
    else:
        carte.perso = carte.fichier[17]
        for i in range(17,26):
            fichier.append(pygame.image.load("img/event/messager/Messager"+str(i)+".png").convert_alpha())

            
        inconnu = fichier[pos]
        position_inconnu = inconnu.get_rect()
        position_inconnu = position_inconnu.move(-10,390)

    deplacement = 0

    while deplacement < 492:
        pos += 1
        if carte.positionx < carte.taille[0] - 1000:
            position_inconnu = position_inconnu.move(-4,0)
        else:
            position_inconnu = position_inconnu.move(4,0)
        deplacement +=4
        if pos not in range(0,8):
            pos = 0

    
            
        carte.affichage(fen1,personnage,item,comp)
        inconnu = fichier[pos]

        fen1.blit(inconnu, position_inconnu)

        carte.contour(fen1,personnage)
        
        pygame.display.flip()
        time.sleep(0.03)

    pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))



    texte1 = font.render("Bonjour voyageur, je vous apporte un message.",1,(206,206,206))
    texte2 = font.render("Voici les nouvelles de la contamination !",1,(206,206,206))
    texte3 = font.render("1.Prendre le message.",1,(206,206,206))
    
    
    fen1.blit(texte1,(10,580))
    pygame.display.flip()
    time.sleep(1)
    fen1.blit(texte2,(10,610))
    fen1.blit(texte3,(10,640))
    pygame.display.flip()
    pygame.display.set_caption("Event-messager")



def prendreMessage(fen1,personnage,item,carte,comp):
    global position_inconnu
    deplacement = 0
    fichier = []
    pos = 1
    if carte.positionx < carte.taille[0] - 1000:
        for i in range(17,26):
            fichier.append(pygame.image.load("img/event/messager/Messager"+str(i)+".png").convert_alpha())

    else:
        for i in range(7,16):
            fichier.append(pygame.image.load("img/event/messager/Messager"+str(i)+".png").convert_alpha())
            
    while deplacement < 450:
        pos += 1
        if carte.positionx < carte.taille[0] - 1000:
            position_inconnu = position_inconnu.move(4,0)
        else:
            position_inconnu = position_inconnu.move(-4,0)
        deplacement +=4
        if pos not in range(0,8):
            pos = 0
            
        carte.affichage(fen1,personnage,item,comp)
        inconnu = fichier[pos]
        
        fen1.blit(inconnu, position_inconnu)

        carte.contour(fen1,personnage)
        
        
        pygame.display.flip()
        time.sleep(0.03)
    carte.mini(fen1,personnage,item)


#----------------------------------------------------- event 3 : boss aléatoires ---------------------------------------------------------------------------#

def event_boss_alea(fen1,carte,personnage,item,comp):
    font = pygame.font.SysFont(None, 32)
    pygame.display.set_caption("Event boss aléa")

    noir = pygame.image.load('img/map/noir.png')
    noir.set_alpha(0)
    carte.perso = carte.fichier[1]

    for i in range (0,150,15):
        noir.set_alpha(i)
        carte.affichage(fen1,personnage,item,comp)
        fen1.blit(noir,(0,0))
        carte.contour(fen1,personnage)
        
        pygame.display.flip()
        time.sleep(0.25)
        if i == 45: carte.perso = carte.fichier[9]
        if i == 90: carte.perso = carte.fichier[17]
        if i == 120: carte.perso = carte.fichier[9]


    pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))



    texte1 = font.render("Il fait froid tout à coup...",1,(206,206,206))
    texte2 = font.render("Des cris se font entendre au loin",1,(206,206,206))
    texte3 = font.render("Un monstre surgit, Tenez vous prêt !",1,(206,206,206))
    
    fen1.blit(texte1,(10,580))
    pygame.display.flip()
    time.sleep(1)
    fen1.blit(texte2,(10,610))
    pygame.display.flip()
    time.sleep(1)
    fen1.blit(texte3,(10,640))
    pygame.display.flip()
    time.sleep(1)

    IDboss = random.randint(401,403)
    module.bind.creaCombat(fen1,IDboss,1,1,1)


    


#----------------------------------------------------- event 4 : compagnon Paladin ---------------------------------------------------------------------------#

def event_compagnon_paladin(fen1,carte,personnage,item,comp,story):
    global position_compagnon
    font = pygame.font.SysFont(None, 32)
    pygame.display.set_caption("Event Compagnon")

    personnage.nouveauCompagnonID = 13
    personnage.nouveauCompagnonIDennemi = 516
    deplacement = 0
    fichier = []
    pos = 0 
    
    if carte.positiony > carte.taille[1] - 1000: #pour éviter que le personnage arrive en marchant sur l'eau
        carte.perso = carte.fichier[25]  
        for i in range(1,9):
            fichier.append(pygame.image.load("img/Compagnon/paladin/Paladin"+str(i)+".png").convert_alpha())


        compagnon = fichier[pos]
        position_compagnon = compagnon.get_rect()
        position_compagnon = position_compagnon.move(512, -50)
    
    else:
        carte.perso = carte.fichier[1]
        for i in range(25,33):
            fichier.append(pygame.image.load("img/Compagnon/paladin/Paladin"+str(i)+".png").convert_alpha())

        compagnon = fichier[pos]
        position_compagnon = compagnon.get_rect()
        position_compagnon = position_compagnon.move(512, 780)
        

    while deplacement < 370:
        pos += 1
        
        
        if carte.positiony > carte.taille[1] - 1000:
            deplacement += 3.7
            position_compagnon = position_compagnon.move(0,4)
        else:
            deplacement += 4
            position_compagnon = position_compagnon.move(0,-4)
        
        if pos not in range(0,8):
            pos = 0

            
        carte.affichage(fen1,personnage,item,comp)
        compagnon = fichier[pos]


        #pour éviter la superposition du joueur et du personnage qui approche
        if carte.positiony > carte.taille[1] - 1000:
            fen1.blit(compagnon, position_compagnon)
            fen1.blit(carte.perso, (512,384))
        else:
            fen1.blit(carte.perso, (512,384))
            fen1.blit(compagnon, position_compagnon)

        carte.contour(fen1,personnage)
        
        
        pygame.display.flip()
        time.sleep(0.03)

    pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))



    texte1 = font.render("Bonjour voyageur ! Je me présente : je suis un noble paladin.",1,(206,206,206))
    texte2 = font.render("Je suis à la recherche d'aventures et je vous propose de vous accompagner.",1,(206,206,206))
    texte3 = font.render("En échange de quelques pièces d'or, je vous suivrai jusqu'à la mort !",1,(206,206,206))


    
    fen1.blit(texte1,(10,580))
    pygame.display.flip()
    time.sleep(2)
    
    fen1.blit(texte2,(10,610))
    pygame.display.flip()
    time.sleep(2)
    
    fen1.blit(texte3,(10,640))
    pygame.display.flip()
    time.sleep(3)

    pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))

    if (story.activation_quetes[5] == 0 or story.activation_quetes[5] == 3):
        if personnage.argent >= 200 :
            if comp.ami == 0 :
                texte1 = font.render("1.Payer 200 pièces d'or pour ce nouveau compagnon.",1,(206,206,206))
                texte2 = font.render("2.Refuser et le laisser partir.",1,(206,206,206))

                fen1.blit(texte1,(10,580))
                pygame.display.flip()
                time.sleep(2)
                
                fen1.blit(texte2,(10,610))
                pygame.display.flip()
                time.sleep(2)
                
            else :
                texte1 = font.render("Vous avez déjà un compagnon. Que voulez-vous faire ?",1,(206,206,206))
                texte2 = font.render("1.Payer 200 pièces d'or pour le paladin et tuer votre ancien compagnon.",1,(206,206,206))
                if personnage.argent >= 400 : texte3 = font.render("2.Engager le paladin et laisser partir votre compagnon en échange de 200 pièces.",1,(206,206,206))
                else : texte3 = font.render("2.Engager le paladin et laisser partir votre compagnon sans argent, il peut vous attaquer.",1,(206,206,206))
                texte4 = font.render("3.Garder votre ancien compagnon et laisser partir le paladin.",1,(206,206,206))

                fen1.blit(texte1,(10,580))
                pygame.display.flip()
                time.sleep(2)
                
                fen1.blit(texte2,(10,610))
                pygame.display.flip()
                time.sleep(2)
                
                fen1.blit(texte3,(10,640))
                pygame.display.flip()
                time.sleep(2)

                fen1.blit(texte4,(10,670))
                pygame.display.flip()
                time.sleep(2)

        else :
            texte1 = font.render("Vous n'avez pas asser d'argent pour engager ce paladin...",1,(206,206,206))
            texte2 = font.render("1.L'attaquer.",1,(206,206,206))
            texte3 = font.render("2.Le laisser partir.",1,(206,206,206))

            fen1.blit(texte1,(10,580))
            pygame.display.flip()
            time.sleep(2)
            
            fen1.blit(texte2,(10,610))
            pygame.display.flip()
            time.sleep(2)

            fen1.blit(texte3,(10,640))
            pygame.display.flip()
            time.sleep(2)
            
        
        
        
        pygame.display.set_caption("Event-Compagnon")

    else :
        texte1 = font.render("Le scientifique est avec vous ? Vous êtes donc en mission.",1,(206,206,206))
        texte2 = font.render("Je ne vous retiens pas plus longtemps dans ce cas, au revoir.",1,(206,206,206))

        fen1.blit(texte1,(10,580))
        pygame.display.flip()
        time.sleep(2)
                
        fen1.blit(texte2,(10,610))
        pygame.display.flip()
        time.sleep(2)
        
        departEventCompagnon(fen1,carte,personnage,item,comp)


#----------------------------------------------------- event 5 : compagnon Assassin ---------------------------------------------------------------------------#

def event_compagnon_assassin(fen1,carte,personnage,item,comp,story):
    global position_compagnon
    font = pygame.font.SysFont(None, 32)
    pygame.display.set_caption("Event Compagnon")

    personnage.nouveauCompagnonID = 14
    personnage.nouveauCompagnonIDennemi = 517
    deplacement = 0
    fichier = []
    pos = 0 
    
    if carte.positiony > carte.taille[1] - 1000: #pour éviter que le personnage arrive en marchant sur l'eau
        carte.perso = carte.fichier[25]  
        for i in range(1,9):
            fichier.append(pygame.image.load("img/Compagnon/assassin/Assassin"+str(i)+".png").convert_alpha())


        compagnon = fichier[pos]
        position_compagnon = compagnon.get_rect()
        position_compagnon = position_compagnon.move(512, -50)
    
    else:
        carte.perso = carte.fichier[1]
        for i in range(25,33):
            fichier.append(pygame.image.load("img/Compagnon/assassin/Assassin"+str(i)+".png").convert_alpha())

        compagnon = fichier[pos]
        position_compagnon = compagnon.get_rect()
        position_compagnon = position_compagnon.move(512, 780)
        

    while deplacement < 370:
        pos += 1
        
        
        if carte.positiony > carte.taille[1] - 1000:
            deplacement += 3.7
            position_compagnon = position_compagnon.move(0,4)
        else:
            deplacement += 4
            position_compagnon = position_compagnon.move(0,-4)
        
        if pos not in range(0,8):
            pos = 0

            
        carte.affichage(fen1,personnage,item,comp)
        compagnon = fichier[pos]


        #pour éviter la superposition du joueur et du personnage qui approche
        if carte.positiony > carte.taille[1] - 1000:
            fen1.blit(compagnon, position_compagnon)
            fen1.blit(carte.perso, (512,384))
        else:
            fen1.blit(carte.perso, (512,384))
            fen1.blit(compagnon, position_compagnon)

        carte.contour(fen1,personnage)
        
        pygame.display.flip()
        time.sleep(0.03)

    pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))



    texte1 = font.render("Je vous trouve enfin. Je suis un assassin à la recherche d'aventure.",1,(206,206,206))
    texte2 = font.render("On parle beaucoup de vous en ce moment et j'aimerais me joindre à vous pour réaliser votre",1,(206,206,206))
    texte3 = font.render("quête ! Je suis un assassin agissant dans l'ombre et tuant mes cibles rapidement !",1,(206,206,206))


    
    fen1.blit(texte1,(10,580))
    pygame.display.flip()
    time.sleep(2)
    
    fen1.blit(texte2,(10,610))
    pygame.display.flip()
    time.sleep(2)
    
    fen1.blit(texte3,(10,640))
    pygame.display.flip()
    time.sleep(3)

    pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))

    if (story.activation_quetes[5] == 0 or story.activation_quetes[5] == 3):
        if personnage.argent >= 200 :
            if comp.ami == 0 :
                texte1 = font.render("1.Payer 200 pièces d'or pour ce nouveau compagnon.",1,(206,206,206))
                texte2 = font.render("2.Refuser et le laisser partir.",1,(206,206,206))

                fen1.blit(texte1,(10,580))
                pygame.display.flip()
                time.sleep(2)
                
                fen1.blit(texte2,(10,610))
                pygame.display.flip()
                time.sleep(2)
                
            else :
                texte1 = font.render("Vous avez déjà un compagnon. Que voulez-vous faire ?",1,(206,206,206))
                texte2 = font.render("1.Payer 200 pièces d'or pour l'assassin et tuer votre ancien compagnon.",1,(206,206,206))
                if personnage.argent >= 400 : texte3 = font.render("2.Engager l'assassin et laisser partir votre compagnon en échange de 200 pièces.",1,(206,206,206))
                else : texte3 = font.render("2.Engager l'assassin et laisser partir votre compagnon sans argent, il peut vous attaquer.",1,(206,206,206))
                texte4 = font.render("3.Garder votre ancien compagnon et laisser partir l'assassin.",1,(206,206,206))

                fen1.blit(texte1,(10,580))
                pygame.display.flip()
                time.sleep(2)
                
                fen1.blit(texte2,(10,610))
                pygame.display.flip()
                time.sleep(2)
                
                fen1.blit(texte3,(10,640))
                pygame.display.flip()
                time.sleep(2)

                fen1.blit(texte4,(10,670))
                pygame.display.flip()
                time.sleep(2)

        else :
            texte1 = font.render("Vous n'avez pas asser d'argent pour engager cet assassin...",1,(206,206,206))
            texte2 = font.render("1.L'attaquer.",1,(206,206,206))
            texte3 = font.render("2.Le laisser partir.",1,(206,206,206))

            fen1.blit(texte1,(10,580))
            pygame.display.flip()
            time.sleep(2)
            
            fen1.blit(texte2,(10,610))
            pygame.display.flip()
            time.sleep(2)

            fen1.blit(texte3,(10,640))
            pygame.display.flip()
            time.sleep(2)
            
        
        
        
        pygame.display.set_caption("Event-Compagnon")

    else :
        texte1 = font.render("Le scientifique est avec vous ? Vous êtes donc en mission.",1,(206,206,206))
        texte2 = font.render("Je ne vous retiens pas plus longtemps dans ce cas, au revoir.",1,(206,206,206))

        fen1.blit(texte1,(10,580))
        pygame.display.flip()
        time.sleep(2)
                
        fen1.blit(texte2,(10,610))
        pygame.display.flip()
        time.sleep(2)
        
        departEventCompagnon(fen1,carte,personnage,item,comp)



#----------------------------------------------------- event 6 : compagnon Sorcier ---------------------------------------------------------------------------#

def event_compagnon_sorcier(fen1,carte,personnage,item,comp,story):
    global position_compagnon
    font = pygame.font.SysFont(None, 32)
    pygame.display.set_caption("Event Compagnon")

    personnage.nouveauCompagnonID = 15
    personnage.nouveauCompagnonIDennemi = 518
    deplacement = 0
    fichier = []
    pos = 0 
    
    if carte.positiony > carte.taille[1] - 1000: #pour éviter que le personnage arrive en marchant sur l'eau
        carte.perso = carte.fichier[25]  
        for i in range(1,9):
            fichier.append(pygame.image.load("img/Compagnon/heretique/Heretique"+str(i)+".png").convert_alpha())


        compagnon = fichier[pos]
        position_compagnon = compagnon.get_rect()
        position_compagnon = position_compagnon.move(512, -50)
    
    else:
        carte.perso = carte.fichier[1]
        for i in range(25,33):
            fichier.append(pygame.image.load("img/Compagnon/heretique/Heretique"+str(i)+".png").convert_alpha())

        compagnon = fichier[pos]
        position_compagnon = compagnon.get_rect()
        position_compagnon = position_compagnon.move(512, 780)
        

    while deplacement < 370:
        pos += 1
        
        
        if carte.positiony > carte.taille[1] - 1000:
            deplacement += 3.7
            position_compagnon = position_compagnon.move(0,4)
        else:
            deplacement += 4
            position_compagnon = position_compagnon.move(0,-4)
        
        if pos not in range(0,8):
            pos = 0

            
        carte.affichage(fen1,personnage,item,comp)
        compagnon = fichier[pos]


        #pour éviter la superposition du joueur et du personnage qui approche
        if carte.positiony > carte.taille[1] - 1000:
            fen1.blit(compagnon, position_compagnon)
            fen1.blit(carte.perso, (512,384))
        else:
            fen1.blit(carte.perso, (512,384))
            fen1.blit(compagnon, position_compagnon)

        carte.contour(fen1,personnage)
        
        
        pygame.display.flip()
        time.sleep(0.03)

    pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))



    texte1 = font.render("Salutation. Qui suis-je ? Je suis un puissant sorcier !",1,(206,206,206))
    texte2 = font.render("Malheureusement, suite à quelques problèmes, ma bourse est devenue vide...",1,(206,206,206))
    texte3 = font.render("Je propose donc mes services, en échange de 200 pièces d'or, biensur !",1,(206,206,206))


    
    fen1.blit(texte1,(10,580))
    pygame.display.flip()
    time.sleep(2)
    
    fen1.blit(texte2,(10,610))
    pygame.display.flip()
    time.sleep(2)
    
    fen1.blit(texte3,(10,640))
    pygame.display.flip()
    time.sleep(3)

    pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))

    if (story.activation_quetes[5] == 0 or story.activation_quetes[5] == 3):
        if personnage.argent >= 200 :
            if comp.ami == 0 :
                texte1 = font.render("1.Payer 200 pièces d'or pour ce nouveau compagnon.",1,(206,206,206))
                texte2 = font.render("2.Refuser et le laisser partir.",1,(206,206,206))

                fen1.blit(texte1,(10,580))
                pygame.display.flip()
                time.sleep(2)
                
                fen1.blit(texte2,(10,610))
                pygame.display.flip()
                time.sleep(2)
                
            else :
                texte1 = font.render("Vous avez déjà un compagnon. Que voulez-vous faire ?",1,(206,206,206))
                texte2 = font.render("1.Payer 200 pièces d'or pour le sorcier et tuer votre ancien compagnon.",1,(206,206,206))
                if personnage.argent >= 400 : texte3 = font.render("2.Engager le sorcier et laisser partir votre compagnon en échange de 200 pièces.",1,(206,206,206))
                else : texte3 = font.render("2.Engager le sorcier et laisser partir votre compagnon sans argent, il peut vous attaquer.",1,(206,206,206))
                texte4 = font.render("3.Garder votre ancien compagnon et laisser partir le sorcier.",1,(206,206,206))

                fen1.blit(texte1,(10,580))
                pygame.display.flip()
                time.sleep(2)
                
                fen1.blit(texte2,(10,610))
                pygame.display.flip()
                time.sleep(2)
                
                fen1.blit(texte3,(10,640))
                pygame.display.flip()
                time.sleep(2)

                fen1.blit(texte4,(10,670))
                pygame.display.flip()
                time.sleep(2)

        else :
            texte1 = font.render("Vous n'avez pas asser d'argent pour engager ce sorcier...",1,(206,206,206))
            texte2 = font.render("1.L'attaquer.",1,(206,206,206))
            texte3 = font.render("2.Le laisser partir.",1,(206,206,206))

            fen1.blit(texte1,(10,580))
            pygame.display.flip()
            time.sleep(2)
            
            fen1.blit(texte2,(10,610))
            pygame.display.flip()
            time.sleep(2)

            fen1.blit(texte3,(10,640))
            pygame.display.flip()
            time.sleep(2)
        
        
    
    
    
        pygame.display.set_caption("Event-Compagnon")
        
    else :
        texte1 = font.render("Le scientifique est avec vous ? Vous êtes donc en mission.",1,(206,206,206))
        texte2 = font.render("Je ne vous retiens pas plus longtemps dans ce cas, au revoir.",1,(206,206,206))

        fen1.blit(texte1,(10,580))
        pygame.display.flip()
        time.sleep(2)
                
        fen1.blit(texte2,(10,610))
        pygame.display.flip()
        time.sleep(2)
        
        departEventCompagnon(fen1,carte,personnage,item,comp)
        


#----------------------------------------------------------------------- Departs des compagnons - event 4 - 5 - 6 ----------------------------------#
def departEventCompagnon(fen1,carte,personnage,item,comp):
    global position_compagnon
    deplacement = 0
    fichier = []
    pos = 1

    if personnage.nouveauCompagnonID == 13 :
        if carte.positiony > carte.taille[1] - 1000:
            for i in range(25,33):
                fichier.append(pygame.image.load("img/Compagnon/paladin/Paladin"+str(i)+".png").convert_alpha())

        else:
            for i in range(1,9):
                fichier.append(pygame.image.load("img/Compagnon/paladin/Paladin"+str(i)+".png").convert_alpha())
                
    if personnage.nouveauCompagnonID == 14 :
        if carte.positiony > carte.taille[1] - 1000:
            for i in range(25,33):
                fichier.append(pygame.image.load("img/Compagnon/assassin/Assassin"+str(i)+".png").convert_alpha())

        else:
            for i in range(1,9):
                fichier.append(pygame.image.load("img/Compagnon/assassin/Assassin"+str(i)+".png").convert_alpha())
                
    if personnage.nouveauCompagnonID == 15 :
        if carte.positiony > carte.taille[1] - 1000:
            for i in range(25,33):
                fichier.append(pygame.image.load("img/Compagnon/heretique/Heretique"+str(i)+".png").convert_alpha())

        else:
            for i in range(1,9):
                fichier.append(pygame.image.load("img/Compagnon/heretique/Heretique"+str(i)+".png").convert_alpha())

                
    while deplacement < 400:
        pos += 1
        if carte.positiony > carte.taille[1] - 1000:
            position_compagnon = position_compagnon.move(0,-4)
        else:
            position_compagnon = position_compagnon.move(0,4)
        deplacement +=4
        if pos not in range(0,8):
            pos = 0
            
        carte.affichage(fen1,personnage,item,comp)
        compagnon = fichier[pos]
        
        if carte.positiony > carte.taille[1] - 1000:
            fen1.blit(compagnon, position_compagnon)
            fen1.blit(carte.perso, (512,384))
        else:
            fen1.blit(carte.perso, (512,384))
            fen1.blit(compagnon, position_compagnon)

        carte.contour(fen1,personnage)
        
        
        pygame.display.flip()
        time.sleep(0.03)
        
    carte.reprise(fen1,personnage,item,comp)

#----------------------------------------------------------------------- Attaque des sorciers - event 7 ----------------------------------#

def EventAttaqueSorcier(fen1,carte,personnage,item,comp):
    deplacementSorcier = 0
    font = pygame.font.SysFont(None, 32)
    pygame.display.set_caption("Cinématique")
    sorcier = []
    BDF1 = []
    BDF2 = []
    BDF3 = []
    explosion = []
    deplacement = 0
    posBDF = 0


    if carte.positiony > carte.taille[1] - 1000:
        carte.perso = carte.fichier[25]

    else:
        carte.perso = carte.fichier[1]



    for i in range(1,12):
        explosion.append(pygame.image.load("img/event/BDF/explosionBDF"+str(i)+".png").convert_alpha())

    for i in range(0,7):
        BDF2.append(pygame.image.load("img/event/BDF/GbouleDeFeu"+str(i)+".png").convert_alpha())
    for i in range(0,7):
        BDF3.append(pygame.image.load("img/event/BDF/DbouleDeFeu"+str(i)+".png").convert_alpha())
                    
    if carte.positiony > carte.taille[1] - 1000:
        for i in range(0,7):
            BDF1.append(pygame.image.load("img/event/BDF/HbouleDeFeu"+str(i)+".png").convert_alpha())

                        
        for i in range(1,9):
            sorcier.append(pygame.image.load("img/Compagnon/heretique/Heretique"+str(i)+".png").convert_alpha())


        Boule1 = BDF1[posBDF]
        position_Boule1 = Boule1.get_rect()
        position_Boule1 = position_Boule1.move(512,-130)
                        
    else:
        for i in range(0,7):
            BDF1.append(pygame.image.load("img/event/BDF/BbouleDeFeu"+str(i)+".png").convert_alpha())
        
        for i in range(25,33):
            sorcier.append(pygame.image.load("img/Compagnon/heretique/Heretique"+str(i)+".png").convert_alpha())


        Boule1 = BDF1[posBDF]
        position_Boule1 = Boule1.get_rect()
        position_Boule1 = position_Boule1.move(512,930)
                        

    Boule2 = BDF2[posBDF]
    position_Boule2 = Boule2.get_rect()
    position_Boule2 = position_Boule2.move(-50,384)
    
    Boule3 = BDF3[posBDF]
    position_Boule3 = Boule3.get_rect()
    position_Boule3 = position_Boule3.move(1074,384)

    
    while deplacement < 400:
        posBDF += 1
        if deplacement == 80: carte.perso = carte.fichier[9]
        if deplacement == 160: carte.perso = carte.fichier[17]
        if deplacement == 240: carte.perso = carte.fichier[9]
        if deplacement == 320: carte.perso = carte.fichier[17]
        if posBDF not in range(0,7):
            posBDF = 0
            
        Boule1 = BDF1[posBDF]
        Boule2 = BDF2[posBDF]
        Boule3 = BDF3[posBDF]
        deplacement += 4
        position_Boule2 = position_Boule2.move(5,0)
        position_Boule3 = position_Boule3.move(-5,0)
        
        if carte.positiony > carte.taille[1] - 1000:
            position_Boule1 = position_Boule1.move(0,5)
        else:
            position_Boule1 = position_Boule1.move(0,-5)

        carte.affichage(fen1,personnage,item,comp)
        fen1.blit(Boule1,position_Boule1)
        fen1.blit(Boule2,position_Boule2)
        fen1.blit(Boule3,position_Boule3)                        
        fen1.blit(carte.perso, (512,384))
        carte.contour(fen1,personnage)
        
        pygame.display.flip()
        time.sleep(0.02)


    for posBDF in range(0,11):
        Boule1 = explosion[posBDF]
        Boule2 = explosion[posBDF]
        Boule3 = explosion[posBDF] 

        carte.affichage(fen1,personnage,item,comp)
        fen1.blit(Boule1,position_Boule1)
        fen1.blit(Boule2,position_Boule2)
        fen1.blit(Boule3,position_Boule3)                        
        fen1.blit(carte.perso, (512,384))
        carte.contour(fen1,personnage)
        
        pygame.display.flip()
        time.sleep(0.015)


    pos = 0
    compagnon = sorcier[pos]
    position_compagnon = compagnon.get_rect()

    if carte.positiony > carte.taille[1] - 1000:
        position_compagnon = position_compagnon.move(512, -50)
        carte.perso = carte.fichier[25]

    else:
        position_compagnon = position_compagnon.move(512, 780)
        carte.perso = carte.fichier[1]



    pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
    texte1 = font.render("Vous tompbez dans une ambusacade de la guilde des sorciers!",1,(206,206,206))
    texte2 = font.render("N'ayez aucune pitié !",1,(206,206,206))
    texte3 = font.render("...En tout cas eux n'en auront aucune...",1,(206,206,206))

    fen1.blit(texte1,(10,580))
    pygame.display.flip()
    time.sleep(2)
    
    fen1.blit(texte2,(10,610))
    pygame.display.flip()
    time.sleep(2)
    
    fen1.blit(texte3,(10,640))
    pygame.display.flip()
    time.sleep(2)


    if carte.positiony > carte.taille[1] - 1000:
        carte.perso = carte.fichier[25]

    else:
        carte.perso = carte.fichier[1]
    
    while deplacementSorcier < 370:
        pos += 1
        if pos not in range(0,8):
            pos = 0
        
        if carte.positiony > carte.taille[1] - 1000:
            deplacementSorcier += 4
            position_compagnon = position_compagnon.move(0,4)

        else:
            deplacementSorcier += 4
            position_compagnon = position_compagnon.move(0,-4)
        

            
        carte.affichage(fen1,personnage,item,comp)
        compagnon = sorcier[pos]


        #pour éviter la superposition du joueur et du personnage qui approche
        if carte.positiony > carte.taille[1] - 1000:
            fen1.blit(compagnon, position_compagnon)
            fen1.blit(carte.perso, (512,384))
        else:
            fen1.blit(carte.perso, (512,384))
            fen1.blit(compagnon, position_compagnon)

        carte.contour(fen1,personnage)
        pygame.display.flip()
        time.sleep(0.03)

    time.sleep(2)
    pygame.display.set_caption("Event BDF")
    if carte.biome == "desert":
        module.bind.creaCombat(fen1,1,518,1,3)

    elif carte.biome == "marais":
        module.bind.creaCombat(fen1,104,518,104,3)

    elif carte.biome == "plaine":
        module.bind.creaCombat(fen1,201,518,201,3)

    else:
        module.bind.creaCombat(fen1,302,518,302,3)




