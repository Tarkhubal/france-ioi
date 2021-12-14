#Transport des bagages
if int(input()) * int(input()) > 105:
   print("Surcharge !")


#Bornes kilométriques
nb1 = int(input())
nb2 = int(input())
rep = 0

if nb1 > nb2:
   rep = nb1 - nb2
if nb2 > nb1:
   rep = nb2 - nb1
print(rep)


#Tarifs dégressifs
prix = 10 + 5 * int(input())
if prix > 53:
   prix = 53
print(prix)


#Bagarre générale
superficieArignon = int(input())
superficieEvaran = int(input())

if superficieArignon > superficieEvaran + 10:
   print("La famille Arignon a un champ trop grand")
if superficieEvaran > superficieArignon + 10:
   print("La famille Evaran a un champ trop grand")


#Tarif du bateau
if int(input()) < 21:
   print("Tarif réduit")
else:
   print("Tarif plein")


#Traversée du pont
valeurDe = int(input()) + int(input())

if valeurDe >= 10:
   print("Taxe spéciale !")
   print(36)
if valeurDe < 10:
   valeurDe *= 2
   print("Taxe régulière")
   print(valeurDe)


#Concours de tir à la corde
totalÉquipe1 = 0
totalÉquipe2 = 0
for loop in range(int(input())):
   totalÉquipe1 += int(input())
   totalÉquipe2 += int(input())
if totalÉquipe1 > totalÉquipe2:
   print("L'équipe 1 a un avantage")
else:
   print("L'équipe 2 a un avantage")
print("Poids total pour l'équipe 1 :", totalÉquipe1)
print("Poids total pour l'équipe 2 :", totalÉquipe2)
