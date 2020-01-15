class Manifestation:
    def __init__(self, nom_manif, code_postal, site_web, date_debut, date_fin, commune, domaine):
        self.nom_manif = nom_manif
        self.code_postal = code_postal
        self.site_web = site_web
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.commune = commune
        self.domaine = domaine
        
    def __str__(self):
        return "Nom : " + self.nom_manif + "\nCode postal : " + self.code_postal + "\nSite web : " + self.site_web + "\nDate début : " + self.date_debut + "\nDate fin : " + self.date_fin + "\nCommune : " + self.commune + "\nDomaine : " + self.domaine
        
    def getNomManif(self):
        return self.nom_manif
    def getCodePostal(self):
        return self.code_postal
    def getSiteWeb(self):
        return self.site_web
    def getDateDebut(self):
        return self.date_debut
    def getDateFin(self):
        return self.date_fin
    def getCommune(self):
        return self.commune
    def getDomaine(self):
        return self.domaine
    
    def setNomManif(self, nom_manif):
        self.nom_manif = nom_manif
    def setCodePostal(self, code_postal):
        self.code_postal = code_postal
    def setSiteWeb(self, site_web):
        self.site_web = site_web
    def setDateDebut(self, date_debut):
        self.date_debut = date_debut
    def setDateFin(self, date_fin):
        self.date_fin = date_fin
    def setCommune(self, commune):
        self.commune = commune
    def setDomaine(self, domaine):
        self.domaine = domaine