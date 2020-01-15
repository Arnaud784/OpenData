import tkinter as tk
from tkinter import ttk

class IHM(tk.Frame):
    def __init__(self, liste_manifestations, liste_domaines, liste_communes, liste_date_debut, liste_date_fin, racine=None):
        tk.Frame.__init__(self, racine)
        self.racine = racine
		  # On initialise les listes
        self.liste_manifestations = liste_manifestations
        self.liste_domaines = liste_domaines
        self.liste_communes = liste_communes
        self.liste_date_debut = liste_date_debut
        self.liste_date_fin = liste_date_fin
		
        self.createWidgets()
        
    # renvoie tout les évènements sous forme de String
    def getTextListeManifestations(self):
        result = ""
        for manif in self.liste_manifestations:
            result += manif.__str__() + "\n\n"
        return result
		
    # renvoie tout les évènements trié avec les options de recherches sous forme de String
    def getSortedListeManifestations(self, commune, domaine, date_debut, date_fin):
        result = ""
        self.liste_domaines = []
        self.liste_communes = []
        self.liste_date_debut = []
        self.liste_date_fin = []
        for manif in self.liste_manifestations:
            if((manif.getCommune() == commune or commune == "Aucune") and (manif.getDomaine() == domaine or domaine == "Aucun") and (manif.getDateDebut() == date_debut or date_debut == "Aucune") and (manif.getDateFin() == date_fin or date_fin == "Aucune")):
                result += manif.__str__() + "\n\n"
                if(not manif.getDomaine() in self.liste_domaines):
                    self.liste_domaines.append(manif.getDomaine())
                if(not manif.getCommune() in self.liste_communes):
                    self.liste_communes.append(manif.getCommune())
                if(not manif.getDateDebut() in self.liste_date_debut):
                    self.liste_date_debut.append(manif.getDateDebut())
                if(not manif.getDateFin() in self.liste_date_fin):
                    self.liste_date_fin.append(manif.getDateFin())
        self.liste_domaines.sort()
        self.liste_communes.sort()
        self.liste_date_debut.sort()
        self.liste_date_fin.sort()
        self.liste_domaines.insert(0, "Aucun")
        self.liste_communes.insert(0, "Aucune")
        self.liste_date_debut.insert(0, "Aucune")
        self.liste_date_fin.insert(0, "Aucune")
        return result
        
    def getListeManifestations(self):
        return self.liste_manifestations
    
    def setListeManifestations(self, liste_manifestations):
        self.liste_manifestations = liste_manifestations
        
    #Evenement de selection déclenché lors de la modification d'une option de recherche
    def selectEvent(self, evt):
        self.textfield.delete("1.0", "end")
        self.textfield.insert(0.0, self.getSortedListeManifestations(self.w.get(), self.w2.get(), self.w3.get(), self.w4.get()))
        self.w.config(values=self.liste_communes)
        self.w2.config(values=self.liste_domaines)
        self.w3.config(values=self.liste_date_debut)
        self.w4.config(values=self.liste_date_fin)
        
    #Crée toute l'interface graphique
    def createWidgets(self):
        
        self.scrollbar = tk.Scrollbar(self.racine)
        self.textfield = tk.Text(self.racine,yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textfield.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.textfield.pack(side='left', expand=0, fill='both')
        self.textfield.insert(0.0, self.getTextListeManifestations())
        
        self.label = tk.Label(self.racine, text=" Options de recherche : \n")
        self.label.pack()
        
        self.label2 = tk.Label(self.racine, text=" Commune : ")
        self.label2.pack()
        
        self.variable = tk.StringVar(self.racine)
        self.variable.set("Aucune")
        self.w = ttk.Combobox(self.racine, values=self.liste_communes, state='readonly')
        self.w.current(0)
        self.w.bind("<<ComboboxSelected>>", self.selectEvent)
        self.w.pack()
        
        self.label3 = tk.Label(self.racine, text="\n Domaine : ")
        self.label3.pack()
        
        self.variable2 = tk.StringVar(self.racine)
        self.variable2.set("Aucun") # default value
        self.w2 = ttk.Combobox(self.racine, values=self.liste_domaines, state='readonly')
        self.w2.current(0)
        self.w2.bind("<<ComboboxSelected>>", self.selectEvent)
        self.w2.pack()
        
        self.label4 = tk.Label(self.racine, text="\n Date de début : ")
        self.label4.pack()
        
        self.variable3 = tk.StringVar(self.racine)
        self.variable3.set("Aucune") # default value
        self.w3 = ttk.Combobox(self.racine, values=self.liste_date_debut, state='readonly')
        self.w3.current(0)
        self.w3.bind("<<ComboboxSelected>>", self.selectEvent)
        self.w3.pack()
        
        self.label5 = tk.Label(self.racine, text="\n Date de fin : ")
        self.label5.pack()
        
        self.variable4 = tk.StringVar(self.racine)
        self.variable4.set("Aucune") # default value
        self.w4 = ttk.Combobox(self.racine, values=self.liste_date_fin, state='readonly')
        self.w4.current(0)
        self.w4.bind("<<ComboboxSelected>>", self.selectEvent)
        self.w4.pack()