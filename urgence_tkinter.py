# Urgence de l'application
from tkinter import * 
from tkinter.messagebox import *


fenetre_urgence= Tk()

fenetre_urgence.title("Urgence !")
fenetre_urgence.configure(bg="red")
fenetre_urgence.geometry("700x600")


label = Label(fenetre_urgence, text="Test d'urgence")
label.pack()

Button(fenetre_urgence, text="Quitter", command=fenetre_urgence.quit).pack()

fenetre_urgence.mainloop()