#Chargement des données Voiture
f2 = open("DATAVoiture.csv","r", encoding='utf8')


y = 0
while y < 24: 
    x = 0
    while x < 4:
        x += 1
        ligne = f2.readline()     
        print(ligne)
    y += 1 
f2.close()


#Chargement des données Velo
f1 = open("DATAVelo.csv","r", encoding='utf8')
y = 0
while y < 24: 
    x = 0
    while x < 4:
        x += 1
        ligne = f1.readline() 
        print(ligne)
        file = open("GnuVelo", "w")
        file.write(ligne)
        file.close()
    
    
    y += 1 
f1.close()
