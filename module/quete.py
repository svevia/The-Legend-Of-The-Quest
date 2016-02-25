import pygame,time
from module.compagnon import *
from module.menu_action import *

'''
Cette classe recense toutes les quêtes du jeu en attribuant à chacune un ID.
Chaque quête a dans sa definition:
-un titre (self.titre)
-une description (self.desc)
-un texte à afficher lorsque la quêtre est terminée mais pas rendue (self.rendre)
-un type (self.type)
-un objetctif (nombre de monstre à tuer, objets à ramener...)
-les gains obtenus (xp et or)
-le texte à affciher lorque la quête vient d'être terminée (self.textfinit)
-dans la boucle (if story.activation_quetes[self.ID] == 0) on écrit les textes à afficher lorsque le joueur prend la quête
-dans la boucle (if story.activation_quetes[self.ID] == 2) on écrit les textes à afficher lorsque le joueur rend la quête

L'activation des quêtes se fait via la liste story.activation_quetes, cette liste contient une valeur pour chaques quête allant de 0 à 3:
-0 : la quête n'est pas activée
-1 : la quête est en cours de réalisation
-2 : la quête est finit mais pas rendu (le joueur n'a pas reçu de récompense) => inutile pour les quêtes de type voyage
-3 : la quête est terminée et rendue
'''



class quest_ID:
    def __init__ (self,fen1,ID,personnage,item,story,comp,carte):
        self.ID = ID
        self.font = pygame.font.SysFont(None, 32)
        self.crea_quete(fen1,personnage,item,story,comp,carte)


    def crea_quete(self,fen1,personnage,item,story,comp,carte):
        if self.ID == 0:
            self.titre = "Libérer les alentours"
            self.desc = "Faites quelques combats autour du village pour éloigner les monstres."
            self.rendre = "Retournez dans le village pour recevoir les acclamations des villageois."
            self.type = "tuerie"
            self.a_tuer = 5
            self.argent = 50
            self.xp = 100
            self.textfinit = self.font.render("Le village est sécurisé ! Retournez chercher la récompense.",1,(206,206,206))
            if story.activation_quetes[self.ID] == 0:
                story.activation_quetes[self.ID] = 1
                story.objectif_quetes[self.ID] = self.a_tuer
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Pauvre fou ! Partez, tant que vous le pouvez encore !",1,(206,206,206))
                self.texte2 = self.font.render("Un mal inconnu touche le Sud de la région.",1,(206,206,206))
                self.texte3 = self.font.render("Des paysans ont disparu, d'étranges créature ont été aperçus...",1,(206,206,206))
                self.texte4 = self.font.render("Si vous êtes assez fou pour rester, aidez-nous !",1,(206,206,206))
                self.affichage_texte(fen1)
                time.sleep(2)
                self.texte1 = self.font.render("Allez donc défendre les alentours.",1,(206,206,206))
                self.texte2 = self.font.render("Repoussez les monstres qui rôdent autour du village.",1,(206,206,206))
                self.texte3 = self.font.render("Nous n'avons pas grand chose mais si vous réussissez, vous recevrez une récompense !",1,(206,206,206))
                self.texte4 = self.font.render("Aller, partez maintenant ! Et restez en vie...",1,(206,206,206))
                self.affichage_texte(fen1)
                time.sleep(2)

            if story.activation_quetes[self.ID] == 2 and carte.lettre == "V" :
                story.activation_quetes[self.ID] = 3
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Vous êtes plus coriace que je ne l'aurais cru...",1,(206,206,206))
                self.texte2 = self.font.render("Félicitation gamin, en tuant ces monstres vous nous avez rendu un fier service !",1,(206,206,206))
                self.texte3 = self.font.render("Voilà pour vous : vous recevez " + str(self.argent) + " d'or et " + str(self.xp) + " d'expérience.",1,(206,206,206))
                self.texte4 = self.font.render("Encore un fois, je vous remercie de nous avoir aidé !",1,(206,206,206))
                personnage.argent += self.argent
                personnage.xp += self.xp

                personnage,comp = self.verification_niveau(personnage,comp)
                
                self.affichage_texte(fen1)
                quete = quest_ID(fen1,1,personnage,item,story,comp,carte)


        elif self.ID == 1:
            self.titre = "De bien piètres renforts !"
            self.desc = "Livrez les vivres au village à l'Est de la région."
            self.type = "voyage"
            self.argent = 4
            self.xp = 100

            if story.activation_quetes[self.ID] == 0:
                story.activation_quetes[self.ID] = 1
                story.objectif_quetes[self.ID] = 1
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Vous avez l'air de savoir vous battre...",1,(206,206,206))
                self.texte2 = self.font.render("Votre aide pourrait nous être très précieuse.",1,(206,206,206))
                self.texte3 = self.font.render("Si vous voulez encore vous rendre utile, apportez ces vivres au village à l'Est.",1,(206,206,206))
                self.texte4 = self.font.render("La seule route pour y accéder est trop dangereuse pour nos marchands...",1,(206,206,206))
                self.affichage_texte(fen1)
                time.sleep(2)
                fen1.blit(self.fond, (0,0))
                pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
                
                if item.inventaireRempli() == 1:
                    self.texte1 = self.font.render("Votre inventaire est plein, revenez quand vous aurez de la place.",1,(206,206,206))
                elif item.inventaireRempli() == 0:
                    story.activation_quetes[self.ID] = 1
                    item.loot(92)
                    self.texte1 = self.font.render("Les vivres sont placé dans votre inventaire.",1,(206,206,206))
                    
                fen1.blit(self.texte1,(10,580))
                pygame.display.flip()
                time.sleep(3)
                Action(fen1)

            if story.activation_quetes[self.ID] == 1 and carte.lettre == "S":
                story.activation_quetes[self.ID] = 3
                story.objectif_quetes[self.ID] = 0
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Oh dieu soit loué ! Voilà enfin du ravitaillement !",1,(206,206,206))
                self.texte2 = self.font.render("Merci beaucoup, nous vous devons la vie !",1,(206,206,206))
                self.texte3 = self.font.render("Nous n'avons pas grand chose à offrir mais prenez ces quelques pièces...",1,(206,206,206))
                self.texte4 = self.font.render("Vous recevez " + str(self.argent) + " d'or et " + str(self.xp) + " d'expérience.",1,(206,206,206))
                personnage.argent += self.argent
                personnage.xp += self.xp

                personnage,comp = self.verification_niveau(personnage,comp)


                self.affichage_texte(fen1)
                quete = quest_ID(fen1,2,personnage,item,story,comp,carte)

        elif self.ID == 2:
            self.titre = "Médecin ambulant"
            self.desc = "Apporter une potion pour soigner la doyenne du village."
            self.rendre = "Donnez la potion à la doyenne du village."
            self.type = "Apporter"
            self.argent = 120
            self.xp = 50

            if story.activation_quetes[self.ID] == 0:
                story.activation_quetes[self.ID] = 1
                story.objectif_quetes[self.ID] = 1
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Vous avez dejà tant fait pour nous mais vous êtes notre dernière chance.",1,(206,206,206))
                self.texte2 = self.font.render("Notre doyenne, Antéa, est gravement malade.",1,(206,206,206))
                self.texte3 = self.font.render("Elle a urgemment besoin d'une potion, apportez cette potion et nous vous serons très",1,(206,206,206))
                self.texte4 = self.font.render("reconnaissant. Mais faîtes vite, son état se dégrade rapidement d'heure en heure !",1,(206,206,206))
                self.affichage_texte(fen1)
                time.sleep(1)
                
            if story.activation_quetes[self.ID] == 1 and carte.lettre == "S" and item.inventaireLook(0) < 1:
                Action(fen1)
            if story.activation_quetes[self.ID] == 1 and carte.lettre == "S" and item.inventaireLook(0) >= 1:
                pygame.display.set_caption("Choix_potion")
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Oh, vous avez une potion ! C'est magnifique !",1,(206,206,206))
                self.texte2 = self.font.render("Grâce à cette potion notre doyenne ira très vite mieux.",1,(206,206,206))
                self.texte3 = self.font.render("1.Donner la potion.",1,(206,206,206))
                self.texte4 = self.font.render("2.Faire patienter cette vielle dame.",1,(206,206,206))
                self.affichage_texte_speciale(fen1)

            if story.activation_quetes[self.ID] == 2 and carte.lettre == "S":
                story.activation_quetes[self.ID] = 3
                story.objectif_quetes[self.ID] = 0
                item.objetPerdu(0)
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Vous recevez " + str(self.argent) + " d'or et " + str(self.xp) + " d'expérience.",1,(206,206,206))
                personnage.argent += self.argent
                personnage.xp += self.xp

                personnage,comp = self.verification_niveau(personnage,comp)
                pygame.display.set_caption("Cinématique")
                fen1.blit(self.fond, (0,0))
                pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
                fen1.blit(self.texte1,(10,580))
                pygame.display.flip()
                time.sleep(2)


        elif self.ID == 3:
            self.titre = "Des nouvelles du front"
            self.desc = "Le village au sud-ouest a subit de gros dégâts, allez leur venir en aide."
            self.type = "voyage"
            

            if story.activation_quetes[self.ID] == 0:
                pygame.display.set_caption("Cinématique")
                story.activation_quetes[self.ID] = 1
                story.objectif_quetes[self.ID] = 1
                fichier = []
                pos =0
                carte.perso = carte.fichier[17]
                for i in range(17,26):
                    fichier.append(pygame.image.load("img/event/messager/Messager"+str(i)+".png").convert_alpha())

                        
                inconnu = fichier[pos]
                position_inconnu = inconnu.get_rect()
                position_inconnu = position_inconnu.move(-10,390)

                deplacement = 0

                while deplacement < 492:
                    pos += 1
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


                self.texte1 = self.font.render("Alors comme ça, c'est de vous dont tout le monde parle ?",1,(206,206,206))
                self.texte2 = self.font.render("J'ai un message pour vous : le village au Sud-Ouest a été attaqué !",1,(206,206,206))
                self.texte3 = self.font.render("Ils ont besoin de renforts, allez là bas pour les aider : tout le monde doit se battre.",1,(206,206,206))
                self.texte4 = self.font.render("Oh, j'allais oublier, contournez la grotte au centre du continent, vous n'êtes pas prêts...",1,(206,206,206))
                self.affichage_texte_carte(fen1,personnage,item,comp)
                time.sleep(2)


                deplacement = 0
                fichier = []
                pos = 1
                for i in range(7,16):
                    fichier.append(pygame.image.load("img/event/messager/Messager"+str(i)+".png").convert_alpha())
                        
                while deplacement < 500:
                    pos += 1
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

                carte.reprise(fen1,personnage,item,comp)
                
            if story.activation_quetes[self.ID] == 1 and carte.lettre == "N":
                story.activation_quetes[self.ID] = 3
                story.objectif_quetes[self.ID] = 0
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Vous... Vous avez réussi à traverser ?",1,(206,206,206))
                self.texte2 = self.font.render("Beaucoup de nos camarades sont tombés en essayant de sortir d'ici.",1,(206,206,206))
                self.texte3 = self.font.render("Cala fait plusieurs jours que nous sommes enfermés dans notre village.",1,(206,206,206))
                self.texte4 = self.font.render("Nous sommes affamés et nous n'avons aucun moyens de nous défendre.",1,(206,206,206))

                self.affichage_texte(fen1)

                quete = quest_ID(fen1,4,personnage,item,story,comp,carte)

        elif self.ID ==4:
            self.titre = "Aux armes citoyens !"
            self.desc = "Apporter aux villageois de quoi fabriquer des armes (3 bois sec et 1 lingot de cuivre)."
            self.type = "Apporter"
            self.argent = 150
            self.xp = 300



            if story.activation_quetes[self.ID] == 0:
                story.activation_quetes[self.ID] = 1
                story.objectif_quetes[self.ID] = 1
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Nous avons besoin d'armes pour repousser l'envahisseur !",1,(206,206,206))
                self.texte2 = self.font.render("Apportez-nous tous les materieaux nécessaires pour fabriquer des armes.",1,(206,206,206))
                self.texte3 = self.font.render("Nos forgerons ce chargeront du reste, 3 bois secs et 1 lingot de cuivre devraient suffir.",1,(206,206,206))
                self.texte4 = self.font.render("Profitez-en pour abattre quelques ennemis...",1,(206,206,206))
                self.affichage_texte(fen1)
                time.sleep(1)

            if story.activation_quetes[self.ID] == 1 and carte.lettre == "N" and (item.inventaireLook(4) < 3 or item.inventaireLook(1) < 1):
                Action(fen1)
            if story.activation_quetes[self.ID] == 1 and carte.lettre == "N" and item.inventaireLook(4) >= 3 and item.inventaireLook(1) >= 1:
                pygame.display.set_caption("Choix_donner_ressources")
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Avez-vous réussi ?",1,(206,206,206))
                self.texte2 = self.font.render("Nous faisons chauffer la forge, donnez-nous les ressources.",1,(206,206,206))
                self.texte3 = self.font.render("1.Donner de quoi forger les armes (3 bois sec + 1 cuivre).",1,(206,206,206))
                self.texte4 = self.font.render("2.Ne pas donner les ressources maintenant.",1,(206,206,206))
                self.affichage_texte_speciale(fen1)


            if story.activation_quetes[self.ID] == 2 and carte.lettre == "N":
                story.activation_quetes[self.ID] = 3
                story.objectif_quetes[self.ID] = 0
                item.objetPerdu(4,3)
                item.objetPerdu(1)
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Vous recevez " + str(self.argent) + " d'or et " + str(self.xp) + " d'expérience.",1,(206,206,206))
                personnage.argent += self.argent
                personnage.xp += self.xp

                personnage,comp = self.verification_niveau(personnage,comp)
                pygame.display.set_caption("Cinématique")
                fen1.blit(self.fond, (0,0))
                pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
                fen1.blit(self.texte1,(10,580))
                pygame.display.flip()
                time.sleep(2)

                quete = quest_ID(fen1,5,personnage,item,story,comp,carte)
                

        elif self.ID == 5:
            self.titre = "Echantillon"
            self.desc = "Allez chercher des échantillons sur des monstres contaminés."
            self.rendre = "Retournez au village aves les échantillons."
            self.type = "Chercher"
            self.argent = 300
            self.xp = 250
            self.textfinit = self.font.render("Vous avez les échantillons, rentrez au village !",1,(206,206,206))
            self.textEchec = self.font.render("Le scientifique à besoin de repos, retournez le chercher au village.",1,(206,206,206))

            if story.activation_quetes[self.ID] == 0:
                if comp.ami == 1 :
                    story.ancienCompID = comp.IDCompagnon
                    story.ancienComp = 1
                else : story.ancienComp = 0

                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Maintenant que nous avons les armes, on a besoin de savoir contre quoi on se bat.",1,(206,206,206))
                self.texte2 = self.font.render("Pour cela, notre éminent scientifique, qui est surtout le plus ancien, à besoin de vous.",1,(206,206,206))
                self.texte3 = self.font.render("Avec votre aide, il veut récupérer des échantillons sur des monstres contaminés.",1,(206,206,206))
                self.texte4 = self.font.render("Allez en tuer avec lui, mais ramenez notre scientifique vivant à tout prix.",1,(206,206,206))
                self.affichage_texte(fen1)
                time.sleep(1)

                pygame.display.set_caption("Choix quête 5")
                self.texte1 = self.font.render("Le scientifique sera votre compagnon le temps de la quête.",1,(206,206,206))
                self.texte2 = self.font.render("Si vous avez déjà un compagnon, vous le retrouverez après votre victoire.",1,(206,206,206))
                self.texte3 = self.font.render("1.Prendre le scientifique et commencer l'expédition.",1,(206,206,206))
                self.texte4 = self.font.render("2.Ne pas encore y aller.",1,(206,206,206))
                self.affichage_texte_speciale(fen1)
                
                

            if story.activation_quetes[self.ID] == 2 and carte.lettre == "N":
                story.activation_quetes[self.ID] = 3
                story.objectif_quetes[self.ID] = 0
                item.objetPerdu(90,3)
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Vous avez réussi ! Notre scientifique est fou de joie !",1,(206,206,206))
                self.texte2 = self.font.render("Même si je dois avouer que je ne suis pas sûr des résultats de ses recherches.",1,(206,206,206))
                self.texte3 = self.font.render("Cependant, vous méritez une petite récompense pour l'aide apportée.",1,(206,206,206))
                self.texte4 = self.font.render("1.Récupérer votre récompense : " + str(self.argent) + " d'or et " + str(self.xp) + " d'expérience.",1,(206,206,206))
                self.affichage_texte(fen1)
                pygame.display.set_caption("Choix quête 5")
                
                personnage.argent += self.argent
                personnage.xp += self.xp
                

        elif self.ID == 6:
            self.titre = "Sérum"
            self.desc = "Apporter le sérum au village du sud-est."
            self.type = "Apporter"
            self.argent = 0
            self.xp = 0
            
            if story.activation_quetes[self.ID] == 0:
                self.objectif_quetes[i] = 1
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Grâce aux échantillons que vous nous avez apportés, notre scientifique a mis au point",1,(206,206,206))
                self.texte2 = self.font.render("un sérum repoussant la contamination. Malheureusement, il ne peut le finir qu'avec une",1,(206,206,206))
                self.texte3 = self.font.render("certaine plante... Et cette plante ne se trouve qu'aux abords du village du sud-est.",1,(206,206,206))
                self.texte4 = self.font.render("Prenez ce sérum et allez trouver une Arnica, vous devez y arriver !",1,(206,206,206))
                self.affichage_texte(fen1)
                fen1.blit(self.fond, (0,0))
                pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
                
                if item.inventaireRempli() == 1:
                    self.texte1 = self.font.render("Votre inventaire est plein, revenez quand vous aurez de la place.",1,(206,206,206))
                elif item.inventaireRempli() == 0:
                    story.activation_quetes[self.ID] = 1
                    item.loot(91)
                    self.texte1 = self.font.render("Le sérum est placé dans votre inventaire.",1,(206,206,206))
                    
                fen1.blit(self.texte1,(10,580))
                pygame.display.flip()
                time.sleep(3)
                Action(fen1)


            if story.activation_quetes[self.ID] == 1 and carte.lettre == "D":
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("A l'aide ! On est attaqué par les contaminés !",1,(206,206,206))
                self.texte2 = self.font.render("Vous, qui êtes-vous ? Attendez, je vous reconnais : vous êtes le héros ?",1,(206,206,206))
                self.texte3 = self.font.render("Celui dont on parle ? Alors, allez aider nos tacticiens à gérer cette bataille !",1,(206,206,206))
                self.texte4 = self.font.render("Dépéchez-vous, votre aide nous sera très précieuse.",1,(206,206,206))
                self.affichage_texte(fen1)

                pygame.display.set_caption("Choix quête 6")
                self.fond = pygame.image.load("img/menuAction.png").convert()
                self.texte1 = self.font.render("Nous avons besoin d'un stratège, vous êtes notre dernière chance",1,(206,206,206))
                self.texte2 = self.font.render("Ce sera un combat long et éprouvant, êtes vous prêt ?",1,(206,206,206))
                self.texte3 = self.font.render("1.Allons-y",1,(206,206,206))
                self.texte4 = self.font.render("2.Je dois encore me préparer",1,(206,206,206))
                self.affichage_texte_speciale(fen1)
                
        elif self.ID == 7:
            self.titre = "La défense du village"
            self.desc = "Défendez le village contre l'invasion"
            self.type = "Défense"
            self.argent = 1000
            self.xp = 500

            if story.activation_quetes[self.ID] == 2:
                if personnage.bataille == 1:
                    self.fond = pygame.image.load("img/menuAction.png").convert()
                    self.texte1 = self.font.render("Notre victoire d'aujourd'hui à porter un coup fatal aux armées de la contamination.",1,(206,206,206))
                    self.texte2 = self.font.render("Il est temps de frapper fort, directement au coeur de leur territoire.",1,(206,206,206))
                    self.texte3 = self.font.render("Il y a une grotte au coeur du continent, c'est de là que la contamination s'étend",1,(206,206,206))
                    self.texte4 = self.font.render("Trouver la cause de la contamination et libérer notre pays de ce fardeau !",1,(206,206,206))
                    self.affichage_texte(fen1)

                    self.fond = pygame.image.load("img/menuAction.png").convert()
                    self.texte1 = self.font.render("Oh j'allais oublier, nos chercheur ont mis au point une protection contre",1,(206,206,206))
                    self.texte2 = self.font.render("cette contamination, il vous protegera de celle-ci, buvez-le",1,(206,206,206))
                    self.texte3 = self.font.render("Nous n'avons pas oublier ce que vous avez fait pour nous en protégeant le village,",1,(206,206,206))
                    self.texte4 = self.font.render("voilà pour vous, Vous recevez " + str(self.argent) + " d'or et " + str(self.xp) + " d'expérience.",1,(206,206,206))
                    self.affichage_texte(fen1)
                    personnage.argent += self.argent
                    personnage.xp += self.xp

                    personnage,comp = self.verification_niveau(personnage,comp)
                    story.activation_quetes[self.ID] = 3
                    story.activation_quetes[8] = 1
                    Action(fen1)
                    
                if personnage.bataille == 0:
                    self.texte1 = self.font.render("Nous avons perdu le village, mais le tenir mobilise leurs troupes",1,(206,206,206))
                    self.texte2 = self.font.render("Il est temps de contre-attaquer, directement au coeur de leur territoire.",1,(206,206,206))
                    self.texte3 = self.font.render("Il y a une grotte au coeur du continent, elle semble être la source de ce désastre",1,(206,206,206))
                    self.texte4 = self.font.render("Allez-y et libérer notre peuple de ce fardeau !",1,(206,206,206))
                    self.affichage_texte_carte(fen1,personnage,item,comp)

                    self.texte1 = self.font.render("Oh j'allais oublier, nos chercheur ont mis au point une protection contre",1,(206,206,206))
                    self.texte2 = self.font.render("cette contamination, il vous protegera de celle-ci, buvez-le",1,(206,206,206))
                    self.texte3 = self.font.render("Vous êtes le seul espoir de ces gens, ne les decevez pas !",1,(206,206,206))
                    self.texte4 = self.font.render("",1,(206,206,206))
                    self.affichage_texte_carte(fen1,personnage,item,comp)

                    story.activation_quetes[self.ID] = 3
                    story.activation_quetes[8] = 1
                    carte.reprise(fen1,personnage,item,comp)

            
                
        elif self.ID == 8:
            self.titre = "Jusqu'au dernier souffle !"
            self.desc = "Rendez vous au centre de la contamination pour l'éradiquer"
            self.type = "voyage"
            self.argent = 1000
            self.xp = 500


                
    def affichage_texte(self,fen1):
        pygame.display.set_caption("Cinématique")
        fen1.blit(self.fond, (0,0))
        pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
        fen1.blit(self.texte1,(10,580))
        pygame.display.flip()
        time.sleep(2)
        fen1.blit(self.texte2,(10,610))
        pygame.display.flip()
        time.sleep(2)
        fen1.blit(self.texte3,(10,640))
        pygame.display.flip()
        time.sleep(2)
        fen1.blit(self.texte4,(10,670))
        pygame.display.flip()
        time.sleep(3)

    def affichage_texte_carte(self,fen1,personnage,item,comp):
        pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
        fen1.blit(self.texte1,(10,580))
        pygame.display.flip()
        time.sleep(2)
        fen1.blit(self.texte2,(10,610))
        pygame.display.flip()
        time.sleep(2)
        fen1.blit(self.texte3,(10,640))
        pygame.display.flip()
        time.sleep(2)
        fen1.blit(self.texte4,(10,670))
        pygame.display.flip()
        time.sleep(3)


    def affichage_texte_speciale(self,fen1):
        fen1.blit(self.fond, (0,0))
        pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
        fen1.blit(self.texte1,(10,580))
        pygame.display.flip()
        time.sleep(2)
        fen1.blit(self.texte2,(10,610))
        pygame.display.flip()
        time.sleep(2)
        fen1.blit(self.texte3,(10,640))
        fen1.blit(self.texte4,(10,670))
        pygame.display.flip()


    def verification_niveau(self,personnage,comp):
        #Passage d'un niveau quand l'xp dépasse l'xpmax, gain de points de compétences, régénération de la vie au max, augmentation de l'xpmax à atteindre
        while personnage.xp >= personnage.xpmax :
            personnage.up = 1
            personnage.niveau += 1
            personnage.competence += 5
            personnage.vie = personnage.viemax
            personnage.xpmax += personnage.xpbase + (personnage.niveau - 1) * 250
            comp = compagnon(1,comp.IDCompagnon,personnage)
        
        return personnage,comp





        
