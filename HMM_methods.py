# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:09:38 2024

@author: user
"""
import re
import pandas
import numpy as np

#probabilité initiale
def vecteur_initial(n):
    v = np.ones(n)
    return v[:]/v[:].sum()

def lire_corpus(nom_fichier):
    
    with open(nom_fichier, 'r') as document:# ici on lit le fichier
        lecture = document.read()
        # ici on néttoie le code en éliminant la ponctuation et les accentuations
    nettoyage = re.sub(r'[^a-z\s]', '', lecture)
    return nettoyage
#lire_corpus('francais.txt')

def matrice_emission(nom_fichier):
    #ici on lit le fichier
    lecture = pandas.read_excel(nom_fichier)
    #ici on élimine la premiere colonne car il contient des caractères grâce à la fonction iloc[]
    #et l'on change le dataframe en matrice grâce à la fonction .values
    matrice = lecture.iloc[:, 1:].values
    return matrice
#print(matrice_emission('matrice_emission.xls'))

def matrice_transition(nom_fichier):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n = len(alphabet)
    A = np.zeros((n, n), dtype= float)
    lecture = lire_corpus(nom_fichier)
    #ici nous séparons les mots du corpus
    tableau_mots = lecture.split()
    for mot in tableau_mots:
        taille = len(mot)
        for i in range(taille-1):
            lettre1 = mot[i]#la première lettre du mot
            lettre2 = mot[i+1]#la deuxieme lettre du mot
            A[alphabet.index(lettre1), alphabet.index(lettre2)] +=1
    for i in range(n):
        
            s = A[i,:].sum()
            if s!=0:
   #la normalisation des lignes de la matrice A pour obtenir la somme des lignes = 1
                A[i,:] = A[i,:]/ s
    return A

# def automate(PI,A,B):
#     return PI,A,B

#méthode pour changer un texte en indices
def inDigitTxt(O):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    indices_O = [[alphabet.index(lettre) for lettre in mot if lettre in alphabet] for mot in O]
    return indices_O

#méthode pour changer un mot en indices
def inDigit(O):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    indices_O = np.array([alphabet.index(lettre) for lettre in O if lettre in alphabet])
    return indices_O

#les methodes forward et backward
def forward(O, A, B, PI):
    n = len(PI)
    T = len(O)
    #verification du type de O(si il s'agit d'une liste de mots ou pas)
    if isinstance(O,list):
        indices_O = inDigitTxt(O)
        #initialisation du tableau des probabilités des mots du texte
        Probabilite_mot = np.zeros(len(indices_O))
        #extration de chaque mot en indice pour le calcul de la probabilité
        for i, indice_mot in enumerate(indices_O):
            taille = len(indice_mot)
            alpha = np.zeros((taille,n))
            alpha[0,:] = PI*B[:,indice_mot[0]]
            #print(indices_O)
            for t in range(taille-1):
                for j in range(n):
                    somme = (alpha[t,:]*A[:,j]).sum()
                    alpha[t+1,j] =B[j,indice_mot[t+1]]* somme
            P = alpha[taille-1,:].sum()
            Probabilite_mot[i] = P
            #calcul de la probabilités moyennes du texte
        P = Probabilite_mot.sum() / T
        return P, alpha
    else:
   # je change le mot en indice par rapport à sa position dans l'aphabet.
        indices_O = inDigit(O)
        alpha = np.zeros((T,n))
    #initialisation du tableau alpha
        alpha[0,:] = PI*B[:,indices_O[0]]
    #print(indices_O)
    for t in range(T-1):
        for j in range(n):
            somme = (alpha[t,:]*A[:,j]).sum()
            alpha[t+1,j] =B[j,indices_O[t+1]]* somme
    #probabilité de la sequence 
    P = alpha[T-1,:].sum()
    return P, alpha

def backward(O, A, B, PI):
    n = len(PI)
    T = len(O)
    if isinstance(O, list):
        indices_O = inDigitTxt(O)
        Probabilite_mot = np.zeros(len(indices_O))
        for i, indice_mot in enumerate(indices_O):
            taille = len(indice_mot)
            beta = np.zeros((taille,n))
            beta[taille-1,:] = 1
            #print(indices_O)
            for t in range(taille-2,-1,-1):
                for j in range(n):
                    beta[t, j] = (beta[t+1, :]*A[j,:]*B[:, indice_mot[t+1]]).sum()
                    
            P = (PI*B[:,indice_mot[0]]*beta[0,:]).sum()
            Probabilite_mot[i] = P
        P = Probabilite_mot.sum() / T
        return P, beta
    else:
        beta = np.zeros((T,n))
        # je change le mot en indice par rapport à sa position dans l'aphabet.
        indices_O = inDigit(O)
        #initialisation du tableau beta
        beta[T-1,:] = 1
        for t in range(T-2,-1,-1):
            for j in range(n):
                beta[t, j] = (beta[t+1, :]*A[j,:]*B[:, indices_O[t+1]]).sum()
         #probabilité de la sequence      
        P = (PI*B[:,indices_O[0]]*beta[0,:]).sum()
        return P, beta

def lire_fichier(nom_fichier):
   with open(nom_fichier, 'r') as fichier:
       lecture= fichier.read()
       nettoyage = re.sub(r'[^a-z\s]', '', lecture)
       nettoyage = nettoyage.split()
       return nettoyage
O= lire_fichier('texte_1.txt')
#print(lire_fichier('texte_1.txt'))
#print(inDigitTxt(O))
A_fr = matrice_transition('french.txt')
A_en = matrice_transition('english.txt')
A_it = matrice_transition('italian.txt')


#print(matrice_transition('english.txt'))