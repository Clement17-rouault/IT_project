from tkinter import *
from tkinter.messagebox import *

import xml.etree.ElementTree as etree

def xmlavb_dos(a,b,c):
    tree = etree.parse('utilisateur.xml')
    root = tree.getroot()
    user = etree.Element("douleur")
    endroit = etree.SubElement(user,"endroit")
    endroit.text= a
    endroitprecis = etree.SubElement(user, "douleur_precise")
    endroitprecis.text = b
    precision = etree.SubElement(user, "precision")
    precision.text = c
    root.append(user)
    tree.write("utilisateur.xml")



def xml(a,b):
    tree = etree.parse('utilisateur.xml')
    root = tree.getroot()
    user = etree.Element("douleur")
    endroit = etree.SubElement(user,"endroit")
    endroit.text= a
    precision = etree.SubElement(user, "precision")
    precision.text = b
    root.append(user)
    tree.write("utilisateur.xml")


def apel(a):
    new = Toplevel(Corps)
    new.title("KeepKalm")
    new.geometry("400x400")
    new.configure(bg="#34d4ff")
    text_urgence = Label(new, text="Douleurs "+a, padx=20, pady=15, relief="raised")
    text_urgence.pack(side=TOP, anchor=N)
    text_urgence.configure(font=90, bg="#34d4ff")


    label1 = Label(new, text="La douleur est plutot articulaire ou musculaire ? :")
    label1.pack()
    label1.configure(bg="#34d4ff")
    douleur = StringVar()
    bouton1 = Radiobutton(new, text="Articulation", variable=douleur, value="Articulation")
    bouton2 = Radiobutton(new, text="Muscle(s)", variable=douleur, value="Muscles")
    bouton1.pack()
    bouton1.configure(bg="#34d4ff")
    bouton2.pack()
    bouton2.configure(bg="#34d4ff")

    label1 = Label(new, text="Depuis combien de temps avez vous mal ? :")
    label1.pack()
    label1.configure(bg="#34d4ff")
    temps = StringVar()
    bouton1 = Radiobutton(new, text="Plusieurs jours", variable=temps, value="jours")
    bouton2 = Radiobutton(new, text="Plusieurs semaines", variable=temps, value="semaines")
    bouton3 = Radiobutton(new, text="Plusieurs mois", variable=temps, value="mois")
    bouton1.pack()
    bouton1.configure(bg="#34d4ff")
    bouton2.pack()
    bouton2.configure(bg="#34d4ff")
    bouton3.pack()
    bouton3.configure(bg="#34d4ff")

    label2 = Label(new, text="Voulez vous nous dire quelque chose à rajouter sur votre douleur ? :")
    label2.pack()
    label2.configure(bg="#34d4ff")
    value = IntVar()
    value.set("")
    entree_temps = Entry(new, textvariable=value, width=30)
    entree_temps.pack()
    #Recupération de la variable temps pour le mettre dans le xml


    def validation():
        if (douleur.get()!="" and temps!=""):
            b = douleur.get()
            print(b)
            xml(a,b)
            new.destroy()
        else :
            showwarning("Attention", "Veuillez remplir tous les champs !")
            new.destroy()
            Undo()
    def retour():
        new.destroy()
        Undo()
    bouton = Button(new, text="Valider", bg="yellow", command=validation)
    bouton.pack()
    bouton1 =Button(new, text="Retour", bg="red", command=retour)
    bouton1.pack()

#----------------------------------------------------------------------Fin fonction ----------------------------------------------------------------------

def CercleTeteCou():
    """ Dessine un cercle de centre (x,y) et de rayon r sur la tête et le cou """
    x = 173
    y = 70
    r = 10

    # on dessine un cercle dans la zone graphique
    item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')

    print("Création du cercle (item", item, ")")
    # affichage de tous les items de Canevas
    print(Canevas.find_all())
    apel("Tete/Cou")


def CercleEPD():
    """ Dessine un cercle de centre (x,y) et de rayon r sur l'épaule droite """
    x = 116
    y = 120
    r = 10

    # on dessine un cercle dans la zone graphique
    item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')

    print("Création du cercle (item", item, ")")
    # affichage de tous les items de Canevas
    print(Canevas.find_all())
    apel("epaule droite")
def CercleEPG():
    """ Dessine un cercle de centre (x,y) et de rayon r sur l'épaule Gauche """
    x = 232
    y = 120
    r = 10

    # on dessine un cercle dans la zone graphique
    item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')

    print("Création du cercle (item", item, ")")
    # affichage de tous les items de Canevas
    print(Canevas.find_all())
    apel("epaule gauche")
def CercleThorax():
    """ Dessine un cercle de centre (x,y) et de rayon r sur l'épaule droite """
    x = 173
    y = 150
    r = 10

    # on dessine un cercle dans la zone graphique
    item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')

    print("Création du cercle (item", item, ")")
    # affichage de tous les items de Canevas
    print(Canevas.find_all())
    apel("thorax")
def CercleAbdomen():
    """ Dessine un cercle de centre (x,y) et de rayon r sur l'abdomen """
    x = 173
    y = 220
    r = 10

    # on dessine un cercle dans la zone graphique
    item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')

    print("Création du cercle (item", item, ")")
    # affichage de tous les items de Canevas
    print(Canevas.find_all())
    apel("abdomen")

def CercleHanchesG():
    """ Dessine un cercle de centre (x,y) et de rayon r sur la Hanche gauche"""
    x = 215
    y = 250
    r = 10

    # on dessine un cercle dans la zone graphique
    item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')

    print("Création du cercle (item", item, ")")
    # affichage de tous les items de Canevas
    print(Canevas.find_all())
    apel("hanche gauche")
def CercleHanchesD():
    """ Dessine un cercle de centre (x,y) et de rayon r sur la Hanche droite"""
    x = 130
    y = 250
    r = 10

    # on dessine un cercle dans la zone graphique
    item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')

    print("Création du cercle (item", item, ")")
    # affichage de tous les items de Canevas
    print(Canevas.find_all())
    apel("hanche droite")
def CercleGG():
    """ Dessine un cercle de centre (x,y) et de rayon r sur le genou gauche """
    x = 215
    y = 400
    r = 10

    # on dessine un cercle dans la zone graphique
    item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')

    print("Création du cercle (item", item, ")")
    # affichage de tous les items de Canevas
    print(Canevas.find_all())
    apel("genoux gauche")
def CercleGD():
        """ Dessine un cercle de centre (x,y) et de rayon r sur le genou droit"""
        x = 130
        y = 400
        r = 10

        # on dessine un cercle dans la zone graphique
        item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')

        print("Création du cercle (item", item, ")")
        # affichage de tous les items de Canevas
        print(Canevas.find_all())
        apel("genoux droit")
def CercleAVBD():
        """ Dessine un cercle de centre (x,y) et un autre de centre(h,g) de rayon r sur l'avant bras droit (poignet et coude)"""
        x = 100
        y = 200
        r = 10
        h = 70
        g = 260
        # on dessine un cercle dans la zone graphique
        item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')
        item2 = Canevas.create_oval(h - r,g - r, h + r, g + r, outline='#22ffb9', fill='#22ffb9')
        print("Création du cercle (item", item, ")")
        print("Création du cercle (item", item2, ")")
        # affichage de tous les items de Canevas
        print(Canevas.find_all())
        avbd = Toplevel(Corps)
        avbd.title("KeepKalm")
        avbd.geometry("400x400")
        avbd.configure(bg="#34d4ff")
        text_urgence = Label(avbd, text="Douleurs avant bras droit", padx=20, pady=15, relief="raised")
        text_urgence.pack(side=TOP, anchor=N)
        text_urgence.configure(font=90, bg="#34d4ff")

        label1 = Label(avbd, text="Ou avez vous mal en particulier ? :")
        label1.pack()
        label1.configure(bg="#34d4ff")
        ouavbd = StringVar()
        bouton1 = Radiobutton(avbd, text="Coude", variable=ouavbd, value="coude")
        bouton2 = Radiobutton(avbd, text="Poignet", variable=ouavbd, value="poignet")
        bouton1.pack()
        bouton1.configure(bg="#34d4ff")
        bouton2.pack()
        bouton2.configure(bg="#34d4ff")



        label1 = Label(avbd, text="La douleur est plutot articulaire ou musculaire ? :")
        label1.pack()
        label1.configure(bg="#34d4ff")
        douleur = StringVar()
        bouton1 = Radiobutton(avbd, text="Articulation", variable=douleur, value="Articulation")
        bouton2 = Radiobutton(avbd, text="Muscle(s)", variable=douleur, value="Muscles")
        bouton1.pack()
        bouton1.configure(bg="#34d4ff")
        bouton2.pack()
        bouton2.configure(bg="#34d4ff")

        label1 = Label(avbd, text="Depuis combien de temps avez vous mal ? :")
        label1.pack()
        label1.configure(bg="#34d4ff")
        temps = StringVar()
        bouton1 = Radiobutton(avbd, text="Plusieurs jours", variable=temps, value=1)
        bouton2 = Radiobutton(avbd, text="Plusieurs semaines", variable=temps, value=2)
        bouton3 = Radiobutton(avbd, text="Plusieurs mois", variable=temps, value=3)
        bouton1.pack()
        bouton1.configure(bg="#34d4ff")
        bouton2.pack()
        bouton2.configure(bg="#34d4ff")
        bouton3.pack()
        bouton3.configure(bg="#34d4ff")

        label2 = Label(avbd, text="Voulez vous nous dire quelque chose à rajouter sur votre douleur ? :")
        label2.pack()
        label2.configure(bg="#34d4ff")
        value = IntVar()
        value.set("")
        entree_temps = Entry(avbd, textvariable=value, width=30)
        entree_temps.pack()

        def validation():
            if (ouavbd.get()!="" and douleur.get() !="" and temps.get() !=""):
                a = "Coude droit"
                b= ouavbd.get()
                c= douleur.get()
                xmlavb_dos(a,b,c)
                avbd.destroy()
            else:
                showwarning("Attention", "Veuillez remplir tous les champs")
                avbd.destroy()
                Undo()
                Undo()
        def retour():
            avbd.destroy()
            Undo()
            Undo()

        bouton = Button(avbd, text="Valider", bg="yellow", command=validation)
        bouton.pack()

        bouton1 = Button(avbd, text="Retour", bg="red", command=retour)
        bouton1.pack()



def CercleAVBG():

        x = 250
        y = 200
        r = 10
        h = 285
        g = 260

        # on dessine un cercle dans la zone graphique
        item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')
        item2 = Canevas.create_oval(h - r,g - r, h + r, g + r, outline='#22ffb9', fill='#22ffb9')
        print("Création du cercle (item", item, ")")
        print("Création du cercle (item", item2, ")")
        # affichage de tous les items de Canevas
        print(Canevas.find_all())
        avbg = Toplevel(Corps)
        avbg.title("KeepKalm")
        avbg.geometry("400x400")
        avbg.configure(bg="#34d4ff")
        text_urgence = Label(avbg, text="Douleurs avant bras gauche", padx=20, pady=15, relief="raised")
        text_urgence.pack(side=TOP, anchor=N)
        text_urgence.configure(font=90, bg="#34d4ff")

        label1 = Label(avbg, text="Ou avez vous mal en particulier ? :")
        label1.pack()
        label1.configure(bg="#34d4ff")
        ouavbg = StringVar()
        bouton1 = Radiobutton(avbg, text="Coude", variable=ouavbg, value="coude")
        bouton2 = Radiobutton(avbg, text="Poignet", variable=ouavbg, value="poignet")
        bouton1.pack()
        bouton1.configure(bg="#34d4ff")
        bouton2.pack()
        bouton2.configure(bg="#34d4ff")

        label1 = Label(avbg, text="La douleur est plutot articulaire ou musculaire ? :")
        label1.pack()
        label1.configure(bg="#34d4ff")
        douleur = StringVar()
        bouton1 = Radiobutton(avbg, text="Articulation", variable=douleur, value="Articulation")
        bouton2 = Radiobutton(avbg, text="Muscle(s)", variable=douleur, value="Muscles")
        bouton1.pack()
        bouton1.configure(bg="#34d4ff")
        bouton2.pack()
        bouton2.configure(bg="#34d4ff")

        label1 = Label(avbg, text="Depuis combien de temps avez vous mal ? :")
        label1.pack()
        label1.configure(bg="#34d4ff")
        temps = StringVar()
        bouton1 = Radiobutton(avbg, text="Plusieurs jours", variable=temps, value=1)
        bouton2 = Radiobutton(avbg, text="Plusieurs semaines", variable=temps, value=2)
        bouton3 = Radiobutton(avbg, text="Plusieurs mois", variable=temps, value=3)
        bouton1.pack()
        bouton1.configure(bg="#34d4ff")
        bouton2.pack()
        bouton2.configure(bg="#34d4ff")
        bouton3.pack()
        bouton3.configure(bg="#34d4ff")

        label2 = Label(avbg, text="Voulez vous nous dire quelque chose à rajouter sur votre douleur ? :")
        label2.pack()
        label2.configure(bg="#34d4ff")
        value = IntVar()
        value.set("")
        entree_temps = Entry(avbg, textvariable=value, width=30)
        entree_temps.pack()

        def validation():
            if (ouavbg.get()!="" and douleur.get() !="" and temps.get() !=""):
                a = "Coude gauche"
                b= ouavbg.get()
                c= douleur.get()
                xmlavb_dos(a,b,c)
                avbg.destroy()
            else:
                showwarning("Attention", "Veuillez remplir tous les champs !")
                avbg.destroy()
                Undo()
                Undo()
        def retour():
            avbg.destroy()
            Undo()
            Undo()

        bouton = Button(avbg, text="Valider", bg="yellow", command=validation)
        bouton.pack()

        bouton1 = Button(avbg, text="Retour", bg="red", command=retour)
        bouton1.pack()


def CerclePiD():
    """ Dessine un cercle de centre (x,y) et de rayon r sur le pied droit"""
    x = 125
    y = 500
    r = 10

    # on dessine un cercle dans la zone graphique
    item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')

    print("Création du cercle (item", item, ")")
    # affichage de tous les items de Canevas
    print(Canevas.find_all())
    apel("pied droit")

def CerclePiG():
        """ Dessine un cercle de centre (x,y) et de rayon r sur le pied gauche"""
        x = 235
        y = 500
        r = 10

        # on dessine un cercle dans la zone graphique
        item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')

        print("Création du cercle (item", item, ")")
        # affichage de tous les items de Canevas
        print(Canevas.find_all())
        apel("pied gauche")

def CercleDos():
    """ Dessine un cercle de centre (x,y) et de rayon r sur le pied gauche"""
    x = 475
    y = 250
    r = 10
    h = 475
    g = 150
    v = 475
    z = 100
    # on dessine un cercle dans la zone graphique
    item = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='#22ffb9', fill='#22ffb9')
    item2 = Canevas.create_oval(h - r, g - r, h + r, g + r, outline='#22ffb9', fill='#22ffb9')
    item3 = Canevas.create_oval(v - r, z - r, v + r, z + r, outline='#22ffb9', fill='#22ffb9')
    print("Création du cercle (item", item, ")")
    print("Création du cercle (item", item2, ")")
    print("Création du cercle (item", item3, ")")
    # affichage de tous les items de Canevas
    print(Canevas.find_all())

    dos = Toplevel(Corps)
    dos.title("KeepKalm")
    dos.geometry("400x400")
    dos.configure(bg="#34d4ff")
    text_urgence = Label(dos, text="Douleurs du dos", padx=20, pady=15, relief="raised")
    text_urgence.pack(side=TOP, anchor=N)
    text_urgence.configure(font=90, bg="#34d4ff")

    label1 = Label(dos, text="Ou avez vous mal en particulier ? :")
    label1.pack()
    label1.configure(bg="#34d4ff")
    oudos = StringVar()
    bouton1 = Radiobutton(dos, text="Haut", variable=oudos, value="haut")
    bouton2 = Radiobutton(dos, text="Milieu", variable=oudos, value="milieu")
    bouton3 = Radiobutton(dos, text="Bas", variable=oudos, value="bas")
    bouton1.pack()
    bouton1.configure(bg="#34d4ff")
    bouton2.pack()
    bouton2.configure(bg="#34d4ff")
    bouton3.pack()
    bouton3.configure(bg="#34d4ff")

    label1 = Label(dos, text="La douleur est plutot articulaire ou musculaire ? :")
    label1.pack()
    label1.configure(bg="#34d4ff")
    douleur = StringVar()
    bouton1 = Radiobutton(dos, text="Articulation", variable=douleur, value="Articulation")
    bouton2 = Radiobutton(dos, text="Muscle(s)", variable=douleur, value="Muscles")
    bouton1.pack()
    bouton1.configure(bg="#34d4ff")
    bouton2.pack()
    bouton2.configure(bg="#34d4ff")

    label1 = Label(dos, text="Depuis combien de temps avez vous mal ? :")
    label1.pack()
    label1.configure(bg="#34d4ff")
    temps = StringVar()
    bouton1 = Radiobutton(dos, text="Plusieurs jours", variable=temps, value=1)
    bouton2 = Radiobutton(dos, text="Plusieurs semaines", variable=temps, value=2)
    bouton3 = Radiobutton(dos, text="Plusieurs mois", variable=temps, value=3)
    bouton1.pack()
    bouton1.configure(bg="#34d4ff")
    bouton2.pack()
    bouton2.configure(bg="#34d4ff")
    bouton3.pack()
    bouton3.configure(bg="#34d4ff")

    label2 = Label(dos, text="Voulez vous nous dire quelque chose à rajouter sur votre douleur ? :")
    label2.pack()
    label2.configure(bg="#34d4ff")
    value = IntVar()
    value.set("")
    entree_temps = Entry(dos, textvariable=value, width=30)
    entree_temps.pack()

    def validation():
        if (oudos.get()!="" and douleur.get() !="" and temps.get() !="") :
            a= "Dos"
            b= oudos.get()
            c= douleur.get()
            xmlavb_dos(a,b,c)
            dos.destroy()
        else :
            showwarning("Attention", "Veuillez remplir tous les champs !")
            dos.destroy()
            Undo()
            Undo()
            Undo()
    def retour():
        dos.destroy()
        Undo()
        Undo()
        Undo()

    bouton = Button(dos, text="Valider", bg="yellow", command=validation)
    bouton.pack()
    bouton1 = Button(dos, text="Retour",bg='red', command=retour)
    bouton1.pack()


def Undo():
    """ Efface le dernier cercle"""
    if len(Canevas.find_all()) > 1:
        item = Canevas.find_all()[-1]
        # on efface le cercle
        Canevas.delete(item)

        print("Suppression du cercle (item", item, ")")
        # affichage de tous les items de Canevas
        print(Canevas.find_all())


# Création de la fenêtre principale (main window)
Corps = Tk()
Corps.title('KeepKalm')
Corps.attributes('-fullscreen', True)

text_Corps = Label(Corps, text="appuyer sur les boutons liés aux zones à problème :", padx=20, pady=15,relief="raised")
text_Corps.pack(side=TOP, anchor=N)
text_Corps.configure(bg="#22ffb9", font=90)

# Image de fond
photo = PhotoImage(file="corpsv2.png")

# Création d'un widget Canvas (zone graphique)
Largeur = 650
Hauteur = 550
Canevas = Canvas(Corps, width=Largeur, height=Hauteur)
item = Canevas.create_image(0, 0, anchor=NW, image=photo)
print("Image de fond (item", item, ")")
Canevas.pack()

BoutonEPD = Button(Corps, text='Tête/Cou', command=CercleTeteCou)
BoutonEPD.pack(side=LEFT, padx=4, pady=10)

BoutonEPD = Button(Corps, text='Epaule Droite', command=CercleEPD)
BoutonEPD.pack(side=LEFT, padx=4, pady=10)

BoutonEPG = Button(Corps, text='Epaule Gauche', command=CercleEPG)
BoutonEPG.pack(side=LEFT, padx=4, pady=10)

BoutonThorax = Button(Corps, text='Thorax', command=CercleThorax)
BoutonThorax.pack(side=LEFT, padx=4, pady=10)

BoutonAbdomen = Button(Corps, text='Abdomen', command=CercleAbdomen)
BoutonAbdomen.pack(side=LEFT, padx=4, pady=10)

BoutonHancheD = Button(Corps, text='Hanche Droite', command=CercleHanchesD)
BoutonHancheD.pack(side=LEFT, padx=4, pady=10)

BoutonHancheG = Button(Corps, text='Hanche Gauche', command=CercleHanchesG)
BoutonHancheG.pack(side=LEFT, padx=4, pady=10)

BoutonGD = Button(Corps, text='Genou Droit', command=CercleGD)
BoutonGD.pack(side=LEFT, padx=4, pady=10)

BoutonGG = Button(Corps, text='Genou Gauche', command=CercleGG)
BoutonGG.pack(side=LEFT, padx=4, pady=10)

BoutonAVBD = Button(Corps, text='Avant Bras Droit', command=CercleAVBD)
BoutonAVBD.pack(side=LEFT, padx=4, pady=10)

BoutonAVBG = Button(Corps, text='Avant Bras Gauche', command=CercleAVBG)
BoutonAVBG.pack(side=LEFT, padx=4, pady=10)

BoutonPiG = Button(Corps, text='Pied Gauche', command=CerclePiG)
BoutonPiG.pack(side=LEFT, padx=4, pady=10)

BoutonPiD = Button(Corps, text='Pied Droit', command=CerclePiD)
BoutonPiD.pack(side=LEFT, padx=4, pady=10)

BoutonDos = Button(Corps, text='Dos', command=CercleDos)
BoutonDos.pack(side=LEFT, padx=3, pady=10)

BoutonEffacer = Button(Corps, text='Revenir en arrière', bg="yellow",command=Undo)
BoutonEffacer.pack(side=LEFT, padx=3, pady=10)



Corps.mainloop()