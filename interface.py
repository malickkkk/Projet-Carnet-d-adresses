from tkinter import ttk
from tkinter import *


# Charger les fonctions du fichier main.py
from main import ajouter_contact, rechercher_contact, modifier_contact, supprimer_contact, mettre_a_jour_table

# Créer la fenêtre principale
root = Tk()
root.title("Carnet d'adresses")
root.geometry("1000x720")
root.configure(bg='#616A6B') 
root.iconbitmap("100218AQ.ico")

# Ajouter un titre
lbTitle = Label(root, text="Adress Book", font=("Arial", 21), bg="white")
lbTitle.place(x=0, y=0, width=250)

# Espace de recherche par nom
lbRechercher_nom = Label(root, text="Rechercher par nom", bg="darkblue", fg="white")
lbRechercher_nom.place(x=250, y=0, width=120)
entryRechercher_nom = Entry(root)
entryRechercher_nom.place(x=380, y=0, width=160)

# Espace de recherche par e-mail
lbRechercher_email = Label(root, text="Rechercher par email", bg="darkblue", fg="white")
lbRechercher_email.place(x=250, y=20, width=120)
entryRechercher_email = Entry(root)
entryRechercher_email.place(x=380, y=20, width=160)

# Espace Nom
lblNom = Label(root, text="Nom", bg="black", fg="yellow")
lblNom.place(x=5, y=50, width=125)
entryNom = Entry(root)
entryNom.place(x=140, y=50, width=400)

# Prenom
lblPrenom = Label(root, text="Prenom", bg="black", fg="yellow")
lblPrenom.place(x=5, y=70, width=125)
entryPrenom = Entry(root)
entryPrenom.place(x=140, y=70, width=400)

# Email
lblMail = Label(root, text="Email", bg="black", fg="yellow")
lblMail.place(x=5, y=90, width=125)
entryMail = Entry(root)
entryMail.place(x=140, y=90, width=400)

# Telephone
lblTelephone = Label(root, text="Telephone", bg="black", fg="yellow")
lblTelephone.place(x=5, y=110, width=125)
entryTelephone = Entry(root)
entryTelephone.place(x=140, y=110, width=400)

# Plus d'informations
lblMore_info = Label(root, text="Plus d'informations", bg="black", fg="yellow")
lblMore_info.place(x=5, y=130, width=125)
entryMore_info = Entry(root)
entryMore_info.place(x=140, y=130, width=400)

# Boutons
btnAdd = Button(root, text="Ajouter", bg="darkblue", fg="Yellow")
btnAdd.place(x=5, y=170, width=225)

btnModifier = Button(root, text="Modifier", bg="darkblue", fg="Yellow")
btnModifier.place(x=5, y=190, width=225)

btnSupp = Button(root, text="Supprimer", bg="darkblue", fg="Yellow")
btnSupp.place(x=5, y=210, width=225)

btnExit = Button(root, text="Sortir de l'application", bg="darkblue", fg="Yellow", command=quit)
btnExit.place(x=5, y=240, width=225)

# Table
tab = ttk.Treeview(root, columns=(1, 2, 3, 4, 5), height=30, show="headings")
tab.place(x=265, y=170, width=700, height=250)

tab.heading(1, text="Id")
tab.heading(2, text="Nom")
tab.heading(3, text="Prenom")
tab.heading(4, text="Email")
tab.heading(5, text="Telephone")

tab.column(1, width=50)
tab.column(2, width=100)
tab.column(3, width=150)
tab.column(4, width=200)
tab.column(5, width=250)

# Configurer les boutons pour appeler les fonctions appropriées
btnAdd.config(command=lambda: ajouter_contact(tab, entryNom.get(), entryPrenom.get(), entryMail.get(), entryTelephone.get()))
btnModifier.config(command=lambda: modifier_contact(tab, tab.item(tab.selection(), 'values')[0], entryNom.get(), entryPrenom.get(), entryMail.get(), entryTelephone.get()))
btnSupp.config(command=lambda: supprimer_contact(tab, tab.item(tab.selection(), 'values')[0]))

# Ajouter la fonction de recherche au bouton de recherche
btnRechercher = Button(root, text="Rechercher", bg="darkblue", fg="Yellow", command=lambda: rechercher_contact(tab, entryRechercher_nom.get(), entryRechercher_email.get()))
btnRechercher.place(x=550, y=5, width=120)

# Lancer la boucle principale Tkinter
root.mainloop()
