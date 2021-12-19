import json
from itertools import count
from utills import GestionFichierJson


class ListeJoueurs():

  def __init__(self):
    self.afficher_liste = input(f'Afficher la liste des joueurs :\n (1) Par ordre alphabétique\n (2) Par classement\n - ')

  def afficher_joueurs(self):
    '''Afficher liste des joueurs selon l'ordre aphabétique ou de classement '''
    self.lj = []
    if self.afficher_liste == '1':
      liste_joueurs = GestionFichierJson().lecture_du_fichier('Joueurs.json')
      lj = []
      for joueur_id, infos_joueur in zip(count(1), liste_joueurs):
        self.infos  = infos_joueur[f'{joueur_id}']
        lj.append(self.infos)
      trie_par_nom = sorted(lj, key = lambda x : x ['Nom de famille'])
      print('Liste des joueurs par ordre alphabétique :\n')
      for i in trie_par_nom :
        self.last_name  = i['Nom de famille']
        self.first_name  = i['Prénom']
        self.birth_date  = i['Date de naissance']
        self.sex  = i['Sexe']
        self.elo  = i['Classement']
        print(f'Nom de famille : {self.last_name}, Prénom : {self.first_name}, Date de naissance : {self.birth_date}, Sexe : {self.sex}, Classement : {self.elo}\n')

    elif self.afficher_liste == '2':
      liste_joueurs = GestionFichierJson().lecture_du_fichier('Joueurs.json')
      for joueur_id, infos_joueur in zip(count(1), liste_joueurs):
        self.infos  = infos_joueur[f'{joueur_id}']
        self.lj.append(self.infos)
      trie_par_classement = sorted(self.lj, key = lambda x : x['Classement'], reverse=True)

      print('\nListe des joueurs par classement ordinal :\n')
      for i in trie_par_classement :
        self.last_name  = i['Nom de famille']
        self.first_name  = i['Prénom']
        self.birth_date  = i['Date de naissance']
        self.sex  = i['Sexe']
        self.elo  = i['Classement']
        print(f'Nom de famille : {self.last_name}, Prénom : {self.first_name}, Date de naissance : {self.birth_date}, Sexe : {self.sex}, Classement : {self.elo}\n')
        



class ListeTournoi():
  '''Affiche la liste des tournois'''

  def afficher_tournoi(self):

    liste_tournois = GestionFichierJson().lecture_du_fichier('Tournois.json')
    print('\nListe des tournois :')
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

