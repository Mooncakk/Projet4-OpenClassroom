
import datetime
import json
import os
import random
import time
from itertools import count, islice
from modules import GestionDossierTemp, GestionFichierJson, CheckDuel as cd, ListeJoueurs
#from gestion_joueurs_et_tournois import ListeJoueurs, GestionFichierJson


class GenerationDesPaires:
  
  def liste_des_joueurs(self):
    '''Récupère et retourne la liste des joueurd du fichier JSON'''
    nb_joueurs = GestionFichierJson().lecture_du_fichier('Tournois.json')[-1]['Joueurs']
    return GestionFichierJson().lecture_du_fichier('Joueurs.json')[:nb_joueurs]
    

  def liste_joueurs_classe(self):
    '''Trie la liste des joueurs par ordre de classement'''

    self.dict_joueurs = dict()
    self.liste_joueurs = GenerationDesPaires().liste_des_joueurs()
    for joueur_id, infos_joueur in zip(count(1), self.liste_joueurs):
      joueur = infos_joueur[f'{joueur_id}']
      self.dict_joueurs[joueur_id] = joueur
    self.liste_trie_par_classement = sorted(self.dict_joueurs, key = lambda x :(self.dict_joueurs[x]['Classement']), reverse = True)
    return self.liste_trie_par_classement

  def duels_tour1(self): 
    '''Sépare la liste des joueurs classé en deux et les associe pour former des duels'''   
    self.duels_precedent = []
    self.duels_tour1 = []
    self.liste_joueurs = GenerationDesPaires().liste_joueurs_classe()
    self.mediane = len(self.liste_joueurs)//2
    for partie1_joueurs, partie2_joueurs in zip(self.liste_joueurs, islice(self.liste_joueurs, self.mediane, None)) :
      duel = partie1_joueurs, partie2_joueurs
      self.duels_tour1.append(duel)
    self.duels_precedent.append(self.duels_tour1)
    '''Mettre les listes de duels dans un fichier temporaire pour pouvoir comparer si il y a une similitude'''
    GestionFichierJson().ecriture_du_fichier(self.duels_precedent, './temp/temp_liste_des_duels.json')
    return self.duels_tour1

  def duels_tour_suivant(self) :
    '''Récupère la liste des duels passé et le classement temporaire du tournoi pour former les duels du tour suivant en évitant que les joueurs affrontent le même adversdaire deuux fois'''
    self.liste_joueurs = GestionFichierJson().lecture_du_fichier('./temp/temp_classement_id_joueurs.json')
    self.duels_precedent = GestionFichierJson().lecture_du_fichier('./temp/temp_liste_des_duels.json')
    self.duels = []
    reserve = []
    nb_duels = int(len(self.liste_joueurs)//2)
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

            duel = [joueur1, joueur2_id]
            duel_inverse = [joueur2_id, joueur1]
            checklist = []
            for i in self.duels_precedent:
                ck = cd().check(duel, duel_inverse, i)
                checklist.append(ck)

            if any(checklist) == False:
                self.duels.append((joueur1, joueur2_id))
                if len(reserve) > 1:
                    reserve.pop(0)
                    reserve.pop(0)
                elif len(reserve) > 0:
                    reserve.pop(0)
                    self.liste_joueurs.pop(0)
                else:
                    self.liste_joueurs.pop(0)
                    self.liste_joueurs.pop(0)
            else:
                    
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

    self.duels_precedent.append(self.duels)
    GestionFichierJson().ecriture_du_fichier(self.duels_precedent, './temp/temp_liste_des_duels.json')
    '''Mettre les listes de duels dans un fichier temporaire pour pouvoir comparer si il y a une similitude !'''
    return self.duels


class IssueDuMatch:

  def resultat(self, joueur1, joueur2):
    '''Détermine l'issue du match'''

    self.issue = ["V", "N", "D"]
    self.resultat = random.choice(self.issue)
    
    if self.resultat == 'V':
      self.score1 = 1
      self.score2 = 0
      self.score_joueur1 = [joueur1, self.score1]
      self.score_joueur2 = [joueur2, self.score2]
      self.score = [self.score1, self.score2]
      return self.score1, self.score2, self.score
    elif  self.resultat == 'D':
      self.score1 = 0
      self.score2 = 1
      self.score_joueur1 = [joueur1, self.score1]
      self.score_joueur2 = [joueur2, self.score2]
      self.score = [self.score1, self.score2]
      return self.score1, self.score2, self.score
    elif  self.resultat == 'N':
      self.score1 = 0.5
      self.score2 = 0.5
      self.score_joueur1 = [joueur1, self.score1]
      self.score_joueur2 = [joueur2, self.score2]
      self.score = [self.score1, self.score2]
      return self.score1, self.score2, self.score

class Match:

  def __init__(self):
    ''''''
    self.filename = 'rounds.json'
    self.instance_tours = []
    path_file = f'./{self.filename}'
    path = os.path.exists(path_file)
    if path == False:
      GestionFichierJson().ecriture_du_fichier(self.instance_tours, self.filename, 4)
    else:
      pass

  def match (self, duels) :
    
    liste_joueurs = GestionFichierJson().lecture_du_fichier('Joueurs.json')
    self.duel = duels
    self.liste_score_joueur1 = []
    self.liste_score_joueur2 = []
    self.match_unique = []
    self.matchs_multiples = []
    for joueur in self.duel:
      self.match = IssueDuMatch().resultat(joueur[0], joueur[1])
      self.liste_score_joueur1.append(self.match[0])
      self.liste_score_joueur2.append(self.match[1])
      self.joueur_et_score = ([joueur[0], self.match[0]], [joueur[1], self.match[1]])
      self.score_match = self.match[2]
      self.match_unique.append(self.joueur_et_score)
      self.matchs_multiples.append(self.score_match)
    self.temp = [self.matchs_multiples, self.match_unique]
    GestionFichierJson().ecriture_du_fichier(self.temp, './temp/temp_infos_tournoi.json')
    return self.liste_score_joueur1, self.liste_score_joueur2


class UpdateJoueurs():
  def score_tour(self, duels):
    self.liste_scores = Match().match(duels)
    self.liste_scores_joueur1 = self.liste_scores[0]
    self.liste_scores_joueur2 = self.liste_scores[1]
    self.id_joueurs = GenerationDesPaires().liste_joueurs_classe()
    self.mediane = len(self.id_joueurs)//2
    self.score_tour = {}
    for id_joueurs1, id_joueurs2, score1, score2 in zip(self.id_joueurs, islice(self.id_joueurs,self.mediane,None), self.liste_scores_joueur1, self.liste_scores_joueur2):
      self.score_tour[id_joueurs1] = score1
      self.score_tour[id_joueurs2] = score2
    GestionFichierJson().ecriture_du_fichier(self.score_tour, './temp/temp_score_tour.json')


  def update_classement_score_tour(self, duels):

    self.score_tour = GestionFichierJson().lecture_du_fichier('./temp/temp_score_tour.json')
    self.classement_joueurs = []
    self.id_joueurs = GenerationDesPaires().liste_joueurs_classe()
    path_file = './temp/temp_scores_tours_precedent.json'
    path = os.path.exists(path_file)
    self.nb_joueurs = GestionFichierJson().lecture_du_fichier('Tournois.json')[-1]['Joueurs'] + 1
    

    if path == True:     
      scores_tours_precedent = GestionFichierJson().lecture_du_fichier('./temp/temp_scores_tours_precedent.json')
      for i in range(1,self.nb_joueurs):
        scores_tours_precedent[f'{i}'] += self.score_tour[f'{i}']

      self.classement_joueurs_par_score = dict(sorted(scores_tours_precedent.items(),key= lambda x : x[1], reverse= True))
        
    else:
      self.classement_joueurs_par_score = dict(sorted(self.score_tour.items(),key= lambda x : x[1], reverse= True))


    for i in self.classement_joueurs_par_score:
      self.classement_joueurs.append(int(i))

    GestionFichierJson().ecriture_du_fichier(self.classement_joueurs_par_score, './temp/temp_scores_tours_precedent.json')

    GestionFichierJson().ecriture_du_fichier(self.classement_joueurs, './temp/temp_classement_id_joueurs.json')
    return self.classement_joueurs
      

  def update_classement_general(self):
    self.liste_joueurs = GestionFichierJson().lecture_du_fichier('Joueurs.json')
    self.score_tournoi = GestionFichierJson().lecture_du_fichier('./temp/temp_scores_tours_precedent.json')
    self.temp = []
    for liste_joueurs, id_joueur, v in zip(self.liste_joueurs, count(1), count(0)):
      nouveau_scores_classement = self.liste_joueurs[v][f'{id_joueur}']['Classement'] + self.score_tournoi[f'{id_joueur}']
      self.infos_joueurs = {}
      self.infos_joueurs[id_joueur] = {'Nom de famille' : self.liste_joueurs[v][f'{id_joueur}']['Nom de famille'],
                          'Prénom' : self.liste_joueurs[v][f'{id_joueur}']['Prénom'],
                          'Date de naissance' : self.liste_joueurs[v][f'{id_joueur}']['Date de naissance'],
                          'Sexe' : self.liste_joueurs[v][f'{id_joueur}']['Sexe'],
                          'Classement' : nouveau_scores_classement
                            }
      self.temp.append(self.infos_joueurs)

    GestionFichierJson().ecriture_du_fichier(self.temp, 'Joueurs.json', 4)

    #'''un dictionnaire pour stocker les score additionné entre eux entre les tours, pour une mise a jour en fin de tournoi'''

    #'''prendre liste trié par classement l utiliser comme indice dans la boucle'''
      

class ExecutionAlgorithm:
  '''éxecution du script'''
  
  def __init__(self):
  
    nb_tours = GestionFichierJson().lecture_du_fichier('Tournois.json')[0]['Nombre de tours']  
    GestionDossierTemp().toto()
    self.round_start = datetime.datetime.now().strftime("%-d/%m/%y %H:%M:%S")
    print(f'Début du tournoi : {self.round_start}')
    print(f'Debut du round 1')
    UpdateJoueurs().score_tour(GenerationDesPaires().duels_tour1())
    UpdateJoueurs().update_classement_score_tour(GenerationDesPaires().duels_tour1())
    self.round_end = datetime.datetime.now().strftime("%-d/%m/%y %H:%M:%S")
    infos_tournoi = GestionFichierJson().lecture_du_fichier('./temp/temp_infos_tournoi.json')
    instance_tournoi = []
    instance_tour = [f'Round {1}, Date et heure de debut : {self.round_start}, Date et heure de fin : {self.round_end}']
    instance_tour.append(infos_tournoi[0])
    instance_tour.append(infos_tournoi[1])
    instance_tournoi.append(instance_tour)
    GestionFichierJson().ecriture_du_fichier(instance_tournoi, 'Instance_Tournoi.json')

    for i in range(nb_tours-1):

      print(f'Debut du round {i+2}')
      self.round_start = datetime.datetime.now().strftime("%-d/%m/%y %H:%M:%S")
      UpdateJoueurs().score_tour(GenerationDesPaires().duels_tour_suivant())
      UpdateJoueurs().update_classement_score_tour(GenerationDesPaires().duels_tour_suivant)
      self.round_end = datetime.datetime.now().strftime("%-d/%m/%y %H:%M:%S")
      infos_tournoi = GestionFichierJson().lecture_du_fichier('./temp/temp_infos_tournoi.json')
      instance_tour = [f'Round {i+2}, Date et heure de debut : {self.round_start}, Date et heure de fin : {self.round_end}']
      instance_tour.append(infos_tournoi[0])
      instance_tour.append(infos_tournoi[1])
      instance_tournoi = GestionFichierJson().lecture_du_fichier('Instance_Tournoi.json')
      instance_tournoi.append(instance_tour)
      GestionFichierJson().ecriture_du_fichier(instance_tournoi, 'Instance_Tournoi.json')

    UpdateJoueurs().update_classement_general()
    GestionDossierTemp().suppression_dossier()
    print(f'Fin du tournoi : {self.round_end}')

