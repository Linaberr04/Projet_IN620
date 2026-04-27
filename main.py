import sys
from MT_Config import *

def main():
    question = sys.argv[1] 

    if question == "q1":

        # MT
        nb_rubans = 1
        I = 'q0'
        F = 'qAccept'
        Transitions = {('q0',('1',)):('q1',('-',),('<',)), 
                       ('q1',('_',)):('qAccept',('_',),('-',))}
        Machine_test = MT(nb_rubans,I,F,Transitions)
        print(f"\n Machine de test créée avec {Machine_test.k} ruban(s).")
        print(f"État initial : {Machine_test.I}")
        print(f"État final : {Machine_test.F}")

       # Configuration
        rubans_test = ["101"]
        tetes_test = [0]
        Config_test = Configuration(rubans_test, tetes_test, Machine_test.I)
        print(f"\n Configuration :")
        print(f"État courant : {Config_test.state}")
        print(f"Contenu du ruban 1 : {Config_test.rubans[0]}")
        print(f"Position de la tête : {Config_test.tete}")
    

    if question == "q2":
        nom_fichier = "test.txt"  
        mot = "101"
        machine = charge_fichier(nom_fichier)
        Config = Configuration_Initiale(machine, mot)
        
        print(f"Machine chargée : {machine.k} rubans")
        print(f"État de départ : {Config.state}")
        print(f"Contenu des rubans : {Config.rubans}")
        print(f"Position des têtes : {Config.tete}")
    
    if question == "q3":
        nom_fichier = "test.txt"  
        mot = "101"
        machine = charge_fichier(nom_fichier)
        Config = Configuration_Initiale(machine, mot)

        print(f"\nNb rubans = {machine.k} rubans\n")

        print(f"\nConfiguration AVANT UN PAS :")
        print(f"État de départ : {Config.state}")
        print(f"Contenu des rubans : {Config.rubans}")
        print(f"Position des têtes : {Config.tete}")

        Un_pas_de_Calcul(machine)
        print(f"\nnConfiguration APRÈS UN PAS : ")
        print(f"État suivant : {Config.state}")
        print(f"Contenu des rubans : {Config.rubans}")
        print(f"Position des têtes : {Config.tete}")

    
    if question == "q4":
        print()

    if question == "q5":
        print()

    if question == "q6_1":
        nom_fichier = "fonction1.txt"
        mot = "10#100"
        machine = charge_fichier(nom_fichier) 

        retour = Execution_complete(machine,mot)
        print(retour)

    if question == "q6_2":
        nom_fichier = "fonction2.txt"
        mot = "10#100#10"
        machine = charge_fichier(nom_fichier) 

        retour = Execution_complete(machine,mot)
        print(retour)
    
    if question == "q7":
        nom_fichier = "test.txt"
        retour = Codage(nom_fichier)
        print(retour)

    if question == "q8_1":
        nom_fichier = "test.txt"

        codage,codage_binaire,entier = Codage_Binaire(nom_fichier)
        print("Codage : ", codage)
        print("Codage binaire : ", codage_binaire)
        print("Interprétation entier : ", entier )

    if question == "q9":
        nom_fichier = "test_q9.txt"
        entree = "110011"

        sortie = Machine_Turing(nom_fichier,entree)

        print("Sortie : ", sortie)
    
    if question == "q10":

        entree_MTU = "0|0|1|>|0|0|1|0|>|0|0|□|□|-|1#000#2"
        code = "0|0|1|>|0|0|1|0|>|0|0|□|□|-|1"
        entree = "000"
        M = Machine_Turing_Universelle_Compteur(entree_MTU)
        n = 2

        print(f"\n L'entrée donné à MTU est : {entree_MTU} (inverse 0 et 1) \n <M> : {code} \n w = {entree} \n nombre d'etapes = {n} ")
        print(f"\n Sortie : {M}")


    if question == "q11":
        print("\nLangage L1")
        print("L1 = { <M>#n | M s'arrête sur n en moins de n étapes }")
        print("Réponse : décidable \n")

        print("Langage L2")
        print("L2 = { <M>#n | M s'arrête sur les mots de taille n } ")
        print("Réponse : indécidable \n")

        print("Langage L3")
        print("L3 = { <M>#x#y | M calcule la même chose sur les entrées x et y }")
        print("Réponse : indécidable \n")








if __name__ == "__main__":
    main()


