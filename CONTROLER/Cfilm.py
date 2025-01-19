#coding: utf-8

#CETTE FONCTION PREND EN  ENTREE UN TREEVIEW ET UN DICTIONNAIRE
#ELLE CLASSE LES ELEMENT DU DICTIONNAIR DANS LE TABLEAU
def listeFilm(tabl1, tabl2):
    i = 0
    for elt in tabl2:
        #on recupre les donnees a afficher
        nomFilm = tabl2.get(elt).nom
        dureeFilm = tabl2.get(elt).duree
        categoriesFilm = tabl2.get(elt).getListeCategorie
        infos = (nomFilm, dureeFilm, categoriesFilm)

        # ON INSERT DANS LE TABLEAU
        tabl1.insert(parent = "", index = i, values = infos)
        i = i+1
