#Vous travaillez sur un système de géolocation s'intitulant à la recherche du pôle Nord utilisant des coordonnées sous la forme degrés minutes secondes (DMS)
#Pour faciliter l'utilisation du système, on vous demande de créer un court programme permettant de convertir ces données sous la forme de degrés décimaux (DD).
#De plus, considérant que le but de l'application est d'indiquer la distance des usagers du pôle Nord magnétique en plus d'indiquer leur position, on vous demande d'ajouter à votre programme une fonction permettant de calculer cette distance.
#Versionner votre travail avec GitHub desktop et publié le sur votre profil GitHub Web une fois terminé
def dms_to_dd(villedms1,villedms2,villedms3):
    ville = villedms1 +(villedms2 / 60) + (villedms3 / 3600)
    return ville

lat1_paris = 50
lat2_paris = 50
lat3_paris = 50

lon1_paris = 45
lon2_paris = 45
lon3_paris = 45

lon_paris, lat_paris = dms_to_dd(lon1_paris, lon2_paris, lon3_paris), dms_to_dd(lat1_paris, lat2_paris, lat3_paris)


