import json
import Manifestation as m
import tkinter as tk
import IHM as ihm

if __name__ == "__main__":
    
    # Ces listes vont servir à stocker les informations à afficher
    liste = []
    liste_domaines = []
    liste_communes = []
    liste_date_debut = []
    liste_date_fin = []
    
    # On ouvre le fichier et récupère les informations
    with open('panorama-des-festivals.json') as json_data:
        data_dict = json.load(json_data)
        for data in data_dict:
            nom_manif = data['fields'].get('nom_de_la_manifestation', "")
            code_postal = data['fields'].get('code_postal', "")
            site_web = data['fields'].get('site_web', "")
            date_debut = data['fields'].get('date_de_debut', "")
            date_fin = data['fields'].get('date_de_fin', "")
            commune = data['fields'].get('commune_principale', "")
            domaine = data['fields'].get('domaine', "")
            manifestation = m.Manifestation(nom_manif, code_postal, site_web, date_debut, date_fin, commune, domaine)
            # On fais une liste des options pour les comboBox
            if(not domaine in liste_domaines):
                liste_domaines.append(domaine)
            if(not commune in liste_communes):
                liste_communes.append(commune)
            if(not date_debut in liste_date_debut):
                liste_date_debut.append(date_debut)
            if(not date_fin in liste_date_fin):
                liste_date_fin.append(date_fin)
            liste.append(manifestation)
    
    racine = tk.Tk()
    racine.title("Projet Arnaud Lieveaux")
	
    # On tri les liste
    liste_domaines.sort()
    liste_communes.sort()
    liste_date_debut.sort()
    liste_date_fin.sort()
    # On ajoute une option pour le retour en arrière d'un choix
    liste_domaines.insert(0, "Aucun")
    liste_communes.insert(0, "Aucune")
    liste_date_debut.insert(0, "Aucune")
    liste_date_fin.insert(0, "Aucune")
    
    app = ihm.IHM(liste, liste_domaines, liste_communes, liste_date_debut, liste_date_fin, racine)
    racine.mainloop()