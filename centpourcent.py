#Je prépare python à travailler avec mon fichier CSV
import csv
fichier = "grants.csv"
f1 = open(fichier, encoding='utf-8')

document = csv.reader(f1)
next(document)
n = 0

#Je crée une boucle qui lira chaque ligne du document. Avec mes "if", je m'assure
#qu'il s'agit bien d'une ligne relative aux subventions; si l'élément numéro 17
#correspond à l'un des trois éléments que je recherche je vais faire imprimer la
#ligne. Aussi, avec "Année", je vais isoler l'année, qui est présente dans l'élément
#numéro 0.
for ligne in document:
	n+=1
	if ligne[17] == "FCP - Aide aux éditeurs de périodiques":
		annee = ligne[0]
		print (ligne)
		print ("Année:", annee[3:7])
	elif ligne[17] == "FCP -Innovation commerciale":
		annee = ligne[0]
		print (ligne)
		print ("Année:", annee[3:7])
	elif ligne[17] == "Initiatives collectives":
		annee = ligne[0]
		print (ligne)
		print ("Année:", annee[3:7])
		

