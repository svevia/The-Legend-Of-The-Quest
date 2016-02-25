'''Programme regroupant toutes fonctions les nécessaires au fonctionnement:
-du forgeron
-de la vente
-de l'alchimiste
'''


import pygame,time
from module.item_ID import *

def Fabrication(fen1,ID,item,personnage): #Cette fonction vérifie si le personnage à les composant nécessaire pour créer l'objets, si oui l'objet est crée.
    objitem = ID_objet(ID,personnage,item)
    composition = True
    i=0
    while i < len(objitem.composant) and composition == True:
        if item.inventaireLook(objitem.composant[i]) >= objitem.composant[i+1] and personnage.argent >= objitem.argent: #vérifie si le joueur a les composnats necessaires
            i += 2
        else: composition = False

    if composition == True: #si le joueur a les composants, l'objet est créé
        item.loot(ID)
        personnage.argent -= objitem.argent
        for i in range(0,len(objitem.composant),2):
            item.objetPerdu(objitem.composant[i],objitem.composant[i+1])
        print("compo terminée")
        if ID > 99:
            personnage.forgeron += 1
            Forgeron_craft(fen1,personnage,item)
        else:
            personnage.alchimiste += 1
            Alchimiste(fen1,personnage,item)
        if ID < 99: anim_chaudron(fen1,personnage,item)
            
    else:   print("compo échouée")
    


#Affiche sous le nom de l'objet les composants nécessaire à sa fabriquation
#si les joueur ne les as pas dans l'inventaire, le texte est rouge

def Composant(fen1,personnage,item,ID,pos):
    font = pygame.font.SysFont(None, 25)
    objitem = ID_objet(ID,personnage,item)
    fen1.blit(piece,(pos[0],pos[1]+50))

    if personnage.argent >= objitem.argent:
        couleuror = (206,206,206)
    else:
        couleuror = (255,0,0)
        
    text_or = font.render(str(objitem.argent) ,1,couleuror)
    fen1.blit(text_or,(pos[0]+30,pos[1]+50))

    #Composant 1:
    position_1 = (pos[0]+70,pos[1]+50)
    if objitem.composant[0] == 1:
        fen1.blit(cuivre,position_1)
    if objitem.composant[0] == 2:
        fen1.blit(argent,position_1)
    if objitem.composant[0] == 3:
        fen1.blit(orichalque,position_1)
    if objitem.composant[0] == 4:
        fen1.blit(sec,position_1)
    if objitem.composant[0] == 5:
        fen1.blit(chene,position_1)
    if objitem.composant[0] == 6:
        fen1.blit(garoe,position_1)
    if objitem.composant[0] == 7:
        fen1.blit(jute,position_1)
    if objitem.composant[0] == 8:
        fen1.blit(velours,position_1)
    if objitem.composant[0] == 9:
        fen1.blit(soie,position_1)
    if objitem.composant[0] == 29:
        fen1.blit(fiole,position_1)
    if objitem.composant[0] == 0:
        fen1.blit(fioleVie,position_1)


        
    if item.inventaireLook(objitem.composant[0]) >= objitem.composant[1]:
        couleur1 = (206,206,206)
    else:
        couleur1 = (255,0,0)
    
    
    text_compo1 = font.render(str(objitem.composant[1]) ,1,couleur1)
    fen1.blit(text_compo1,(pos[0]+100,pos[1]+50))

    if len(objitem.composant)>=4: #si plus d'un composant
        #Composant 2:
        position_2 = (pos[0]+120,pos[1]+50)
        if objitem.composant[2] == 1:
            fen1.blit(cuivre,position_2)
        if objitem.composant[2] == 2:
            fen1.blit(argent,position_2)
        if objitem.composant[2] == 3:
            fen1.blit(orichalque,position_2)
        if objitem.composant[2] == 4:
            fen1.blit(sec,position_2)
        if objitem.composant[2] == 5:
            fen1.blit(chene,position_2)
        if objitem.composant[2] == 6:
            fen1.blit(garoe,position_2)
        if objitem.composant[2] == 7:
            fen1.blit(jute,position_2)
        if objitem.composant[2] == 8:
            fen1.blit(velours,position_2)
        if objitem.composant[2] == 9:
            fen1.blit(soie,position_2)
        if objitem.composant[2] == 20:
            fen1.blit(datura,position_2)
        if objitem.composant[2] == 21:
            fen1.blit(jusquiame,position_2)
        if objitem.composant[2] == 22:
            fen1.blit(hamamelis,position_2)
        if objitem.composant[2] == 23:
            fen1.blit(callune,position_2)
        if objitem.composant[2] == 24:
            fen1.blit(belladone,position_2)
            
        if item.inventaireLook(objitem.composant[2]) >= objitem.composant[3]:
            couleur2 = (206,206,206)
        else:
            couleur2 = (255,0,0)
            
        text_compo2 = font.render(str(objitem.composant[3]) ,1,couleur2)
        fen1.blit(text_compo2,(pos[0]+150,pos[1]+50))
    



#Affichage du menu alchimiste
def Alchimiste(fen1,personnage,item):
    global datura,jusquiame,hamamelis,callune,belladone,piece,fiole,fioleVie
    fond = pygame.image.load("img/MenuAuberge.png").convert()
    pygame.display.set_caption("Alchimiste")
    fen1.blit(fond,(0,0))
    font = pygame.font.SysFont(None, 25)

    jauge = pygame.image.load("img/jauge.png").convert_alpha()
    
    datura = pygame.image.load("img/objet/Datura.png").convert_alpha()
    jusquiame = pygame.image.load("img/objet/Jusquiame.png").convert_alpha()
    hamamelis = pygame.image.load("img/objet/Hamamelis.png").convert_alpha()
    callune = pygame.image.load("img/objet/Callune.png").convert_alpha()
    belladone = pygame.image.load("img/objet/Belladone.png").convert_alpha()
    piece = pygame.image.load("img/objet/piece.png").convert_alpha()
    fiole = pygame.image.load("img/objet/fioleVide.png").convert_alpha()
    fioleVie = pygame.image.load("img/objet/fioleDeVie.png").convert_alpha()

    chaudron = pygame.image.load("img/objet/chaudron.png").convert_alpha()
    
    text1 = font.render("1.Potion de soin" ,1,(206,206,206))
    Composant(fen1,personnage,item,0,(450,100))
        
    if personnage.alchimiste >= 5:
        text2 = font.render("2.Potion de soin multiple" ,1,(206,206,206))
        Composant(fen1,personnage,item,30,(450,200))
        if personnage.classe != "mage":
            text3 = font.render("3.Potion de force" ,1,(206,206,206))
            Composant(fen1,personnage,item,31,(450,300))
        else:
            text3 = font.render("3.Potion de magie" ,1,(206,206,206))
            Composant(fen1,personnage,item,32,(450,300))
            
        if personnage.alchimiste >= 15:
            text4 = font.render("4.Potion de repousse" ,1,(206,206,206))
            Composant(fen1,personnage,item,33,(450,400))
            text5 = font.render("5.Potion de vitesse" ,1,(206,206,206))            
            Composant(fen1,personnage,item,34,(450,500))

                


    fen1.blit(text1,(450,100))
    if personnage.alchimiste >= 5:
        fen1.blit(text2,(450,200))
        fen1.blit(text3,(450,300))
        if personnage.alchimiste >= 15:
            fen1.blit(text4,(450,400))
            fen1.blit(text5,(450,500))



    text_niveau = font.render("Niveau alchimiste: " + str(personnage.alchimiste) ,1,(206,206,206))
    fen1.blit(text_niveau,(450,610))

    if personnage.alchimiste < 5:
        pygame.draw.rect(fen1, (255,185,15), [14, 632, (personnage.alchimiste/5)*998, 30])
        for i in range(1,5):
             pygame.draw.line(fen1,(122,122,122), [14+(998/5)*i, 632], [14+(998/5)*i,662], 3)
    if personnage.alchimiste >= 5 and personnage.alchimiste < 15:
        pygame.draw.rect(fen1, (255,185,15), [14, 632, ((personnage.alchimiste-5)/10)*998, 30])
        for i in range(1,10):
             pygame.draw.line(fen1,(122,122,122), [14+(998/10)*i, 632], [14+(998/10)*i,662], 3)
    if personnage.alchimiste >= 15 and personnage.alchimiste < 30:
        pygame.draw.rect(fen1, (255,185,15), [14, 632, ((personnage.alchimiste-15)/15)*998, 30])
        for i in range(1,15):
             pygame.draw.line(fen1,(122,122,122), [14+(998/15)*i, 632], [14+(998/15)*i,662], 3)
    if personnage.alchimiste >= 30:
        pygame.draw.rect(fen1, (255,185,15), [14, 632, 998, 30])
        for i in range(1,15):
             pygame.draw.line(fen1,(122,122,122), [14+(998/15)*i, 632], [14+(998/15)*i,662], 3)


    fen1.blit(jauge,(12,630))
    text_retour = font.render("6.Retour" ,1,(206,206,206))
    fen1.blit(text_retour,(480,700))

    fen1.blit(chaudron, (100,350))
    fen1.blit(chaudron, (800,350))    

    pygame.display.flip()





def anim_chaudron(fen1,personnage,item):
    global chaudron
    for i in range(1,12):
        Alchimiste(fen1,personnage,item)
        chaudron = pygame.image.load("img/objet/chaudron" + str(i) + ".png").convert_alpha()
        fen1.blit(chaudron, (100,350))
        fen1.blit(chaudron, (800,350))    

        pygame.display.flip()
        time.sleep(0.07)
    Alchimiste(fen1,personnage,item)

        
    
    
#affichage du menu forgeron

def Forgeron_craft(fen1,personnage,item):
    global piece,sec,chene,garoe,cuivre,argent,orichalque,jute,velours,soie
    fond = pygame.image.load("img/MenuArtisanat.png").convert()
    pygame.display.set_caption("Forgeron_craft")
    fen1.blit(fond,(0,0))
    font = pygame.font.SysFont(None, 25)

    pointeur = pygame.image.load("img/pointeur.png").convert_alpha()
    jauge = pygame.image.load("img/jauge.png").convert_alpha()
    piece = pygame.image.load("img/objet/piece.png").convert_alpha()
    sec = pygame.image.load("img/objet/Bois_sec.png").convert_alpha()
    chene = pygame.image.load("img/objet/chene.png").convert_alpha()
    garoe = pygame.image.load("img/objet/garoe.png").convert_alpha()
    cuivre = pygame.image.load("img/objet/cuivre.png").convert_alpha()
    argent = pygame.image.load("img/objet/argent.png").convert_alpha()
    orichalque = pygame.image.load("img/objet/orichalque.png").convert_alpha()
    jute = pygame.image.load("img/objet/jute.png").convert_alpha()
    velours = pygame.image.load("img/objet/velour.png").convert_alpha()
    soie = pygame.image.load("img/objet/soie.png").convert_alpha()

    
    fen1.blit(pointeur,(150+220*int(personnage.position_pointeur),50))
    

    if personnage.classe == "mage":
        text1 = font.render("1.Baton en bois" ,1,(206,206,206))
        Composant(fen1,personnage,item,250,(100,200)) #objet necessaire : 200or + 2 bois
        text2 = font.render("1.Robe de novice" ,1,(206,206,206))
        Composant(fen1,personnage,item,100,(320,200))
        text3 = font.render("1.Capuche de novice" ,1,(206,206,206))
        Composant(fen1,personnage,item,150,(540,200))
        text4 = font.render("1.Sandales" ,1,(206,206,206))
        Composant(fen1,personnage,item,200,(760,200))
        
    if personnage.classe == "paladin":
        text1 = font.render("1.Masse" ,1,(206,206,206)) #objet necessaire : 200or + 2 bois
        Composant(fen1,personnage,item,251,(100,200))
        text2 = font.render("1.Armure en fer" ,1,(206,206,206))
        Composant(fen1,personnage,item,101,(320,200))
        text3 = font.render("1.Casque en fer" ,1,(206,206,206))
        Composant(fen1,personnage,item,151,(540,200))
        text4 = font.render("1.Pantalon de fer" ,1,(206,206,206))
        Composant(fen1,personnage,item,201,(760,200))

    if personnage.classe == "voleur":
        text1 = font.render("1.Dagues de fer" ,1,(206,206,206)) #objet necessaire : 200or + 1 bois + 1 métal
        Composant(fen1,personnage,item,252,(100,200))
        text2 = font.render("1.Armure de cuir" ,1,(206,206,206))
        Composant(fen1,personnage,item,102,(320,200))
        text3 = font.render("1.Capuche en cuir" ,1,(206,206,206))
        Composant(fen1,personnage,item,152,(540,200))
        text4 = font.render("1.Pantalon en cuir" ,1,(206,206,206))
        Composant(fen1,personnage,item,202,(760,200))

    if personnage.forgeron >= 5:
        if personnage.classe == "mage":
            text5 = font.render("2.Baton précieux" ,1,(206,206,206))
            Composant(fen1,personnage,item,253,(100,300))
            text6 = font.render("2.Robe mystique" ,1,(206,206,206))
            Composant(fen1,personnage,item,103,(320,300))
            text7 = font.render("2.Capuche mystique" ,1,(206,206,206))
            Composant(fen1,personnage,item,153,(540,300))
            text8 = font.render("2.Bottes mystique" ,1,(206,206,206))
            Composant(fen1,personnage,item,203,(760,300))
            
            
        if personnage.classe == "paladin":
            text5 = font.render("2.Marteau de combat" ,1,(206,206,206))
            Composant(fen1,personnage,item,254,(100,300))
            text6 = font.render("2.Armure en Argent" ,1,(206,206,206))
            Composant(fen1,personnage,item,104,(320,300))
            text7 = font.render("2.Casque en argent" ,1,(206,206,206))
            Composant(fen1,personnage,item,154,(540,300))
            text8 = font.render("2.Pantalon en argent" ,1,(206,206,206))
            Composant(fen1,personnage,item,204,(760,300))
            

        if personnage.classe == "voleur":
            text5 = font.render("2.Dague de Galakran" ,1,(206,206,206))
            Composant(fen1,personnage,item,255,(100,300))
            text6 = font.render("2.Cotte de maille" ,1,(206,206,206))
            Composant(fen1,personnage,item,105,(320,300))
            text7 = font.render("2.Capuche ouvert" ,1,(206,206,206))
            Composant(fen1,personnage,item,155,(540,300))
            text8 = font.render("2.Pantalon en peau" ,1,(206,206,206))
            Composant(fen1,personnage,item,205,(760,300))
            
        if personnage.forgeron >= 15:
            if personnage.classe == "mage":
                text9 = font.render("3.Baton d'Archimage" ,1,(206,206,206))
                Composant(fen1,personnage,item,256,(100,400))
                text10 = font.render("3.Robe d'invocateur" ,1,(206,206,206))            
                Composant(fen1,personnage,item,106,(320,400))
                text11 = font.render("3.Capuche d'invocateur" ,1,(206,206,206))
                Composant(fen1,personnage,item,156,(540,400))
                text12 = font.render("3.Bottes d'invocateur" ,1,(206,206,206))
                Composant(fen1,personnage,item,206,(760,400))
                
                
            if personnage.classe == "paladin":
                text9 = font.render("3.Marteau de seigneur" ,1,(206,206,206))
                Composant(fen1,personnage,item,257,(100,400))
                text10 = font.render("3.Armure d'orichalque" ,1,(206,206,206))
                Composant(fen1,personnage,item,107,(320,400))
                text11 = font.render("3.Casque d'orichalque" ,1,(206,206,206))
                Composant(fen1,personnage,item,157,(540,400))
                text12 = font.render("3.Bottes d'orichalque" ,1,(206,206,206))
                Composant(fen1,personnage,item,207,(760,400))
                
            if personnage.classe == "voleur":
                text9 = font.render("3.Dague sanguinolante" ,1,(206,206,206))
                Composant(fen1,personnage,item,258,(100,400))
                text10 = font.render("3.Armure de la guilde" ,1,(206,206,206))
                Composant(fen1,personnage,item,108,(320,400))
                text11 = font.render("3.Capuche de la guilde" ,1,(206,206,206))
                Composant(fen1,personnage,item,158,(540,400))
                text12 = font.render("3.Bottes de la guilde" ,1,(206,206,206))
                Composant(fen1,personnage,item,208,(760,400))
        
        

    fen1.blit(text1,(100,200))
    fen1.blit(text2,(320,200))
    fen1.blit(text3,(540,200))
    fen1.blit(text4,(760,200))
    if personnage.forgeron >= 5:
        fen1.blit(text5,(100,300))
        fen1.blit(text6,(320,300))
        fen1.blit(text7,(540,300))
        fen1.blit(text8,(760,300))
        if personnage.forgeron >= 15:
            fen1.blit(text9,(100,400))
            fen1.blit(text10,(320,400))
            fen1.blit(text11,(540,400))
            fen1.blit(text12,(760,400))


    text_niveau = font.render("Niveau forgeage: " + str(personnage.forgeron) ,1,(206,206,206))
    fen1.blit(text_niveau,(450,610))

    if personnage.forgeron < 5:
        pygame.draw.rect(fen1, (255,185,15), [14, 632, (personnage.forgeron/5)*998, 30])
        for i in range(1,5):
             pygame.draw.line(fen1,(122,122,122), [14+(998/5)*i, 632], [14+(998/5)*i,662], 3)
    if personnage.forgeron >= 5 and personnage.forgeron < 15:
        pygame.draw.rect(fen1, (255,185,15), [14, 632, ((personnage.forgeron-5)/10)*998, 30])
        for i in range(1,10):
             pygame.draw.line(fen1,(122,122,122), [14+(998/10)*i, 632], [14+(998/10)*i,662], 3)
    if personnage.forgeron >= 15 and personnage.forgeron < 30:
        pygame.draw.rect(fen1, (255,185,15), [14, 632, ((personnage.forgeron-15)/15)*998, 30])
        for i in range(1,15):
             pygame.draw.line(fen1,(122,122,122), [14+(998/15)*i, 632], [14+(998/15)*i,662], 3)
    if personnage.forgeron >= 30:
        pygame.draw.rect(fen1, (255,185,15), [14, 632, 998, 30])
        for i in range(1,15):
             pygame.draw.line(fen1,(122,122,122), [14+(998/15)*i, 632], [14+(998/15)*i,662], 3)


    fen1.blit(jauge,(12,630))
    text_retour = font.render("4.Retour" ,1,(206,206,206))
    fen1.blit(text_retour,(480,700))

    pygame.display.flip()



#Fonction gérant la vente d'un objet
def Echanger(fen1,personnage,item):
    objitem = ID_objet(ID[personnage.position_pointeur-1],personnage,item)
    if objitem.vente != -1:
        item.objetPerdu(pos=personnage.position_pointeur-1)
        personnage.argent += objitem.vente
        Vente(fen1,personnage,item)


#Affichage du menu vente
def Vente(fen1,personnage,item):
    global ID
    fond = pygame.image.load("img/MenuVente.png").convert()
    pygame.display.set_caption("Vente")
    piece = pygame.image.load("img/objet/piece.png").convert_alpha()
    fen1.blit(fond,(0,0))
    fondtext = pygame.font.SysFont(None, 22)
    fontnom = pygame.font.SysFont(None, 45)

    couleur = (0, 0, 0)
    pygame.draw.rect(fen1, couleur, [150, 90 + 50*personnage.position_pointeur , 220, 40])

    pygame.display.flip()

    ID=[]
    
    text0 = fondtext.render((str(item.affichage(item.ID0,personnage))) ,1,(206,206,206))
    ID.append(item.ID0)
    text1 = fondtext.render((str(item.affichage(item.ID1,personnage))) ,1,(206,206,206))
    ID.append(item.ID1)
    text2 = fondtext.render((str(item.affichage(item.ID2,personnage))) ,1,(206,206,206))
    ID.append(item.ID2)
    text3 = fondtext.render((str(item.affichage(item.ID3,personnage))) ,1,(206,206,206))
    ID.append(item.ID3)
    text4 = fondtext.render((str(item.affichage(item.ID4,personnage))) ,1,(206,206,206))
    ID.append(item.ID4)
    text5 = fondtext.render((str(item.affichage(item.ID5,personnage))) ,1,(206,206,206))
    ID.append(item.ID5)
    text6 = fondtext.render((str(item.affichage(item.ID6,personnage))) ,1,(206,206,206))
    ID.append(item.ID6)
    text7 = fondtext.render((str(item.affichage(item.ID7,personnage))) ,1,(206,206,206))
    ID.append(item.ID7)
    text8 = fondtext.render((str(item.affichage(item.ID8,personnage))) ,1,(206,206,206))
    ID.append(item.ID8)
    text9 = fondtext.render((str(item.affichage(item.ID9,personnage))) ,1,(206,206,206))
    ID.append(item.ID9)
    
    fen1.blit(text0,(200,150))
    fen1.blit(text1,(200,200))
    fen1.blit(text2,(200,250))
    fen1.blit(text3,(200,300))
    fen1.blit(text4,(200,350))
    fen1.blit(text5,(200,400))
    fen1.blit(text6,(200,450))
    fen1.blit(text7,(200,500))
    fen1.blit(text8,(200,550))
    fen1.blit(text9,(200,600))


    pygame.display.flip()

    if ID[personnage.position_pointeur-1] != -1:
        objitem = ID_objet(ID[personnage.position_pointeur-1],personnage,item)
        text_titre = fontnom.render((str(item.nomObjet(objitem.ID,personnage))) ,1,(206,206,206))
        if objitem.vente != -1:
            text_quantite = fondtext.render(("Quantité : " + str(item.inventaireLook(objitem.ID))) ,1,(206,206,206))
            text_vente = fondtext.render(("Prix de vente : " + str(objitem.vente)) ,1,(206,206,206))
            text_enter = fondtext.render(("Entrer: Vendre !") ,1,(206,206,206))
            fen1.blit(piece,(500,500))
            text_or = fondtext.render(str(personnage.argent) ,1,(206,206,206))
            fen1.blit(text_or,(530,500))

            fen1.blit(text_quantite,(400,350))
            fen1.blit(text_vente,(400,400))
            fen1.blit(text_enter,(600,600))

        else:
            text_objquete = fontnom.render("Objet de quête !" ,1,(255,0,0))
            fen1.blit(text_objquete,(520,500))
        fen1.blit(text_titre,(520,150))
        pygame.display.flip()



    
    text_retour = fondtext.render(("1: Retour") ,1,(206,206,206))
    fen1.blit(text_retour,(400,600))


    pygame.display.flip()
    

