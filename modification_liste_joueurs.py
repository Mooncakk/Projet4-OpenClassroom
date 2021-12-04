import json

class EditData():
  def afficher_joueurs(self):
    with open("Joueurs.json", 'r') as file:
      listejoueurs = json.load(file)
      taille = len(listejoueurs) - 1
      print(taille)

class EditData():
  def afficher_joueurs(self):
    with open("Joueurs.json", 'r') as file:
      listejoueurs = json.load(file)
      taille = len(listejoueurs)
      #print(listejoueurs[2['Nom de famille']])

#EditData().afficher_joueurs()