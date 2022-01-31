#Importation des librairies.
from encodings import utf_8
import requests
from lxml import etree
import time
from time import gmtime, strftime, localtime
import os
import cmath
from datetime import datetime

#Liste des parkings.
parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB',
'FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT', 'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC',
'FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109',
'FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']

#Boucle infinie. Il est possible de limiter la boucle.
Boucle = 0
while Boucle <= 1:

        #Création liste avec des données exploitables definitive.
        CalculTotal2 = []
        CalculLibre2 = []

        #Suppression des ancien fichiers temporaires
        file = open("DonnéesParkings.txt", "w")
        file.close()
        file = open("PlacesTotal.txt", "w")
        file.close()
        file = open("PlacesLibre.txt", "w")
        file.close()
        file = open("DonnéesUtilisateur.txt","w") #Ce documents est présenter de façons à être facilement lisible.
        file.close()


        #Début boucle récupération données
        for i in range (len(parkings)):

                #Récupere les données.
                liens="https://data.montpellier3m.fr/sites/default/files/ressources/"+parkings[i]+".xml"
                response=requests.get(liens)

                #S'assure que les données reçus soit utilisable en regardant le code status.
                Status = response.status_code
                print(Status)

                #Si code status égale à 200, alors il n'y a pas d'erreur les données sont exploité. 
                if Status == 200:

                        #Crée la liste de donnée exploitable temporaires.
                        CalculTotal = 0
                        CalculLibre = 0
                        
                        #ajout de l'heure
                        file = open("DATAVoiture.csv","a", encoding='utf8')
                        file.write(time.strftime('%Y-%m-%d %H:%M:%S', localtime()))
                        file.write("\n")
                        file.close()
                        
                        #Crée un fichier de données brutes par parking.
                        f1 = open(parkings[i]+".txt","w", encoding='utf8')
                        f1.write(response.text)
                        f1.close()

                        #Met toute les données brutes des parkings dans un seul fichiers. 
                        f1=open("DonnéesParkings.txt","a", encoding='utf8')
                        f1.write(response.text)
                        f1.close()

                        #Recherche dans le fichier XML du parking sont nom. 
                        tree = etree.parse(parkings[i]+".txt")
                        for user in tree.xpath("Name"):
                                #print('Nom du parking :',user.text)

                                file = open("DATAVoiture.csv","a", encoding='utf8')
                                file.write(parkings[i])
                                file.write("\n")
                                file.close()

                                f1 = open("DonnéesUtilisateur.txt", "a")
                                f1.write(f"Nom = "+parkings[i]+"\n")
                                f1.close()

                        #Recherche dans le fichier XML du parking actuel les places total. 
                        for user in tree.xpath("Total"):
                                Place_Total = user.text
                                #print('Nombre total de places :',user.text)

                                #Change la données en integral.
                                CalculT = user.text
                                CalculTotalInt = int(CalculT)
                                CalculTotal += CalculTotalInt
                                
                                #Enregistrement des donnnées dans le fichier de données.
                                file = open("DATAVoiture.csv","a", encoding='utf8')
                                file.write(user.text)
                                file.write("\n")
                                file.close()
                        
                        
                                #Enregistrement des place total dans un ficher exploitable.
                                f1=open("PlacesTotal.txt","a", encoding='utf8')
                                f1.write(user.text+'\n')
                                f1.close()
                                
                                #Enregistrement des places total dans le .txt utilisateur.
                                f1 = open("DonnéesUtilisateur.txt", "a")
                                f1.write(f"Place aux Total = "+user.text+"\n")
                                f1.close()

                        #Recherche dans le fichier XML du parking actuel les places libre. 
                        for user in tree.xpath("Free"):
                                Place_Libres = user.text
                                #print('Nombre de places libres :',user.text)

                                #Change la données en intégral.
                                CalculL = user.text
                                CalculLibreInt = int(CalculL)
                                CalculLibre += CalculLibreInt


                                file = open("DATAVoiture.csv","a", encoding='utf8')
                                file.write(user.text)
                                file.write("\n")
                                file.close()
                                
                                
                                #Enregistrement des place libre dans un ficher exploitable.
                                f1=open("PlacesLibre.txt","a", encoding='utf8')
                                f1.write(user.text+'\n')
                                f1.close()

                                #Enregistrement des places libres dans le .txt utilisateur.
                                f1 = open("DonnéesUtilisateur.txt", "a")
                                f1.write(f"Place de libre = "+user.text+"\n")
                                f1.close

                        #Ajout à la liste des nombre de place total. 
                        CalculTotal2.append(CalculTotal)

                        #Ajout à la liste des nombre de place total. 
                        CalculLibre2.append(CalculLibre)

                        #Calcul pourcentage de place libre.
                        Place_Libres = int(Place_Libres)
                        Place_Total = int(Place_Total)
                        Pourcentage = str(round((Place_Libres * 100)/Place_Total))
                        #print("Pourcentage de place libre : "+Pourcentage+" %")

                        #Enregistrement du pourcentage de place libre dans le .txt utilisateur.
                        f1 = open("DonnéesUtilisateur.txt", "a")
                        f1.write(f"Pourcentages de libre = "+Pourcentage+" %"+"\n \n")
                        f1.close()

                        #Enregistrement du pourcentage de place libre dans un ficher exploitable.
                        f1 = open("DonnéesPourcentages.txt", "a")
                        f1.write(f""+Pourcentage+"\n")
                        f1.close()
        
                #Si le fichiers XML reçus à un code de status autre que 200 refait une demande, avec une attente de 2 secondes.
                #Mais cela ne fonctionne pas ici.
                else:
                        print('Redemande')
                        time.sleep(2)

        #Calcul moyenne de place Libre.
        somme = 0
        for i in range (len(CalculLibre2)):
                somme += CalculLibre2[i]
        somme = str(somme / len(CalculLibre2))
        #print(somme)

        #Sauvegarde données
        f1 = open("DonnéesMoyenneLibre.log", "a")
        f1.write(f""+somme+"\n")
        f1.close()

        #ecart type
        Moy = float(somme)
        N = len (CalculLibre2)
        var = 0
        for nb in CalculLibre2 : 
                var = var + (int(nb) - int(Moy))**2
        n = cmath.sqrt((1/N)* var)
        EcartType = float(n.real)
        EcartType = str(EcartType)

        #sauvegarde donnée
        f1 = open("DonnéesEcartType.log", "a")
        f1.write(""+EcartType+"\n")
        f1.close()

        #Enregistrement des données utiles.
        f1 = open("DATA1.csv", "a")
        f1.write(str())
        f1.write('\n')
        f1.close()
        #print(DATA)

        #Chargement des données
        f1 = open("DATA1.csv","r")
        print(f1.readline())
        f1.close()

        #Affiche la liste de liste des données utiles des parkings. En suite on attend 5 minutes le temps d'avoir la mise à jour du site.               
        print("Attend 5 min")
        time.sleep(300)
        

