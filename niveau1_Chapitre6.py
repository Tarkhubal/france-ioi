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


#Type d'arbres
hauteur = int(input())
nbFolioles = int(input())
if hauteur < 9:
   if nbFolioles > 6:
      print("Tinuviel")
   else:
      print("Falarion")
else:
   if nbFolioles < 8:
      print("Dorthonion")
   else:
      print("Calaelen")


#Tarifs de l'auberge
age = int(input())
if age < 10:
   print(5)
elif age == 60:
   print(0)
elif int(input()) >= 20:
   print(40)
else:
   print(30)


#Protection du village
nbMaisons = int(input())

xMin = 1000 * 1000
xMax = 0
yMin = 1000 * 1000
yMax = 0

for loop in range(nbMaisons):
   x = int(input())
   y = int(input())
   
   if x < xMin:
      xMin = x
   if x > xMax:
      xMax = x
   if y < yMin:
      yMin = y
   if y > yMax:
      yMax = y

largeur = xMax - xMin
longueur = yMax - yMin
p = 2*(largeur + longueur)

print(p)
