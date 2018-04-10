import misc

def main():
	

	# Require: T: um conjunto de treinamento
	dataset = misc.loadData('cm1.arff')
	print len(dataset),len(dataset[0])
	# Require: P: uma lista para os prot otipos
	misc.getPrototypes(dataset)


main()