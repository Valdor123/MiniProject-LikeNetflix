#coding: utf-8
from  MODEL.Categorie import Categorie

class Film:
    listeFilme = {}
    def __init__(self, nom, duree, description, categorie, listeActeur):
        self._nom = nom
        self._duree = duree
        self._description = description
        self._listeCategorie = categorie
        self._listeActeur = listeActeur

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
    def _getListeCategorie(self):
        listeCate =''
        for elt in self._listeCategorie:
            listeCate = self._listeCategorie.get(elt).nom + listeCate + "\n"
        return listeCate
    getListeCategorie = classmethod(_getListeCategorie)
    
    def _ajouterCategorie(self, nouveau):
        self._listeCategorie[id] = nouveau
    ajouterCategorie = property(_ajouterCategorie)

    #ENCAPSULATION DE listeActeur
    def _getListeActeur(self):
        return self._listeActeur
    def _setListeActeur(self, nouveau):
        self._listeActeur = nouveau
    categorie = property(_getListeActeur, _setListeActeur)

    # FOCNTION POUR AJOUTER UN FILM A LA LISTE DES FILMS
    def _addFilm(id, val):
        Film.listeFilme[id] = val
    addFilm = staticmethod(_addFilm)