import json
import os

import algorithm
import chess_program
import gestion_joueurs_et_tournois


class Menu():
  '''Menu du programme'''

  def selection_menu(self):

    self.repeat = 0
    while self.repeat == 0:
      self.menu = input('\nTapez le chiffre du menu souhaité : \n\n (1) Ajouter joueurs\n (2) Ajouter tournoi\n (3) Afficher la liste des joueurs\n (4) Afficher la liste des tournois\n (5) Commencer le tournoi\n (6) Quitter\n\n - ')
      if self.menu == '1':
        gestion_joueurs_et_tournois.AjJ()
      elif self.menu == '2':
        gestion_joueurs_et_tournois.AjoutTournoi().infos_tournoi()
      elif self.menu == '3':
        gestion_joueurs_et_tournois.ListeJoueurs()      
      elif self.menu == '4':
        gestion_joueurs_et_tournois.ListeTournoi().afficher_tournoi()
      elif self.menu == '5':
        path = os.path.exists('./Tournois.json')
        if path == True:
          algorithm.ExecutionAlgorithm()
        else :
          print('\nAucun tournoi trouvé\n')
          self.repeat = 0
      elif self.menu == '6':
        return
      else :
        print('\nERREUR! Veuillez taper un chiffre correspondant à un menu\n')
        self.repeat = 0


if __name__ == '__main__':
  Menu().selection_menu()
  



