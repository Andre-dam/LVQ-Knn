import misc
import numpy as np
from LVQ import lvq1
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def main():	
	dataset = misc.loadData('cm1.arff')
	dataset = np.asarray(dataset)

	#Random partition the dataset into 30%test 70%train
	trainset, testset = train_test_split(dataset, test_size=0.30)
	#LVQ1

	plt.scatter(dataset[:,0],dataset[:,1], c = dataset[:,2])
	
	#get the centroid prototypes of each class
	protypes = misc.getRandomPrototypes(dataset,3)
	#protypes = misc.getPrototypes(trainset)

	plt.scatter(protypes[:,0],protypes[:,1], c = ['g','b'])
	plt.show()

	#print protypes[0]

	#VAMOS SELECIONAR 1,2 E 3 PROTOTIPOS ALEATORIOS POR CLASSE TREINAR O LVQ1 E TESTAR NO KNN COM 1 2 E 3
	protypes = lvq1(protypes,dataset)

	plt.scatter(dataset[:,0],dataset[:,1], c = dataset[:,2])
	plt.scatter(protypes[:,0],protypes[:,1], c = ['g','b'])
	plt.show()

main()