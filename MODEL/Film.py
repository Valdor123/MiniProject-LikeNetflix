#coding: utf-8
from  Categorie import Categorie

class Film:
    def __init__(self, nom, duree, description, categorie):
        self._nom = nom
        self._duree = duree
        self._description = description
        self._categorie = categorie

    #ENCAPSULATION DE _nom
    def _getNom(self):
        return self._nom
    def _setNom(self, nouveau):
        self._nom = nouveau
    nom = property(_getNom, _setNom)
    
    #ENCAPSULATION DE _duree
    def getDuree(self):
        return self._duree
    def _setDuree(self, nouveau):
        self._duree = nouveau
    duree = property(getDuree, _setDuree)

    #ENCAPSULATION DE _description
    def _getDescription(self):
        return self._description
    def _setDescription(self, nouveau):
        self._description = nouveau
    description = property(_getDescription, _setDescription)
    
    #ENCAPSULATION DE _categorie
    def _getCategorie(self):
        return self._categorie
    def _setCategorie(self, nouveau):
        self._categorie = nouveau
    categorie = property(_getCategorie, _setCategorie)