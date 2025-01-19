#coding:utf-8
import tkinter
from tkinter import messagebox
from MODEL.Client import Client


class FenetreModifierClient:
    fenetre = None
    racine = None
    titreFenetre = None
    nomClient = None
    prenomClient = None
    sexeClient = None
    dateInscriptionClient = None
    courrielClient = None
    passWordClient = None
    btnEnregistre = None
    varAjouterClientALaListe = None
    clientAModifier = None

    def __init__(self):
        pass
    
    # CETTE FONCTION VA PERMETTRE D'OUVRIR LA FENETRE DE CONNEXION
    def _ouvrirFenetre(hauteur, largeur, titre, racinee):
        FenetreModifierClient.initialiserFenetre(racinee, largeur, hauteur)
        racinee.title(titre)
        racinee.minsize(500,500)
        racinee.maxsize(1000,800) 

        # ON DEFINIT LA TAILLE DE L'ECRAN
        largeurFenetre = largeur
        hauteurFenetre = hauteur
        #ON CALCULE LA POSITION DE L'ECRAN
        #1. on recupere les caracteristiques de l'ecran
        largeurEcran = int(racinee.winfo_screenwidth())
        hauteurEcran = int(racinee.winfo_screenheight())
        #2. ON CALCULE LA POSITION DE NOTRE FENETRE
        #POSITION EN ABSCISSE
        position_x = (largeurEcran // 2) - (largeurFenetre // 2)
        #POSITION EN ORDONNE
        position_y = (hauteurEcran // 2) - (hauteurFenetre // 2)
        #ON DEFINIT LES COORDONNES
        positionnement = "{}x{}+{}+{}".format(largeurFenetre, hauteurFenetre, position_x, position_y)
        racinee.geometry(positionnement)
        # CREATION DES ELEMENTS GRAPHIQUES A AFFICHER
        # FenetreModifierClient.codeUtilisateur.trace( "w", FenetreModifierClient.saveCode(FenetreModifierClient.codeUtilisateur.get() ) )
        # FenetreModifierClient.motDePasseUtilisateur.trace( "w",  FenetreModifierClient.saveMP( FenetreModifierClient.motDePasseUtilisateur.get() ) )
        FenetreModifierClient.fenetre.pack()
    ouvrirFenetre = staticmethod(_ouvrirFenetre)

    # CETTE FONTION CREER LES ELEMENTS GRAPHIQUES POUR SAISIR LES COORDONNEES UTILISATEUR
    def _creerWidgetModifierCilent(titre):
        titreFenetreZ = tkinter.Label(FenetreModifierClient.fenetre, text=titre, textvariable=FenetreModifierClient.titreFenetre)
        titreFenetreZ.pack()
        
        nomClientLabel = tkinter.Label(FenetreModifierClient.fenetre, text="Nom du client")
        nomClientLabel.pack()
        FenetreModifierClient.nomClient = tkinter.Entry(FenetreModifierClient.fenetre)
        FenetreModifierClient.nomClient.insert(0, FenetreModifierClient.clientAModifier.nom)
        FenetreModifierClient.nomClient.pack()
        
        prenomClientLabel = tkinter.Label(FenetreModifierClient.fenetre, text="Prenom du client")
        prenomClientLabel.pack()
        FenetreModifierClient.prenomClient = tkinter.Entry(FenetreModifierClient.fenetre)
        FenetreModifierClient.prenomClient.insert(0, FenetreModifierClient.clientAModifier.prenom)
        FenetreModifierClient.prenomClient.pack()

        sexeClientLabel = tkinter.Label(FenetreModifierClient.fenetre, text="Sexe du client")
        sexeClientLabel.pack()
        FenetreModifierClient.sexeClient = tkinter.Entry(FenetreModifierClient.fenetre)
        FenetreModifierClient.sexeClient.insert(0, FenetreModifierClient.clientAModifier.sexe)
        FenetreModifierClient.sexeClient.pack()

        dateDinscriptionClientLabel = tkinter.Label(FenetreModifierClient.fenetre, text="Date d'inscription du client")
        dateDinscriptionClientLabel.pack()
        FenetreModifierClient.dateInscriptionClient = tkinter.Entry(FenetreModifierClient.fenetre)
        FenetreModifierClient.dateInscriptionClient.insert(0, FenetreModifierClient.clientAModifier.dateDinscription)
        FenetreModifierClient.dateInscriptionClient.pack()

        courrielClientLabel = tkinter.Label(FenetreModifierClient.fenetre, text="Courriel du client")
        courrielClientLabel.pack()
        FenetreModifierClient.courrielClient = tkinter.Entry(FenetreModifierClient.fenetre)
        FenetreModifierClient.courrielClient.insert(0, FenetreModifierClient.clientAModifier.courriel)
        FenetreModifierClient.courrielClient.pack()

        motDePasseClientLabel = tkinter.Label(FenetreModifierClient.fenetre, text="Mot de passe du client")
        motDePasseClientLabel.pack()
        FenetreModifierClient.passWordClient = tkinter.Entry(FenetreModifierClient.fenetre, show="*")
        FenetreModifierClient.passWordClient.pack()

        FenetreModifierClient.btnEnregistre = tkinter.Button(FenetreModifierClient.fenetre, text="Enregistré", command=FenetreModifierClient.modifier)
        FenetreModifierClient.btnEnregistre.pack()

    creerWidgetModifierCilent = staticmethod(_creerWidgetModifierCilent) 


    # fonction pour fermer la fenetre
    def _fermerFenetre():
        FenetreModifierClient.fenetre.destroy()
    fermerFenetre = staticmethod(_fermerFenetre)

    # ON INITIALISE LA FENETRE
    def _initialiserFenetre(elt, l, h):
        FenetreModifierClient.racine = elt
        FenetreModifierClient.fenetre = tkinter.Frame(elt, width=l, height=h)
    initialiserFenetre = staticmethod(_initialiserFenetre)
    def _modifier():
        id = FenetreModifierClient.courrielClient.get()
        nom = FenetreModifierClient.nomClient.get()
        prenom = FenetreModifierClient.prenomClient.get()
        sexe = FenetreModifierClient.sexeClient.get()
        dateInscription = FenetreModifierClient.dateInscriptionClient.get()
        courriel = FenetreModifierClient.courrielClient.get()
        motDePaase = FenetreModifierClient.passWordClient.get()
        Client.supprimerClient(FenetreModifierClient.clientAModifier.courriel)
        client = Client(nom, prenom, sexe, dateInscription, courriel, motDePaase)
        FenetreModifierClient.ajouterClientALaListe()
        messagebox.showinfo("INFO", "Modifier Avec avec succes")
    modifier = staticmethod(_modifier)

    def afficherFenetre():
        FenetreModifierClient.racine.mainloop()
    
    def _initialiserAjouterClientALaListe(functi, selection):
        FenetreModifierClient.varModifierClientDeLaListe = functi
        FenetreModifierClient.clientAModifier = selection
    initialiserModifierClientALaListe = staticmethod(_initialiserAjouterClientALaListe)
    
    def _ajouterClientALaListe():
        return FenetreModifierClient.varModifierClientDeLaListe()
    ajouterClientALaListe = staticmethod(_ajouterClientALaListe)