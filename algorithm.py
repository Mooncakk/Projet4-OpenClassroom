
import datetime
import json
import os
import random
import time
from itertools import count, islice
from utills import GestionDossierTemp, GestionFichierJson, CheckDuel as cd

from afficher_liste_joueurs_et_tournois import ListeJoueurs


class GenerationDesPaires:
  
  def liste_des_joueurs(self):
    return GestionFichierJson().lecture_du_fichier('Joueurs.json')

  def liste_joueurs_classe(self):
    self.dict_joueurs = dict()
    self.liste_joueurs = GenerationDesPaires().liste_des_joueurs()
    for joueur_id, infos_joueur in zip(count(1), self.liste_joueurs):
      joueur = infos_joueur[f'{joueur_id}']
      self.dict_joueurs[joueur_id] = joueur
    self.liste_trie_par_classement = sorted(self.dict_joueurs, key = lambda x :(self.dict_joueurs[x]['Classement']), reverse = True)
    return self.liste_trie_par_classement

  def duels_tour1(self):    
    self.duels_precedent = []
    self.duels_tour1 = []
    self.liste_joueurs = GenerationDesPaires().liste_joueurs_classe()
    for partie1_joueurs, partie2_joueurs in zip(self.liste_joueurs, islice(self.liste_joueurs, 4, None)) :
      duel = partie1_joueurs, partie2_joueurs
      self.duels_tour1.append(duel)
    self.duels_precedent.append(self.duels_tour1)
    '''Mettre les listes de duels dans un fichier temporaire pour pouvoir comparer si il y a une similitude'''
    GestionFichierJson().ecriture_du_fichier(self.duels_precedent, './temp/temp_liste_des_duels.json')
    print(self.duels_tour1)
    return self.duels_tour1

  def duels_tour_suivant(self) :
    self.liste_joueurs = GestionFichierJson().lecture_du_fichier('./temp/temp_classement_id_joueurs.json')
    '''for joueur1, joueur2 in zip(islice(self.liste_joueurs, 0, None, 2), islice(self.liste_joueurs, 1, None, 2)):
      self.duel.append((joueur1, joueur2))'''
    self.duels_precedent = GestionFichierJson().lecture_du_fichier('./temp/temp_liste_des_duels.json')
    self.duels = []
    reserve = []
    nb_duels = int(len(self.liste_joueurs)/2)
    #joueur1 = c[0]
    while len(self.liste_joueurs) > 0:
        for i in range(nb_duels):

            if len(reserve) > 1:
                joueur1 = reserve[0]
                joueur2_id = reserve[1]
            elif len(reserve) > 0:
                joueur1 = reserve[0]
                joueur2_id = self.liste_joueurs[0]
            else:
                joueur1 = self.liste_joueurs[0]
                joueur2_id = self.liste_joueurs[1]

                #print(joueur2_id)
            duel = [joueur1, joueur2_id]
            duel_inverse = [joueur2_id, joueur1]
            checklist = []
            for i in self.duels_precedent:
                ck = cd().check(duel, duel_inverse, i)
                checklist.append(ck)

            if any(checklist) == False:
                print('le duel peut avoir lieu sans problème !')
                self.duels.append((joueur1, joueur2_id))
                print(self.duels)
                if len(reserve) > 1:
                    reserve.pop(0)
                    reserve.pop(0)
                elif len(reserve) > 0:
                    reserve.pop(0)
                    self.liste_joueurs.pop(0)
                else:
                    self.liste_joueurs.pop(0)
                    self.liste_joueurs.pop(0)
                    print(self.liste_joueurs)
            else:
                print('le duel a déjà eu lieu, prendre de le joueur suivant !')
                    
                if len(reserve) > 1:
                    joueur2_id = self.liste_joueurs[0]
                    self.duels.append((joueur1, joueur2_id))
                    reserve.pop(0)
                    self.liste_joueurs.pop(0)

                elif len(reserve) > 0:
                    reserve.append(joueur2_id)
                    self.liste_joueurs.pop(0)
                    joueur2_id = self.liste_joueurs[0]
                    self.duels.append((joueur1, joueur2_id))
                    self.liste_joueurs.pop(0)
                    reserve.pop(0)

                else:    
                    
                    reserve.append(joueur2_id)
                    self.liste_joueurs.pop(1)
                    joueur2_id = self.liste_joueurs[1]
                    duel = [joueur1, joueur2_id]
                    duel_inverse = [joueur2_id, joueur1] 
                    ct = []
                    for i in self.duels_precedent:
                            ck = cd().check(duel, duel_inverse, i)
                            ct.append(ck)
                    if any(ct) == True : 
                        cc = True
                        while cc == True:
                            reserve.append(joueur2_id)
                            self.liste_joueurs.pop(1)
                            joueur2_id = self.liste_joueurs[1]
                            duel = [joueur1, joueur2_id]
                            duel_inverse = [joueur2_id, joueur1]  
                            ckt = [] 
                            for i in self.duels_precedent:
                                ck = cd().check(duel, duel_inverse, i)
                                ckt.append(ck)
                            cc = any(ckt) 
            
                    self.duels.append((joueur1, joueur2_id))
                    self.liste_joueurs.pop(0)
                    self.liste_joueurs.pop(0)

                print(reserve)
            print(self.duels)

    self.duels_precedent.append(self.duels)
    GestionFichierJson().ecriture_du_fichier(self.duels_precedent, './temp/temp_liste_des_duels.json')
    '''Mettre les listes de duels dans un fichier temporaire pour pouvoir comparer si il y a une similitude !UTILISÉ a+ !'''
    return self.duels


class IssueDuMatch:

  def resultat(self, joueur1='', joueur2=''):
    self.issue = ["V", "N", "D"]
    self.resultat = random.choice(self.issue)
    self.temps_du_match = random.randint(10,180)
    
    if self.resultat == 'V':
      self.score1 = 1
      self.score2 = 0
      self.score_joueur1 = [joueur1, self.score1]
      self.score_joueur2 = [joueur2, self.score2]
      self.score = (self.score_joueur1, self.score_joueur2)
      #print(f'Durée du match : {self.temps_du_match} minutes\n')
      #print(self.round_start)
      return self.score, self.score1, self.score2
    elif  self.resultat == 'D':
      self.score1 = 0
      self.score2 = 1
      self.score_joueur1 = [joueur1, self.score1]
      self.score_joueur2 = [joueur2, self.score2]
      self.score = (self.score_joueur1, self.score_joueur2)
      #print(f'Durée du match : {self.temps_du_match} minutes\n')
      #print(self.round_start)
      return self.score, self.score1, self.score2
    elif  self.resultat == 'N':
      self.score1 = 0.5
      self.score2 = 0.5
      self.score_joueur1 = [joueur1, self.score1]
      self.score_joueur2 = [joueur2, self.score2]
      self.score = (self.score_joueur1, self.score_joueur2)
      #print(self.round_start)
      #print(f'Durée du match : {self.temps_du_match} minutes\n')
      return self.score, self.score1, self.score2

class Match:

  def __init__(self):
    self.filename = 'rounds.json'
    self.score_joueur = []
    path_file = f'./{self.filename}'
    path = os.path.exists(path_file)
    if path == False:
      GestionFichierJson().ecriture_du_fichier(self.score_joueur, self.filename, 4)
    else:
      pass

  def match (self, duels) :
    
    liste_joueurs = GestionFichierJson().lecture_du_fichier('Joueurs.json')
    self.duel = duels
    self.round_start = datetime.datetime.now().strftime("%-d/%m/%y %H:%M:%S")
    self.round_end = datetime.datetime.now().strftime("%-d/%m/%y %H:%M:%S")
    self.round = (f'Round :\n Date et heure de début du round : {self.round_start}\n Date et heure de fin du round : {self.round_end}\n')
    print(self.round)
    self.liste_score_joueur1 = []
    self.liste_score_joueur2 = []
    for joueur in self.duel:
      self.match = IssueDuMatch().resultat(joueur[0], joueur[1])
      #print(self.match)
      self.liste_score_joueur1.append(self.match[1])
      self.liste_score_joueur2.append(self.match[2])
      '''with open('rounds.json', 'r') as file:
        temp = json.load(file)'''
      temp = GestionFichierJson().lecture_du_fichier('rounds.json')
        #temp.append(self.match)
      '''with open(self.filename, 'w') as file :
          #json.dump(self.round1, file)
          #json.dump('Format : ID , Score')
          json.dump(temp, file)'''
    return self.liste_score_joueur1, self.liste_score_joueur2

  


class UpdateJoueurs():
  def score_tour(self, duels):
    self.liste_scores = Match().match(duels)
    self.liste_scores_joueur1 = self.liste_scores[0]
    self.liste_scores_joueur2 = self.liste_scores[1]
    self.id_joueurs = GenerationDesPaires().liste_joueurs_classe()
    self.score_tour = {}
    self.temp = []
    for id_joueurs1, id_joueurs2, score1, score2 in zip(self.id_joueurs, islice(self.id_joueurs,4,None), self.liste_scores_joueur1, self.liste_scores_joueur2):
      '''d = {'ID' : id_joueurs1, 'Score' : score1}
      e = {'ID' : id_joueurs2, 'Score' : score2}'''
      self.score_tour[id_joueurs1] = score1
      self.score_tour[id_joueurs2] = score2
      
      """stocker dans un autre fichier temp pour eviter la 2e execution du round"""
      '''self.score_tour.append(d)
      self.score_tour.append(e)'''
      self.temp.append((id_joueurs1,score1))
      self.temp.append((id_joueurs2,score2))

    GestionFichierJson().ecriture_du_fichier(self.score_tour, './temp/temp_score_tour.json')
    print(self.score_tour)
    return self.score_tour, self.temp


  def update_classement_score_tour(self, duels):

    #with open('temp_score_tour.json', 'r') as file:
    self.score_tour = GestionFichierJson().lecture_du_fichier('./temp/temp_score_tour.json')
    #self.score_tour = UpdateJoueurs().score_tour(self.duels)[0]
    #self.scores_tour_list = UpdateJoueurs().score_tour(self.duels)[1]
    #print(self.scores_tour_list)
    self.classement_joueurs = []
    self.id_joueurs = GenerationDesPaires().liste_joueurs_classe()
    path_file = f'./temp/temp_scores_tours_precedent.json'
    path = os.path.exists(path_file)
    if path == True:     
      scores_tours_precedent = GestionFichierJson().lecture_du_fichier('./temp/temp_scores_tours_precedent.json')
      '''i = '8'
    print(scores_tours_precedent[i])'''
      for i in range(1,9):
        scores_tours_precedent[f'{i}'] += self.score_tour[f'{i}']

      self.classement_joueurs_par_score = dict(sorted(scores_tours_precedent.items(),key= lambda x : x[1], reverse= True))
      print(self.classement_joueurs_par_score)
        
    else:
      self.classement_joueurs_par_score = dict(sorted(self.score_tour.items(),key= lambda x : x[1], reverse= True))
      print(self.score_tour)


    for i in self.classement_joueurs_par_score:
      self.classement_joueurs.append(int(i))
      print(i)
    print(self.classement_joueurs_par_score)

    GestionFichierJson().ecriture_du_fichier(self.classement_joueurs_par_score, './temp/temp_scores_tours_precedent.json')

    GestionFichierJson().ecriture_du_fichier(self.classement_joueurs, './temp/temp_classement_id_joueurs.json')
    return self.classement_joueurs
      

    
    #'''un dictionnaire pour stocker les score additionné entre eux entre les tours, pour une mise a jour en fin de tournoi'''

    #'''prendre liste trié par classement l utiliser comme indice dans la boucle'''
      
  


#Match().match(GenerationDesPaires().duels_tour1())
#CreationDossierTemp().creation_dossier()
#UpdateJoueurs().score_tour(GenerationDesPaires().duels_tour1())
#UpdateJoueurs().update_classement_score_tour(GenerationDesPaires().duels_tour1())
#GenerationDesPaires().duels_tour_suivant()
#Match().match(GenerationDesPaires().duels_tour_suivant())
#UpdateJoueurs().score_tour(GenerationDesPaires().duels_tour1())
#UpdateJoueurs().score_tour(GenerationDesPaires().duels_tour_suivant())
#CreationDossierTemp().suppression_dossier()


class ExecutionAlgorithm:
  '''éxecution du script'''
  def __init__(self):
    nb_tours = GestionFichierJson().lecture_du_fichier('Tournois.json')[0]['Nombre de tours']
    print(nb_tours)
    GestionDossierTemp().toto()
    #GestionDossierTemp().creation_dossier()
    print(f'Debut du round 1')
    UpdateJoueurs().score_tour(GenerationDesPaires().duels_tour1())
    UpdateJoueurs().update_classement_score_tour(GenerationDesPaires().duels_tour1())
    for i in range(nb_tours-1):
      print(f'Debut du round {i+2}')
      UpdateJoueurs().score_tour(GenerationDesPaires().duels_tour_suivant())
      UpdateJoueurs().update_classement_score_tour(GenerationDesPaires().duels_tour_suivant)
    GestionDossierTemp().suppression_dossier()


ExecutionAlgorithm()

#toto = GestionFichierJson().lecture_du_fichier('./temp/temp_liste_des_duels.json')
