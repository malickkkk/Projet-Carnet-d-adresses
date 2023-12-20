import sqlite3

import re

# Se connecter à la base de données SQLite
connection = sqlite3.connect('carnet_adresses.db')
cursor = connection.cursor()

def is_valid_phone_number(phone_number):
    # Définir le modèle du numéro de téléphone

    phone_number_pattern = re.compile(r'^\d{10,}$')

    # Vérifier si le numéro correspond au modèle
    return bool(re.match(phone_number_pattern, phone_number))


def is_valid_email(email):
    # Définir le modèle de l'adresse e-mail
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    # Vérifier si l'adresse e-mail correspond au modèle
    return bool(re.match(email_pattern, email))


def mettre_a_jour_table(tab):
    # Effacer les données existantes dans la Tab
    for row in tab.get_children():
        tab.delete(row)

    # Récupérer tous les contacts de la base de données
    contacts = cursor.execute("SELECT * FROM contacts").fetchall()

    # Ajouter chaque contact a la Tab
    for contact in contacts:
        tab.insert("", "end", values=contact)

# main.py

# Importer les modules nécessaires pour la validation des numéros de téléphone
import re

# Définir une fonction pour vérifier si le numéro de téléphone est valide
def is_valid_phone_number(phone_number):
    # Utiliser une expression régulière pour correspondre à un format de numéro de téléphone valide
    pattern = re.compile(r'^\d{10}$')
    return bool(pattern.match(phone_number))

# Reste de votre code...

# main.py

# Importez la fonction `is_valid_email` ici si ce n'est pas déjà fait

def ajouter_contact(tab, nom, prenom, email, telephone):
    # Vérifier si l'e-mail est dans un format correct
    if not is_valid_email(email):
       
        print("Adresse e-mail invalide. Veuillez entrer une adresse e-mail valide.")
        return


    # Si le numéro de téléphone est correct, procédez à l'ajout du contact
    cursor.execute('''
        INSERT INTO contacts (nom, prenom, email, telephone)
        VALUES (?, ?, ?, ?)
    ''', (nom, prenom, email, telephone))

    connection.commit()
    mettre_a_jour_table(tab)



def modifier_contact(tab, contact_id, nom, prenom, email, telephone):
    cursor.execute('''
        UPDATE contacts
        SET nom = ?, prenom = ?, email = ?, telephone = ?
        WHERE id = ?
    ''', (nom, prenom, email, telephone, contact_id))
    connection.commit()
    mettre_a_jour_table(tab)

def supprimer_contact(tab, contact_id):
    cursor.execute('''
        DELETE FROM contacts
        WHERE id = ?
    ''', (contact_id,))
    connection.commit()
    mettre_a_jour_table(tab)

# main.py

def rechercher_contact(tab, nom, email):
    # Effacer le contenu actuel du Tab
    for row in tab.get_children():
        tab.delete(row)

    # Vérifier si le nom ou l'e-mail est spécifié pour la recherche
    if nom or email:
        if nom and email:
            # Recherche avec le nom et l'e-mail spécifiés
            cursor.execute("SELECT * FROM contacts WHERE nom LIKE ? AND email LIKE ?", ('%' + nom + '%', '%' + email + '%'))
        elif nom:
            # Recherche avec le nom spécifié
            cursor.execute("SELECT * FROM contacts WHERE nom LIKE ?", ('%' + nom + '%',))
        elif email:
            # Recherche avec l'e-mail spécifié
            cursor.execute("SELECT * FROM contacts WHERE email LIKE ?", ('%' + email + '%',))

        results = cursor.fetchall()

        # Ajouter chaque contact trouvé au Tab
        for contact in results:
            tab.insert("", "end", values=contact)
    else:
        # Si ni le nom ni l'e-mail ne sont spécifiés, afficher tous les contacts
        mettre_a_jour_table(tab)
