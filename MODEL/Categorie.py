#coding: utf-8

class Categorie:
    def __init__(self, nom, description):
        self._nom = nom
        self._description = description
    
    #ENCAPSULATION DE _nom
    def _getNom(self):
        return self._nom
    def _setNom(self, nouveau):
        self._nom = nouveau
    nom = property(_getNom, _setNom)
    
    #ENCAPSULATION DE _description
    def _getDescription(self):
        return self._description
    def _setDescription(self, nouveau):
        self._description = nouveau
    description = property(_getDescription, _setDescription)