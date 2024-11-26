nous avons implémenter un outil de reconnaissance basé sur les chaînes de Markov cachées (HMM, pour Hidden Markov Models). 
L'objectif est de construire un modèle capable de déterminer la langue à laquelle appartient un mot donné. 
Pour cela, le modèle sera entraîné à partir de séquences de lettres correspondant à différentes langues. 
Il devra ensuite prédire la langue d’un mot en fonction de sa structure et des régularités linguistiques apprises.



 Vous trouverez les fichiers suivants :
- french.txt : fichier texte contenant le corpus de mots en français.
- english.txt : fichier texte contenant le corpus de mots en anglais.
- italian.txt : fichier texte contenant le corpus de mots en italien.
- matrice_emission.xls : Fichier Excel contenant la matrice d'émission, qui représente les probabilités
d'émission des lettres dans les différents états (modélisant des erreurs ou des variations possibles dans la
lecture/écriture des lettres).
- texte_1.txt, texte_2.txt et texte_3.txt : ces fichiers texte contiennent des textes échantillons dont la
langue devra être reconnue par le modèle HMM.
