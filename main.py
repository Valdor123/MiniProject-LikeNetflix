#conding:utf-8
import tkinter
from MODEL.Personne import Personne
from MODEL.Acteur import Acteur
from MODEL.Categorie import Categorie
from MODEL.Client import Client
from MODEL.Employe import Employe
from MODEL.Film import Film
from VIEW.FenetreDeConnexion import FenetreDeConnexion

e = Employe('N', 'P', 'S', '23-2321-13', '78', '12345678', 'TOTAL')
Employe.addEmploye("78", e)
# print(type(Employe.obtenirEmploye("78")))
print(type(Employe.listeEmloye.get('78')))
# print(Employe.listeEmloye['78'])
print(e.passWord)
f = tkinter.Tk()
c2 = Client("Teuky", "TghtgR", "Masculin", "12-12-2233", "teuky1@gmail.com", "12345678")
c3 = Client("Teuky", "TKr33R", "Masculin", "12-12-2233", "teuky2@gmail.com", "12345678")
c4 = Client("Teuky", "TK11R", "Masculin", "12-12-2233", "teuky3@gmail.com", "12345678")
fil = Film("L'atke", "2h50min", "Un film de minset positif qui parle d'amour, d'intelligence, de business et de croissance financiere", {"1":Categorie("Culturiste", "Des emotions forte, remplis de plein de choses"), "2":Categorie("Culturiste2", "Des emostions forte, remplis de plein de choses")}, {"Bily Rodrigues", "Amanda Karter", "Jason Smith", "Santana Martines"} )
Film.addFilm("L'atke", fil)

print(len(Client.listeClient))
print( Client
      .listeDeTousLesClients())
FenetreDeConnexion.ouvrirFenetre(600, 600, "CONNEXION A L'APPLICATION",f)
FenetreDeConnexion.creerWidgetConnexion("CONNEXION")
f.mainloop()