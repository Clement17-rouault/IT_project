# Menu principal de l'application
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import xml.etree.ElementTree as etree
import webbrowser

menu_fenetre = tk.Tk()
menu_fenetre.title("KeepKalm")
menu_fenetre.geometry("700x600")
menu_fenetre.configure(bg="#34d4ff")
menu_fenetre.minsize(1000, 720)
menu_fenetre.attributes('-fullscreen', True)

l1 = LabelFrame(menu_fenetre, text="Langues", padx=20, pady=15,relief="raised",bd=5)
l1.pack(side=LEFT, anchor=NW)
l1.configure(bg="#22ffb9")
Label(l1, text="FR", bg="#22ffb9").pack()

l2 = LabelFrame(menu_fenetre, text="Infos", padx=20, pady=15,relief="raised",bd=5)
l2.pack(side=RIGHT, anchor=NE)
l2.configure(bg="#22ffb9")
Label(l2, text="Rouault", bg="#22ffb9").pack()
Label(l2, text="Clément", bg="#22ffb9").pack()

text_bienvenue = Label(menu_fenetre, text="BIENVENUE", padx=20, pady=20,relief="raised")
text_bienvenue.pack(side=TOP, anchor=N)
text_bienvenue.configure(bg="#22ffb9", font=50)


def propos():
    webbrowser.open('A_propos.html')


def alert1():
    showinfo("Vide", "Auncun diagnostics")


menubar = Menu(menu_fenetre)

menu1 = Menu(menubar, tearoff=0,bg="#22ffb9")
menu1.add_command(label="Mes diagnostics", command=alert1)
menu1.add_separator()
menu1.add_command(label="Quitter", command=menu_fenetre.quit)
menubar.add_cascade(label="Moi", menu=menu1)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=propos)
menubar.add_cascade(label="Aide", menu=menu3)

menu_fenetre.config(menu=menubar)


def urgence():
    menu_fenetre.destroy()
    import GUI1


Frame3 = Frame(menu_fenetre, borderwidth=50,bg="#22ffb9")
Frame3.pack(anchor="n", pady=60)

Frame1 = Frame(Frame3)
Frame1.pack()
Button(Frame1, text='URGENCE', bg="red", command=urgence,relief=RAISED,width=24, borderwidth=10).pack()
text_frame1 = Label(Frame1, text="Retrouver ici les numéros d'urgence", pady=5,bg="#22ffb9")
text_frame1.pack()

text_bienvenue = Label(Frame3, text="KᕮᕮᑭKᗩᒪᗰ", font=100)
text_bienvenue.pack()
text_bienvenue.configure(bg="#22ffb9")


def rendezvous():
        menu_fenetre.destroy()
        import saisietkinter


#----------------------------------------------------- FIN de la fonction ------------------------------------------------------



Frame2 = Frame(Frame3)
Frame2.pack()
Button(Frame2, text='Rendez-vous', bg="green", command=rendezvous,width=21, borderwidth=10,relief=RAISED).pack()
text_frame2 = Label(Frame2, text="Vous ne savez pas qui consulter \n c'est ICI ! ",bg="#22ffb9")
text_frame2.pack()

photo1 = PhotoImage(file="KeepKalmlogo.PNG")
zone_dessin = Canvas(menu_fenetre, width=200, height=195, bg='#00c2ff', bd=0)
zone_dessin.create_image(95,95, image=photo1)
zone_dessin.pack(anchor="n")


menu_fenetre.mainloop()
