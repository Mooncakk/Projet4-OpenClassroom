import json
import os
import shutil


class GestionDossierTemp:
    '''Gestion du dossier temporaire'''

    def creation_dossier(self):
        '''Création du dossier temporaire'''
        os.mkdir('./temp/')

    def suppression_dossier(self):
        '''Suppression du dossier temporaire'''

        shutil.rmtree('./temp/')

    def gestion_dossier(self):
        try :
            GestionDossierTemp().creation_dossier()
        except :
            GestionDossierTemp().suppression_dossier()
            GestionDossierTemp().creation_dossier()

    



class GestionFichierJson:
    ''''''
    def ecriture_du_fichier(self, to_write, filename, ind= None):
        '''Création des fichiers temporaire'''

        with open(filename, 'w') as file:
            json.dump(to_write, file, indent= ind)

    def lecture_du_fichier(self, filename):
        '''Suppression des fichiers temporaire'''

        with open(filename, 'r') as file:
            return json.load(file)

class CheckDuel:
    def check(self, J1, J2, liste_duels):
        '''Vérifie si un duel est présent dans la liste des duels passé'''
        self.joueurs = [J1, J2]
        self.joueurs_inverse = [J2, J1]
        self.check1 = any(x == self.joueurs for x in liste_duels)
        self.check2 = any(x == self.joueurs_inverse for x in liste_duels)
        return any((self.check1, self.check2))

    def retour_check(self, J1, J2):
        '''Vérifie dans tous les tours précédent si l'affrontement de la paire de joueurs séléctionné a déjà eu lieu'''
                  
        self.duels_precedent = GestionFichierJson().lecture_du_fichier('./temp/temp_liste_des_duels.json')
        self.checklist = []
        for duel in self.duels_precedent:
            self.check = CheckDuel().check(J1, J2, duel)
            self.checklist.append(self.check)
        return any(self.checklist)
