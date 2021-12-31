import json
from modules import GestionFichierJson as GJ

class EditData():
  '''Supprimer un joueur présent dans la liste des joueurs '''
  def supprimer_joueurs(self):
    self.listejoueurs = GJ().lecture_du_fichier('Joueurs.json')
    self.nb_joueurs = len(self.listejoueurs)
    self.id_joueur = 0
    if self.nb_joueurs > 0:
      while self.id_joueur > self.nb_joueurs or self.id_joueur == 0 :
        self.id_joueur = input('Quel joueur souhaitez-vous supprimer ?\n - ')
        try :
          self.id_joueur = int(self.id_joueur)
        except:
          print("\nERREUR !!! Veuillez rentrer un chiffre correspondant à l'ID d'un joueur.\n")
          self.id_joueur = 0
        else:
          if self.id_joueur > self.nb_joueurs or self.id_joueur == 0 :
            print("\nID de joueur inexistant !\nVeuillez taper l'ID d'un joueur existant !\n")
          elif self.id_joueur > 0 and self.id_joueur <= self.nb_joueurs :
            self.listejoueurs.pop(self.id_joueur-1)
            GJ().ecriture_du_fichier(self.listejoueurs, 'test.json', 4)
            print(f'Le joueur {self.id_joueur} à été supprimé !')

    RetourMenuJoueur().retour3()

EditData().supprimer_joueurs()