from tkinter import *
from tkinter import tix
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter as tk
import xml.etree.ElementTree as etree

tree = etree.parse('utilisateur.xml')
root = tree.getroot()
# Une fonction très simpliste pour l'exemple

fenetre = tix.Tk()
fenetre.configure(bg = "#00c2ff")
fenetre.geometry("700x600")
fenetre.title("KeepKalm")
fenetre.minsize(1000,720)
fenetre.attributes('-fullscreen', True)



"""
filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
photo = PhotoImage(file=filepath)
canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="yellow")
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()
"""
l1 = LabelFrame(fenetre, text="", padx=20, pady=15)
l1.pack()
l1.configure(bg="#00c2ff")

def recupere():
    Kine_Ostheo = 0
    Cardiologue = 0
    Gynecologue = 0
    Nutritionniste = 0
    user = etree.Element("root")
    if (entree_nom.get()!=""):
        nom = etree.SubElement(user, "nom")

    else :
        showwarning("Attention","Case vide")
    if (entree_age.get()!=""):
        Age = entree_age.get()
        Age = int(Age)
        if (Age < 100 and Age >0):
            if (Age > 50):
                Cardiologue = Cardiologue + 3
            elif (Age < 50 and Age > 30):
                Cardiologue = Cardiologue + 2
            elif (Age < 30):
                Cardiologue = Cardiologue + 1

            Age = str(Age)
            age = etree.SubElement(user, "age")

        else:
            showwarning("Attention", "Superieur à 100")
    else :
        showwarning("Attention","case Vide")
        print(Cardiologue)


    if value2.get()=="Homme" or value2.get()=="Femme" or value2.get()=="Autre":
        sexeuser = etree.SubElement(user, "sexe")

    else:
        showwarning("Attention","Choissiser le sexe")

    poidsuser = value5.get()
    tailleuser = value4.get()
    IMC = poidsuser / ((tailleuser / 100) ** 2)
    IMC = int(IMC)
    print(IMC)
    imc = etree.SubElement(user, "imc")
    if (IMC < 18):
        Nutritionniste = Nutritionniste + 3


    elif (IMC > 25 and IMC < 30):
        Nutritionniste = Nutritionniste + 3
        Cardiologue = Cardiologue + 2
        Kine_Ostheo = Kine_Ostheo + 1


    elif (IMC > 30 and IMC < 35):
        Nutritionniste = Nutritionniste + 4
        Cardiologue = Cardiologue + 3
        Kine_Ostheo = Kine_Ostheo + 3


    elif (IMC > 35 and IMC < 50):
        Nutritionniste = Nutritionniste + 4
        Cardiologue = Cardiologue + 4
        Kine_Ostheo = Kine_Ostheo + 4


    print(Nutritionniste,Cardiologue,Kine_Ostheo)

    if entree_traitement.get()=="":
        traitementuser = etree.SubElement(user, "traitement")
        traitementuser.text = "*"
    else :
        traitementuser = etree.SubElement(user, "traitement")
        traitementuser.text = entree_traitement.get()
    if entree_allergie.get()=="":
        allergieuser = etree.SubElement(user, "allergie")
        allergieuser.text = "*"
    else :
        allergieuser = etree.SubElement(user, "allergie")
        allergieuser.text = entree_allergie.get()

    if (entree_nom.get()!="" and entree_age.get()!="" and (value2.get()=="Homme" or value2.get()=="Femme" or value2.get()=="Autre") and IMC < 50):
        nom.text = entree_nom.get()
        age.text = Age
        sexeuser.text = value2.get()
        IMC = str(IMC)
        imc.text = IMC
        root.append(user)
        tree.write("utilisateur.xml")
        fenetre.destroy()
        import corps
    else:
        showwarning("Attention","Veuillez tout remplir")






label = Label(fenetre, text="Entrer votre nom")
label.pack()
label.configure(bg="#00c2ff")
value = StringVar()
entree_nom = Entry(fenetre, textvariable=value, width=30)
entree_nom.pack()

label1 = Label(fenetre, text="Entrer votre age")
label1.pack()
label1.configure(bg="#00c2ff")
value1 = IntVar()
value1.set("")
entree_age = Entry(fenetre, textvariable=value1, width=30)
entree_age.pack()


value2 = StringVar()
bouton1 = Radiobutton(fenetre, text="Homme", variable=value2, value="Homme")
bouton2 = Radiobutton(fenetre, text="Femme", variable=value2, value="Femme")
bouton3 = Radiobutton(fenetre, text="Autre", variable=value2, value="Autre")
bouton1.pack()
bouton1.configure(bg="#00c2ff")
bouton2.pack()
bouton2.configure(bg="#00c2ff")
bouton3.pack()
bouton3.configure(bg="#00c2ff")

value4 = IntVar()
scale = Scale(fenetre, variable=value4, from_=1, to= 250, label='Taille (cm)',tickinterval=25)
scale.pack()
scale.configure(bg="#00c2ff")

value5 = IntVar()
scale = Scale(fenetre, variable=value5, from_=1, to=150, label='Poids (Kg)',orient='horizontal')
scale.pack()
scale.configure(bg="#00c2ff")

def choixsport():
    Label(fenetre, text='Quel sport ?',bg="#00c2ff").pack()
    varcombo = tix.StringVar()
    combo = tix.ComboBox(fenetre, editable=1, dropdown=1, variable=varcombo, anchor=N)
    combo.entry.config(state='readonly')  ## met la zone de texte en lecture seule
    combo.insert(0, 'sports de contact/combats')
    combo.insert(1, "sports d'addresse")
    combo.insert(2, 'sports de fond/endurance')
    combo.insert(3, 'Autre')
    combo.pack()



label2 = Label(fenetre, text="Pratiquez-vous un sport ?")
label2.pack()
label2.configure(bg="#00c2ff")
sport = StringVar()
bouton1 = Radiobutton(fenetre, text="oui", variable=sport, value=1, command=choixsport)
bouton2 = Radiobutton(fenetre, text="non", variable=sport, value=2)
bouton1.pack()
bouton1.configure(bg="#00c2ff")
bouton2.pack()
bouton2.configure(bg="#00c2ff")


labelL3= Label(fenetre, text="Veuillez renseiger  le traitement que vous prenez: ")
labelL3.pack()
labelL3.configure(bg="#00c2ff")
choix_traitement = StringVar()
entree_traitement = Entry(fenetre, textvariable=choix_traitement, width=30)
entree_traitement.pack()

labelL4= Label(fenetre, text="Veuillez renseiger  une allergie que vous avez: ")
labelL4.pack()
labelL4.configure(bg="#00c2ff")
choix_allergie = StringVar()
entree_allergie = Entry(fenetre, textvariable=choix_allergie, width=30)
entree_allergie.pack()

"""
traitement = etree.SubElement(user, "traitement")
traitement.text = quel_traitement

allerigie = etree.SubElement(user, "allergie")
allerigie.text = allergieclient

"""
def retour():
    fenetre.destroy()
    import tkinter_interface


bouton = Button(fenetre, text="Accéder au corps", bg="#22ffb9", command=recupere)
bouton.pack()


bouton = Button(fenetre, text="Retour", bg="red", command=retour)
bouton.pack(pady=15)

photo1 = PhotoImage(file="KeepKalmlogo.PNG")
zone_dessin = Canvas(fenetre, width=100, height=95, bg='#00c2ff', bd=0)
zone_dessin.create_image(48.5,80, image=photo1)
zone_dessin.pack(anchor="n")


fenetre.mainloop()