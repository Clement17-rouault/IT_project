from tkinter import *


#creer une première fenêtre
urgence_fenetre = Tk()

#personnalisation
urgence_fenetre.title("KeepKalm")
urgence_fenetre.geometry("700x600")
urgence_fenetre.config(bg="#34d4ff")
urgence_fenetre.minsize(1200,720)
urgence_fenetre.attributes('-fullscreen', True)

l1 = LabelFrame(urgence_fenetre, text="Langues", padx=20, pady=15,relief="raised",bd=5)
l1.pack(side=LEFT, anchor=NW)
l1.configure(bg="#22ffb9")
Label(l1, text="FR", bg="#22ffb9").pack()

l2 = LabelFrame(urgence_fenetre, text="Infos", padx=20, pady=15,relief="raised",bd=5)
l2.pack(side=RIGHT, anchor=NE)
l2.configure(bg="#22ffb9")
Label(l2, text="Rouault",bg="#01ffbb").pack()
Label(l2, text="Clément",bg="#01ffbb").pack()

text_urgence = Label(urgence_fenetre, text="URGENCE", padx=20, pady=15,relief="raised")
text_urgence.pack(side=TOP, anchor=N)
text_urgence.configure(bg="red", font=90)

Frame3 = Frame(urgence_fenetre,bg="#34d4ff", borderwidth=0)
Frame3.pack(anchor="n", pady=50)

Frame8 = Frame(urgence_fenetre, bg="#34d4ff", borderwidth=0)
Frame8.pack(anchor="n",side=RIGHT, pady=50)

Frame4 = Frame(urgence_fenetre,bg="#34d4ff", borderwidth=0)
Frame4.pack(anchor="n", side=LEFT, pady=50, padx=50)



Frame1 = Frame(Frame3)
Frame1.pack()

text_frame1=Label(Frame1, text="En cas de problème appeler d'urgence le personnel de santé qualifié : ",bg="#34d4ff", pady=20,font=30,fg="red")
text_frame1.pack()

Frame2 = Frame(Frame4)
Frame2.pack()
text_frame2 = Label(Frame2,text="Numéros d'urgence à contacter :",bg="#34d4ff",font=10,fg="red")
text_frame2.pack()

Frame5 = Frame(Frame4)
Frame5.pack()
text_frame5 = Label(Frame5, text="Samu : 15 \n\n Pompiers : 18 \n\n Police secours : 17 \n\n général : 112", bg="#34d4ff", font=20 )
text_frame5.pack()

Frame6 = Frame(Frame8)
Frame6.pack()
text_frame6 = Label(Frame6, text="Conseils en cas d'urgence : ", bg="#34d4ff", font=20, fg="red")
text_frame6.pack()

Frame7 = Frame(Frame8)
Frame7.pack()
text_frame7 = Label(Frame7, text="Allonger la personne en position latéral de sécurité. \n\n Laisser de l'espace. \n\n Ne pas laisser sans surveillance jusqu'à l'arrivé des secours!", bg="#34d4ff", font=10)
text_frame7.pack()

def retour():
    urgence_fenetre.destroy()
    import tkinter_interface

boutonsortie = Button(urgence_fenetre, text="Retour", bg="red",command=retour).pack()


urgence_fenetre.mainloop()
