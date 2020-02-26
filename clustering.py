from math import sqrt
from random import randrange
from argparse import ArgumentParser
#from matplotlib import pyplot as plt


def cluster():
    parser = ArgumentParser(description='clustering.py')
    parser.add_argument('samplesfile', type=str,
                        help='Please give file path to samples.csv')
    parser.add_argument('--iters', default=10, type=int,
                        help='Please give number of iterations')
    arguments = parser.parse_args()


    datapoints = open(arguments.samplesfile, 'r').readlines()
    #point matrix = point_m
    point_m=[]
    
    for datapoint in datapoints: point_m.append(tuple(map(float, datapoint.strip().split(','))))

    m=[point_m[randrange(len(point_m))], point_m[randrange(len(point_m))], point_m[randrange(len(point_m))]]

    alloc=[None]*len(point_m)
    n=0
    
    #plt.scatter([i[0] for i in point_m],[i[1] for i in point_m])

    while n<arguments.iters:
      for i in range(len(point_m)):
        p=point_m[i]
        d=[None] * 3
        d[0]=sqrt((p[0]-m[0][0])**2 + (p[1]-m[0][1])**2)
        d[1]=sqrt((p[0]-m[1][0])**2 + (p[1]-m[1][1])**2)
        d[2]=sqrt((p[0]-m[2][0])**2 + (p[1]-m[2][1])**2)
        alloc[i]=d.index(min(d))
      for i in range(3):
        alloc_ps=[p for j, p in enumerate(point_m) if alloc[j] == i]
        new_mean=(sum([a[0] for a in alloc_ps]) / len(alloc_ps), sum([a[1] for a in alloc_ps]) / len(alloc_ps))
        m[i]=new_mean
      n += 1 

    for i in range(3):
      alloc_ps=[p for j, p in enumerate(point_m) if alloc[j] == i]
      print("Cluster " + str(i) + " is centred at " + str(m[i]) + " and has " + str(len(alloc_ps)) + " points.")
   

if __name__ == "__main__":
    cluster()