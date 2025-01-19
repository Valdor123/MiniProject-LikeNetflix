#coding:utf-8
import tkinter
from tkinter import messagebox
from CONTROLER.connexionEmploye import connexionUtilisateur
from MODEL.Employe import Employe
from VIEW.FenetrePrincipale import FenetrePrincipale


class FenetreDeConnexion:
    fenetre = None
    racine = None
    titreFenetre = tkinter.StringVar()
    titreFenetre.set("CONNEXION....")
    codeUtilisateur = None
    C = '222'
    MP = '333'
    motDePasseUtilisateur = None
    def __init__(self):
        pass
    
    # CETTE FONCTION VA PERMETTRE D'OUVRIR LA FENETRE DE CONNEXION
    def _ouvrirFenetre(hauteur, largeur, titre, racinee):
        FenetreDeConnexion.initialiserFenetre(racinee, largeur, hauteur)
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
        # FenetreDeConnexion.codeUtilisateur.trace( "w", FenetreDeConnexion.saveCode(FenetreDeConnexion.codeUtilisateur.get() ) )
        # FenetreDeConnexion.motDePasseUtilisateur.trace( "w",  FenetreDeConnexion.saveMP( FenetreDeConnexion.motDePasseUtilisateur.get() ) )
        FenetreDeConnexion.fenetre.pack()
    ouvrirFenetre = staticmethod(_ouvrirFenetre)

    # CETTE FONTION CREER LES ELEMENTS GRAPHIQUES POUR SAISIR LES COORDONNEES UTILISATEUR
    def _creerWidgetConnexion(titre):
        titreFenetreZ = tkinter.Label(FenetreDeConnexion.fenetre, text=titre, textvariable=FenetreDeConnexion.titreFenetre)
        titreFenetreZ.pack()
        FenetreDeConnexion.codeUtilisateur = tkinter.Entry(FenetreDeConnexion.fenetre)
        FenetreDeConnexion.codeUtilisateur.pack()
        FenetreDeConnexion.motDePasseUtilisateur = tkinter.Entry(FenetreDeConnexion.fenetre, show="*")
        FenetreDeConnexion.motDePasseUtilisateur.pack()
        btnConnexionZ = tkinter.Button(FenetreDeConnexion.fenetre, text="Se connecter", command=FenetreDeConnexion.conexion)
        btnConnexionZ.pack()
    creerWidgetConnexion = staticmethod(_creerWidgetConnexion) 

    def _conexion():
        resultatConnexion = connexionUtilisateur(FenetreDeConnexion.codeUtilisateur.get(), FenetreDeConnexion.motDePasseUtilisateur.get())
        if( type(resultatConnexion) == Employe):
            FenetreDeConnexion.fermerFenetre()
            FenetrePrincipale.ouvrirFenetreP(600, 500, "STREAMING MOV", FenetreDeConnexion.racine)
            FenetrePrincipale.creerWidgetConnexion("STREAM MOVIS")
        elif (type(resultatConnexion) == str):
            messagebox.showinfo("Connexion...", "{}".format(resultatConnexion))
    
    conexion = staticmethod(_conexion)

    # fonction pour fermer la fenetre
    def _fermerFenetre():
        FenetreDeConnexion.fenetre.destroy()
    fermerFenetre = staticmethod(_fermerFenetre)

    # ON INITIALISE LA FENETRE
    def _initialiserFenetre(elt, l, h):
        FenetreDeConnexion.racine = elt
        FenetreDeConnexion.fenetre = tkinter.Frame(elt, width=l, height=h)
    initialiserFenetre = staticmethod(_initialiserFenetre)

    def _saveCode(v):
        FenetreDeConnexion.c = v
    saveCode =staticmethod(_saveCode)

    def _saveMP(v):
        FenetreDeConnexion.MP = v
    saveMP = staticmethod(_saveMP)