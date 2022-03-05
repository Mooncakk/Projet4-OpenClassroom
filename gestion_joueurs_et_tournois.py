import json
import os
from itertools import count, zip_longest

from utills import GestionFichierJson as GFJ


class AjoutJoueurs():

  filename = 'Joueurs.json'

  def __init__(self):
    '''Création du fichier JSON contenant la liste des joueurs'''

    print("\nAjout d'un nouveau joueur\n")

    self.liste_de_joueurs = []
    path_file = f'./{self.filename}'
    path = os.path.exists(path_file)
    if path == False:
      GFJ().ecriture_du_fichier(self.liste_de_joueurs, self.filename, 4)


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
    self.liste_de_joueurs = GFJ().lecture_du_fichier(self.filename)
    self.liste_id_joueurs = []
    self.next_id = []
    for infos_joueur in self.liste_de_joueurs:
      for joueur_id in infos_joueur:
        self.liste_id_joueurs.append(int(joueur_id))
    for i, _id_ in zip_longest(range(1,100), self.liste_id_joueurs):
      if i not in self.liste_id_joueurs:
        self.next_id.append(i)

    id_joueur = self.next_id[0]
    id_infos  = {id_joueur : self.infos_joueurs}
    self.liste_de_joueurs.append(id_infos)
    GFJ().ecriture_du_fichier(self.liste_de_joueurs, self.filename, 4)

    print('\nJoueur ajouté avec succès !\n')


class RetourMenuJoueur():
  '''Sous menu joueur'''

  def retour1(self):
    rep = input('(1) Ajouter un nouveau joueur\n(2) Supprimer un joueur\n(3) Retourner au menu\n - ')
    if rep == '1':
      AjoutJoueurs().infos_joueur()
    elif rep == '2':
      EditData().supprimer_joueurs()
    elif rep =='3':
      RetourMenu()
    else :
      print('ERREUR! Veuillez taper un chiffre correspondant à un menu.')
  
  def retour2(self):
    rep = input(
      '(1) Ajouter un nouveau joueur\n(2) Appuyez sur entrer pour avancer\n - '
      )
    if rep == '1':
      AjoutJoueurs().infos_joueur()
    elif rep =='2':
      pass
    else :
      print('ERREUR! Veuillez taper un chiffre correspondant à un menu.')


  def retour3(self):
    rep = input(
      '(1) Ajouter un nouveau joueur\n(2) Supprimer un autre joueur\n(3) Retourner au menu\n - '
      )
    if rep == '1':
      AjoutJoueurs().infos_joueur()
    elif rep == '2':
      ListeJoueursParId().afficher_joueurs_par_id()
      EditData().supprimer_joueurs()
    elif rep =='3':
      RetourMenu()
    else :
      print('ERREUR! Veuillez taper un chiffre correspondant à un menu.')

class AjJ(AjoutJoueurs):
  '''Prise d'infos et ajout d'un nouveau joueur dans la liste des joueurs'''
  
  def __init__(self):
    super().__init__()
    super().infos_joueur()
    RetourMenuJoueur().retour1()

class AjT(AjoutJoueurs):
  '''Prise d'infos et ajout d'un nouveau joueur dans la liste des joueurs'''

  def __init__(self):
    super().__init__()
    super().infos_joueur()
    RetourMenuJoueur().retour2()


class ListeJoueurs():

  def __init__(self):
    self.afficher_liste = input('Afficher la liste des joueurs :\n (1) Par ordre alphabétique\n (2) Par classement\n - ')
    if self.afficher_liste == '1':
      self.afficher_joueurs_par_nom()
    elif self.afficher_liste == '2':
      self.afficher_joueurs_par_classement()
    
  def afficher_joueurs_par_nom(self):
    '''Afficher liste des joueurs selon l'ordre alphabétique ou de classement '''

    self.lj = []
    liste_joueurs = GFJ().lecture_du_fichier('Joueurs.json')
    for infos_joueur in liste_joueurs:
      for  joueur_id in infos_joueur:
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
    RetourMenuJoueur().retour1()


  def afficher_joueurs_par_classement(self):
    '''Afficher liste des joueurs par ordre de classement '''

    liste_joueurs = GFJ().lecture_du_fichier('Joueurs.json')
    self.lj = []
    for infos_joueur in liste_joueurs:
      for joueur_id in infos_joueur:
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
    RetourMenuJoueur().retour1()
    

class EditData():
  '''Supprimer un joueur présent dans la liste des joueurs '''
  def supprimer_joueurs(self):
    self.listejoueurs = GFJ().lecture_du_fichier('Joueurs.json')
    self.nb_joueurs = len(self.listejoueurs)
    self.id_joueur = 0
    if self.nb_joueurs > 0:
      while self.id_joueur > self.nb_joueurs or self.id_joueur == 0:
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
            GFJ().ecriture_du_fichier(self.listejoueurs, 'Joueurs.json', 4)
            print(f'Le joueur {self.id_joueur} à été supprimé !\n')

    RetourMenuJoueur().retour3()


class ListeJoueursParId:

  def afficher_joueurs_par_id(self):
    '''Afficher la liste des joueurs par classer par id'''

    self.lj = []
    liste_joueurs = GFJ().lecture_du_fichier('Joueurs.json')
    for infos_joueur in liste_joueurs:
      for joueur_id in infos_joueur:
        self.infos  = infos_joueur[f'{joueur_id}']
        self.infos['ID'] = joueur_id
      self.lj.append(self.infos)

    for i in self.lj :
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

    RetourMenuTournoi()

class RetourMenuTournoi():
  '''Sous menu tournoi'''

  def __init__(self):
    rep = input('(1) Ajouter un nouveau tournoi\n(2) Retourner au menu\n - ')
    if rep == '1':
      AjoutTournoi().infos_tournoi()
    elif rep =='2':
      RetourMenu()
    else :
      print('ERREUR! Veuillez taper un chiffre correspondant à un menu')
      


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
    RetourMenuTournoi()

class RetourMenu():

  def __init__(self):
    
    import chess_program
    