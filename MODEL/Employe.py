#coding: utf-8
import hashlib
from MODEL.Personne import Personne

class Employe(Personne):
    listeEmloye = {}
    def __init__(self, nom, prenom, sexe, dateDambauche, codeUtilisateur, passWord, typeDacces):
        Personne.__init__(self, nom, prenom, sexe)
        self._dateDambauche = dateDambauche
        self._codeUtilisateur = codeUtilisateur
        self._passWord = ""
        #ICI ON UTILISE LA METHODE la propriete passWord POUR DEFINIR COORECTEMENT LE MOTE DE PASSE
        self.passWord = passWord
        self._typeDacces = typeDacces

        #ON AJOUTE L'EMPLYER CREE A LA LISTE DE EMPLOYE
        Employe.addEmploye(codeUtilisateur, self)
        
    #ENCAPSULATION DE _dateDambauche
    def _getDateDambauche(self):
        return self._dateDambauche
    def _setDateDambauche(self ,nouveau):
        self._dateDambauche = nouveau
    dateDambauche = property(_getDateDambauche, _setDateDambauche)

    #ENCAPSULATION DE _codeUtilisateur
    def _getCodeUtilisateure(self):
        return self._codeUtilisateur
    def _setCodeUtilisateure(self ,nouveau):
        self._codeUtilisateur = nouveau
    codeUtilisateur = property(_getCodeUtilisateure, _setCodeUtilisateure)


    #ENCAPSULATION DE _passWord
    def _getPassWord(self):
        return self._password
    def _setPassWord(self ,nouveau):
        if(len(nouveau) >= 8):
            #CRYPTAGE DU MOT DE PASSE
            hash = hashlib.new('sha512_256')
            #ON ENCODE LE MOT DE PASSE
            hash.update(nouveau.encode(encoding="utf-8"))
            self._password = hash.hexdigest()
        else:
            raise ValueError("Nombre de caractere insuffusant")
    passWord = property(_getPassWord, _setPassWord)


    #ENCAPSULATION DE _typeDacces
    def _getTypeDacces(self):
        return self._typeDacces
    def _setTypeDacces(self ,nouveau):
        self._typeDacces = nouveau
    typeDacces = property(_getTypeDacces, _setTypeDacces)

    #ICI NOUS AVONS UNE METHODES POUR COMPTER LE NOMBRE DE PERSONNE CREER
    def incrementerNombreDeEmploye(cls):
        Employe.nombreDeEmploye = Employe.nombreDeEmploye+1
        return Employe.nombreDeEmploye
    incrementerNombreDeEmploye = classmethod(incrementerNombreDeEmploye)

    #AJOUT D'UN EPLOYER DANS LA LISTE
    def _addEmploye(id, val):
        Employe.listeEmloye[id] = val
    addEmploye = staticmethod(_addEmploye)

    #OBTENIR UN EMPLOYE 
    def _obtenirEmploye(id):
        try:
            return Employe.listeEmloye.get(id)
        except:
            return "CE CODE N'EXISTE PAS"
        
    obtenirEmploye = staticmethod(_obtenirEmploye)

    #SUPPRIMER UN EMPLOYE
    def _supprimerEmploye(id):
        try:
            Employe.listeEmloye.pop(id)
        except:
            return "IMPOSSIBLE DE SUPPRIMER"
    supprimerEmploye = staticmethod(_supprimerEmploye)

    #LA METHODFE POUR SE CONNECTER: CETTE METHODE EST STATIC:
    """
        CETTE METHODE CONTROLE SI LE CDE EST PRESENT DANS LA LISTE ET E SUITE SI LE MOT DE PASSE CORRESPON A LA VALEUR HASHER
        SI TOUT EST CORECT ELLE RETOURNE L'OBJET (L'EMPLOYE QUI SE CONNECTE) SI NON ELLE RETOURNE DES PHRASESS PRECISES
    """
    def _connexion(id, mo):
        #ON VERIFI SI L'EMPLOYER EXISTE DANS LA LISTE
        resultat = Employe.obtenirEmploye(id)
        if( type(resultat) == Employe):
            print('resultat')
            try:
                if(resultat.codeUtilisateur ==  Employe.listeEmloye[id].codeUtilisateur):
                    #ON HASH LE MOT DE PASS ENTRER
                    hash = hashlib.new('sha512_256')
                    hash.update(mo.encode(encoding="utf-8"))
                    motDePasseHasher = hash.hexdigest()
                    if( resultat.passWord == motDePasseHasher):
                        return resultat
                    else:
                        return "Mot de passe incorrect"
                else:
                    return "Ce code utilisateur n'est pas reconnu"
            except:
                    return "Ce code utilisateur n'est pas reconnu"
        elif (type(resultat) == str):
            print('str')
            return resultat
        print( )
        # for elt in Employe.listeEmloye:
        #     try:
        #         if(Employe.listeEmloye[elt].codeUtilisateur ==  Employe.listeEmloye[id].codeUtilisateur):
        #             #ON HASH LE MOT DE PASS ENTRER
        #             hash = hashlib.new('sha512_256')
        #             hash.update(mo.encode(encoding="utf-8"))
        #             motDePasseHasher = hash.hexdigest()
        #             if( Employe.listeEmloye[elt].passWord == motDePasseHasher):
        #                 return Employe.listeEmloye[elt]
        #             else:
        #                 return "Mot de passe incorrect"
        #         else:
        #             return "Ce code utilisateur n'est pas reconnu"
        #     except:
        #             return "Ce code utilisateur n'est pas reconnu"
    connexion = staticmethod(_connexion)

    def _AfficheEmploye():
        print(len(Employe.listeEmloye))
        for elt in Employe.listeEmloye:
            print('E:{}\n'.format(elt))
    AfficheEmploye = staticmethod(_AfficheEmploye)