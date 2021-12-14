#Villes et villages
nbLieux = int(input())
nbVilles = 0
for loop in range(nbLieux):
   population = int(input())
   if population > 10 * 1000:
      nbVilles += 1
print(nbVilles)


#Planning de la journée
Position = int(input())
nbVillages = int(input())
TotalVillages = 0
for loop in range(nbVillages):
   distanceVillage = int(input())
   if (distanceVillage - Position) <= 50 and (distanceVillage - Position) >= (-50):
      TotalVillages += 1
print(TotalVillages)


#Étape la plus longue
nbJours = int(input())
distanceMax = 0
for loop in range(nbJours):
   distance = int(input())
   if distance > distanceMax:
      distanceMax = distance
print(distanceMax)


#Calcul des dénivelées
nbVariations = int(input())
sommePos = 0
sommeNeg = 0
for loop in range(nbVariations):
   variation = int(input())
   if variation > 0:
      sommePos += variation
   else:
      sommeNeg -= variation
print(sommePos)
print(sommeNeg)
