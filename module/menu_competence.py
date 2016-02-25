import pygame
from module.population import *
from module.item_ID import *
from module.quete import *
'''Menu affichant les stats du personnage et compagnon
et permet d'augmenter les stats du joueur si il a des points de compétences'''

def Competence(fen1,personnage,item,GestionPop,comp):
    pygame.key.set_repeat(500, 500)
    pygame.display.set_caption("Competences")
    AffichageCompetences(fen1,personnage,item,GestionPop,comp)

def AffichageCompetences(fen1,personnage,item,GestionPop,comp):
    if comp.ami == 1:
        fond = pygame.image.load("img/competence_comp.png").convert()
    else:
        fond = pygame.image.load("img/competence.png").convert()
    fen1.blit(fond, (0,0))
    fondtext = pygame.font.SysFont("Arial", 18)
    fondtitle = pygame.font.SysFont("Arial", 24)
    textJoueur = fondtext.render("Personnage :",1,(255,255,255))
    textVieJoueur = fondtext.render("Vie : " + str(personnage.vie) + "/" + str(personnage.viemax),1,(255,255,255))
    textXp = fondtext.render("XP : " + str(personnage.xp) + "/" + str(personnage.xpmax),1,(255,255,255))
    textNiveau = fondtext.render("Niveau : " + str(personnage.niveau),1,(255,255,255))
    textor = fondtext.render("Or : " + str(personnage.argent),1,(255,255,255))
    
    population = fondtext.render("Population : " + str(GestionPop.population),1,(255,255,255))
    contamination = fondtext.render("Contaminés : " + str(GestionPop.contamination),1,(255,255,255))

    fen1.blit(population,(50,690))
    fen1.blit(contamination,(50,720))


    
    if personnage.competence > 1:
        textCompetence = fondtext.render("Points de compétence : " + str(personnage.competence),1,(255,255,255))
    elif personnage.competence == 1 :
        textCompetence = fondtext.render("Point de compétence : " + str(personnage.competence),1,(255,255,255))
    else:
        textCompetence = fondtext.render("0 point de compétence",1,(255,255,255))


    
    if item.IDArme != -1:
        objitem = ID_objet(item.IDArme,personnage,item)
        if personnage.classe == "mage":
            textPrincipal = fondtext.render("Intelligence : " + str(personnage.principale - objitem.arme)+ " ( + " + str(objitem.arme) + " )",1,(255,255,255))
        elif personnage.classe == "paladin":
            textPrincipal = fondtext.render("Force : " + str(personnage.principale-objitem.arme)+ " ( + "  + str(objitem.arme) +" )",1,(255,255,255))
        else:
            textPrincipal = fondtext.render("Agilité : " + str(personnage.principale-objitem.arme)+ " ( + "  + str(objitem.arme) +" )",1,(255,255,255))

    else:
        if personnage.classe == "mage":
            textPrincipal = fondtext.render("Intelligence : " + str(personnage.principale),1,(255,255,255))
        elif personnage.classe == "paladin":
            textPrincipal = fondtext.render("Force : " + str(personnage.principale),1,(255,255,255))
        else:
            textPrincipal = fondtext.render("Agilité : " + str(personnage.principale),1,(255,255,255))

  
    
    textDmini = fondtext.render("Dégats mini : " + str(int(1/2 * personnage.principale)),1,(255,255,255))
    textDmaxi = fondtext.render("Dégats maxi : " + str(int(5/4 * personnage.principale)),1,(255,255,255))
    textEsquive = fondtext.render("Esquive : " + str(personnage.esquive) + " %",1,(255,255,255))
    textCritique = fondtext.render("Critique : " + str(personnage.critique)+ " %",1,(255,255,255))
    if personnage.armure > 0:
        textConstitution = fondtext.render("Constitution : " + str(personnage.constitution) + " ( + " + str(personnage.armure) +" )",1,(255,255,255))
    else:
        textConstitution = fondtext.render("Constitution : " + str(personnage.constitution),1,(255,255,255))

    


    fen1.blit(textJoueur,(820,150))
    fen1.blit(textVieJoueur,(820,180))
    fen1.blit(textXp,(820,210))
    fen1.blit(textNiveau,(820,240))
    fen1.blit(textor,(820,270))
    fen1.blit(textCompetence,(820,300))
    


    fen1.blit(textPrincipal,(820,430))
    fen1.blit(textDmini,(820,460))
    fen1.blit(textDmaxi,(820,490))
    fen1.blit(textEsquive,(820,520))
    fen1.blit(textCritique,(820,550))
    fen1.blit(textConstitution,(820,580))
    


    if comp.ami == 1:
        textComp = fondtext.render(str(comp.name) + " :",1,(255,255,255))
        textVieComp = fondtext.render("Vie : " + str(comp.vie) + "/" + str(comp.viemax),1,(255,255,255))
        textDminiComp = fondtext.render("Dégats mini : " + str(comp.degatMin),1,(255,255,255))
        textDmaxiComp = fondtext.render("Dégats maxi : " + str(comp.degatMax),1,(255,255,255))
        textEsquiveComp = fondtext.render("Esquive : " + str(comp.esquive) + " %",1,(255,255,255))
        textCritiqueComp = fondtext.render("Critique : " + str(comp.critique)+ " %",1,(255,255,255))




        fen1.blit(textComp,(620,150))
        fen1.blit(textVieComp,(620,180))
        fen1.blit(textDminiComp,(620,210))
        fen1.blit(textDmaxiComp,(620,240))
        fen1.blit(textEsquiveComp,(620,270))
        fen1.blit(textCritiqueComp,(620,300))




    
    if personnage.competence > 0:
        Augmenter = fondtext.render("Que souhaitez vous augmenter ?",1,(255,255,255))
        AugmenterVie = fondtext.render("1.Vie (" + str(personnage.vie) + ")",1,(255,255,255))
        
        if personnage.classe == "mage":
            AugmenterPrincipal = fondtext.render("2.Intelligence (" + str(personnage.principale) + ")",1,(255,255,255))
        elif personnage.classe == "paladin":
            AugmenterPrincipal = fondtext.render("2.Force (" + str(personnage.principale) + ")",1,(255,255,255))
        else:
            AugmenterPrincipal = fondtext.render("2.Agilité (" + str(personnage.principale) + ")",1,(255,255,255))

        AugmenterConstitution = fondtext.render("3.Constitution (" + str(personnage.constitution) + ")",1,(255,255,255))
        if personnage.esquive < 50:
            AugmenterEsquive = fondtext.render("4.Esquive (" + str(personnage.esquive) + ")",1,(255,255,255))
        if personnage.critique < 50 and personnage.esquive <50:
            AugmenterCritique = fondtext.render("5.Critique (" + str(personnage.critique) + ")(+1crit/-2cpts)",1,(255,255,255))
        if personnage.critique <50 and personnage.esquive >=50:
            AugmenterCritique = fondtext.render("4.Critique (" + str(personnage.critique) + ")(+1crit/-2cpts)",1,(255,255,255))
            
        fen1.blit(Augmenter,(200,170))
        fen1.blit(AugmenterVie,(150,230))
        fen1.blit(AugmenterPrincipal,(150,260))
        fen1.blit(AugmenterConstitution,(150,290))
        if personnage.esquive < 50:
            fen1.blit(AugmenterEsquive,(150,320))
        if personnage.critique < 50 and personnage.esquive < 50:
            fen1.blit(AugmenterCritique,(150,350))
        if personnage.critique < 50 and personnage.esquive >= 50:
            fen1.blit(AugmenterCritique,(150,320))
    pygame.display.flip()



