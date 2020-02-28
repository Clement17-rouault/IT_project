
def calculIMC(poids,taille):
    IMC = poids / ((taille/100)**2)
    return IMC


def sports(Oui_ou_Non):
    Oui_ou_Non = raw_input('Pratiquez vous un sport ? Oui ou Non ')
    while(Oui_ou_Non != "Oui" and Oui_ou_Non !="Non" and Oui_ou_Non != "oui" and Oui_ou_Non != " Oui" and Oui_ou_Non != " Non" and Oui_ou_Non != " non"):
        Oui_ou_Non = input('Pratiquez vous un sport ? Oui ou Non')

    if (Oui_ou_Non == "Oui" or Oui_ou_Non == "oui"):
        print(sports_pratique)
    sport = raw_input(d)
    while (sport not in liste_sport):
        sport = raw_input(d)
