#Espion étranger
dateDébut = int(input())
dateFin = int(input())
nbEntrées = int(input())
nbPersonnes = 0
for loop in range(nbEntrées):
   date = int(input())
   if dateDébut <= date and date <= dateFin:
      nbPersonnes += 1
print(nbPersonnes)


#Maison de l'espion
xMin = int(input())
xMax = int(input())
yMin = int(input())
yMax = int(input())
nbMaisons = int(input())
nbAFouiller = 0
for loop in range(nbMaisons):
   x = int(input())
   y = int(input())
   if (xMin <= x) and (x <= xMax) and (yMin <= y) and (y <= yMax):
      nbAFouiller += 1
print(nbAFouiller)


#Nombre de jours dans le mois
numero = int(input())
if numero == 11:
   print(29)
else:
   if ( (4 <= numero) and (numero <= 6) ) or (numero == 10):
      print(31)
   else:
      print(30)


#Amitié entre gardes
dateDebutPremier = int(input())
dateFinPremier = int(input())
dateDebutSecond = int(input())
dateFinSecond = int(input())

if (dateFinSecond < dateDebutPremier) or (dateFinPremier < dateDebutSecond):
   print("Pas amis")
else:
   print("Amis")


#Nombre de personnes à la fête
nbMax = 0
nbActuel = 0
for loop in range(int(input()) * 2):
   numero = int(input())
   if numero > 0:
      nbActuel += 1
   else:
      nbActuel -= 1
   if nbActuel > nbMax:
      nbMax = nbActuel
print(nbMax)


#Casernes de pompiers
nbPaires = int(input())
for loop in range(nbPaires):
   xMin1 = int(input())
   xMax1 = int(input())
   yMin1 = int(input())
   yMax1 = int(input())
   xMin2 = int(input())
   xMax2 = int(input())
   yMin2 = int(input())
   yMax2 = int(input())
   if ( (xMax2 <= xMin1) or (xMax1 <= xMin2) ) or ( (yMax2 <= yMin1) or (yMax1 <= yMin2) ):
      print("NON")
   else:
      print("OUI")


#Personne disparue
# -- Recherche en cours -- #


#La grande fête
# -- Recherche en cours -- #


#L'espion est démasqué !
# -- Recherche en cours -- #
