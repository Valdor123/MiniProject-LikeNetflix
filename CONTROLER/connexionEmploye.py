#condinf:utf-8
from MODEL.Employe import Employe

def connexionUtilisateur(code, motDePasse):
    
    try:
        return Employe.connexion(code, motDePasse)
    except:
        return "Une ERREUR est survenue! Connexion impossible"