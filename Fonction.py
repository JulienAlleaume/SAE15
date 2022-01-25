from cmath import sqrt
from multiprocessing.sharedctypes import Value

#Calcul de la moyenne
def Moyenne(A): 
    Moy = sum(A)/len(A)
    return(Moy)
   
# Calcul de l'écart-type
def Sigma(B):
    Moy=Moyenne(B)
    N = len (B)
    var = 0
    for nb in B : 
        var += (nb - Moy)**2

        return sqrt ((1/N)* var)