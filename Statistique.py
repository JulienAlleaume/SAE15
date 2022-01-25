import Fonction as fc


T=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
L1=[3,3,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,8,7,4]
L2=[103,203,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,-92,-93,-96]

moyenneT = fc.Moyenne(T)
moyenneL1 = fc.Moyenne(L1)
moyenneL2 = fc.Moyenne(L2)

print(moyenneT)
print(moyenneL1)
print(moyenneL2)

sigmaT = fc.Sigma(T)
sigmaL1 = fc.Sigma(L1)
sigmaL2 = fc.Sigma(L2)

print(sigmaT)
print(sigmaL1)
print(sigmaL2)
