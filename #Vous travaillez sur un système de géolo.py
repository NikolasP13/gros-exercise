#Vous travaillez sur un système de géolocation s'intitulant à la recherche du pôle Nord utilisant des coordonnées sous la forme degrés minutes secondes (DMS)
#Pour faciliter l'utilisation du système, on vous demande de créer un court programme permettant de convertir ces données sous la forme de degrés décimaux (DD).
#De plus, considérant que le but de l'application est d'indiquer la distance des usagers du pôle Nord magnétique en plus d'indiquer leur position, on vous demande d'ajouter à votre programme une fonction permettant de calculer cette distance.
#Versionner votre travail avec GitHub desktop et publié le sur votre profil GitHub Web une fois terminé
from ast import Return
from math import sqrt

# DMS à DD definition de la fonction
def dms_to_dd(villedms1,villedms2,villedms3):
    return villedms1 +(villedms2 / 60) + (villedms3 / 3600)

lat1_paris = 80
lat2_paris = 50
lat3_paris = 20

lon1_paris = 75
lon2_paris = 35
lon3_paris = 25

#appelle de la fonction DMS À DD

lon_paris, lat_paris = dms_to_dd(lon1_paris, lon2_paris, lon3_paris), dms_to_dd(lat1_paris, lat2_paris, lat3_paris)

print(lon_paris,lat_paris)
# definition de la fonction de distance entre 2 points et donner la réponse

def distance_km(LONG_1, LONG_2 , LAT_2, LAT_1):
    return sqrt((LONG_1 - LONG_2)**2 + (LAT_2 - LAT_1)**2)

# testing

distance_entre_2 = distance_km(120,90,150,20)
distance_entre_8 = distance_km(150,80,120,70)

print(distance_entre_2)
print(distance_entre_8)
print(distance_km( 150, 120, 15, 5))