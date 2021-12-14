#Récoltes
print((int(input())**2) * 23)


#Retraite spirituelle
print((60**2) * 16 * int(input()))


#Âge des petits-enfants
âgeCadet = int(input())
âgeAîné = int(input())
print(âgeAîné - âgeCadet)


#Encore des punitions
nbRep = int(input())
for loop in range(nbRep):
   print("Je dois suivre en cours")


#Graduation de thermomètres
tempMin = int(input())
tempMax = int(input())
temperature = tempMin
for loop in range(tempMax - tempMin + 1):
   print(temperature)
   temperature += 1
   
   
#Jeu de calcul mental
nbChef = int(input())
étape = 1
calcul = 66
for loop in range(nbChef):
   calcul *= étape
   étape += 1
   print(calcul)


#La Grande Braderie
position = int(input())
largeurEmplacement = int(input())

for iVendeur in range(int(input()) + 1):
   print(position)
   position += largeurEmplacement


#Bétail
rep = 0
for loop in range(20):
   rep = int(input()) + rep
print(rep)


#Socles pour statues
Hmax = int(input())
Hmin = int(input())
rep = 0
for loop in range(Hmax - Hmin + 1):
   rep += Hmin * Hmin
   Hmin += 1
print(rep)


#Le plus beau Karva
for loop in range(int(input())):
   poids = int(input())
   âge = int(input())
   print(int(input()) * int(input()) + poids)
