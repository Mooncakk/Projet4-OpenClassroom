import json
import os
from utills import *
from gestion_joueurs_et_tournois import *
from algorithm import ExecutionAlgorithm

class AjoutJoueurs():

  filename = 'Joueurs.json'

  def __init__(self):

    print(f"\nAjout d'un nouveau joueur\n")

    self.liste_de_joueurs = []
    path_file = f'./{self.filename}'
    path = os.path.exists(path_file)
    if path == False:
      GestionFichierJson().ecriture_du_fichier(self.liste_de_joueurs, self.filename, 4)
    else:
      pass

  def infos_joueur(self):
  
    self.nom = input(f'Nom de famille :\n - ')
    self.prenom =  input(f'Prénom :\n - ')
    self.date_de_naissance = input(f'Date de naissance (jj/mm/aaaa) :\n - ')
    self.sexe = input(f'Sexe (M ou F) :\n - ')
    self.classement = float(input(f'Votre classement :\n - ')) 
    self.infos_joueurs = {'Nom de famille' : self.nom,
                     'Prénom' : self.prenom,
                     'Date de naissance' : self.date_de_naissance,
                     'Sexe' : self.sexe,
                     'Classement' : self.classement}
    self.temp = GestionFichierJson().lecture_du_fichier(self.filename)
    id_joueur = len(self.temp) + 1
    id_infos  = {id_joueur : self.infos_joueurs}
    self.temp.append(id_infos)
    GestionFichierJson().ecriture_du_fichier(self.temp, self.filename, 4)

    print(f'\nJoueur ajouté avec succès !\n')

class AjJ(AjoutJoueurs):
  def __init__(self):
    super().__init__()
    super().infos_joueur()
    RetourMenuJoueur().retour1()

class AjT(AjoutJoueurs):
  def __init__(self):
    super().__init__()
    super().infos_joueur()
    RetourMenuJoueur().retour2()


class RetourMenu():
  def __init__(self):
    Menu().selection_menu()

class RetourMenuJoueur():
  def retour1(self):
    rep = input(f'(1) Ajouter un nouveau joueur\n(2) Retourner au menu\n -')
    if rep == '1':
      AjoutJoueurs().infos_joueur()
    elif rep =='2':
      RetourMenu()
  
  def retour2(self):
    rep = input(f'(1) Ajouter un nouveau joueur\n(2) Sélectionner un joueur\n(3) Appuyez sur entrer pour avancer\n -')
    if rep == '1':
      AjoutJoueurs().infos_joueur()
    elif rep =='2':
      pass
    elif rep =='':
      pass


class AjoutTournoi():
  
  filename = 'Tournois.json'

  def __init__(self):

    self.liste_des_tournois = []
    path_file = f'./{self.filename}'
    path = os.path.exists(path_file)
    if path == False:
      GestionFichierJson().ecriture_du_fichier(self.liste_des_tournois, self.filename, 4)
    else:
      pass

  def infos_tournoi(self):

    print(f"\nAjout d'un nouveau tournoi\n")
    
    self.nom_tournoi = input(f'Nom du tournoi : \n - ')
    self.lieu = input(f'Lieu du tournoi : \n - ')
    self.date = input(f'Date :\n - ')
    self.nombre_de_tours = 4
    self.tournees = input(f'Tournées :\n - ')
    self.joueur = input(f' (1) - Sélectionner un joueur - \n (2) - Ajouter un joueur\n - ')
    if self.joueur == '1':
      pass
    elif self.joueur == '2':
      AjT()
    self.temps = input(f'Contrôle du temps :\n (1) Bullet\n (2) Blitz\n (3) Coup rapide\n - ')
    if self.temps == '1':
      self.temps = 'Bullet'
    elif self.temps == '2':
      self.temps = 'Blitz'
    elif self.temps == '3':
      self.temps = 'Coup rapide'

    self.description = input(f'Description :\n')
    infos_tournoi = {'Nom du tournoi' : self.nom_tournoi,
                     'Lieu' : self.lieu,
                     'Date' : self.date,
                     'Nombre de tours' : self.nombre_de_tours,
                     'Tournées': int(self.tournees),
                     'Joueurs' : int(self.joueur),
                     'Temps' : self.temps,
                     'Description' : self.description}

    print(f"\nAjout d'un nouveau tournoi\n")

    self.temp = GestionFichierJson().lecture_du_fichier(self.filename)
    self.temp.append(infos_tournoi)
    GestionFichierJson().ecriture_du_fichier(self.temp, self.filename, 4)
    print(f'Tournoi {self.nom_tournoi} ajouté avec succès !')

    RetourMenuTournoi()

class RetourMenuTournoi():

  def __init__(self):
    rep = input(f'(1) Ajouter un nouveau tournoi\n(2) Retourner au menu\n -')
    if rep == '1':
      AjoutTournoi().infos_tournoi()
    elif rep =='2':
      RetourMenu()
    
class Menu():

 def selection_menu(self):
    self.menu = input(f'Tapez le chiffre du menu souhaité : \n (1) Ajouter joueurs\n (2) Ajouter tournoi\n (3) Afficher la liste des joueurs\n (4) Afficher la liste des tournois\n (5) Commencer le tournoi\n (6) Quitter\n - ')
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
