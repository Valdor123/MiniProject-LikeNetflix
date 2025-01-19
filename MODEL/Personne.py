#coding: UTF-8

class Personne:
    
    listePersonne = {} #ICI ON INITIALISE LA LISTE DES PERSONNE QU'ON VA CREER AU COURS DU PROGRAMME
    nombreDePersonne = 0 #ICI ON DEFINIT LE NOMBRE DE PERSONNE CREER A 0 IL AUGMENTERA A CHAQUE CREATION D'UN OBJET DE TYPE PERSONNE
    def __init__(self, nom, prenom, sexe):
        self._identifiant = Personne.incrementerNombreDePersonne()
        self._nom = nom
        self._prenom = prenom
        self._sexe = sexe
    
    #L'ENCAPSULATION DE L'ATTRIBUT _nom
    #LA FONCTION POUR RETOURNER _nom
    def _getNom(self):
        return self._nom

    #LA FONCTION POUR DEFINIR _nom
    def _setNom(self, nouveau):
        self._nom = nouveau
    
    #L'ACCESSEUR DE L'ATTRIBUT _nom
    nom = property(_getNom, _setNom)

    
    #L'ENCAPSULATION DE L'ATTRIBUT _prenom
    #LA FONCTION POUR RETOURNER _prenom
    def _getPrenom(self):
        return self._prenom
    
    #LA FONCTION POUR DEFINIR _prenom
    def _setPrenom(self, nouveau):
        self._prenom = nouveau
    
    #L'ACCESSEUR DE L'ATTRIBUT _prenom
    prenom = property(_getPrenom, _setPrenom)


    #L'ENCAPSULATION DE L'ATTRIBUT _sexe
    #LA FONCTION POUR RETOURNER _sexe
    def _getSexe(self):
        return self._sexe
    
    #LA FONCTION POUR DEFINIR _sexe
    def _setSexe(self ,nouveau):
        self._sexe = nouveau
    
    #L'ACCESSEUR DE L'ATTRIBUT _sexe
    sexe = property(_getSexe, _setSexe)


    #L'ENCAPSULATION DE L'ATTRIBUT _identifiant
    #LA FONCTION POUR RETOURNER _identifiant
    def _getIdentifiant(self):
        return self._identifiant
    
    #LA FONCTION POUR DEFINIR _identifiant
    def _setIdentifiant(self ,nouveau):
        self._identifiant = nouveau
    
    #L'ACCESSEUR DE L'ATTRIBUT _identifiant
    identifiant = property(_getIdentifiant, _setIdentifiant)


    #ICI NOUS AVONS LA METHODES POUR AJOUTER UNE PERSONNE A LA LISTE
    def addPersonne(self):
        pass
    
    #ICI NOUS AVONS LA METHODES POUR SUPPRIMER UNE PERSONNE A LA LISTE
    def addPersonne(self):
        pass
    
    #ICI NOUS AVONS LA METHODES POUR OBTENIR UNE PERSONNE DE LA LISTE
    def addPersonne(self):
        pass

    #ICI NOUS AVONS UNE METHODES POUR COMPTER LE NOMBRE DE PERSONNE CREER
    def incrementerNombreDePersonne(cls):
        Personne.nombreDePersonne = Personne.nombreDePersonne+1
        return Personne.nombreDePersonne
    incrementerNombreDePersonne = classmethod(incrementerNombreDePersonne)
