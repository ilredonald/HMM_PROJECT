# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:47:30 2024

@author: user
"""
import numpy as np
import pandas as pd
import HMM_methods as m
#la initial
#La probabilité initiale
PI = m.vecteur_initial(26)
#print(PI)

#matrice identité
identité = np.eye(26)
#print(identite)
#les matrices de transitions
A_fr = m.matrice_transition('french.txt')
A_en = m.matrice_transition('english.txt')
A_it = m.matrice_transition('italian.txt')

#la matrice d'observations
B = m.matrice_emission('matrice_emission.xls')
#print(B)


def matrice_confusion1():
    mots = ['probablement','probably','probabilmente']
    langues =['français', 'anglais', 'italien']
    tableau = np.zeros((3,3))
    
    for i,O in enumerate(mots):
          probabilités_fr, tableau_fr= m.backward(O, A_fr, identité, PI)
                #probabilités_FR, tableau_FR= m.backward(O, A_fr, B, PI)
          probabilités_en, tableau_en= m.backward(O, A_en, identité, PI)
          probabilités_it, tableau_it= m.backward(O, A_it, identité, PI)
          probabilités = [probabilités_fr, probabilités_en, probabilités_it]
          for j in range(3):
            tableau[i, j]= probabilités[j]/np.sum(probabilités)
    tableau = pd.DataFrame(tableau, index= mots, columns=langues)
    return tableau

def matrice_confusion2():
    textes = ['texte_1.txt','texte_2.txt','texte_3.txt']
    langues =['français', 'anglais', 'italien']
    tableau = np.zeros((3,3))
 
    for i, texte in enumerate(textes):
        #lecture du fichier texte
          O = m.lire_fichier(texte)
          #calcule des probabiiés pour chaque langue
          probabilités_fr, tableau_fr= m.forward(O, A_fr, B, PI)
                        #probabilités_FR, tableau_FR= m.backward(O, A_fr, B, PI)
          probabilités_en, tableau_en= m.forward(O, A_en, B, PI)
          probabilités_it, tableau_it= m.forward(O, A_it, B, PI)
          probabilités = [probabilités_fr, probabilités_en, probabilités_it]
          for j in range(3):
              # normalisation des probabilités
              tableau[i, j]= probabilités[j]/np.sum(probabilités)
    #conservation des resultats dans un dataframe
    tableau = pd.DataFrame(tableau, index= textes, columns=langues)
    return tableau


t = matrice_confusion1()

t1 = matrice_confusion2()

print(t)
print(t1)
   