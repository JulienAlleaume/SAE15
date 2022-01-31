#Importation des librairies.
from encodings import utf_8
from lxml import etree
import xml.etree.ElementTree as P
import time
from cmath import sqrt
from datetime import datetime
import requests
import csv

file = open("DATAVelo.csv","w", encoding='utf8')
file.close()

x = 1
while x < 2:
    
    URL = "https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml"
    response = requests.get(URL)
    with open("velo.xml", 'wb') as fichier:
        fichier.write(response.content)
    
    Velo = str("velo.xml")
    tree = P.parse(Velo)
    root = tree.getroot()
    fils = list(root)[0]

    for i in range(len(fils)):
            d = ((str(datetime.now())))
            n = (int(fils[i].attrib["id"]))
            a = (int(fils[i].attrib["av"]))
            f = (int(fils[i].attrib["fr"]))
            t = (int(fils[i].attrib["to"]))
            #print(d, n, a, f, t)
        
            file = open("DATAVelo.csv","a", encoding='utf8')
            file.write(str(d))
            file.write("\n")
            file.write(str(n))
            file.write("\n")
            file.write(str(a))
            file.write("\n")
            file.write(str(f))
            file.write("\n")
            file.write(str(t))
            file.write("\n")
            file.close()
            
    #available = velo dispo 
    #free place = place dispo
    #Place total = t 
          
    print("Attend 5 min")
    time.sleep(300)
    
   
     
     
     