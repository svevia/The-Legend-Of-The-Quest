import pygame,random,time

class CombatAuberge :


    def __init__ (self) :
        self.renommee = 0 #Augmente/diminue à chaque self.victoire/défaite en duel dans l'auberge, permet de combattre des ennemis de plus en plus fort
        self.victoire = 0 #self.victoire/self.defaite des duels 
        self.defaite = 0
        self.premiereVisite = 0 #Permet l'affichage d'un texte uniquement lors de la première visite du menu des duels
        self.premierParie = 0 #Permet l'affichage d'un texte uniquement lors de la première visite du menu des paris
        self.gainTotal = 0 #Argent gagné lors des duels
        self.parie = 0 #Argent parié par le joueur
        self.argent = 0
        self.gain = 0

           
    def menuDuel(self,fen1,personnage,item):
        global fondtext
        
        self.parie = 0
        
        self.fond = pygame.image.load("img/menuAuberge.png").convert()
        fen1.blit(self.fond,(0,0))
        pygame.display.set_caption("Combat auberge")
        
        fondtext = pygame.font.SysFont(None, 22)

        #Textes lorsqu'aucun combat à l'auberge n'à encore été effectué
        if self.premiereVisite == 0 :
            text1 = fondtext.render("Un homme s'approche de vous, visiblement saoul !",1,(206,206,206))
            text2 = fondtext.render("'Tu veux t'battre ?'",1,(206,206,206))
            text3 = fondtext.render("Vous regardez autour de vous, il ne peut que vous parler.",1,(206,206,206))
            text4 = fondtext.render("Vous remarquez des ivrognes se battant dans un coin de l'auberge.",1,(206,206,206))
            text5 = fondtext.render("Quelques hommes autour d'eux, des pièces d'or dans les mains.",1,(206,206,206))
            text6 = fondtext.render("Un des hommes tombe, assommé pour un bon bout de temps.",1,(206,206,206))
            text7 = fondtext.render("On vous propose de combattre, à mains nues et avec honneur.",1,(206,206,206))
            text8 = fondtext.render("Tant qu'à faire : parier !",1,(206,206,206))

            fen1.blit(text1,(450,230))
            fen1.blit(text2,(450,260))
            fen1.blit(text3,(450,290))
            fen1.blit(text4,(450,320))
            fen1.blit(text5,(450,350))
            fen1.blit(text6,(450,380))
            fen1.blit(text7,(450,410))
            fen1.blit(text8,(450,440))

        #Après le premier combat, affiche les self.victoires/défaites et la renommée
        else :
            text1 = fondtext.render("Envie de vous battre ?",1,(206,206,206))
            if self.victoire == 0 or self.victoire == 1 : text2 = fondtext.render(str(self.victoire) + " victoire",1,(206,206,206))
            else : text2 = fondtext.render(str(self.victoire) + " victoires",1,(206,206,206))
            if self.defaite == 0 or self.defaite == 1 : text3 = fondtext.render(str(self.defaite) + " defaite",1,(206,206,206))
            else : text3 = fondtext.render(str(self.defaite) + " defaites",1,(206,206,206))
            text4 = fondtext.render("Renommée : " + str(self.renommee),1,(206,206,206))

            fen1.blit(text1,(450,230))
            fen1.blit(text2,(450,260))
            fen1.blit(text3,(450,290))
            fen1.blit(text4,(450,320))


        #Permet la navigation dans le menu, gérer par les binds ("boutons")
        textretour = fondtext.render("1.Retourner boire",1,(206,206,206))
        textcombat = fondtext.render("2.Combattre",1,(206,206,206))
        if personnage.argent < 10 :
            textparie = fondtext.render("Vous n'avez pas assez d'argent pour parier.",1,(206,206,206))
        else :
            textparie = fondtext.render("3.Parier et combattre",1,(206,206,206))
            
        #Place les "boutons"
        fen1.blit(textretour,(120,230))    
        fen1.blit(textcombat,(120,260))
        fen1.blit(textparie,(120,290))

        pygame.display.flip()



    def parieurs(self,fen1,personnage,item):
        if self.renommee < 10 :
            self.temps = 2
            self.toucher = 4
        elif self.renommee >= 10 and self.renommee < 50 :
            self.temps = 1.5
            self.toucher = 3
        elif self.renommee >= 50 and self.renommee < 80 :
            self.temps = 1
            self.toucher = 2
        elif self.renommee >= 80 and self.renommee <= 100 :
            self.temps = 0.5
            self.toucher = 1

        if self.renommee < 10 : self.observateur = random.randint(0,5)
        if self.renommee >= 10 and self.renommee < 30 : self.observateur = random.randint(0,10)
        if self.renommee >= 30 and self.renommee < 50 : self.observateur = random.randint(0,15)
        if self.renommee >= 50 and self.renommee < 80 : self.observateur = random.randint(0,20)
        if self.renommee >= 80 and self.renommee <= 100 : self.observateur = random.randint(0,30)

        self.pariePour = random.randint(0,self.observateur)


    def gestionCombatAuberge(self,fen1,personnage,item):
        
        if self.premiereVisite == 0 : self.premiereVisite = 1
        self.vieJoueur = 5
        self.vieJoueurMax = 5
        self.vieEnnemi = 5
        self.vieEnnemiMax = 5
        
        self.fond = pygame.image.load("img/menuCombat.png").convert()
        fen1.blit(self.fond,(0,0))
        pygame.display.set_caption("Combat d'ivrognes")
        
        fondtext = pygame.font.SysFont(None, 22)

        
        self.perso = pygame.image.load("img/monstre/CombattantTaverne.png")
        self.ennemi = pygame.image.load("img/monstre/Combattant0.png")


        self.parieurs(fen1,personnage,item)
        self.affichageInfos(fen1,personnage,item)
        
        pygame.display.flip()

        time.sleep(0.5)
        self.choixAleaAttaque(fen1,personnage,item)
        pygame.display.flip()



    def choixAleaAttaque(self,fen1,personnage,item):
        self.attaque = random.randint(1,3)

        if self.attaque == 1 :
            textAttaque = fondtext.render("Crochet droit",1,(206,206,206))
            self.choixAttaque = 1
            
        elif self.attaque == 2 :
            textAttaque = fondtext.render("Crochet gauche",1,(206,206,206))
            self.choixAttaque = 2
            
        elif self.attaque == 3 :
            textAttaque = fondtext.render("Direct du droit",1,(206,206,206))
            self.choixAttaque = 3

        posX = random.randint(150,750)
        posY = random.randint(150,280)

        
        fen1.blit(textAttaque,(posX,posY))

        pygame.display.flip()

        time.sleep(self.temps)
        self.affichageInfos(fen1,personnage,item)

        pygame.display.flip()

        


    def attaqueCombatAuberge(self,fen1,personnage,item):
        self.vieEnnemi -= 1

        textAttaqueJoueur = fondtext.render("-1",1,(206,206,206))
        fen1.blit(textAttaqueJoueur,(500,280))
        pygame.display.flip()

        time.sleep(0.5)
        
        self.affichageInfos(fen1,personnage,item)

        if self.vieEnnemi != 0 : self.attaqueEnnemiAuberge(fen1,personnage,item)
        else : self.victoireCombatAuberge(fen1,personnage,item)
        
        pygame.display.flip()

        
    def attaqueEnnemiAuberge(self,fen1,personnage,item):
        self.chanceToucher = random.randint(1,self.toucher)

        if self.chanceToucher == 1 :
            self.vieJoueur -= 1
            textAttaqueEnnemi = fondtext.render("-1",1,(206,206,206))
        else : textAttaqueEnnemi = fondtext.render("Rate",1,(206,206,206))
            
        fen1.blit(textAttaqueEnnemi,(440,280))
        pygame.display.flip()

        time.sleep(0.5)

        if self.vieJoueur != 0 :
            self.affichageInfos(fen1,personnage,item)
            pygame.display.flip()
            self.choixAleaAttaque(fen1,personnage,item)
        
        else : self.defaiteCombatAuberge(fen1,personnage,item)
        

        

        
    def attaqueRater(self,fen1,personnage,item):
        textAttaqueJoueur = fondtext.render("Rate",1,(206,206,206))
        fen1.blit(textAttaqueJoueur,(500,280))
        pygame.display.flip()

        time.sleep(0.5)
        self.affichageInfos(fen1,personnage,item)
        self.attaqueEnnemiAuberge(fen1,personnage,item)
        pygame.display.flip()
        


    def affichageInfos(self,fen1,personnage,item):

        fen1.blit(self.fond,(0,0))

        fen1.blit(self.perso,(425,300))
        fen1.blit(self.ennemi,(485,300))
        
        textAttaque1 = fondtext.render("1.Crochet droit",1,(206,206,206))
        textAttaque2 = fondtext.render("2.Crochet gauche",1,(206,206,206))
        textAttaque3 = fondtext.render("3.Direct du droit",1,(206,206,206))

        fen1.blit(textAttaque1,(120,560))
        fen1.blit(textAttaque2,(120,600))
        fen1.blit(textAttaque3,(120,640))

        textJoueur = fondtext.render(personnage.pseudo + " :",1,(206,206,206))
        textVieJoueur = fondtext.render("Vie : " + str(self.vieJoueur) + "/" + str(self.vieJoueurMax),1,(206,206,206))

        fen1.blit(textJoueur,(450,580))
        fen1.blit(textVieJoueur,(450,610))

        textEnnemi = fondtext.render("Combattant :",1,(206,206,206))
        textVieEnnemi = fondtext.render("Vie : " + str(self.vieEnnemi) + "/" + str(self.vieEnnemiMax),1,(206,206,206))

        fen1.blit(textEnnemi,(700,580))
        fen1.blit(textVieEnnemi,(700,610))
        


    def victoireCombatAuberge(self,fen1,personnage,item):
        self.victoire += 1
        
        pygame.display.set_caption("Victoire Auberge")
        fen1.blit(self.fond, (0,0))
        textVictoire = fondtext.render("Victoire",1,(206,206,206))
        textRetour = fondtext.render("1.Retourner à l'auberge.",1,(206,206,206))

        fen1.blit(textVictoire,(470,160))
        fen1.blit(textRetour,(250,190))


        if self.renommee != 100 :
            self.renommee += 1


        for i in range (0,self.pariePour) :
            self.gain += random.randint(2,15)

        personnage.argent = personnage.argent + (self.parie * 2) + self.gain
        self.gainTotal = self.gainTotal + self.parie + self.gain
        
        if self.observateur == 0 :
            text1 = fondtext.render("Personne ne regarde votre combat...",1,(206,206,206))
            text2 = fondtext.render("Mais votre adversaire finit par terre !",1,(206,206,206))
            
        elif self.observateur == 1 :
            if self.pariePour == 1 :
                text1 = fondtext.render("Une personne vous regarde et parie sur vous.",1,(206,206,206))
                text2 = fondtext.render("Et vous gagnez le combat !",1,(206,206,206))
                text3 = fondtext.render("La joie se lit dans les yeux du parieur !",1,(206,206,206))
            elif self.pariePour == 0 :
                text1 = fondtext.render("Une personne regarde le combat.",1,(206,206,206))
                text2 = fondtext.render("Elle parie sur votre adversaire.",1,(206,206,206))
                text3 = fondtext.render("Cependant vous écrasez votre adversaire !",1,(206,206,206))
                text4 = fondtext.render("La colère se lit dans les yeux du parieur...",1,(206,206,206))
                fen1.blit(text4,(250,320))
            fen1.blit(text3,(250,290))
            
        elif self.observateur != 1 :
            if self.pariePour == 0 :
                text1 = fondtext.render(str(self.observateur) + " personnes regardent le combat.",1,(206,206,206))
                text2 = fondtext.render("Personne ne parie sur vous.",1,(206,206,206))
                if self.parie == 0 :
                    text3 = fondtext.render("Vous gagnez le combat et vous vous moquez des parieurs qui",1,(206,206,206))
                    text4 = fondtext.render("viennent de perdre de l'or grâce à vous !",1,(206,206,206))
                else :
                    text3 = fondtext.render("Vous gagnez le combat et vous vous pavanez devant les parieurs ",1,(206,206,206))
                    text4 = fondtext.render("avec votre bourse pleine d'or ! ",1,(206,206,206))
                fen1.blit(text4,(250,320))
            elif self.pariePour == 1 :
                text1 = fondtext.render(str(self.observateur) + " personnes regardent le combat.",1,(206,206,206))
                text2 = fondtext.render("Une personne parie sur vous.",1,(206,206,206))
                text3 = fondtext.render("Vous gagnez le combat et vous fêtez votre victoire avec le parieur !",1,(206,206,206))
            elif self.pariePour > 1 and self.pariePour != self.observateur :
                text1 = fondtext.render(str(self.observateur) + " personnes regardent le combat.",1,(206,206,206))
                text2 = fondtext.render(str(self.pariePour) + " parient sur vous.",1,(206,206,206))
                text3 = fondtext.render("Et vous remportez la victoire. Les parieurs viennent vous féliciter ",1,(206,206,206))
                text4 = fondtext.render("à coup de tapes dans le dos !",1,(206,206,206))
                fen1.blit(text4,(250,320))
            elif self.pariePour == self.observateur :
                text1 = fondtext.render(str(self.observateur) + " personnes regardent le combat.",1,(206,206,206))
                text2 = fondtext.render("Ils parient tous sur vous.",1,(206,206,206))
                text3 = fondtext.render("Et vous remportez la victoire. Les parieurs fêtent la victoire ",1,(206,206,206))
                text4 = fondtext.render("avec vous, oubliant votre adversaire !",1,(206,206,206))
                fen1.blit(text4,(250,320))
            fen1.blit(text3,(250,290))

        if self.parie == 0 and self.pariePour != 0:
            text5 = fondtext.render("Vous n'avez pas parié mais vous gagnez " + str(self.gain) + " d'or",1,(206,206,206))
            if self.pariePour == 1 :
                text6 = fondtext.render("grâce au parieur.",1,(206,206,206))
            else :
                text6 = fondtext.render("grâce aux parieurs.",1,(206,206,206))
            fen1.blit(text6,(250,380))
            
        elif self.parie == 0 and self.pariePour == 0 :
            text5 = fondtext.render("Aucun parie pour ce combat donc aucun gain.",1,(206,206,206))

        elif self.parie != 0 and self.pariePour == 0 :
            text5 = fondtext.render("Vous gagnez " + str(self.parie*2) + " d'or grâce à vos paris.",1,(206,206,206))

        else : 
            text5 = fondtext.render("Vous gagnez " + str(self.parie*2) + " d'or grâce à vos paris et " + str(self.gain) + " d'or ",1,(206,206,206))
            if self.pariePour == 1 :
                text6 = fondtext.render("grâce au parieur.",1,(206,206,206))
            else :
                text6 = fondtext.render("grâce au parieur.",1,(206,206,206))
            fen1.blit(text6,(250,380))
        fen1.blit(text5,(250,350))


        fen1.blit(text1,(250,230))
        fen1.blit(text2,(250,260))

        pygame.display.flip()

        
    def defaiteCombatAuberge(self,fen1,personnage,item):
        self.defaite += 1
        
        pygame.display.set_caption("Victoire Auberge")
        fen1.blit(self.fond, (0,0))
        textVictoire = fondtext.render("Défaite",1,(206,206,206))
        textRetour = fondtext.render("1.Retourner à l'auberge.",1,(206,206,206))

        fen1.blit(textVictoire,(470,160))
        fen1.blit(textRetour,(250,190))


        self.gainTotal = self.gainTotal - self.parie
        
        if self.renommee != 0 :
            self.renommee -= 1

        
        if self.observateur == 0 :
            text1 = fondtext.render("Personne ne regarde votre combat...",1,(206,206,206))
            text2 = fondtext.render("De toute façon, vous finissez assommé...",1,(206,206,206))
        elif self.observateur == 1 :
            if self.pariePour == 1 :
                text1 = fondtext.render("Une personne vous regarde et parie sur vous.",1,(206,206,206))
                text2 = fondtext.render("Cependant, vous perdez le combat...",1,(206,206,206))
                text3 = fondtext.render("La colère se lit dans les yeux du parieur !",1,(206,206,206))
            elif self.pariePour == 0 :
                text1 = fondtext.render("Une personne regarde le combat.",1,(206,206,206))
                text2 = fondtext.render("Elle parie sur votre adversaire.",1,(206,206,206))
                text3 = fondtext.render("Finalement, vous perdez le combat...",1,(206,206,206))
                text4 = fondtext.render("La joie se lit dans les yeux du parieur !",1,(206,206,206))
                fen1.blit(text4,(250,320))
            fen1.blit(text3,(250,290))
        elif self.observateur != 1 :
            if self.pariePour == 0 :
                text1 = fondtext.render(str(self.observateur) + " personnes regardent le combat.",1,(206,206,206))
                text2 = fondtext.render("Personne ne parie sur vous.",1,(206,206,206))
                text3 = fondtext.render("Et vous perdez le combat...",1,(206,206,206))
                text4 = fondtext.render("La joie se lit dans les yeux des parieurs !",1,(206,206,206))
            elif self.pariePour == 1 :
                text1 = fondtext.render(str(self.observateur) + " personnes regardent le combat.",1,(206,206,206))
                text2 = fondtext.render("Une personne parie sur vous.",1,(206,206,206))
                text3 = fondtext.render("Et vous perdez le combat...",1,(206,206,206))
                text4 = fondtext.render("La colère se lit dans les yeux du parieur !",1,(206,206,206))
            elif self.pariePour > 1 :
                text1 = fondtext.render(str(self.observateur) + " personnes regardent le combat.",1,(206,206,206))
                text2 = fondtext.render(str(self.pariePour) + " parient sur vous.",1,(206,206,206))
                text3 = fondtext.render("Et vous perdez le combat...",1,(206,206,206))
                text4 = fondtext.render("La colère se lit dans les yeux des parieur !",1,(206,206,206))                
            fen1.blit(text3,(250,290))
            fen1.blit(text4,(250,320))         

        if self.premierParie != 0 : 
            text5 = fondtext.render("Mais cet échec ne signe pas votre fin !",1,(206,206,206))
            if self.parie != 0 :
                text6 = fondtext.render("Cependant, vous perdez l'argent misé et votre renommée en pâtit...",1,(206,206,206))
                text7 = fondtext.render(str(self.parie) + " d'or perdu.",1,(206,206,206))        
                fen1.blit(text6,(250,380))
                fen1.blit(text7,(250,410))
      
            fen1.blit(text5,(250,350))

        fen1.blit(text1,(250,230))
        fen1.blit(text2,(250,260))

        pygame.display.flip()


        


    #Permet de parier sur les duels, la somme maximum augmente avec la renommée
    def menuParies(self,fen1,personnage,item) :
        self.premierParie = 1
        
        self.fond = pygame.image.load("img/menuAuberge.png").convert()
        fen1.blit(self.fond,(0,0))
        pygame.display.set_caption("Parie")
        
        fondtext = pygame.font.SysFont(None, 25)

        text1 = fondtext.render("Vous avez " + str(personnage.argent) +" d'or.",1,(206,206,206))
        if self.parie == 0 :
            text2 = fondtext.render("Vous ne pariez pas d'or.",1,(206,206,206))
        else :
            text2 = fondtext.render("Vous pariez " + str(self.parie) + " d'or.",1,(206,206,206))
            
        if self.gainTotal == 0 :
            text3 = fondtext.render("Vous n'avez ni gagné ni perdu d'or avec les duels.",1,(206,206,206))        
        elif self.gainTotal < 0 :
            self.gainTotal = - int(self.gainTotal)
            text3 = fondtext.render("Vous avez perdu " + str(self.gainTotal) + " d'or à cause des duels.",1,(206,206,206))
        elif self.gainTotal > 0 :
            text3 = fondtext.render("Vous avez gagné " + str(self.gainTotal) + " d'or grâce aux duels.",1,(206,206,206))

        fen1.blit(text1,(300,230))
        fen1.blit(text2,(300,260))
        fen1.blit(text3,(300,290))

        textcombat = fondtext.render("1.Combattre",1,(206,206,206))
        if personnage.argent < 10 :
            textparie1 = fondtext.render("Vous n'avez plus assez d'argent pour parier.",1,(206,206,206))
        else :
            textparie1 = fondtext.render("2.Parier 10 pièces d'or",1,(206,206,206))
        
        fen1.blit(textcombat,(120,230))
        fen1.blit(textparie1,(120,260))
        
        pygame.display.flip()



    def parie1(self,fen1,personnage,item) :
        if personnage.argent >= 10 :
            self.parie += 10
            personnage.argent -= 10
            self.menuParies(fen1,personnage,item)
        

