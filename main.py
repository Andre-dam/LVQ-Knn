import misc
import numpy as np
from LVQ import lvq
import matplotlib.pyplot as plt

def main():
		# Require: T: um conjunto de treinamento
	dataset = misc.loadData('cm1.arff')
	dataset = np.asarray(dataset)
	plt.scatter(dataset[:,0],dataset[:,1], c = dataset[:,2])
	#print len(dataset),len(dataset[0])
	# Require: P: uma lista para os prot otipos
	protypes = misc.getPrototypes(dataset)
	protypes = np.asarray(protypes)
	
	
	test = []
	test.append(dataset[0])
	test.append(dataset[-1])
	test.append(dataset[2])
	test.append(dataset[-2])
	test = np.asarray(test)
	print test
	protypes = lvq(test,dataset)

	plt.scatter(test[:,0],test[:,1])
	plt.show()

main()