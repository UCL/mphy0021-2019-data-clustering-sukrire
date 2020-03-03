from math import sqrt
from random import randrange
from argparse import ArgumentParser
import json
#from matplotlib import pyplot as plt


def cluster(samplesfile,iters=10):
    #random start points = rsp
    rsp=[point_m[randrange(len(point_m))], point_m[randrange(len(point_m))], point_m[randrange(len(point_m))]]

    #define and empty matrix for allocations
    alloc=[None]*len(point_m)
    n=0
    
    while n<iters:
      for i in range(len(point_m)):
        p=point_m[i]
        d=[None] * 3
        d[0]=sqrt((p[0]-rsp[0][0])**2 + (p[1]-rsp[0][1])**2)
        d[1]=sqrt((p[0]-rsp[1][0])**2 + (p[1]-rsp[1][1])**2)
        d[2]=sqrt((p[0]-rsp[2][0])**2 + (p[1]-rsp[2][1])**2)
        alloc[i]=d.index(min(d))
      for i in range(3):
        alloc_point_m=[p for j, p in enumerate(point_m) if alloc[j] == i]
        if len(alloc_point_m) == 0:
            pass
        else:
            new_mean=(sum([a[0] for a in alloc_point_m]) / len(alloc_point_m), sum([a[1] for a in alloc_point_m]) / len(alloc_point_m))
            rsp[i]=new_mean
      n += 1 

    for i in range(3):
      alloc_point_m=[p for j, p in enumerate(point_m) if alloc[j] == i]
      print("Cluster " + str(i) + " is centred at " + str(rsp[i]) + " and has " + str(len(alloc_point_m)) + " points.")
   

if __name__ == "__main__":
    parser = ArgumentParser(description='clustering.py')
    parser.add_argument('samplesfile', type=str,
                        help='Please give file path to samples.csv')
    parser.add_argument('--iters', default=10, type=int,
                        help='Please give number of iterations')
    arguments = parser.parse_args()
    samplesfile=arguments.samplesfile
    iters=arguments.iters
    
    #point matrix = point_m
    point_m=[]
    
    #chooses how to open a file depending on the filetype
    if samplesfile.endswith('csv'):
        datapoints = open(samplesfile, 'r').readlines()
        for datapoint in datapoints: point_m.append(tuple(map(float, datapoint.strip().split(','))))
    elif samplesfile.endswith('json'):
        with open(samplesfile, "r") as infile:
            lines_json = json.load(infile)
            for city in lines_json:
                point_m.append((lines_json[city]['population'], lines_json[city]['books']))
                
    cluster(samplesfile,iters)