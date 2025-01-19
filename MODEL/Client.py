#coding: utf-8
from MODEL.Personne import Personne
import hashlib
class Client(Personne):
    nombreDeClient = 0
    listeClient = {}
    def __init__(self, nom, prenom, sexe, dateDinscription, courriel, password):
        Personne.__init__(self, nom, prenom, sexe)
        self._dateDinscription = dateDinscription
        # LE COURRIEL EST L'IDENTIFIIANT D'UN CLIENT
        self._courriel = courriel
        self.courriel = courriel
        self._passWord = ""
        #ICI ON UTILISE LA METHODE la propriete passWord POUR DEFINIR COORECTEMENT LE MOTE DE PASSE
        self.passWord = password
        #ON AJOUTE LE CLIENT CREE A LA LISTE DES CLIENTS
        Client.addClient(courriel, self)

    #L'ENCAPSULATION DE L'ATTRIBUT _dateDinscription
    #LA FONCTION POUR RETOURNER _dateDinscription
    def _getDateDinscription(self):
        return self._dateDinscription
    
    #LA FONCTION POUR DEFINIR _dateDinscription
    def _setDateDinscription(self ,nouveau):
        self._dateDinscription = nouveau
    
    #L'ACCESSEUR DE L'ATTRIBUT _dateDinscription
    dateDinscription = property(_getDateDinscription, _setDateDinscription)


    #L'ENCAPSULATION DE L'ATTRIBUT _courriel
    #LA FONCTION POUR RETOURNER _courriel
    def _getCourriel(self):
        return self._courriel
    
    #LA FONCTION POUR DEFINIR _courriel
    """
    ``ON DOIT S'ASSURER QU LE COURREIL ENTRER EST UNIQUE
    SI LE COURIEL EXISTE ON LEVE UN EXECPTION
    SI NON ON ENREGISTRE NORMALEMENT
    """
    def _setCourriel(self ,nouveau):
        for elt in Client.listeClient:
            if(Client.listeClient[elt].courriel == nouveau):
                raise ValueError("CE COURRIEL EXISTE DEJA")
            else:
                self._courriel = nouveau
    
    #L'ACCESSEUR DE L'ATTRIBUT _courriel
    courriel = property(_getCourriel, _setCourriel)


    #L'ENCAPSULATION DE L'ATTRIBUT _password
    #LA FONCTION POUR RETOURNER _password
    def _getPassWord(self):
        return self._password
    
    #LA FONCTION POUR DEFINIR _password
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
    

    #ICI NOUS AVONS UNE METHODES POUR COMPTER LE NOMBRE DE PERSONNE CREER
    def incrementerNombreDeClient(cls):
        Client.nombreDeClient = Client.nombreDeClient+1
        return Client.nombreDeClient
    incrementerNombreDeClient = classmethod(incrementerNombreDeClient)

    
    #AJOUT D'UN CLIENT DANS LA LISTE 
    def _addClient(id, val):
        Client.listeClient[id] = val
    addClient = staticmethod(_addClient)

    #OBTENIR UN CLIENT 
    def _obtenirClient(id):
        try:
            return Client.listeClient.get(id)
        except:
            return "CE CODE N'EXISTE PAS"
    obtenirClient = staticmethod(_obtenirClient)

    #SUPPRIMER UN CLIENT
    """
    ``CETTE METHORE VA RETOURNE LE NOM LE CLEIT SUPPRIMER POUR CONFIRMER LA SUPPRESSION
    """
    def _supprimerClient(id):
        return Client.listeClient.pop(id)
    supprimerClient = staticmethod(_supprimerClient)
    

    def modifierCLient(self, nom, prenom, sexe, dateDinscription, courriel, password):
        # ON MODIFIE LES VALEURS DES SES DIFFERENTS ATTRIBUT
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.dateDinscription = dateDinscription
        self.courriel = courriel
        self.passWord = password
        #ON MET A JOUR CA VALEUR DANS LA LISTE
        Client.listeClient[courriel] = self

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
            return  True
        else:
            # raise ValueError("Nombre de caractere insuffusant")
            return False
    passWord = property(_getPassWord, _setPassWord)

    #LISTE DE TOUS LES CLIENTS
    def _listeDeTousLesClients():
        listeC = ""
        for elt in Client.listeClient:
            listeC = listeC + "\n" + str(Client.listeClient[elt].nom)
            listeC = listeC + "\n" + str(Client.listeClient[elt].courriel)
            listeC = listeC + "\n" + str(Client.listeClient[elt].passWord)
            listeC = listeC + "\n\n ==============================="
        return listeC
    listeDeTousLesClients = staticmethod(_listeDeTousLesClients)
    