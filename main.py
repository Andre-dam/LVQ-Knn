import misc
import numpy as np
from LVQ import lvq
import matplotlib.pyplot as plt

def main():
		# Require: T: um conjunto de treinamento
	dataset = misc.loadData('cm1.arff')
	dataset = np.asarray(dataset)
	plt.scatter(dataset[:,0],dataset[:,1], c = dataset[:,2])

	protypes = misc.getPrototypes(dataset)
	
	protypes = lvq(protypes,dataset)
	#plt.scatter(protypes[:,0],protypes[:,1], c = ['g','b'])

	#plt.show()

main()