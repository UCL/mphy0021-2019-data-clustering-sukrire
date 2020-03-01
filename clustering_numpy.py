import numpy as np
from numpy import random
from argparse import ArgumentParser

def cluster_num():
    parser = ArgumentParser(description='clustering_numpy.py')
    parser.add_argument('samplesfile', type=str, 
                        help='Please give file path to samples.csv')
    parser.add_argument('--iters', default=10, type=int,
                        help='Please give number of iterations')
    arguments = parser.parse_args()

    datapoints = np.genfromtxt(arguments.samplesfile, 
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
    
 
    for j in range(arguments.iters):
        for i in range(len(datapoints)):
            p=datapoints
            d=np.empty(shape=(3,1))
            d1=(p[i]-rsp[0])
            d2=(p[i]-rsp[1])
            d3=(p[i]-rsp[2])
            d[0]=np.hypot(d1[0],d1[1])
            d[1]=np.hypot(d2[0],d3[1])
            d[2]=np.hypot(d3[0],d3[1])
            str_ary[i]=(np.argmin(d,axis=0))

        rsp[0]=np.sum(datapoints[np.argwhere(str_ary==0)],axis=0)/len(np.argwhere(str_ary==0))
        rsp[1]=np.sum(datapoints[np.argwhere(str_ary==1)],axis=0)/len(np.argwhere(str_ary==1))
        rsp[2]=np.sum(datapoints[np.argwhere(str_ary==2)],axis=0)/len(np.argwhere(str_ary==2))


    print("Cluster 1 is centred at " + str(rsp[0]) + " and has " + str(len(np.argwhere(str_ary==0))) + " points.")
    print("Cluster 2 is centred at " + str(rsp[1]) + " and has " + str(len(np.argwhere(str_ary==1))) + " points.")
    print("Cluster 3 is centred at " + str(rsp[2]) + " and has " + str(len(np.argwhere(str_ary==2))) + " points.")
    
if __name__ == "__main__":
    cluster_num()