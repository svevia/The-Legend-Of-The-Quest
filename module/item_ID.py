''''Cette class regroupe l'ensemble des ID des objets du jeu et attribut à chacun:
-un prix de vente
-un nom
-Si cette objet est créable via les menus forgeron ou alchimiste, il attribut la liste des composants
-Si armure ou armes : l'augemntation de stats procurés'''




class ID_objet:
    def __init__ (self,ID,personnage,item):
        self.ID = ID
        self.stats_item(personnage,item)
        
        

    def stats_item(self,personnage,item):
        if self.ID == -1 :
            self.affichage = "Vide"
            self.nom = "Vide"
            self.vente = 0
                                             
        elif self.ID == 0 :
            self.nom = "Potion"
            self.vente = 10
            self.composant = [29,1,20,1]
            self.argent = 20
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Potion"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Potion x "+str(item.inventaireLook(self.ID))
            
        elif self.ID == 1 :
            self.nom = "Cuivre"
            self.vente = 3
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Cuivre"                                     
            elif item.inventaireLook(self.ID) == 0 : self.affichage = ""
            else : self.affichage = "Cuivre x "+str(item.inventaireLook(self.ID))
            
        elif self.ID == 2 :
            self.nom = "Argent"
            self.vente = 7
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Argent"                                     
            elif item.inventaireLook(self.ID) == 0 : self.affichage = ""
            else : self.affichage = "Argent x "+str(item.inventaireLook(self.ID))

        elif self.ID == 3 :
            self.nom = "Orichalque"
            self.vente = 15
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Orichalque"                                     
            elif item.inventaireLook(self.ID) == 0 : self.affichage = ""
            else : self.affichage = "Orichalque x "+str(item.inventaireLook(self.ID))

        elif self.ID == 4 :
            self.nom = "Bois sec"
            self.vente = 3
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Bois sec"                                       
            elif item.inventaireLook(self.ID) == 0 : self.affichage = ""            
            else : self.affichage = "Bois sec x " + str(item.inventaireLook(self.ID))

        elif self.ID == 5 :
            self.nom = "Chêne"
            self.vente = 7
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Chêne"                                       
            elif item.inventaireLook(self.ID) == 0 : self.affichage = ""            
            else : self.affichage = "Chêne x " + str(item.inventaireLook(self.ID))

        elif self.ID == 6 :
            self.nom = "Garoé"
            self.vente = 15
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Garoé"                                       
            elif item.inventaireLook(self.ID) == 0 : self.affichage = ""            
            else : self.affichage = "Garoé x " + str(item.inventaireLook(self.ID))

        elif self.ID == 7 :
            self.nom = "Jute"
            self.vente = 3
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Jute"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Jute x "+str(item.inventaireLook(self.ID))

        elif self.ID == 8 :
            self.nom = "Velours"
            self.vente = 7
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Velours"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Velours x "+str(item.inventaireLook(self.ID))

        elif self.ID == 9 :
            self.nom = "Soie"
            self.vente = 15
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Soie"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Soie x "+str(item.inventaireLook(self.ID))

        elif self.ID == 10 :
            self.nom = "Loot Boss"
            self.vente = 500
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Loot Boss"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Loot Boss x "+str(item.inventaireLook(self.ID))

        elif self.ID == 20 :
            self.nom = "Datura"
            self.vente = 7
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Datura"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Datura x "+str(item.inventaireLook(self.ID))

        elif self.ID == 21 :
            self.nom = "Jusquiame"
            self.vente = 7
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Jusquiame"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Jusquiame x "+str(item.inventaireLook(self.ID))

        elif self.ID == 22 :
            self.nom = "Hamamélis"
            self.vente = 7
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Hamamélis"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Hamamélis x "+str(item.inventaireLook(self.ID))

        elif self.ID == 23 :
            self.nom = "Callune"
            self.vente = 7
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Callune"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Callune x "+str(item.inventaireLook(self.ID))

        elif self.ID == 24 :
            self.nom = "Belladone"
            self.vente = 7
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Belladone"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Belladone x "+str(item.inventaireLook(self.ID))


        elif self.ID == 29:
            self.nom = "Fiole vide"
            self.vente = 3
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Fiole vide"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Fiole vide x "+str(item.inventaireLook(self.ID))

        elif self.ID == 30:
            self.nom = "Pot. Mult."
            self.vente = 7
            self.composant = [0,1,21,1]
            self.argent = 30
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Pot. Mult."                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Pot. Mult. x "+str(item.inventaireLook(self.ID))
        

        elif self.ID == 31:
            if personnage.classe  == "paladin" or personnage.classe == "voleur" : 
                self.nom = "Pot. Force"
                if item.inventaireLook(self.ID) == 1 : self.affichage = "Pot. Force"                                      
                elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
                else : self.affichage = "Pot. Force x "+str(item.inventaireLook(self.ID))
            elif personnage.classe == "mage":
                self.nom = "Pot. Magie"
                if item.inventaireLook(self.ID) == 1 : self.affichage = "Pot. Magie"                                      
                elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
                else : self.affichage = "Pot. Magie x "+str(item.inventaireLook(self.ID))
                
            self.vente = 7
            self.composant = [29,1,22,1]
            self.argent = 30


        elif self.ID == 32:
            self.nom = "Pot. Repousse"
            self.vente = 7
            self.composant = [29,1,23,1]
            self.argent = 50
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Pot. Repousse"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Pot. Repousse x "+str(item.inventaireLook(self.ID))


        elif self.ID == 33:
            self.nom = "Pot. Vitesse"
            self.vente = 7
            self.composant = [29,1,24,1]
            self.argent = 50
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Pot. Vitesse"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Pot. Vitesse x "+str(item.inventaireLook(self.ID))
            

        elif self.ID == 50 :
            self.nom = "Epée rouillée"
            self.vente = 8
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Epée rouillée"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Epée rouillée x "+str(item.inventaireLook(self.ID))

        elif self.ID == 51 :
            self.nom = "Vieux tissus"
            self.vente = 5
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Vieux tissus"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Vieux tissus x "+str(item.inventaireLook(self.ID))

        elif self.ID == 52 :
            self.nom = "Hache brisée"
            self.vente = 6
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Hache brisée"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Hache brisée x "+str(item.inventaireLook(self.ID))

        elif self.ID == 53 :
            self.nom = "Cuir usé"
            self.vente = 4
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Cuir usé"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Cuir usé x "+str(item.inventaireLook(self.ID))
        
        
        elif self.ID == 90 :
            self.nom = "Echantillon"
            self.vente = -1
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Echantillon"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Echantillon x "+str(item.inventaireLook(self.ID))

        elif self.ID == 91 :
            self.nom = "Sérum"
            self.vente = -1
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Sérum"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Sérum x "+str(item.inventaireLook(self.ID))

        elif self.ID == 92 :
            self.nom = "Vivres"
            self.vente = -1
            if item.inventaireLook(self.ID) == 1 : self.affichage = "Vivres"                                      
            elif item.inventaireLook(self.ID) == 0 :self.affichage = ""
            else : self.affichage = "Vivres x "+str(item.inventaireLook(self.ID))
        
        #Fonctionement de la varibale composant : [ID,Nombre,ID2,Nombre2...]


        # -------------------------------------------------Armures--------------------------------------------#
                                                                                                
        elif self.ID == 100 :
            self.nom = "Robe Nov."       # Robe novice -- > ID 100    #
            self.composant = [7,3]
            self.argent = 200
            self.vente = 40
            self.armure = 2

        elif self.ID == 101 :
            self.nom = "Arm.Fer"        # Armure en Fer -- > ID 101     #
            self.composant = [7,1,1,2]
            self.argent = 200
            self.vente = 40
            self.armure = 4
            
        elif self.ID == 102 :
            self.nom = "Arm.Cuir"         # Armure en cuir -- > ID 102      #
            self.composant = [7,3]
            self.argent = 200
            self.vente = 40
            self.armure = 3

        elif self.ID == 103 :
            self.nom = "Rob.Myst."       # Robe de nécromanciens -- > ID 103    #
            self.composant = [8,5,2,2]
            self.argent = 500
            self.vente = 80
            self.armure = 4

        elif self.ID == 104 :
            self.nom = "Arm.Arg"        # Armure en argent -- > ID 104     #
            self.composant = [8,3,2,4]
            self.argent = 500
            self.vente = 80
            self.armure = 8

        elif self.ID == 105 :
            self.nom = "Cot.Maille"         # Cote de maille -- > ID 105      #
            self.composant = [8,2,2,5]
            self.argent = 500
            self.vente = 80
            self.armure = 6

        elif self.ID == 106 :
            self.nom = "Rob.Invoc."       # Robe d'invocateur -- > ID 106    #
            self.composant = [9,10,3,4]
            self.argent = 1000
            self.vente = 200
            self.armure = 8

        elif self.ID == 107 :
            self.nom = "Arm.Ori"        # Armure en orichalque -- > ID 107     #
            self.composant = [9,6,3,8]
            self.argent = 1000
            self.vente = 200
            self.armure = 16

        elif self.ID == 108 :
            self.nom = "Arm.Conf"         # Armure confrérie -- > ID 108      #
            self.composant = [9,10,3,4]
            self.argent = 1000
            self.vente = 200
            self.armure = 12
        #------------------------------------------------------------------------------------------------------#
            
        # ---------------------------------------------------Casques-------------------------------------------#

        elif self.ID == 150 :
            self.nom = "Capu.Nov."       # Capuchon de novice -- > ID 150    #
            self.composant = [7,2]
            self.argent = 200
            self.vente = 30
            self.armure = 1


        elif self.ID == 151 :
            self.nom = "Cas.Fer"        # Casque en Fer -- > ID 151     #
            self.composant = [7,1,1,1]
            self.argent = 200
            self.vente = 30
            self.armure = 3
            
        elif self.ID == 152 :
            self.nom = "Capu.Cui."         # Casque en cuir -- > ID 152      #
            self.composant = [7,2]
            self.argent = 200
            self.vente = 30
            self.armure = 2

        elif self.ID == 153 :
            self.nom = "Capu.Myst."       # Capuchon de nécromanciens -- > ID 153    #
            self.composant = [8,4,2,1]
            self.argent = 500
            self.vente = 60
            self.armure = 2

        elif self.ID == 154 :
            self.nom = "Cas.Arg"        # Casque en argent -- > ID 154     #
            self.composant = [8,2,2,3]
            self.argent = 500
            self.vente = 60
            self.armure = 6

        elif self.ID == 155 :
            self.nom = "Capu.ouv."         # Cpuche ouverte -- > ID 155      #
            self.composant = [8,4,2,1]
            self.argent = 500
            self.vente = 60
            self.armure = 4
            

        elif self.ID == 156 :
            self.nom = "Capu.Invoc."       # Capuchon de l'Invocateur -- > ID 156    #
            self.composant = [9,8,3,2]
            self.argent = 1000
            self.vente = 100
            self.armure = 4

        elif self.ID == 157 :
            self.nom = "Cas.Ori"        # Casque en orichalque -- > ID 157     #
            self.composant = [9,4,3,6]
            self.argent = 1000
            self.vente = 100
            self.armure = 12

        elif self.ID == 158 :
            self.nom = "Capu.Conf."         # Capuchon de la confrérie-- > ID 158     #
            self.composant = [9,8,3,2]
            self.argent = 1000
            self.vente = 100
            self.armure = 8
            
        #------------------------------------------------------------------------------------------------------#
            
        # ---------------------------------------------------Pantalon------------------------------------------#
        elif self.ID == 200 :
            self.nom = "Sandales"      # Sandales -- > ID 200  #
            self.composant = [7,2]
            self.argent = 200
            self.vente = 30
            self.armure = 1

        elif self.ID == 201 :
            self.nom = "Pant.Fer"       # Pantalon en Fer -- > ID 201   #
            self.composant = [7,1,1,1]
            self.argent = 200
            self.vente = 30
            self.armure = 3
            
        elif self.ID == 202 :
            self.nom = "Pant.Cui."        # Pantalon en cuir -- > ID 202    #
            self.composant = [7,2]
            self.argent = 200
            self.vente = 30
            self.armure = 2

        elif self.ID == 203 :
            self.nom = "Bot.Myst"       # Bottes de nécromanciens -- > ID 203    #
            self.composant = [8,4,2,1]
            self.argent = 500
            self.vente = 60
            self.armure = 2

        elif self.ID == 204 :
            self.nom = "Pant.Arg"        # pantalon en argent -- > ID 204     #
            self.composant = [8,2,2,3]
            self.argent = 500
            self.vente = 60
            self.armure = 6

        elif self.ID == 205 :
            self.nom = "Pant.Peau"         # Pantalon galakran -- > ID 205    #
            self.composant = [8,4,2,1]
            self.argent = 500
            self.vente = 60
            self.armure = 4

        elif self.ID == 206 :
            self.nom = "Bot.Invoc."       # Bottes de l'Invocateur -- > ID 206    #
            self.composant = [9,8,3,2]
            self.argent = 1000
            self.vente = 100
            self.armure = 4

        elif self.ID == 207 :
            self.nom = "Bot.Ori"        # Bottes en orichalque -- > ID 207     #
            self.composant = [9,4,3,6]
            self.argent = 1000
            self.vente = 100
            self.armure = 12

        elif self.ID == 208 :
            self.nom = "Bottes.Conf."         # Bottes de la confrérie-- > ID 208     #
            self.composant = [9,8,3,2]
            self.argent = 1000
            self.vente = 100
            self.armure = 8

        #------------------------------------------------------------------------------------------------------#
            
        # ----------------------------------------------------Armes--------------------------------------------#

        elif self.ID == 250 :
            self.nom = "Baton Bois"     # Baton en bois -- > ID 250     #
            self.composant = [4,2]
            self.argent = 200
            self.vente = 40
            self.arme = 8

        elif self.ID == 251 :
            self.nom = "Masse"          # Masse -- > ID 251             #
            self.composant = [4,2]
            self.argent = 200
            self.vente = 40
            self.arme = 4

        elif self.ID == 252 :
            self.nom = "Dagues fer"     # Dagues de fer -- > ID 252     #
            self.composant = [4,1,1,1]
            self.argent = 200
            self.vente = 40
            self.arme = 6

        elif self.ID == 253 :
            self.nom = "Bat.Précie."     # Baton Précieux -- > ID 253     #
            self.composant = [5,4,2,2]
            self.argent = 500
            self.vente = 80
            self.arme = 16

        elif self.ID == 254 :
            self.nom = "Mart.Comb."          # Marteau de combat -- > ID 254             #
            self.composant = [5,3,2,3]
            self.argent = 500
            self.vente = 80
            self.arme = 8

        elif self.ID == 255 :
            self.nom = "Dag.Galak."     # Dagues de Galakran -- > ID 255     #
            self.composant = [5,3,2,3]
            self.argent = 500
            self.vente = 80
            self.arme = 12

        elif self.ID == 256 :
            self.nom = "Bat.Archi."     # Baton d'archimage -- > ID 256     #
            self.composant = [6,8,3,3]
            self.argent = 1000
            self.vente = 200
            self.arme = 24

        elif self.ID == 257 :
            self.nom = "Mart.Seig."          # Marteau de seigneur de guerre -- > ID 257             #
            self.composant = [6,6,3,5]
            self.argent = 1000
            self.vente = 200
            self.arme = 12

        elif self.ID == 258 :
            self.nom = "Dag.Sang."     # Dagues sanguinolantes -- > ID 258     #
            self.composant = [6,5,3,6]
            self.argent = 1000
            self.vente = 200
            self.arme = 18
        #------------------------------------------------------------------------------------------------------#

        
        








