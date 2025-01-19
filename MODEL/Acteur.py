#coding: utf-8
from MODEL.Personne import Personne

class Acteur(Personne):
    nombreDeActeur = 0
    listeActeur = {}
    def __init__(self, nom, prenom, sexe, nomPersonnage, dateDebutEmploi, dateFinEmploi, cachet):
        Personne.__init__(self, nom, prenom, sexe)
        self._identifiant = Acteur.incrementerNombreDeActeur()
        self._nomPersonnage = nomPersonnage
        self._dateDebutEmploi = dateDebutEmploi
        self._dateFinEmploi = dateFinEmploi
        self._cachet = cachet
        
    #ENCAPSULATION DE _nomPersonnage
    def _getNomPersonnage(self):
        return self._nomPersonnage
    def _setNomPersonnage(self ,nouveau):
        self._nomPersonnage = nouveau
    nomPersonnage = property(_getNomPersonnage, _setNomPersonnage)


    #ENCAPSULATION DE _dateDebutEmploi
    def _getDateDebutEmploi(self):
        return self._dateDebutEmploi
    def _setDateDebutEmploi(self ,nouveau):
        self._dateDebutEmploi = nouveau
    dateDebutEmploi = property(_getDateDebutEmploi, _setDateDebutEmploi)


    #ENCAPSULATION DE _dateFinEmploi
    def _getDateDebutEmploi(self):
        return self._dateFinEmploi
    def _setDateDebutEmploi(self ,nouveau):
        self._dateFinEmploi = nouveau
    dateFinEmploi = property(_getDateDebutEmploi, _setDateDebutEmploi)


    #ENCAPSULATION DE _cachet
    def _getCachet(self):
        return self._cachet
    def _setCachet(self ,nouveau):
        self._cachet = nouveau
    cachet = property(_getCachet, _setCachet)
    
    #ICI NOUS AVONS UNE METHODES POUR COMPTER LE NOMBRE DE PERSONNE CREER
    def incrementerNombreDeActeur(cls):
        Acteur.nombreDeActeur = Acteur.nombreDeActeur+1
        return Acteur.nombreDeActeur
    incrementerNombreDeActeur = classmethod(incrementerNombreDeActeur)
    
    # FOCNTION POUR AJOUTER UN FILM A LA LISTE DES FILMS
    def _addActeur(id, val):
        Acteur.listeActeur[id] = val
    addActeur = staticmethod(_addActeur)