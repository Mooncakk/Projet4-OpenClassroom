import json
from itertools import count
from optparse import Values


class ListeJoueurs():

  affichage_joueurs = dict()
  


  def serialiser_liste_joueur(self):
    '''faire une fonction poure extraire chaque joueurs et une fonction pour afficher (une fois classé)''' 
    
    return self.donnees_joueurs

  def afficher_joueurs(self):

    afficher_liste = input(f'Afficher la liste des joueurs :\n (1) Par ordre alphabétique\n (2) Par classement\n - ')
    self.lj = []
    if afficher_liste == '1':
      with open("Joueurs.json", 'r') as file:
        liste_joueurs = json.load(file)
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

    elif afficher_liste == '2':
      with open("Joueurs.json", 'r') as file:
        liste_joueurs = json.load(file)
        for joueur_id, infos_joueur in zip(count(1), liste_joueurs):
          self.infos  = infos_joueur[f'{joueur_id}']
          self.lj.append(self.infos)
        trie_par_classement = sorted(self.lj, key = lambda x : x['Classement'], reverse=True)

        print('Liste des joueurs par classement ordinal :\n')
        for i in trie_par_classement :
          self.last_name  = i['Nom de famille']
          self.first_name  = i['Prénom']
          self.birth_date  = i['Date de naissance']
          self.sex  = i['Sexe']
          self.elo  = i['Classement']
          print(f'Nom de famille : {self.last_name}, Prénom : {self.first_name}, Date de naissance : {self.birth_date}, Sexe : {self.sex}, Classement : {self.elo}\n')
        

#ListeJoueurs().afficher_joueurs()


class ListeTournoi():
  def afficher_tournoi(self):
    with open("Tournois.json", 'r') as file:
      listejoueurs = json.load(file)
      print(listejoueurs)
