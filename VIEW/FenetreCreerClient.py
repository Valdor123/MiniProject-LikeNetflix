#coding:utf-8
import tkinter
from tkinter import messagebox
from MODEL.Client import Client


class FenetreCreerClient:
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

    def __init__(self):
        pass
    
    # CETTE FONCTION VA PERMETTRE D'OUVRIR LA FENETRE DE CONNEXION
    def _ouvrirFenetre(hauteur, largeur, titre, racinee):
        FenetreCreerClient.initialiserFenetre(racinee, largeur, hauteur)
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
        # FenetreCreerClient.codeUtilisateur.trace( "w", FenetreCreerClient.saveCode(FenetreCreerClient.codeUtilisateur.get() ) )
        # FenetreCreerClient.motDePasseUtilisateur.trace( "w",  FenetreCreerClient.saveMP( FenetreCreerClient.motDePasseUtilisateur.get() ) )
        FenetreCreerClient.fenetre.pack()
    ouvrirFenetre = staticmethod(_ouvrirFenetre)

    # CETTE FONTION CREER LES ELEMENTS GRAPHIQUES POUR SAISIR LES COORDONNEES UTILISATEUR
    def _creerWidgetModifierCilent(titre):
        titreFenetreZ = tkinter.Label(FenetreCreerClient.fenetre, text=titre, textvariable=FenetreCreerClient.titreFenetre)
        titreFenetreZ.pack()
        
        nomClientLabel = tkinter.Label(FenetreCreerClient.fenetre, text="Nom du client")
        nomClientLabel.pack()
        FenetreCreerClient.nomClient = tkinter.Entry(FenetreCreerClient.fenetre)
        FenetreCreerClient.nomClient.pack()
        
        prenomClientLabel = tkinter.Label(FenetreCreerClient.fenetre, text="Prenom du client")
        prenomClientLabel.pack()
        FenetreCreerClient.prenomClient = tkinter.Entry(FenetreCreerClient.fenetre)
        FenetreCreerClient.prenomClient.pack()

        sexeClientLabel = tkinter.Label(FenetreCreerClient.fenetre, text="Sexe du client")
        sexeClientLabel.pack()
        FenetreCreerClient.sexeClient = tkinter.Entry(FenetreCreerClient.fenetre)
        FenetreCreerClient.sexeClient.pack()

        dateDinscriptionClientLabel = tkinter.Label(FenetreCreerClient.fenetre, text="Date d'inscription du client")
        dateDinscriptionClientLabel.pack()
        FenetreCreerClient.dateInscriptionClient = tkinter.Entry(FenetreCreerClient.fenetre)
        FenetreCreerClient.dateInscriptionClient.pack()

        courrielClientLabel = tkinter.Label(FenetreCreerClient.fenetre, text="Courriel du client")
        courrielClientLabel.pack()
        FenetreCreerClient.courrielClient = tkinter.Entry(FenetreCreerClient.fenetre)
        FenetreCreerClient.courrielClient.pack()

        motDePasseClientLabel = tkinter.Label(FenetreCreerClient.fenetre, text="Mot de passe du client")
        motDePasseClientLabel.pack()
        FenetreCreerClient.passWordClient = tkinter.Entry(FenetreCreerClient.fenetre, show="*")
        FenetreCreerClient.passWordClient.pack()

        FenetreCreerClient.btnEnregistre = tkinter.Button(FenetreCreerClient.fenetre, text="Enregistré", command=FenetreCreerClient.enregistrer)
        FenetreCreerClient.btnEnregistre.pack()

    creerWidgetModifierCilent = staticmethod(_creerWidgetModifierCilent) 


    # fonction pour fermer la fenetre
    def _fermerFenetre():
        FenetreCreerClient.fenetre.destroy()
    fermerFenetre = staticmethod(_fermerFenetre)

    # ON INITIALISE LA FENETRE
    def _initialiserFenetre(elt, l, h):
        FenetreCreerClient.racine = elt
        FenetreCreerClient.fenetre = tkinter.Frame(elt, width=l, height=h)
    initialiserFenetre = staticmethod(_initialiserFenetre)
    def _enregistrer():
        id = FenetreCreerClient.courrielClient.get()
        nom = FenetreCreerClient.nomClient.get()
        prenom = FenetreCreerClient.prenomClient.get()
        sexe = FenetreCreerClient.sexeClient.get()
        dateInscription = FenetreCreerClient.dateInscriptionClient.get()
        courriel = FenetreCreerClient.courrielClient.get()
        motDePaase = FenetreCreerClient.passWordClient.get()
        client = Client(nom, prenom, sexe, dateInscription, courriel, motDePaase)
        resultat = FenetreCreerClient.ajouterClientALaListe(id, client)
        print(FenetreCreerClient.passWordClient.get())
        print(len(Client.listeClient))
        if(resultat):
            messagebox.showinfo("INFO", "Enregistrer avec succes")
        else:
            messagebox.showerror("ERREUR", "Une erreur c'est produit /n Votre mot de passe doit avoir au moins 08 caractères")
    enregistrer = staticmethod(_enregistrer)

    def afficherFenetre():
        FenetreCreerClient.racine.mainloop()
    
    def _initialiserAjouterClientALaListe(functi):
        FenetreCreerClient.varAjouterClientALaListe = functi
    initialiserAjouterClientALaListe = staticmethod(_initialiserAjouterClientALaListe)
    
    def _ajouterClientALaListe(id, client):
        return FenetreCreerClient.varAjouterClientALaListe(id, client)
    ajouterClientALaListe = staticmethod(_ajouterClientALaListe)
    