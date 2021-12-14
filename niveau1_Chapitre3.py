#Réponds
print(42)


#L'éclipse
print(12581 - 11937)


#Bonbons pour tout le monde !
print((25 + 30 + 27 + 22 - 8) * 3)


#L'algoréathlon
print(2 + 34 + 6, end = " ")
print((2 + 34 + 6) * 2, end = " ")
print((2 + 34 + 6) * 3, end = " ")


#Cour de récréation
longueur = 17 * 5 + 7 * 2 + 5 * 1 + 2 * 2
print(longueur * longueur)
print(longueur * 4)


#Une partie de cache-cache
compte = 1
for loop in range(100):
   print(compte)
   compte += 1
print("J'arrive !")


#Progresser par l'erreur
print("V")
print("V")
print("I")
print("I")
print("V")
print("I")
print("I")


#Décollage de fusée
compte = 100
for loop in range(101):
   print(compte)
   compte -= 1
print("Décollage !")


#Invasion de batraciens
nbCrapauds = 1337
for loop in range(12):
   nbCrapauds *= 2
print(nbCrapauds)


#Kermesse
nbPlus = 1
result = 0
tour = 0
for loop in range(50):
   tour += 1
   result += tour
   print(result)


#Course avec les enfants
from robot import *

nbTour = 1
for loop in range(10):
   for loop in range(nbTour):
      droite()
   ramasser()
   for loop in range(nbTour):
      gauche()
   deposer()
   nbTour += 1


#Construction d'une pyramide
nbCubes = 0
largeurArête = 1
for loop in range(9):
   nbCubes += largeurArête**3
   largeurArête += 2
print(nbCubes)

#Table de multiplicationligne = 1
for loop in range(20):
   colonne = 1
   for loop in range(20):
      print(colonne * ligne, end = " ")
      colonne += 1
   print()
   ligne += 1
