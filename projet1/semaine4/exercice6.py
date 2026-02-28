import matplotlib.pyplot as plt

'''
Les valeurs stockées dans ces variables sont des listes,
structure de donnéees que nous verrons plus tard dans le cours.
Pour l'instant, contentez-vous de copier-coller ces lignes dans votre script.
 '''
temps = [0, 6, 12, 18, 24, 30, 36]          # Valeurs en X pour les 2 gènes
exp_gene_myc = [95, 80, 60, 45, 30, 15, 5]  # Valeurs en Y pour le gène Myc
exp_gene_p21 = [5, 20, 40, 55, 70, 85, 95]  # Valeurs en Y pour le gène p21

# Mettre immédiatement après la création des tableaux de données
plt.figure(figsize=(10, 6))