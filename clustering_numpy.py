import numpy as np
from numpy import random
from argparse import ArgumentParser

def cluster_num(datapoints,iters=10):
    datapoints = np.genfromtxt(samplesfile, 
                               delimiter=",", dtype='float')
    
    point1 = np.random.randint(len(datapoints))
    point2 = np.random.randint(len(datapoints))
    point3 = np.random.randint(len(datapoints))

    #random starting points
    rsp = np.array([[datapoints[point1,0],datapoints[point1,1]],
                   [datapoints[point2,0],datapoints[point2,1]],
                   [datapoints[point3,0],datapoints[point3,1]]])

    #storing array
    str_ary = np.empty(len(datapoints))
    
 
    for j in range(iters):
        a=datapoints-rsp[0]
        b=datapoints-rsp[1]
        c=datapoints-rsp[2]
        nearest1 = np.hypot(a[:,0],a[:,1])
        nearest2 = np.hypot(b[:,0],b[:,1])
        nearest3 = np.hypot(c[:,0],c[:,1])
        stacked_matrix = np.stack((nearest1,nearest2,nearest3))
        str_ary = np.argmin(stacked_matrix, axis=0)
            
        rsp[0]=np.sum(datapoints[np.argwhere(str_ary==0)],axis=0)/len(np.argwhere(str_ary==0))
        rsp[1]=np.sum(datapoints[np.argwhere(str_ary==1)],axis=0)/len(np.argwhere(str_ary==1))
        rsp[2]=np.sum(datapoints[np.argwhere(str_ary==2)],axis=0)/len(np.argwhere(str_ary==2))


    print("Cluster 1 is centred at " + str(rsp[0]) + " and has " + str(len(np.argwhere(str_ary==0))) + " points.")
    print("Cluster 2 is centred at " + str(rsp[1]) + " and has " + str(len(np.argwhere(str_ary==1))) + " points.")
    print("Cluster 3 is centred at " + str(rsp[2]) + " and has " + str(len(np.argwhere(str_ary==2))) + " points.")
    
if __name__ == "__main__":
    parser = ArgumentParser(description='clustering_numpy.py')
    parser.add_argument('samplesfile', type=str, 
                        help='Please give file path to samples.csv')
    parser.add_argument('--iters', default=10, type=int,
                        help='Please give number of iterations')
    arguments = parser.parse_args()
    samplesfile=arguments.samplesfile
    iters=arguments.iters
    datapoints = np.genfromtxt(samplesfile, delimiter=",", dtype='float')
    cluster_num(datapoints,iters)