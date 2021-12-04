import json
import os
import shutil


class GestionDossierTemp:
    def creation_dossier(self):
        os.mkdir('./temp/')

    def suppression_dossier(self):
        shutil.rmtree('./temp/')

    def toto(self):
        try :
            GestionDossierTemp().creation_dossier()
        except :
            GestionDossierTemp().suppression_dossier()
            GestionDossierTemp().creation_dossier()

    



class GestionFichierJson:
    def ecriture_du_fichier(self, to_write, filename, ind= None):
        with open(filename, 'w') as file:
            json.dump(to_write, file, indent= ind)

    def lecture_du_fichier(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

class CheckDuel:
    def check(self, a, b, c):
        self.check1 = any([x == a for x in c])
        self.check2 = any([x == b for x in c])
        self.check = any((self.check1, self.check2))
        return self.check
