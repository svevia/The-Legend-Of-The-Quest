import random,pygame,time
from PIL import Image, ImageDraw

"""Ce programme attribut à chaque lettre présente dans le fichier texte un biome spécifique
ensuite chaque lettre est remplacée par l'image correspondant au biome (au format 128*128)
l'image ainsi formée est sauvergardé au format .png pui reduite au format 1024*768 pour former la minimap
La map est composé de:
-4 Biomes (contients) différents : désert, plaine, marais, contaminé
-4 villages repartit sur chaques biomes et qui sont différents en fonction du biome où il est
-des points fixes(auberge,oasis...) variant dans chaques biomes et qui déclenches des évenement

La map est aménée à changer en fonction de la population de contaminé, ainsi, plus celle-ci est importante
plus la zone occupé par la contamination s'étend autour de la grotte
Pour permettre ça, ce programme sera appelé régulièrement au cours du jeu pour regénérer la carte
"""

def attribution(var):
    global desert,marais,plaine
    if var == "desert":
        var = desert
    elif var == "marais":
        var = marais
    elif var == "plaine":
        var = plaine
    return var



def Village_attribution(var):
    if var == "desert":
        return VillageGalakran
    elif var == "plaine":
        return VillageHumain
    else:
        return VillageElfe

def GenerationMap(fen1,population,varA_texte,varB_texte,varC_texte,personnage):
    global desert,marais,plaine,VillageGalakran,village,VillageHumain,VillageElfe

    #affiche un écran de chargement pendant la génération
    chargement = pygame.image.load('img/chargement.png').convert()
    fen1.blit(chargement,(0,0))
    time.sleep(0.5)
    pygame.display.flip()

    #fichier texte contenant le squelette de la map
    map = open('module/map' + str(personnage.cartenum) + '.txt','r')
    
    #lecture linéaire du fichier texte
    liste = map.readlines()
    map.close()

    #ouverture des blocs de chaque biomes
    desert = Image.open('img/map/Desert.png','r')
    marais = Image.open('img/map/Marais.png','r')
    plaine = Image.open('img/map/Plaine.png','r')
    contamine = Image.open('img/map/Contamination.png','r')
    grotte = Image.open('img/map/Grotte.png','r')
    VillageGalakran = Image.open('img/map/VillageGalakran.png','r')
    VillageHumain = Image.open('img/map/VillageHumain.png','r')
    VillageElfe = Image.open('img/map/VillageElfe.png','r')


    #attribution aléatoire des zones de la carte aux biomes
    if varA_texte == 0 and varB_texte == 0 and varC_texte == 0:
        biomes = ["desert","marais","plaine"]
        varA_texte = biomes[random.randint(0,len(biomes)-1)]
        biomes.remove(varA_texte)
        varA = attribution(varA_texte)
        
        varB_texte = biomes[random.randint(0,len(biomes)-1)]
        biomes.remove(varB_texte)
        varB = attribution(varB_texte)
        
        varC_texte = biomes[random.randint(0,len(biomes)-1)]
        biomes.remove(varC_texte)
        varC = attribution(varC_texte)

    else:
        varA = attribution(varA_texte)
        varB = attribution(varB_texte)
        varC = attribution(varC_texte)




    varG_texte = "grotte"

    
    #création d'une nouvelles image (la map)
    background = Image.new('RGBA', ((len(liste[1])-1)*128,len(liste)*128+64), (255, 255, 255, 255))

    for i in range(0,len(liste)):
        ligne=liste[i]
        for j in range(0,len(ligne)):
            if ligne[j]=='A':
                background.paste(varA, (128*j+64,i*128+64))
            elif ligne[j]=='B':
                background.paste(varB, (128*j+64,i*128+64))
            elif ligne[j]=='C':
                background.paste(varC, (128*j+64,i*128+64))

                '''Les lettre R,P,Q,Z,M appartiennent au biome C, mais plus la population de contamine est importante
                plus ces lettres vont passé dans le biome contaminé de cette manière:
                -R à 1500 contaminés
                -P à 5000 contaminés
                -Q à 15000 contaminés
                -Z à 25000 contaminés
                -M à 30000 contaminés'''

            elif ligne[j]=='R' and population.contamination >= 1500:
                background.paste(contamine, (128*j+64,i*128+64))
                varR_texte = "contaminée"
            elif ligne[j]=='R' and population.contamination < 1500:
                background.paste(varC, (128*j+64,i*128+64))
                varR_texte = varC_texte

            elif ligne[j]=='P' and population.contamination >= 5000:
                background.paste(contamine, (128*j+64,i*128+64))
                varP_texte = "contaminée"
            elif ligne[j]=='P' and population.contamination < 5000:
                background.paste(varC, (128*j+64,i*128+64))
                varP_texte = varC_texte

            elif ligne[j]=='Q' and population.contamination >= 15000:
                background.paste(contamine, (128*j+64,i*128+64))
                varQ_texte = "contaminée"
            elif ligne[j]=='Q' and population.contamination < 15000:
                background.paste(varC, (128*j+64,i*128+64))
                varQ_texte = varC_texte

            elif ligne[j]=='Z' and population.contamination >= 25000:
                background.paste(contamine, (128*j+64,i*128+64))
                varZ_texte = "contaminée"
            elif ligne[j]=='Z' and population.contamination < 25000:
                background.paste(varC, (128*j+64,i*128+64))
                varZ_texte = varC_texte

            elif ligne[j]=='M' and population.contamination >= 30000:
                background.paste(contamine, (128*j+64,i*128+64))
                varM_texte = "contaminée"
            elif ligne[j]=='M' and population.contamination < 30000:
                background.paste(varB, (128*j+64,i*128+64)) 
                varM_texte = varB_texte


                '''Positionnements des villages et des points fixes sur la carte (oasis, auberge...)'''
                
            elif ligne[j]=='G':
                background.paste(grotte, (128*j+64,i*128+64))
            elif ligne[j]=='V':
                background.paste(Village_attribution(varA_texte), (128*j+64,i*128+64))

            elif ligne[j]=='S' :
                background.paste(Village_attribution(varB_texte), (128*j+64,i*128+64))
                
            elif ligne[j]=='N':
                background.paste(Village_attribution(varC_texte), (128*j+64,i*128+64))

            elif ligne[j]=='D':
                background.paste(Village_attribution(varC_texte), (128*j+64,i*128+64))




    #sauvegarde de la map
    background.save('img/map/map.png')
    mini = Image.open('img/map/map.png')
    resolution = (1024,768)
    minimap = mini.resize(resolution)
    minimap.save('img/map/minimap.png')
    print("génération terminé")

    #retourne à quel biome correspondent chaque lettre pour pouvoir l'afficher sur la carte
    return varA_texte,varB_texte,varC_texte,varG_texte,varR_texte,varP_texte,varQ_texte,varZ_texte,varM_texte
