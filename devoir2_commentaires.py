### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###


#Je prépare python à travailler avec mon fichier CSV
import csv

### Je modifie simplement le nom du fichier pour faire rouler ton code sur mon ordi

fichier = "../grants.csv"
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

### Je mets ton compteur en commentaire et j'en crée dans chacune des conditions afin de ne compter que les subventions du Fonds
	### n+=1

	if ligne[17] == "FCP - Aide aux éditeurs de périodiques":

### Compteur que j'ajoute
		n += 1

### Pour trouver l'année, tu vas chercher l'item «ligne[0]».
### Il s'agit du numéro de la subvention.
### Ici, l'item ligne[13], qui contient la date de la subvention, est meilleur,
### car parfois, l'année contenue dans le numéro de subvention est antérieur à l'année contenue dans la date
### ce qui signifie que le numéro de subvention nous dit quand la subvention a été octroyée
### alors que la date nous dit quand la subvention a bel et bien été versée.

		annee = ligne[0]

### Mon année

		anneeJHR = ligne[13][:4]

### J'ajoute aussi, dans ton premier «print», le nombre de subventions où on est rendu («n»)

		print (ligne,n)
		print ("Année:", annee[3:7])

### J'imprime mon année
### Si les deux sont différentes, j'imprime un message d'alerte

		print("Année JHR : {}".format(anneeJHR))
		if annee[3:7] != anneeJHR:
			print("*"*80)
			print("    >>>>    ALERTE ROUGE    <<<<")
			print("    ANNÉES DIFFÉRENTES !!!!")
			print("    TOUS AUX ABRIS !!!!")
			print("#"*80)


	elif ligne[17] == "FCP -Innovation commerciale":

### Compteur que j'ajoute
		n += 1

		annee = ligne[0]

### Mon année

		anneeJHR = ligne[13][:4]

### J'ajoute aussi, dans ton premier «print», le nombre de subventions où on est rendu («n»)

		print (ligne,n)
		print ("Année:", annee[3:7])

### J'imprime mon année
### Si les deux sont différentes, j'imprime un message d'alerte

		print("Année JHR : {}".format(anneeJHR))
		if annee[3:7] != anneeJHR:
			print("*"*80)
			print("    >>>>    ALERTE ROUGE    <<<<")
			print("    ANNÉES DIFFÉRENTES !!!!")
			print("    TOUS AUX ABRIS !!!!")
			print("#"*80)

	elif ligne[17] == "Initiatives collectives":

### Compteur que j'ajoute
		n += 1

		annee = ligne[0]

### Mon année

		anneeJHR = ligne[13][:4]

### J'ajoute aussi, dans ton premier «print», le nombre de subventions où on est rendu («n»)

		print (ligne,n)
		print ("Année:", annee[3:7])

### J'imprime mon année
### Si les deux sont différentes, j'imprime un message d'alerte

		print("Année JHR : {}".format(anneeJHR))
		if annee[3:7] != anneeJHR:
			print("*"*80)
			print("    >>>>    ALERTE ROUGE    <<<<")
			print("    ANNÉES DIFFÉRENTES !!!!")
			print("    TOUS AUX ABRIS !!!!")
			print("#"*80)

### L'enchaînement de conditions que tu utilises fait en sorte que tu n'obtiens pas tout à fait les bonnes subventions
### Résultat, tu obtiens 2350 subventions.
### La solution, un seul «if», mais avec un «or»:
### «if "Fonds du Canada pour les périodiques" in ligne[17] or "FCP -" in ligne[17]:»
### Cela nous permet d'isoler vraiment les subventions du Fonds qui nous intéresse
### et de constater qu'il y en a 4608.