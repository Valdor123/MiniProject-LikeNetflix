#conding:utf-8
import tkinter
from tkinter import ttk
from tkinter import messagebox
from CONTROLER.Cfilm import listeFilm
from CONTROLER.client import  listeClient, supprimerClient
from MODEL.Film import Film
from MODEL.Client import Client
from VIEW.FenetreCreerClient import FenetreCreerClient
from VIEW.FenetreModifierClient import FenetreModifierClient

class FenetrePrincipale:
    fenetreP = tkinter.Frame()
    fenetreP2 = tkinter.Frame()
    fenetreboutonP = tkinter.Frame()
    tableListeFilm = ttk.Treeview()
    tableauListeClient = ttk.Treeview()
    btnSupprimerP = tkinter.Button()
    btnModifierP = tkinter.Button()
    btnAjouterP = tkinter.Button()
    
    racine = None
    def __init__(self):
        pass
    
    # FONCTION POUR DEMARRER LA FENETRE
    def _ouvrirFenetreP(hauteur, largeur, titre, racinee):
        FenetrePrincipale.initialiserFenetre(racinee, largeur, hauteur)
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
        
        FenetrePrincipale.fenetreP.pack(side="top", fill="x")
        FenetrePrincipale.fenetreBoutonP.pack(side="top", fill="x")
        FenetrePrincipale.fenetreP2.pack(side="bottom", fill="x")

    ouvrirFenetreP = staticmethod(_ouvrirFenetreP)
    
    # CETTE FONTION CREER LES ELEMENTS GRAPHIQUES POUR SAISIR LES COORDONNEES UTILISATEUR
    def _creerWidgetConnexion(titre):
        LC = tkinter.Label(FenetrePrincipale.racine)
        FenetrePrincipale.tableauListeClient = ttk.Treeview(FenetrePrincipale.fenetreP, columns=['col1', 'col2', 'col3'], show='headings')
        FenetrePrincipale.tableauListeClient.heading('col1', text='NOM')
        FenetrePrincipale.tableauListeClient.heading('col2', text='PRENOM')
        FenetrePrincipale.tableauListeClient.heading('col3', text='EMAIL')
        FenetrePrincipale.listeClient()
        FenetrePrincipale.tableauListeClient.pack(fill="both", expand=True)
        
        FenetrePrincipale.tableauListeFilm = ttk.Treeview(FenetrePrincipale.fenetreP2, columns=['col1', 'col2', 'col3'], show='headings')
        FenetrePrincipale.tableauListeFilm.heading('col1', text='TITRE')
        FenetrePrincipale.tableauListeFilm.heading('col2', text='DUREE')
        FenetrePrincipale.tableauListeFilm.heading('col3', text='CATEGORIE')
        FenetrePrincipale.tableauListeFilm.pack(fill="both", expand=True)
        FenetrePrincipale.listeFilm()
        FenetrePrincipale.btnSupprimerP = tkinter.Button(FenetrePrincipale.fenetreBoutonP, text= "Supprimer", command=FenetrePrincipale.supprimerClientDeListe)
        FenetrePrincipale.btnSupprimerP.pack(side='left', padx=10)
        FenetrePrincipale.btnModifierP = tkinter.Button(FenetrePrincipale.fenetreBoutonP, text= "Modifier", command=FenetrePrincipale.modifierClientSelectionne)
        FenetrePrincipale.btnModifierP.pack(side='left', padx=10)
        FenetrePrincipale.btnAjouterP = tkinter.Button(FenetrePrincipale.fenetreBoutonP, text= "Ajouter", command=FenetrePrincipale.ouvrirCreeClient)
        FenetrePrincipale.btnAjouterP.pack(side='left', padx=10)

    creerWidgetConnexion = staticmethod(_creerWidgetConnexion) 

    # ON INITIALISE LA FENETRE
    def _initialiserFenetre(elt, l, h):
        FenetrePrincipale.racine = elt
        FenetrePrincipale.fenetreP = tkinter.Frame(elt)
        FenetrePrincipale.fenetreBoutonP = tkinter.Frame(elt)
        FenetrePrincipale.fenetreP2 = tkinter.Frame(elt)
        FenetrePrincipale.fenetreBoutonP1 = tkinter.Frame(elt)
    initialiserFenetre = staticmethod(_initialiserFenetre)
    
    def _ouvrirCreeClient():
        FenetreCreerClient.ouvrirFenetre(600, 500, "AJOUTER UN CLIEN", tkinter.Tk())
        FenetreCreerClient.creerWidgetModifierCilent("Ajouter un client")
        FenetreCreerClient.initialiserAjouterClientALaListe(FenetrePrincipale.ajouterClient)
    ouvrirCreeClient = staticmethod(_ouvrirCreeClient)
    
    def _supprimerClientDeListe():
        # ICI ON VA FAIRE UNE BOUCLE POUR PERMETTRE LA SUPPRESSION D'UNE SELECTION EGALEMENT
        elts = FenetrePrincipale.tableauListeClient.selection()
        for elt in FenetrePrincipale.tableauListeClient.selection():
            supprimerClient(FenetrePrincipale.tableauListeClient.item(elt)["values"][2])
            FenetrePrincipale.tableauListeClient.delete(elt)
            print(len(Client.listeClient))
    supprimerClientDeListe =  staticmethod(_supprimerClientDeListe)
    #Fonction pour fermer la fenetre
    def _fermerFenetre():
        FenetrePrincipale.fenetreP.destroy()
        FenetrePrincipale.fenetreP2.destroy()
        FenetrePrincipale.fenetreBoutonP.destroy()
    fermerFenetre = staticmethod(_fermerFenetre)

    def _modifierClientSelectionne():
        if FenetrePrincipale.initialiserModifierClientALaListe() :
            FenetreModifierClient.ouvrirFenetre(600, 500, "MODIFIER UN CLIEN", tkinter.Tk())
            FenetreModifierClient.creerWidgetModifierCilent("Modifier un client")
        
    modifierClientSelectionne =  staticmethod(_modifierClientSelectionne)

    def _ajouterClient(id, client):
        try:
            Client.addClient(id, client)
            nomClient = client.nom
            prenomClient = client.prenom
            courriellient = client.courriel
            infos = (nomClient, prenomClient, courriellient)
            # ON INSERT DANS LE TABLEAU
            FenetrePrincipale.tableauListeClient.insert(parent = "", index = 0 , values = infos)
            return True
        except:
            return False
    ajouterClient = staticmethod(_ajouterClient)

    def _listeClient():
        listeClient(FenetrePrincipale.tableauListeClient, Client.listeClient)
    listeClient = staticmethod(_listeClient)
    
    def _listeFilm():
        listeFilm(FenetrePrincipale.tableauListeFilm, Film.listeFilme)
    listeFilm = staticmethod(_listeFilm)

    def _initialiserModifierClientALaListe():
        if len(FenetrePrincipale.tableauListeClient.selection()) > 0 and len(FenetrePrincipale.tableauListeClient.selection()) <= 1:
            cli = Client.obtenirClient(FenetrePrincipale.tableauListeClient.item(FenetrePrincipale.tableauListeClient.selection())["values"][2])
            FenetreModifierClient.initialiserModifierClientALaListe(FenetrePrincipale.listeClient, cli)
            return True
        else:
            messagebox.showerror("ERREUR", "Selection un element pour le modifier")
            return False
    initialiserModifierClientALaListe = staticmethod(_initialiserModifierClientALaListe)