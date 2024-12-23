#coding: UTF-8
import hashlib
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
        return Employe.listeEmloye[id]
    obtenirEmploye = staticmethod(_obtenirEmploye)

    #SUPPRIMER UN EMPLOYE
    def _supprimerEmploye(id):
        Employe.listeEmloye.pop(id)
    supprimerEmploye = staticmethod(_supprimerEmploye)

    #LA METHODFE POUR SE CONNECTER: CETTE METHODE EST STATIC:
    """
        CETTE METHODE CONTROLE SI LE CDE EST PRESENT DANS LA LISTE ET E SUITE SI LE MOT DE PASSE CORRESPON A LA VALEUR HASHER
        SI TOUT EST CORECT ELLE RETOURNE L'OBJET (L'EMPLOYE QUI SE CONNECTE) SI NON ELLE RETOURNE DES PHRASESS PRECISES
    """
    def _connexion(id, mo):
        #ON VERIFI SI L'EMPLOYER EXISTE DANS LA LISTE
        exite = False
        for elt in Employe.listeEmloye:
            try:
                if(Employe.listeEmloye[elt].codeUtilisateur ==  Employe.listeEmloye[id].codeUtilisateur):
                    #ON HASH LE MOT DE PASS ENTRER
                    hash = hashlib.new('sha512_256')
                    hash.update(mo.encode(encoding="utf-8"))
                    motDePasseHasher = hash.hexdigest()
                    if( Employe.listeEmloye[elt].passWord == motDePasseHasher):
                        return Employe.listeEmloye[elt]
                    else:
                        return "Mot de passe incorrect"
                else:
                    return "Ce code utilisateur n'est pas reconnu"
            except:
                    return "Ce code utilisateur n'est pas reconnu"
    connexion = staticmethod(_connexion)


class Client(Personne):
    nombreDeClient = 0
    listeClient = {}
    def __init__(self, nom, prenom, sexe, dateDinscription, courriel, password):
        Personne.__init__(self, nom, prenom, sexe)
        self._dateDinscription = dateDinscription
        self._courriel = ""
        self.courriel = courriel
        self._password = password
        #ON AJOUTE LE CLIENT CREE A LA LISTE DES CLIENTS
        Client.addClient(self._identifiant, self)

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
    
    #L'ACCESSEUR DE L'ATTRIBUT _password
    passWord = property(_getPassword, _setPassword)

    #ICI NOUS AVONS UNE METHODES POUR COMPTER LE NOMBRE DE PERSONNE CREER
    def incrementerNombreDeClient(cls):
        Client.nombreDeClient = Client.nombreDeClient+1
        return Client.nombreDeClient
    incrementerNombreDeClient = classmethod(incrementerNombreDeClient)

    
    #AJOUT D'UN CLIENT DANS LA LISTE
    """
    ``CETTE METHODE VA REOURNE VRAI SI LE CLIENT A ETE AJOUTER A LA LISTE
    ``SI NON SA VA SE REEXECUTER
    """
    def _addClient(id, val):
        Client.listeClient[id] = val
        if(Client.listeClient[id].identifiant == id):
            return True
        else:
            Client.addClient(id, val)
            return False
    addClient = staticmethod(_addClient)

    #OBTENIR UN CLIENT 
    def _obtenirClient(id):
        return Client.listeClient[id]
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

    #LISTE DE TOUS LES CLIENTS
    def _listeDeTousLesClients():
        listeC = ""
        for elt in Client.listeClient:
            listeC = listeC + "\n" + str(Client.listeClient[elt].nom)
        return listeC
    listeDeTousLesClients = staticmethod(_listeDeTousLesClients)
    
    supprimerClient = staticmethod(_supprimerClient)


class Acteur(Personne):
    nombreDeActeur = 0
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
