from encodings import utf_8
import requests
from lxml import etree
from Fonction import Moyenne
from os import read

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB',
'FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT', 'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC',
'FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109',
'FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']


file = open("DonnéesPlaces.txt", "w")
file.close()
file = open("DonnéesParkings.txt", "w")
file.close()
file = open("PlacesTotal.txt", "w")
file.close()
file = open("PlacesLibre.txt", "w")
file.close()

DATA = []

for i in range (len(parkings)):
    liens="https://data.montpellier3m.fr/sites/default/files/ressources/"+parkings[i]+".xml"
    response=requests.get(liens)
    print(response.text)

    DATA2 = []

    f1=open(parkings[i]+".txt","w", encoding='utf8')
    f1.write(response.text)
    f1.close()

    f1=open("DonnéesParkings.txt","a", encoding='utf8')
    f1.write(response.text)
    f1.close()

    tree = etree.parse(parkings[i]+".txt")
    for user in tree.xpath("Name"):
        print('Nom du parking :',user.text)
        DATA2.append(user.text)


    for user in tree.xpath("Total"):
        Place_Total = user.text
        print('Nombre total de places :',user.text)
        DATA2.append(user.text)
        f1=open("PlacesTotal.txt","a", encoding='utf8')
        f1.write(user.text+'\n')
        f1.close()
        
    for user in tree.xpath("Free"):
        Place_Libres = user.text
        print('Nombre de places libres :',user.text)
        DATA2.append(user.text)
        f1=open("PlacesLibre.txt","a", encoding='utf8')
        f1.write(user.text+'\n')
        f1.close()
    
    DATA.append(DATA2)
    

print(DATA)





