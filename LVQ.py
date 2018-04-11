import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import math

def lvq(prototypes, trainSet):
    prototypes = np.asarray(prototypes)
    trainSet = np.asarray(trainSet)

    knn = KNeighborsClassifier(n_neighbors=1)
    print prototypes[:,range(len(prototypes[0])-1)],prototypes[:,-1]
    knn.fit(prototypes[:,range(len(prototypes[0])-1)] , prototypes[:,-1])
    print "de boas"
    alfa_ = 1
    misses = 0
    iteration = 0
    while True:
        alfa_ = 1/math.exp(iteration/2)
        #print alfa_
        for i in range(len(trainSet)):
            query_ = []
            query_.append(trainSet[i,range(len(trainSet[i])-1)])
            
            neighbor_index = knn.kneighbors(query_, return_distance=False)
            #print neighbor_index
            neighbor_index = neighbor_index[0][0]
            neighbor_class = prototypes[neighbor_index][-1]
            #print neighbor_class, trainSet[i][-1]
            if neighbor_class != trainSet[i][-1]:
                misses += 1
                for x in range(len(prototypes[neighbor_index])-1):
                    prototypes[neighbor_index][x] = float(prototypes[neighbor_index][x]) + alfa_ * (float(prototypes[neighbor_index][x])-trainSet[i][x])
            else:
                for x in range(len(prototypes[neighbor_index])-1):
                    prototypes[neighbor_index][x] = float(prototypes[neighbor_index][x]) - alfa_ * (float(prototypes[neighbor_index][x])-trainSet[i][x])
            knn.fit(prototypes[:,range(len(prototypes[0])-1)],prototypes[:,-1])

        print misses,iteration
        if misses == 0 or iteration == 1000:
            break
        misses = 0
        iteration += 1
    return prototypes