import pickle,pygame,time,os
from module.menu_action import *
from module.menu_classe import *

'''Ce programme regroupe les 2 menus gérant la sauvegarde et le chargemetn parmis les 3 emplacemants de sauvergarde
Ainsi que les 2 fonction permettant de sauvegarder ou de charger un emplacement précis'''



def save(fen1): #Affiche au joueur les 3 emplacement de sauvegarde au début du jeu pour initialiser l'emplacement de sauvegarde de la partie
    fonttext = pygame.font.SysFont(None, 35)
    font = pygame.font.SysFont(None, 30)
    pygame.display.set_caption("Save")
    fond = pygame.image.load("img/Sauvegarde.png").convert()
    fen1.blit(fond,(0,0))
    for i in range (1,4):
        try:
            f = open('save/save'+ str(i)+'.p','rb')
            sauvegarde = pickle.Unpickler(f) #charge la class personnage de chacunes des 3 sauvergade pour afficher certaines statisitques
            perso = sauvegarde.load()

            if perso.classe == "paladin":
                tete = pygame.image.load("img/paladin/tetepaladin.png").convert_alpha()

            if perso.classe == "mage":
                tete = pygame.image.load("img/heretique/teteHeretique.png").convert_alpha()

            if perso.classe == "voleur":
                tete = pygame.image.load("img/assassin/teteAssassin.png").convert_alpha()


            
            text_nom = fonttext.render(perso.pseudo,1,(255,255,255))
            fen1.blit(text_nom,(490,70+i*140))
            text_classe = font.render(perso.classe,1,(255,255,255))
            fen1.blit(text_classe,(440,100+i*140))
            text_niveau = font.render('Niv. ' + str(perso.niveau),1,(255,255,255))
            fen1.blit(text_niveau,(540,100+i*140))
            text_or = font.render(str(perso.argent) + " d'or",1,(255,255,255))
            fen1.blit(text_or,(490,130+i*140))
            fen1.blit(tete,(250,80+i*140))
            
        except FileNotFoundError: #si un emplacement n'a pas de fichiers sauvegarde alors aucune partie n'y est sauveghardé
            texte = fonttext.render("NOUVELLE PARTIE",1,(255,255,255))
            fen1.blit(texte,(430,90+i*140))
            
        except EOFError:
            texte = fonttext.render("NOUVELLE PARTIE",1,(255,255,255))
            fen1.blit(texte,(430,90+i*140))

    pygame.display.flip()

def sauvegarde(fen1,personnage,carte,auberge,GestionPop,item,story,comp,fichier,menu): #Fonction sauvegardant les class dans l'emplacement de la partie
                                                                                        #initialisé en début de jeu
    f = open('save/save'+ str(fichier) +'.p','wb')
    personnage.save = fichier #initialise l'emplacemetn où la partie sera sauvegardé

    #sauvergade toutes les class
    pickle.dump(personnage,f,pickle.HIGHEST_PROTOCOL)
    pickle.dump(carte,f,pickle.HIGHEST_PROTOCOL)
    pickle.dump(auberge,f,pickle.HIGHEST_PROTOCOL)
    pickle.dump(GestionPop,f,pickle.HIGHEST_PROTOCOL)
    pickle.dump(item,f,pickle.HIGHEST_PROTOCOL)
    pickle.dump(story,f,pickle.HIGHEST_PROTOCOL)
    pickle.dump(comp,f,pickle.HIGHEST_PROTOCOL)   
    f.close()
    #affiche "Sauvegarde..." en haut de l'écran pendant 0.4 s
    font = pygame.font.SysFont("Mael", 35)
    textesave = font.render("Sauvegarde...",1,(255,255,255))
    fen1.blit(textesave, (20,60))
    pygame.display.flip()
    fin = pygame.time.get_ticks() + 400
    visible = True
    while visible == True:
        if fin <= pygame.time.get_ticks():
            visible = False
            if menu == "action":
                Action(fen1)
            elif menu == "carte":
                carte.reprise(fen1,personnage,item,comp)
            

    
def load(fen1): #Menu affichant les 3 emplacmeent de sauvegarde pour que le joueur choisisse la partie à charger
    fonttext = pygame.font.SysFont(None, 35)
    font = pygame.font.SysFont(None, 30)
    pygame.display.set_caption("Load")
    fond = pygame.image.load("img/charger.png").convert()
    fen1.blit(fond,(0,0))
    for i in range (1,4):
        try:
            f = open('save/save'+ str(i)+'.p','rb')
            sauvegarde = pickle.Unpickler(f)
            perso = sauvegarde.load()


            if perso.classe == "paladin":
                tete = pygame.image.load("img/paladin/tetepaladin.png").convert_alpha()

            if perso.classe == "mage":
                tete = pygame.image.load("img/heretique/teteHeretique.png").convert_alpha()

            if perso.classe == "voleur":
                tete = pygame.image.load("img/assassin/teteAssassin.png").convert_alpha()

            
            text_nom = fonttext.render(perso.pseudo,1,(255,255,255))
            fen1.blit(text_nom,(490,70+i*140))
            text_classe = font.render(perso.classe,1,(255,255,255))
            fen1.blit(text_classe,(440,100+i*140))
            text_niveau = font.render('Niv. ' + str(perso.niveau),1,(255,255,255))
            fen1.blit(text_niveau,(540,100+i*140))
            text_or = font.render(str(perso.argent) + " d'or",1,(255,255,255))
            fen1.blit(text_or,(490,130+i*140))
            fen1.blit(tete,(250,80+i*140))

            #Exceptions gérant si il n'existe aucun fichier de sauvegarde à un emplacemetn donné
            #dans ce cas le joueur ne peut rien charger, l'emplacement est vide.
        except FileNotFoundError:
            texte = fonttext.render("NOUVELLE PARTIE",1,(255,255,255))
            fen1.blit(texte,(430,90+i*140))
            
        except EOFError:
            texte = fonttext.render("NOUVELLE PARTIE",1,(255,255,255))
            fen1.blit(texte,(430,90+i*140))

    pygame.display.flip()


def Chargement(fen1,emplacement): #Charge la partie d'un emplacement précis
    #try:
    f = open('save/save' + str(emplacement) + '.p','rb')
    sauvegardes = pickle.Unpickler(f)
    personnage = sauvegardes.load()
    carte = sauvegardes.load()
    auberge = sauvegardes.load()
    GestionPop = sauvegardes.load()
    item = sauvegardes.load()
    story = sauvegardes.load()
    comp = sauvegardes.load()
    carte.regenere(fen1,GestionPop,personnage)
        
    return carte,personnage,auberge,GestionPop,item,story,comp
    '''except FileNotFoundError:
        personnage,carte,auberge,GestionPop,item,story,comp = ChoixClasse(fen1)
        personnage.save = emplacement
        if story.cinematique == True:
            story.Affichage_cine(fen1,personnage,carte,item,comp)
        sauvegarde(fen1,personnage,carte,auberge,GestionPop,item,story,comp,emplacement,"")

        carte.chargement(fen1,personnage,item,comp)'''


    
        

