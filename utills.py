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

    def toto(self):
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
    def check(self, a, b, c):
        '''Vérifie si un duel est présent dans la liste des duels passé'''
        self.check1 = any([x == a for x in c])
        self.check2 = any([x == b for x in c])
        self.check = any((self.check1, self.check2))
        return self.check
