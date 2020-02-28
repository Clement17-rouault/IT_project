# coding: utf-8
# Se connecter au fichier XML
import lxml
from lxml import etree
import xml.etree.ElementTree as ET
tree = ET.parse('datax.xml')
# ChatBot d'orientation


# Creation des questions à appeler plus tard
prenom = "Quel est votre prenom ? : "
a= "Quel est votre age ? : "
b = "Quel est votre sexe ? h pour Homme et f pour femme : "
c = "Quel est votre poids en Kg ? : "
d = "Quel est votre sport pratique ? : "
sports_pratique = "sports de contact/combats=0 ,sports d'addresse=1,sports de fond/endurance=2, Autre =3: "
t = "Utilisez vous un traitement particulier ? 'oui' ou 'non' : "
quelt = "Quel traitement prenez vous ? : "
allergie = "Avez vous des allergies connues ? 'oui' ou 'non' : "
allergi_util = "Quelles allergies ? : "
nature1 = "Douleur=0,Gonflement=1,Invalidite=2,antecedants comparable=3 : "
nature = "Pourquoi avez vous besoin de consulter ? : "
liste_nature = ['0', '1', '2', '3']
liste_sport = ['0', '1', '2','3']
douleur = "Ou avez vous mal ? : "

liste_endroit_douleur2 = ['Cheville','Genoux','Hanche','Bassin', 'Coude','Poignet','Epaule','Cou', 'Ventre','Dos', 'CHEVILLE',
                          'GENOUX', 'HANCHE','BASSIN','COUDE','POIGNET','EPAULE','COU','VENTRE','DOS','ventre','cheville','genoux',
                          'hanche','bassin', 'coude','poignet','epaule','cou','dos']
liste_douleur = ['tendon', 'Tendon', 'TENDON', 'articulation', 'Articulation', 'ARTICULATION', 'articulaire',
                 'Articulaire', 'ARTICULAIRE', 'muscle', 'Muscle', 'MUSCLE', 'muscles', 'Muscles', 'MUSCLES',
                 'Autre', 'autre', 'AUTRES', ' Autres', ' autre', ' Autre', ' AUTRE', ' AUTRES']
liste_date_douleur = ['quelques semaines', 'quelques jours', 'plusieurs mois']
# Variable du corps médical
Kine_Ostheo = 0
Cardiologue = 0
Gynecologue = 0
Nutritionniste = 0



name = input(prenom)
print("Bonjour", name)


"""
creeruser = input("Voulez vous creer un compte ? : ")
if (creeruser == "oui"):
    root = etree.Element("root")
    config = etree.SubElement(root, "config")
    mode = etree.SubElement(config, "nom")
    mode.text = "Zorro"
    langue = etree.SubElement(config, "metier")
    langue.text = "Danseur"
    #print(etree.tostring(root, pretty_print=True))
    tree.write('test.xml')
"""

age = int(input(a))
while (age < 0 or age > 100):
    age = int(input(a))
if (age > 50) :
    Cardiologue=Cardiologue + 3
elif (age<50 and age>30 ):
    Cardiologue=Cardiologue + 2
elif (age<30):
    Cardiologue= Cardiologue + 1

print(Cardiologue)

sexe = input(b)
while (sexe != "h" and sexe != "f"):
    sexe = input(b)
if (sexe == "f") :
    Gynecologue = Gynecologue + 2

print(Gynecologue)

taille = float(input("Quelle taille faites-vous ? (en cm) : "))
                                                 #inclure blindage si taille n'est pas un int redemander
while (taille <0):
    taille = float(input("Quelle taille faites-vous ? (en cm) :"))

poids = float(input(c))
while (poids < 0):
    poids = float(input(c))



IMC = poids / ((taille/100)**2)
IMC = int(IMC)
print("Votre IMC :",IMC)

if (IMC < 18):
    Nutritionniste = Nutritionniste + 3
elif(IMC > 18 and IMC < 24):
    print("Votre IMC est dans la moyenne continuer comme ça")
elif (IMC > 25 and IMC < 30):
    Nutritionniste = Nutritionniste + 3
    Cardiologue = Cardiologue + 2
    Kine_Ostheo = Kine_Ostheo + 1
elif (IMC > 30 and IMC < 35):
    Nutritionniste = Nutritionniste + 4
    Cardiologue = Cardiologue + 3
    Kine_Ostheo = Kine_Ostheo + 3
    print("Faites attention vous êtes en surpoids")
elif (IMC > 35):
    Nutritionniste = Nutritionniste + 4
    Cardiologue = Cardiologue + 4
    Kine_Ostheo = Kine_Ostheo + 4





Oui_ou_Non = input('Pratiquez vous un sport ? Oui ou Non :')

while(Oui_ou_Non != "Oui" and Oui_ou_Non !="Non" and Oui_ou_Non != "oui" and Oui_ou_Non != " Oui" and Oui_ou_Non != " Non" and Oui_ou_Non != " non" and Oui_ou_Non!="non"):
    Oui_ou_Non = input('Pratiquez vous un sport ? Oui ou Non : ')
if (Oui_ou_Non == "Oui" or Oui_ou_Non == "oui" or Oui_ou_Non == " Oui" or Oui_ou_Non == " oui"):
    print(sports_pratique)
    sport = input(d)
    while (sport not in liste_sport):
        sport = input(d)



traitement = input(t)
while (traitement != "Oui" and traitement !="Non" and traitement != "oui" and traitement != " Oui" and traitement != " Non" and traitement != " non"):
    traitement = input(t)
if (traitement=="Non" or traitement=="non" or traitement==" Non" or traitement==" non"):
    print("Parfait")
elif (traitement == "oui" or traitement == "Oui" or traitement == " Oui" or traitement == " oui"):
    quel_traitement = input(quelt)


allergiesconnues = input(allergie)
while (allergiesconnues != "Oui" and allergiesconnues !="Non" and allergiesconnues != "oui" and allergiesconnues != " Oui" and allergiesconnues != " Non" and allergiesconnues != " non" and allergiesconnues="non"):
    allergiesconnues = input(allergie)
if (allergiesconnues == "oui" or allergiesconnues == "Oui" or allergiesconnues == " oui" or allergiesconnues == " Oui" or allergiesconnues == "OUI" or allergiesconnues == " OUI"):
    allergieclient = input(allergi_util)
    Nutritionniste=Nutritionniste +1

else:
    print("Ok")

print(nature1)
natureconsul = input(nature)
while (natureconsul not in liste_nature):
    natureconsul = input(nature)
Kine_Ostheo = Kine_Ostheo+3    

print(liste_endroit_douleur2)
oudouleur = input(douleur)
while (oudouleur not in liste_endroit_douleur2):
    oudouleur = input(douleur)
Kine_Ostheo = Kine_Ostheo+3

endroitdouleur = input("Pensez vous que la douleur provient du : Articulation, Muscle ou Autre :")
while (endroitdouleur not in liste_douleur):
    endroitdouleur = input("Pensez vous que la douleur provient du : Articulation, Muscle ou Autre :")

if (endroitdouleur in liste_douleur):
    Kine_Ostheo = Kine_Ostheo  + 2


print(liste_date_douleur)
datedouleur = input("Depuis combien de temps avez vous mal ? :")
while (datedouleur not in liste_date_douleur):
    datedouleur = input("Depuis combien de temps avez vous mal ? :")


# Arbitraire
"""
if (Kine_Ostheo>Cardiologue):
    Medecin = "Kine_Ostheo"
elif (Kine_Ostheo<Cardiologue):
    Medecin ="Cardiologue"

elif (Kine_Ostheo==Cardiologue):
    Medecin = "Cardiologue/Kine Ostheo"

if (Medecin>Nutritionniste):
    Medecin = Medecin
elif (Medecin<Nutritionniste):
    Medecin = "Nutritionniste"
elif (Medecin==Nutritionniste):
    Medecin = "Nutritionniste/"+Medecin

if (Medecin>Gynecologue):
    Medecin = Medecin
elif (Medecin<Gynecologue):
    Medecin = "Gynecologue"
elif (Medecin==Gynecologue):
    Medecin = "Gynecologue/"+Medecin
"""

root = tree.getroot()
mode = root.find('user/nom')
mode1 = root.find('user/age')
mode2 = root.find('user/sexe')
mode3 = root.find('user/imc')
mode4 = root.find('user/traitement')
mode5 = root.find('user/allergie')
#mode6 = root.find('user/medecin')
mode.text = name
mode1.text = age
mode2.text = sexe
mode3.text = IMC
mode4.text = quel_traitement
mode5.text = allergieclient
#mode6.text = 'kine ostheo'

tree.write('datax.xml')

print
open('datax.xml').read()
