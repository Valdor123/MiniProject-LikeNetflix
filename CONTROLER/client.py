#coding: utf-8

from MODEL.Client import Client

#CETTE FONCTION PREND EN  ENTREE UN TREEVIEW ET UN DICTIONNAIRE
#ELLE CLASSE LES ELEMENT DU DICTIONNAIR DANS LE TABLEAU
def listeClient(tabl1, tabl2):
    viderListe(tabl1)
    i = 0
    for elt in tabl2:
        #on recupre les donnees a afficher
        nomClient = tabl2.get(elt).nom
        prenomClient = tabl2.get(elt).prenom
        courriellient = tabl2.get(elt).courriel
        infos = (nomClient, prenomClient, courriellient)

        # ON INSERT DANS LE TABLEAU
        tabl1.insert(parent = "", index = i, values = infos)
        i = i+1
def viderListe(tab1):
     tout = tab1.get_children()
     if tout != '()':
          for elt in tout:
               tab1.delete(elt)

def supprimerClient(id):
    # if type(
        Client.supprimerClient(id)
        # ) == Client:
        return True
    # else:
    #     return False