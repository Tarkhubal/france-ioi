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
