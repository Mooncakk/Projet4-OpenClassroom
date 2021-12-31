import json
import os
from itertools import count
#from modules import GestionFichierJson as GFJ, RetourMenuJoueur
import modules
'''from utills import GestionFichierJson as GFJ
from chess_program import RetourMenuJoueur'''



class AjoutJoueurs():

  filename = 'Joueurs.json'

  def __init__(self):
    '''Création du fichier JSON contenant la liste des joueurs'''

    print("\nAjout d'un nouveau joueur\n")

    self.liste_de_joueurs = []
    path_file = f'./{self.filename}'
    path = os.path.exists(path_file)
    if path == False:
      modules.GFJ().ecriture_du_fichier(self.liste_de_joueurs, self.filename, 4)


  def infos_joueur(self):
    '''Prise d'infos et ajout d'un nouveau joueur dans la liste des joueurs'''
  
    self.nom = input('Nom de famille :\n - ')
    self.prenom =  input('Prénom :\n - ')
    self.date_de_naissance = input('Date de naissance (jj/mm/aaaa) :\n - ')
    self.sexe = input('Sexe (M ou F) :\n - ')
    self.classement = float(input('Votre classement :\n - ')) 
    self.infos_joueurs = {'Nom de famille' : self.nom,
                     'Prénom' : self.prenom,
                     'Date de naissance' : self.date_de_naissance,
                     'Sexe' : self.sexe,
                     'Classement' : self.classement}
    self.temp = modules.GFJ().lecture_du_fichier(self.filename)
    id_joueur = len(self.temp) + 1
    id_infos  = {id_joueur : self.infos_joueurs}
    self.temp.append(id_infos)
    modules.GFJ().ecriture_du_fichier(self.temp, self.filename, 4)

    print('\nJoueur ajouté avec succès !\n')

class AjJ(AjoutJoueurs):
  '''Prise d'infos et ajout d'un nouveau joueur dans la liste des joueurs'''
  
  def __init__(self):
    super().__init__()
    super().infos_joueur()
    modules.RetourMenuJoueur().retour1()

class AjT(AjoutJoueurs):
  '''Prise d'infos et ajout d'un nouveau joueur dans la liste des joueurs'''

  def __init__(self):
    super().__init__()
    super().infos_joueur()
    modules.RetourMenuJoueur().retour2()


class ListeJoueurs():

  def __init__(self):
    self.afficher_liste = input('Afficher la liste des joueurs :\n (1) Par ordre alphabétique\n (2) Par classement\n - ')

  def afficher_joueurs(self):
    '''Afficher liste des joueurs selon l'ordre alphabétique ou de classement '''

    self.lj = []
    if self.afficher_liste == '1':
      liste_joueurs = modules.GFJ().lecture_du_fichier('Joueurs.json')
      for joueur_id, infos_joueur in zip(count(1), liste_joueurs):
        self.infos  = infos_joueur[f'{joueur_id}']
        self.infos['ID'] = joueur_id
        self.lj.append(self.infos)
      trie_par_nom = sorted(self.lj, key = lambda x : x ['Nom de famille'])

      print('Liste des joueurs par ordre alphabétique :\n')
      for i in trie_par_nom :
        self.id = i['ID']
        self.last_name  = i['Nom de famille']
        self.first_name  = i['Prénom']
        self.birth_date  = i['Date de naissance']
        self.sex  = i['Sexe']
        self.elo  = i['Classement']
        print(f'ID : {self.id}, Nom de famille : {self.last_name}, Prénom : {self.first_name}, Date de naissance : {self.birth_date}, Sexe : {self.sex}, Classement : {self.elo}\n')

    elif self.afficher_liste == '2':
      liste_joueurs = modules.GFJ().lecture_du_fichier('Joueurs.json')
      for joueur_id, infos_joueur in zip(count(1), liste_joueurs):
        self.infos  = infos_joueur[f'{joueur_id}']
        self.infos['ID'] = joueur_id
        self.lj.append(self.infos)
      trie_par_classement = sorted(self.lj, key = lambda x : x['Classement'], reverse=True)

      print('\nListe des joueurs par classement ordinal :\n')
      for i in trie_par_classement :
        self.id = i['ID']
        self.last_name  = i['Nom de famille']
        self.first_name  = i['Prénom']
        self.birth_date  = i['Date de naissance']
        self.sex  = i['Sexe']
        self.elo  = i['Classement']
        print(f'ID : {self.id}, Nom de famille : {self.last_name}, Prénom : {self.first_name}, Date de naissance : {self.birth_date}, Sexe : {self.sex}, Classement : {self.elo}\n')
    modules.RetourMenuJoueur().retour1()
    

#ListeJoueurs().afficher_joueurs()

class ListeJoueursParId:

  def afficher_joueurs_par_id(self):
    '''Afficher la liste des joueurs par classer par id'''

    self.lj = []
    liste_joueurs = modules.GFJ().lecture_du_fichier('Joueurs.json')
    for joueur_id, infos_joueur in zip(count(1), liste_joueurs):
      self.infos  = infos_joueur[f'{joueur_id}']
      self.infos['ID'] = joueur_id
      self.lj.append(self.infos)
    trie_par_classement = sorted(self.lj, key = lambda x : x['ID'])

    for i in trie_par_classement :
      self.id = i['ID']
      self.last_name  = i['Nom de famille']
      self.first_name  = i['Prénom']
      self.birth_date  = i['Date de naissance']
      self.sex  = i['Sexe']
      self.elo  = i['Classement']
      print(f'ID : {self.id}, Nom de famille : {self.last_name}, Prénom : {self.first_name}, Date de naissance : {self.birth_date}, Sexe : {self.sex}, Classement : {self.elo}\n')

class AjoutTournoi():
  
  filename = 'Tournois.json'

  def __init__(self):
    '''Création du fichier JSON contenant la liste des tournois'''

    self.liste_des_tournois = []
    path_file = f'./{self.filename}'
    path = os.path.exists(path_file)
    if path == False:
      GFJ().ecriture_du_fichier(self.liste_des_tournois, self.filename, 4)
    

  def infos_tournoi(self):
    '''Prise d'infos et ajout d'un nouveau tournoi dans le fichier contenant la liste des tournois'''

    print("\nAjout d'un nouveau tournoi\n")

    self.nom_tournoi = input('Nom du tournoi : \n - ')
    self.lieu = input('Lieu du tournoi : \n - ')
    self.date = input('Date :\n - ')
    self.nombre_de_tours = 4
    self.tournees = input('Tournées :\n - ')
    self.joueur = input('\n (2) - Ajouter un joueur\n - ')
    if self.joueur == '1':
      pass
    elif self.joueur == '2':
      AjT()
    self.temps = input('Contrôle du temps :\n (1) Bullet\n (2) Blitz\n (3) Coup rapide\n - ')
    if self.temps == '1':
      self.temps = 'Bullet'
    elif self.temps == '2':
      self.temps = 'Blitz'
    elif self.temps == '3':
      self.temps = 'Coup rapide'

    self.description = input('Description :\n')
    infos_tournoi = {'Nom du tournoi' : self.nom_tournoi,
                     'Lieu' : self.lieu,
                     'Date' : self.date,
                     'Nombre de tours' : self.nombre_de_tours,
                     'Tournées': int(self.tournees),
                     'Joueurs' : int(self.joueur),
                     'Temps' : self.temps,
                     'Description' : self.description}

    print("\nAjout d'un nouveau tournoi\n")

    self.temp = GFJ().lecture_du_fichier(self.filename)
    self.temp.append(infos_tournoi)
    GFJ().ecriture_du_fichier(self.temp, self.filename, 4)
    print(f'Tournoi {self.nom_tournoi} ajouté avec succès !')

    chess_program.RetourMenuTournoi()


class ListeTournoi():
  '''Affiche la liste des tournois'''

  def afficher_tournoi(self):

    liste_tournois = GFJ().lecture_du_fichier('Tournois.json')
    print('\nListe des tournois :\n')
    for tournoi in liste_tournois :
      self.nom_tournoi = tournoi['Nom du tournoi']
      self.lieu = tournoi['Lieu']
      self.date = tournoi['Date']
      self.nombre_de_tours = tournoi['Nombre de tours']
      self.tournees = tournoi['Tournées']
      self.joueur = tournoi['Joueurs']
      self.temps = tournoi['Temps']
      self.description = tournoi['Description']
      self.infos_tournoi = (f'\nNom du tournoi : {self.nom_tournoi}\nLieu : {self.lieu}\nDate : {self.date}\nNombre de tours : {self.nombre_de_tours}\nTournées : {self.tournees}\nJoueurs : {self.joueur}\nTemps : {self.temps}\nDescription : {self.description}\n')
      print(self.infos_tournoi)
