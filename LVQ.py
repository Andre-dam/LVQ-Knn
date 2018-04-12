import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import math

def lvq1(prototypes, trainSet):
    prototypes_instances = prototypes[:,range(len(prototypes[0])-1)]
    prototypes_class = map(str,prototypes[:,-1])

    trainSet_instances = trainSet[:,range(len(trainSet[0])-1)]
    trainSet_class = trainSet[:,-1]
    
    #fit the prototypes
    knn = KNeighborsClassifier(n_neighbors=1)  
    knn.fit(prototypes_instances , prototypes_class)


    misses = 0
    iteration = 0
    while True:
        iteration += 1
        alfa_ = 1/math.pow(2,iteration/6.0)
        
        for i in range(len(trainSet_instances)):
            neighbor_index = knn.kneighbors([trainSet_instances[i]], return_distance=False)
            neighbor_index = neighbor_index[0][0] 
            neighbor_class = prototypes_class[neighbor_index]

            if neighbor_class != trainSet_class[i]:
                misses += 1
                for x in range(len(prototypes_instances[neighbor_index])):
                    prototypes_instances[neighbor_index][x] -=  alfa_ * (trainSet_instances[i][x]-float(prototypes_instances[neighbor_index][x]))
            else:
                for x in range(len(prototypes_instances[neighbor_index])):
                    prototypes_instances[neighbor_index][x] +=  alfa_ * (trainSet_instances[i][x]-float(prototypes_instances[neighbor_index][x]))
            knn.fit(prototypes_instances , prototypes_class)
        print misses,iteration
        if misses == 0 or iteration == 100:
            break
        misses = 0

    prototypes_class = np.reshape(prototypes_class,(len(prototypes_class), 1))
    prototypes= np.append(prototypes_instances, prototypes_class,axis=1)
    #prototypes = np.asarray(prototypes,dtype=float)

    return prototypes