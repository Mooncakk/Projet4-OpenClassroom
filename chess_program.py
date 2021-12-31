import json
import os
#from algorithm import ExecutionAlgorithm
from modules import AjoutJoueurs, AjoutTournoi, ListeJoueurs, ListeJoueursParId, ListeTournoi, EditData, ExecutionAlgorithm
#from modification_liste_joueurs import EditData
#from utills import GestionFichierJson





class RetourMenu():
  def __init__(self):
    Menu().selection_menu()

class RetourMenuJoueur():
  def retour1(self):
    rep = input('(1) Ajouter un nouveau joueur\n(2) Supprimer un joueur\n(3) Retourner au menu\n -')
    if rep == '1':
      AjoutJoueurs().infos_joueur()
    elif rep == '2':
      EditData().supprimer_joueurs
    elif rep =='3':
      RetourMenu()
  
  def retour2(self):
    rep = input(
      '(1) Ajouter un nouveau joueur\n(2) Appuyez sur entrer pour avancer\n -'
      )
    if rep == '1':
      AjoutJoueurs().infos_joueur()
    elif rep =='2':
      pass


  def retour3(self):
    rep = input(
      '(1) Ajouter un nouveau joueur\n(2) Supprimer un autre joueur\n(3) Retourner au menu\n -'
      )
    if rep == '1':
      AjoutJoueurs().infos_joueur()
    elif rep == '2':
      ListeJoueursParId().afficher_joueurs_par_id()
      EditData().supprimer_joueurs
    elif rep =='3':
      RetourMenu()
   



class RetourMenuTournoi():

  def __init__(self):
    rep = input('(1) Ajouter un nouveau tournoi\n(2) Retourner au menu\n -')
    if rep == '1':
      AjoutTournoi().infos_tournoi()
    elif rep =='2':
      RetourMenu()
    


class Menu():

 def selection_menu(self):
    self.menu = input('Tapez le chiffre du menu souhaité : \n (1) Ajouter joueurs\n (2) Ajouter tournoi\n (3) Afficher la liste des joueurs\n (4) Afficher la liste des tournois\n (5) Commencer le tournoi\n (6) Quitter\n - ')
    if self.menu == '1':
      AjJ()
    elif self.menu == '2':
      AjoutTournoi().infos_tournoi()
    elif self.menu == '3':
      ListeJoueurs().afficher_joueurs()      
    elif self.menu == '4':
      ListeTournoi().afficher_tournoi()
    elif self.menu == '5':
      path = os.path.exists('./Tournois.json')
      if path == True:
        ExecutionAlgorithm()
      else :
        print('Aucun tournoi trouvé')
    elif self.menu == '6':
      return
    else :
      print('ERREUR! Veuillez taper un chiffre correspondant à un menu')


#AjoutJoueurs().infos_joueur()
#Menu().selection_menu()

Menu().selection_menu()
#ListeJoueurs().afficher_joueurs()



#import brouill
#import afficher_liste_joueurs_et_tournois
