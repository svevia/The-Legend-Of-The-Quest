from module.item_ID import *



class objet :
    """Classe définissant l'inventaire du jeu,
    son contenu et l'utilision qu'on en fera, ainsi
    la gestion des objets."""

    def __init__(self):
        self.ID0 = self.ID1 = self.ID2 = self.ID3 = self.ID4 = self.ID5 = self.ID6 = self.ID7 = self.ID8 = self.ID9 = self.IDArmure = self.IDCasque = self.IDPantalon = self.IDArme = -1
        self.IDN0 = self.IDN1 = self.IDN2 = self.IDN3 = self.IDN4 = self.IDN5 = self.IDN6 = self.IDN7 = self.IDN8 = self.IDN9 = 0
        self.lootSecondaire = (29,50,51,52,53)


    def ObjetID(self,ID,personnage):
        objitem = ID_objet(ID,personnage,self)
        

    #Fonction retournant le nom d'un objet d'ID donné.
    def nomObjet(self,ID,personnage) :
        objitem = ID_objet(ID,personnage,self)
        return objitem.nom


    def affichage(self,ID,personnage):
        objitem = ID_objet(ID,personnage,self)
        if ID < 99:
            return objitem.affichage
        else:
            return objitem.nom
        
    #Fonction gérant l'équipement.
    def equipement(self,ID,personnage,pos):
        if ID<150 and ID > 99 and self.IDArmure == -1 :
            self.IDArmure = ID
            self.objetPerdu(pos = pos)
            objitem = ID_objet(ID,personnage,self)
            personnage.armure += objitem.armure

        if ID<200 and ID > 149 and self.IDCasque == -1 :
            self.IDCasque = ID
            self.objetPerdu(pos = pos)
            objitem = ID_objet(ID,personnage,self)
            personnage.armure += objitem.armure

        if ID<250 and ID > 199 and self.IDPantalon == -1 :
            self.IDPantalon = ID
            self.objetPerdu(pos = pos)
            objitem = ID_objet(ID,personnage,self)
            personnage.armure += objitem.armure      

        elif ID >= 250 and self.IDArme == -1 :
            self.IDArme = ID
            self.objetPerdu(pos = pos)
            objitem = ID_objet(ID,personnage,self)
            personnage.principale += objitem.arme

    def desequipement (self,ID,personnage) :
        self.loot (ID)
        if ID < 150 and ID > 99 :
            objitem = ID_objet(ID,personnage,self)
            personnage.armure -= objitem.armure
            self.IDArmure = -1

        if ID < 200 and ID > 149 :
            objitem = ID_objet(ID,personnage,self)
            personnage.armure -= objitem.armure
            self.IDCasque = -1

        if ID < 250 and ID > 199 :
            objitem = ID_objet(ID,personnage,self)
            personnage.armure -= objitem.armure
            self.IDPantalon = -1
            
        elif ID > 249 :
            objitem = ID_objet(ID,personnage,self)
            personnage.principale -= objitem.arme
            self.IDArme = -1

            
    #Fonction gérant l'obtention de nouveaux objets. Renvoie -1 si l'inventaire est plein.
    def loot(self,ID):
        if ID>99:
            if self.ID0 == -1 : self.ID0 = ID
            elif self.ID1 == -1 : self.ID1 = ID
            elif self.ID2 == -1 : self.ID2 = ID
            elif self.ID3 == -1 : self.ID3 = ID
            elif self.ID4 == -1 : self.ID4 = ID
            elif self.ID5 == -1 : self.ID5 = ID
            elif self.ID6 == -1 : self.ID6 = ID
            elif self.ID7 == -1 : self.ID7 = ID
            elif self.ID8 == -1 : self.ID8 = ID
            elif self.ID9 == -1 : self.ID9 = ID
        else :
            if  self.ID0 == ID :
                self.IDN0 += 1

            elif self.ID1 == ID :
                self.IDN1 += 1

            elif  self.ID2 == ID :
                self.IDN2 += 1

            elif self.ID3 == ID :
                self.IDN3 += 1

            elif self.ID4 == ID :
                self.IDN4 += 1

            elif self.ID5 == ID :
                self.IDN5 += 1

            elif self.ID6 == ID :
                self.IDN6 += 1

            elif self.ID7 == ID :
                self.IDN7 += 1

            elif self.ID8 == ID :
                self.IDN8 += 1

            elif self.ID9 == ID :
                self.IDN9 += 1
                    
            elif self.ID0 == -1 :
                self.ID0 = ID
                self.IDN0 = 1
            elif self.ID1 == -1 :
                self.ID1 = ID
                self.IDN1 = 1
            elif self.ID2 == -1 :
                self.ID2 = ID
                self.IDN2 = 1
            elif self.ID3 == -1 :
                self.ID3 = ID
                self.IDN3 = 1
            elif self.ID4 == -1 :
                self.ID4 = ID
                self.IDN4 = 1
            elif self.ID5 == -1 :
                self.ID5 = ID
                self.IDN5 = 1
            elif self.ID6 == -1 :
                self.ID6 = ID
                self.IDN6 = 1
            elif self.ID7 == -1 :
                self.ID7 = ID
                self.IDN7 = 1
            elif self.ID8 == -1 :
                self.ID8 = ID
                self.IDN8 = 1
            elif self.ID9 == -1 :
                self.ID9 = ID
                self.IDN9 = 1

            
    #Fonction gérant la perte d'objet. Si pos est définit, ignore ID et retire l'item à l'emplacement pos de l'inventaire (de 0 à 9, en partant du haut à droite).
    def objetPerdu(self,ID=-1,num=1,pos=-1):
        if pos != -1 :
            if pos == 0 and self.ID0 != -1 :
                if self.ID0>99 : self.ID0 = -1
                else :
                    self.IDN0 -= num
                    if self.IDN0 < 1 : self.ID0 = -1
            if pos == 1 and self.ID1 != -1 :
                if self.ID1>99 : self.ID1 = -1
                else :
                    self.IDN1 -= num
                    if self.IDN1 < 1 : self.ID1 = -1    
            if pos == 2 and self.ID2 != -1 :
                if self.ID2>99 : self.ID2 = -1
                else :
                    self.IDN2 -= num
                    if self.IDN2 < 1 : self.ID2 = -1  
            if pos == 3 and self.ID3 != -1 :
                if self.ID3>99 : self.ID3 = -1
                else :
                    self.IDN3 -= num
                    if self.IDN3 < 1 : self.ID3 = -1  
            if pos == 4 and self.ID4 != -1 :
                if self.ID4>99 : self.ID4 = -1
                else :
                    self.IDN4 -= num
                    if self.IDN4 < 1 : self.ID4 = -1  
            if pos == 5 and self.ID5 != -1 :
                if self.ID5>99 : self.ID5 = -1
                else :
                    self.IDN5 -= num
                    if self.IDN5 < 1 : self.ID5 = -1  
            if pos == 6 and self.ID6 != -1 :
                if self.ID6>99 : self.ID6 = -1
                else :
                    self.IDN6 -= num
                    if self.IDN6 < 1 : self.ID6 = -1  
            if pos == 7 and self.ID7 != -1 :
                if self.ID7>99 : self.ID7 = -1
                else :
                    self.IDN7 -= num
                    if self.IDN7 < 1 : self.ID7 = -1  
            if pos == 8 and self.ID8 != -1 :
                if self.ID8>99 : self.ID8 = -1
                else :
                    self.IDN8 -= num
                    if self.IDN8 < 1 : self.ID8 = -1  
            if pos == 9 and self.ID9 != -1 :
                if self.ID9>99 : self.ID9 = -1
                else :
                    self.IDN9 -= num
                    if self.IDN9 < 1 : self.ID9 = -1              
                
        elif pos == -1 and ID>99 :
            if self.ID0 == ID : self.ID0 = -1
            elif self.ID1 == ID : self.ID1 = -1
            elif self.ID2 == ID : self.ID2 = -1
            elif self.ID3 == ID : self.ID3 = -1
            elif self.ID4 == ID : self.ID4 = -1
            elif self.ID5 == ID : self.ID5 = -1
            elif self.ID6 == ID : self.ID6 = -1
            elif self.ID7 == ID : self.ID7 = -1
            elif self.ID8 == ID : self.ID8 = -1
            elif self.ID9 == ID : self.ID9 = -1
        else :
            if self.ID0 == ID :
                self.IDN0 -= num
                if self.IDN0 < 1 :
                    self.ID0 = -1
            elif self.ID1 == ID :
                self.IDN1 -= num
                if self.IDN1 < 1 :
                    self.ID1 = -1
            elif self.ID2 == ID :
                self.IDN2 -= num
                if self.IDN2 < 1 :
                    self.ID2 = -1
            elif self.ID3 == ID :
                self.IDN3 -= num
                if self.IDN3 < 1 :
                    self.ID3 = -1
            elif self.ID4 == ID :
                self.IDN4 -= num
                if self.IDN4 < 1 :
                    self.ID4 = -1
            elif self.ID5 == ID :
                self.IDN5 -= num
                if self.IDN5 < 1 :
                    self.ID5 = -1
            elif self.ID6 == ID :
                self.IDN6 -= num
                if self.IDN6 < 1 :
                    self.ID6 = -1
            elif self.ID7 == ID :
                self.IDN7 -= num
                if self.IDN7 < 1 :
                    self.ID7 = -1
            elif self.ID8 == ID :
                self.IDN8 -= num
                if self.IDN8 < 1 :
                    self.ID8 = -1
            elif self.ID9 == ID :
                self.IDN9 -= num
                if self.IDN9 < 1 :
                    self.ID9 = -1


    def emplacement(self,pos,personnage,carte,comp):
        if pos == 0 : ID = self.ID0
        elif pos == 1 : ID = self.ID1
        elif pos == 2 : ID = self.ID2
        elif pos == 3 : ID = self.ID3
        elif pos == 4 : ID = self.ID4
        elif pos == 5 : ID = self.ID5
        elif pos == 6 : ID = self.ID6
        elif pos == 7 : ID = self.ID7
        elif pos == 8 : ID = self.ID8
        elif pos == 9 : ID = self.ID9
        elif pos == 10 : ID = self.IDArmure
        elif pos == 11 : ID = self.IDCasque
        elif pos == 12 : ID = self.IDPantalon
        elif pos == 13 : ID = self.IDArme

        
        
        if ID == 0 : #potion de soin (rajoute de la vie au personnage)
            personnage.vie += 20 + personnage.alchimiste
            self.objetPerdu(pos = pos)
            if personnage.vie > personnage.viemax :
                personnage.vie = personnage.viemax
        if ID == 30 : #potion de soins personnages + compagnons (rajoute de la vie aux 2)
            personnage.vie += 10 + personnage.alchimiste
            if comp.ami == 1:
                comp.vie += 10 + personnage.alchimiste
            self.objetPerdu(pos = pos)
            if personnage.vie > personnage.viemax :
                personnage.vie = personnage.viemax
            if comp.vie > comp.viemax :
                comp.vie = comp.viemax

        if ID == 31:
            if personnage.temps_force == 0 :
                personnage.principale += 5
                personnage.temps_force = 3
                self.objetPerdu(pos = pos)
        

        if ID == 32: #potion repousse (bloque 5 combats et empêche leur déclenchement)
            carte.repousse += 5
            self.objetPerdu(pos = pos)

        if ID == 33: #augmente la vitesse de déplacement du personnage sur la carte
            carte.vitesse = 6
            personnage.temps_vitesse = 500
            self.objetPerdu(pos = pos)
        
                
        elif ID > 99 :
            if pos < 10 : self.equipement(ID,personnage,pos)
            else : self.desequipement(ID,personnage)

                
    #Fonction vérifiant l'existance d'un objet dans votre inventaire. Si équipement : Retourne 1 si true, 0 si false. Si Objet stackable, retourne la quantité dans l'inventaire, sinon 0.
    def inventaireLook(self,ID):
        if ID > 99 :
            if self.ID0 == ID or self.ID1 == ID or self.ID2 == ID or self.ID3 == ID or self.ID4 == ID or self.ID5 == ID or self.ID6 == ID or self.ID7 == ID or self.ID8 == ID or self.ID9 == ID : return 1
            else : return 0
        else :
            if self.ID0 == ID : return self.IDN0
            elif self.ID1 == ID : return self.IDN1
            elif self.ID2 == ID : return self.IDN2
            elif self.ID3 == ID : return self.IDN3
            elif self.ID4 == ID : return self.IDN4
            elif self.ID5 == ID : return self.IDN5
            elif self.ID6 == ID : return self.IDN6
            elif self.ID7 == ID : return self.IDN7
            elif self.ID8 == ID : return self.IDN8
            elif self.ID9 == ID : return self.IDN9
            else : return 0
        

    #Fonction vérifiant si l'inventaire est remplie. Retourne 1 si true, 0 si false.
    def inventaireRempli(self):
        if self.ID0 != -1 and self.ID1 != -1 and self.ID2 != -1 and self.ID3 != -1 and self.ID4 != -1 and self.ID5 != -1 and self.ID6 != -1 and self.ID7 != -1 and self.ID8 != -1 and self.ID9 != -1 : return 1
        else : return 0    

    #Fonction renvoyant la position d'un objet
    def inventairePosition(self,ID):
        if self.ID0==ID : return 0
        elif self.ID1==ID : return 1
        elif self.ID2==ID : return 2
        elif self.ID3==ID : return 3
        elif self.ID4==ID : return 4
        elif self.ID5==ID : return 5
        elif self.ID6==ID : return 6
        elif self.ID7==ID : return 7
        elif self.ID8==ID : return 8
        elif self.ID9==ID : return 9
        else : return -1
