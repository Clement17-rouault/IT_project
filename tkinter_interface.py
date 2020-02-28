# Menu principal de l'application
from tkinter import * 
from tkinter.messagebox import *

menu_fenetre= Tk()
menu_fenetre.title("KeepKalm")
menu_fenetre.geometry("700x600")
menu_fenetre.configure(bg = "cyan")


l1 = LabelFrame(menu_fenetre, text="Langues", padx=20, pady=15)
l1.pack(side=LEFT, anchor=NW)
l1.configure(bg="cyan")
Label(l1, text="FR", bg="cyan").pack()



l2 = LabelFrame(menu_fenetre, text="Infos", padx=20, pady=15)
l2.pack(side=RIGHT, anchor=NE)
l2.configure(bg="cyan")
Label(l2, text="Rouault",bg="cyan").pack()
Label(l2, text="Clément",bg="cyan").pack()





text_bienvenue = Label(menu_fenetre, text="Bienvenue", font="50")
text_bienvenue.pack()
text_bienvenue.configure(bg="cyan")


photo1=PhotoImage(file="index.png")
zone_dessin = Canvas(menu_fenetre,width=100,height=100,bg='cyan',bd=0,relief="ridge") 
zone_dessin.create_image(50,0,image=photo1)
zone_dessin.pack()


"""
def callback():
    if askyesno('Attention', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('', 'Tant pis...')
    else:
        showinfo('', 'Vous avez peur!')
        

Button(text='Action', command=callback).pack()
"""

def propos():
    import A_propos.html

def alert1():
	showinfo("Vide", "Auncun diagnostics")

menubar = Menu(menu_fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Mes diagnostics", command=alert1)
menu1.add_separator()
menu1.add_command(label="Quitter", command=menu_fenetre.quit)
menubar.add_cascade(label="Moi", menu=menu1)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=propos)
menubar.add_cascade(label="Aide", menu=menu3)

menu_fenetre.config(menu=menubar)


def urgence():
	import urgence_tkinter	


Frame3 = Frame(menu_fenetre, borderwidth=20)
Frame3.pack(anchor="center", pady=160)

Frame1 = Frame(Frame3)
Frame1.pack()
Button(Frame1, text ='URGENCE', bg="red", command=urgence).pack()
text_frame1=Label(Frame1, text="Retrouver ici les numéros d'urgence", pady=5)
text_frame1.pack()


text_bienvenue = Label(Frame3, text="KᕮᕮᑭKᗩᒪᗰ", font=100)
text_bienvenue.pack()
text_bienvenue.configure(bg="cyan")

def rendezvous():
	import question_de_base_Update

Frame2 = Frame(Frame3)
Frame2.pack()
Button(Frame2, text ='Rendez-vous', bg="green",command=rendezvous).pack()
text_frame2=Label(Frame2, text="Vous ne savez pas qui consulter \n c'est ICI ! ")
text_frame2.pack()




menu_fenetre.mainloop()
